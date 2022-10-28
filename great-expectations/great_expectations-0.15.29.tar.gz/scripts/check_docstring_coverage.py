import ast
import glob
import logging
import subprocess
from collections import defaultdict
from typing import Dict, List, Tuple, cast

Diagnostics = Dict[str, List[Tuple[ast.FunctionDef, bool]]]

DOCSTRING_ERROR_THRESHOLD: int = (
    1095  # This number is to be reduced as we document more public functions!
)

logger = logging.getLogger(__name__)


def get_changed_files(branch: str) -> List[str]:
    """Perform a `git diff` against a given branch.

    Args:
        branch (str): The branch to diff against (generally `origin/develop`)

    Returns:
        A list of changed files.
    """
    git_diff: subprocess.CompletedProcess = subprocess.run(
        ["git", "diff", branch, "--name-only"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    return [f for f in git_diff.stdout.split()]


def collect_functions(directory_path: str) -> Dict[str, List[ast.FunctionDef]]:
    """Using AST, iterate through all source files to parse out function definition nodes.

    Args:
        directory_path (str): The directory to traverse through.

    Returns:
        A dictionary that maps source file with the function definition nodes contained therin.
    """
    all_funcs: Dict[str, List[ast.FunctionDef]] = {}

    file_paths: List[str] = _gather_source_files(directory_path)
    for file_path in file_paths:
        all_funcs[file_path] = _collect_functions(file_path)

    return all_funcs


def _gather_source_files(directory_path: str) -> List[str]:
    return glob.glob(f"{directory_path}/**/*.py", recursive=True)


def _collect_functions(file_path: str) -> List[ast.FunctionDef]:
    with open(file_path) as f:
        root: ast.Module = ast.parse(f.read())

    return cast(
        List[ast.FunctionDef],
        list(filter(lambda n: isinstance(n, ast.FunctionDef), ast.walk(root))),
    )


def gather_docstring_diagnostics(
    all_funcs: Dict[str, List[ast.FunctionDef]]
) -> Diagnostics:
    """Given all function definitions in a repository, filter out the one's relevant to docstring testing.

    Args:
        all_funcs (Dict[str, List[ast.FunctionDef]]): The mapping generated by `collect_functions`.

    Returns:
        A set of diagnostics that are relevant to docstring checking.
        (Diagnostics is a dictionary that associates each func with a bool to denote adherence/conflict with the style guide).
    """
    diagnostics: Diagnostics = defaultdict(list)
    for file, func_list in all_funcs.items():
        public_funcs: List[ast.FunctionDef] = list(
            filter(
                lambda f: _function_filter(f),
                func_list,
            )
        )
        for func in public_funcs:
            result: Tuple[ast.FunctionDef, bool] = (func, bool(ast.get_docstring(func)))
            diagnostics[file].append(result)

    return diagnostics


def _function_filter(func: ast.FunctionDef) -> bool:
    # Private and dunder funcs/methods
    if func.name.startswith("_"):
        return False
    # Getters and setters
    for decorator in func.decorator_list:
        if (isinstance(decorator, ast.Name) and decorator.id == "property") or (
            isinstance(decorator, ast.Attribute) and decorator.attr == "setter"
        ):
            return False
    return True


def review_diagnostics(diagnostics: Diagnostics, changed_files: List[str]) -> None:
    """Generate the report to stdout.

    Args:
        diagnostics (Diagnostics): The diagnostics generated in `gather_docstring_diagnostics`.
        changed_files (List[str]): The list of files generated from `get_changed_files`.

    Raises:
        AssertionError if threshold is surpassed. This threshold ensures we don't introduce new regressions.
    """
    total_passed: int = 0
    total_funcs: int = 0

    relevant_diagnostics: Dict[str, List[ast.FunctionDef]] = defaultdict(list)

    for file, diagnostics_list in diagnostics.items():
        relevant_file: bool = file in changed_files
        for func, success in diagnostics_list:
            if success:
                total_passed += 1
            elif not success and relevant_file:
                relevant_diagnostics[file].append(func)
            total_funcs += 1

    total_failed: int = total_funcs - total_passed
    print(
        f"[SUMMARY] {total_failed} of {total_funcs} public functions ({100 * total_failed / total_funcs:.2f}%) are missing docstrings!"
    )

    if relevant_diagnostics:
        print(
            "\nHere are violations of the style guide that are relevant to the files changed in your PR:"
        )

        for file, func_list in relevant_diagnostics.items():
            print(f"\n  {file}:")
            for func in func_list:
                print(f"    L{func.lineno}:{func.name}")

    # Chetan - 20220305 - While this number should be 0, getting the number of style guide violations down takes time
    # and effort. In the meanwhile, we want to set an upper bound on errors to ensure we're not introducing
    # further regressions. As docstrings are added, developers should update this number.
    assert (
        total_failed <= DOCSTRING_ERROR_THRESHOLD
    ), f"""A public function without a docstring was introduced; please resolve the matter before merging.
                We expect there to be {DOCSTRING_ERROR_THRESHOLD} or fewer violations of the style guide (actual: {total_failed})"""

    if DOCSTRING_ERROR_THRESHOLD != total_failed:
        logger.warning(
            f"The threshold needs to be updated! {DOCSTRING_ERROR_THRESHOLD} should be reduced to {total_failed}"
        )


if __name__ == "__main__":
    changed_files: List[str] = get_changed_files("origin/develop")
    all_funcs: Dict[str, List[ast.FunctionDef]] = collect_functions(
        "great_expectations"
    )
    docstring_diagnostics: Diagnostics = gather_docstring_diagnostics(all_funcs)
    review_diagnostics(docstring_diagnostics, changed_files)

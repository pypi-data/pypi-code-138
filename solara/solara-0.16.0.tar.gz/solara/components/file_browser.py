import os
from os.path import isfile, join
from pathlib import Path
from typing import Callable, List, Optional, Union, cast

import humanize
import ipyvuetify as vy
import solara
import traitlets
from solara.components import Div


def list_dir(path, filter=filter):
    def mk_item(n):
        full_path = join(path, n)
        is_file = isfile(full_path)
        return {"name": n, "is_file": is_file, "size": humanize.naturalsize(os.stat(full_path).st_size) if is_file else None}

    files = [mk_item(k) for k in os.listdir(path) if not k.startswith(".") if filter(Path(path) / k)]
    sorted_files = sorted(files, key=lambda item: ("0" if item["is_file"] else "1") + item["name"].lower())
    return sorted_files


class FileListWidget(vy.VuetifyTemplate):
    template_file = (__file__, "file_list_widget.vue")

    files = traitlets.List().tag(sync=True)
    clicked = traitlets.Dict(allow_none=True, default_value=None).tag(sync=True)
    double_clicked = traitlets.Dict(allow_none=True, default_value=None).tag(sync=True)
    scroll_pos = traitlets.Int(allow_none=True).tag(sync=True)

    def test_click(self, path: Union[Path, str], double_click=False):
        """Simulate a click or double click at the Python side"""
        matches = [k for k in self.files if k["name"] == str(path)]
        if len(matches) == 0:
            names = [k["name"] for k in self.files]
            raise NameError(f"Could not find {path}, possible filenames: {names}")
        item = matches[0]
        if double_click:
            self.double_clicked = item
        else:
            self.clicked = item

    def __contains__(self, name):
        """Test if filename/directory name is in the current directory."""
        return name in [k["name"] for k in self.files]


@solara.component
def FileBrowser(
    directory: Union[str, Path] = None,
    on_directory_change: Callable[[Path], None] = None,
    on_path_select: Callable[[Optional[Path]], None] = None,
    on_file_open: Callable[[Path], None] = None,
    filter: Callable[[Path], bool] = lambda x: True,
    on_file_name: Callable[[str], None] = None,
    start_directory=None,
    can_select=False,
):
    """
    on_file_name is deprecated, use on_file_open
    start_directory is deprecated, use directory
    """
    if start_directory is not None:
        directory = start_directory  # pragma: no cover
    if directory is None:
        directory = os.getcwd()  # pragma: no cover
    current_dir, set_current_dir = solara.use_state_or_update(str(directory))
    selected, set_selected = solara.use_state(None)
    double_clicked, set_double_clicked = solara.use_state(None)
    warning, set_warning = solara.use_state(cast(Optional[str], None))
    scroll_pos_stack, set_scroll_pos_stack = solara.use_state(cast(List[int], []))
    scroll_pos, set_scroll_pos = solara.use_state(0)
    selected, set_selected = solara.use_state(None)

    def change_dir(new_dir):
        if os.access(new_dir, os.R_OK):
            set_current_dir(new_dir)
            if on_directory_change:
                on_directory_change(Path(new_dir))
            set_warning(None)
            return True
        else:
            set_warning(f"[no read access to {new_dir}]")

    def on_item(item, double_click):
        if item is None:
            if can_select and on_path_select:
                on_path_select(None)
            return
        if item["name"] == "..":
            new_dir = current_dir[: current_dir.rfind(os.path.sep)]
            action_change_directory = (can_select and double_click) or (not can_select and not double_click)
            if action_change_directory and change_dir(new_dir):
                if scroll_pos_stack:
                    last_pos = scroll_pos_stack[-1]
                    set_scroll_pos_stack(scroll_pos_stack[:-1])
                    set_scroll_pos(last_pos)
                set_selected(None)
                set_double_clicked(None)
                if on_path_select and can_select:
                    on_path_select(None)
            if can_select and not double_click:
                if on_path_select:
                    on_path_select(Path(new_dir))
            return

        path = os.path.join(current_dir, item["name"])
        is_file = item["is_file"]
        if (can_select and double_click) or (not can_select and not double_click):
            if is_file:
                if on_file_open:
                    on_file_open(Path(path))
                if on_file_name is not None:
                    on_file_name(path)
            else:
                if change_dir(path):
                    set_scroll_pos_stack(scroll_pos_stack + [scroll_pos])
                    set_scroll_pos(0)
                set_selected(None)
            set_double_clicked(None)
            if on_path_select and can_select:
                on_path_select(None)
        elif can_select and not double_click:
            if on_path_select:
                on_path_select(Path(path))
        else:  # not can_select and double_click is ignored
            raise RuntimeError("Combination should not happen")  # pragma: no cover

    def on_click(item):
        set_selected(item)
        on_item(item, False)

    def on_double_click(item):
        set_double_clicked(item)
        if can_select:
            on_item(item, True)
        # otherwise we can ignore it, single click will handle it

    with Div(class_="solara-file-browser") as main:
        Div(children=[current_dir])
        FileListWidget.element(
            files=[{"name": "..", "is_file": False}] + list_dir(current_dir, filter=filter),
            selected=selected,
            clicked=selected,
            on_clicked=on_click,
            double_clicked=double_clicked,
            on_double_clicked=on_double_click,
            scroll_pos=scroll_pos,
            on_scroll_pos=set_scroll_pos,
        ).key("FileList")
        if warning:
            Div(style_="font-weight: bold; color: red", children=[warning])

    return main

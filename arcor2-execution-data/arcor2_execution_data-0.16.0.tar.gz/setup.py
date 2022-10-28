
# DO NOT EDIT THIS FILE -- AUTOGENERATED BY PANTS
# Target: src/python/arcor2_execution_data:arcor2_execution_data_dist

from setuptools import setup

setup(**{
    'author': 'Robo@FIT',
    'author_email': 'imaterna@fit.vut.cz',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.10',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
    ],
    'description': 'ARCOR2 Execution service data',
    'install_requires': (
        'arcor2_runtime~=0.4.0',
        'arcor2~=0.25.0',
        'dataclasses-jsonschema[apispec,fast-dateparsing,fast-uuid,fast-validation]~=2.16.0',
    ),
    'license': 'LGPL',
    'long_description': """# arcor2_execution_data
# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),

## [0.16.0] - 2022-10-28

### Changed

- Switched to Python 3.10, updated dependencies.

## [0.15.0] - 2022-01-25

### Changed

- Breaking change of WebSockets API (`ActionStateBefore` event).
- Switched to Python 3.9, updated dependencies.

## [0.14.1] - 2021-11-08

## Fixed

- Fixed mutual dependency between `arcor2_execution_data` and `arcor2_runtime` (`package.py` moved to `arcor2_runtime`).

## [0.14.0] - 2021-10-25

### Changed

- Stuff needed by the main script moved to `arcor2_runtime`.
- New RPC `StepAction`, debugging-related arguments added to `RunPackage`.

## [0.13.0] - 2021-08-05

### Changed

- `Resources` can now handle `CollisionObject`.


## [0.12.0] - 2021-07-29

### Changed

- Property `description` added to `ProjectMeta`.

## [0.11.0] - 2021-06-14

### Changed
- Modules `package` and `resources` moved here from `arcor2` package.
- `Resources` class now do not have any parameters (it used to have `project_id`).

### Fixed
- In `Resources/__exit__`, collision models were deleted before calling `cleanup` for each object.

## [0.10.0] - 2021-02-08

### Changed
- `PackageState` RPC removed.

## [0.9.0] - 2020-10-22

### Changed
- `PackageSummary` now contains optional `project_meta` property which may hold basic information about the project embedded in the execution package.

## [0.8.1] - 2020-10-19

### Changed
- ARCOR2 dependency updated

## [0.8.0] - 2020-09-24
### Changed
- The first release of the separated package.""",
    'long_description_content_type': 'text/markdown',
    'name': 'arcor2_execution_data',
    'namespace_packages': (
    ),
    'package_data': {
        'arcor2_execution_data': (
            'VERSION',
            'py.typed',
        ),
    },
    'packages': (
        'arcor2_execution_data',
    ),
    'python_requires': '==3.10.*',
    'version': '0.16.0',
})

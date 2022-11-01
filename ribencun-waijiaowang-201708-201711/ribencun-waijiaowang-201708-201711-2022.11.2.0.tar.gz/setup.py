#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import RibencunWaijiaowang201708201711
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('RibencunWaijiaowang201708201711'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="ribencun-waijiaowang-201708-201711",
    version=RibencunWaijiaowang201708201711.__version__,
    url="https://github.com/apachecn/ribencun-waijiaowang-201708-201711",
    author=RibencunWaijiaowang201708201711.__author__,
    author_email=RibencunWaijiaowang201708201711.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="日本村外教网 2017.8~2017.11",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "ribencun-waijiaowang-201708-201711=RibencunWaijiaowang201708201711.__main__:main",
            "RibencunWaijiaowang201708201711=RibencunWaijiaowang201708201711.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

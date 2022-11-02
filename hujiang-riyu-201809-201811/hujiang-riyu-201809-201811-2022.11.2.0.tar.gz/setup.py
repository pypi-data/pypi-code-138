#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import HujiangRiyu201809201811
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('HujiangRiyu201809201811'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="hujiang-riyu-201809-201811",
    version=HujiangRiyu201809201811.__version__,
    url="https://github.com/apachecn/hujiang-riyu-201809-201811",
    author=HujiangRiyu201809201811.__author__,
    author_email=HujiangRiyu201809201811.__email__,
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
    description="沪江日语 2018.9~2018.11",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "hujiang-riyu-201809-201811=HujiangRiyu201809201811.__main__:main",
            "HujiangRiyu201809201811=HujiangRiyu201809201811.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

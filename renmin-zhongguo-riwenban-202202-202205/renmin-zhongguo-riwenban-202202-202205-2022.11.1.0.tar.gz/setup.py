#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import RenminZhongguoRiwenban202202202205
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('RenminZhongguoRiwenban202202202205'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="renmin-zhongguo-riwenban-202202-202205",
    version=RenminZhongguoRiwenban202202202205.__version__,
    url="https://github.com/apachecn/renmin-zhongguo-riwenban-202202-202205",
    author=RenminZhongguoRiwenban202202202205.__author__,
    author_email=RenminZhongguoRiwenban202202202205.__email__,
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
    description="人民中国日文版 2022.2~2022.5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "renmin-zhongguo-riwenban-202202-202205=RenminZhongguoRiwenban202202202205.__main__:main",
            "RenminZhongguoRiwenban202202202205=RenminZhongguoRiwenban202202202205.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

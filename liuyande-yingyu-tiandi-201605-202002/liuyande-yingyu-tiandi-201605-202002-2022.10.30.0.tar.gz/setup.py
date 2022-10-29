#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import LiuyandeYingyuTiandi201605202002
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('LiuyandeYingyuTiandi201605202002'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="liuyande-yingyu-tiandi-201605-202002",
    version=LiuyandeYingyuTiandi201605202002.__version__,
    url="https://github.com/apachecn/liuyande-yingyu-tiandi-201605-202002",
    author=LiuyandeYingyuTiandi201605202002.__author__,
    author_email=LiuyandeYingyuTiandi201605202002.__email__,
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
    description="刘彦的英语天地TheRealDeal 2016.5~2020.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "liuyande-yingyu-tiandi-201605-202002=LiuyandeYingyuTiandi201605202002.__main__:main",
            "LiuyandeYingyuTiandi201605202002=LiuyandeYingyuTiandi201605202002.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import YueshuoYuehaoLianyingyu201410202206
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('YueshuoYuehaoLianyingyu201410202206'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="yueshuo-yuehao-lianyingyu-201410-202206",
    version=YueshuoYuehaoLianyingyu201410202206.__version__,
    url="https://github.com/apachecn/yueshuo-yuehao-lianyingyu-201410-202206",
    author=YueshuoYuehaoLianyingyu201410202206.__author__,
    author_email=YueshuoYuehaoLianyingyu201410202206.__email__,
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
    description="悦说越好炼英语 2014.10~2022.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "yueshuo-yuehao-lianyingyu-201410-202206=YueshuoYuehaoLianyingyu201410202206.__main__:main",
            "YueshuoYuehaoLianyingyu201410202206=YueshuoYuehaoLianyingyu201410202206.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

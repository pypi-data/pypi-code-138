#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import XujilinChuantongWenhua30jiang
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('XujilinChuantongWenhua30jiang'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="xujilin-chuantong-wenhua-30jiang",
    version=XujilinChuantongWenhua30jiang.__version__,
    url="https://github.com/apachecn/xujilin-chuantong-wenhua-30jiang",
    author=XujilinChuantongWenhua30jiang.__author__,
    author_email=XujilinChuantongWenhua30jiang.__email__,
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
    description="许纪霖传统文化30讲",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "xujilin-chuantong-wenhua-30jiang=XujilinChuantongWenhua30jiang.__main__:main",
            "XujilinChuantongWenhua30jiang=XujilinChuantongWenhua30jiang.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

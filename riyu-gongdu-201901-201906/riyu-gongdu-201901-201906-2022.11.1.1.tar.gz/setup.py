#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import RiyuGongdu201901201906
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('RiyuGongdu201901201906'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="riyu-gongdu-201901-201906",
    version=RiyuGongdu201901201906.__version__,
    url="https://github.com/apachecn/riyu-gongdu-201901-201906",
    author=RiyuGongdu201901201906.__author__,
    author_email=RiyuGongdu201901201906.__email__,
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
    description="日语共读 2019.1~2019.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "riyu-gongdu-201901-201906=RiyuGongdu201901201906.__main__:main",
            "RiyuGongdu201901201906=RiyuGongdu201901201906.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

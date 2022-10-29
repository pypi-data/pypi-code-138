#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import YasiKaoshiGuanfangWeishequ201503201903
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('YasiKaoshiGuanfangWeishequ201503201903'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="yasi-kaoshi-guanfang-weishequ-201503-201903",
    version=YasiKaoshiGuanfangWeishequ201503201903.__version__,
    url="https://github.com/apachecn/yasi-kaoshi-guanfang-weishequ-201503-201903",
    author=YasiKaoshiGuanfangWeishequ201503201903.__author__,
    author_email=YasiKaoshiGuanfangWeishequ201503201903.__email__,
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
    description="雅思考试官方微社区 2015.3~2019.3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "yasi-kaoshi-guanfang-weishequ-201503-201903=YasiKaoshiGuanfangWeishequ201503201903.__main__:main",
            "YasiKaoshiGuanfangWeishequ201503201903=YasiKaoshiGuanfangWeishequ201503201903.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

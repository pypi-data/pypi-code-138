#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ZhuokeKexueSiweiBixiuke20180608
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ZhuokeKexueSiweiBixiuke20180608'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="zhuoke-kexue-siwei-bixiuke-201806-08",
    version=ZhuokeKexueSiweiBixiuke20180608.__version__,
    url="https://github.com/apachecn/zhuoke-kexue-siwei-bixiuke-201806-08",
    author=ZhuokeKexueSiweiBixiuke20180608.__author__,
    author_email=ZhuokeKexueSiweiBixiuke20180608.__email__,
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
    description="卓克科学思维必修课201806-08",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "zhuoke-kexue-siwei-bixiuke-201806-08=ZhuokeKexueSiweiBixiuke20180608.__main__:main",
            "ZhuokeKexueSiweiBixiuke20180608=ZhuokeKexueSiweiBixiuke20180608.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ChuxinLianmengRiyu201408201801
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ChuxinLianmengRiyu201408201801'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="chuxin-lianmeng-riyu-201408-201801",
    version=ChuxinLianmengRiyu201408201801.__version__,
    url="https://github.com/apachecn/chuxin-lianmeng-riyu-201408-201801",
    author=ChuxinLianmengRiyu201408201801.__author__,
    author_email=ChuxinLianmengRiyu201408201801.__email__,
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
    description="初心联盟日语 2014.8~2018.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "chuxin-lianmeng-riyu-201408-201801=ChuxinLianmengRiyu201408201801.__main__:main",
            "ChuxinLianmengRiyu201408201801=ChuxinLianmengRiyu201408201801.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

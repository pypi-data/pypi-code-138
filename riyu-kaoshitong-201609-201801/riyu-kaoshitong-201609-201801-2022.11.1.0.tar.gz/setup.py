#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import RiyuKaoshitong201609201801
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('RiyuKaoshitong201609201801'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="riyu-kaoshitong-201609-201801",
    version=RiyuKaoshitong201609201801.__version__,
    url="https://github.com/apachecn/riyu-kaoshitong-201609-201801",
    author=RiyuKaoshitong201609201801.__author__,
    author_email=RiyuKaoshitong201609201801.__email__,
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
    description="日语考试通 2016.9~2018.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "riyu-kaoshitong-201609-201801=RiyuKaoshitong201609201801.__main__:main",
            "RiyuKaoshitong201609201801=RiyuKaoshitong201609201801.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

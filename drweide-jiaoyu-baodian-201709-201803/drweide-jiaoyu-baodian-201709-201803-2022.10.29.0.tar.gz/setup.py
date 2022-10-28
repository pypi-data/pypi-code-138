#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import DrweideJiaoyuBaodian201709201803
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('DrweideJiaoyuBaodian201709201803'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="drweide-jiaoyu-baodian-201709-201803",
    version=DrweideJiaoyuBaodian201709201803.__version__,
    url="https://github.com/apachecn/drweide-jiaoyu-baodian-201709-201803",
    author=DrweideJiaoyuBaodian201709201803.__author__,
    author_email=DrweideJiaoyuBaodian201709201803.__email__,
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
    description="Dr魏的教育宝典201709-201803",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "drweide-jiaoyu-baodian-201709-201803=DrweideJiaoyuBaodian201709201803.__main__:main",
            "DrweideJiaoyuBaodian201709201803=DrweideJiaoyuBaodian201709201803.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

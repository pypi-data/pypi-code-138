#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import YingyuKouyuXiaozhen202007202010
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('YingyuKouyuXiaozhen202007202010'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="yingyu-kouyu-xiaozhen-202007-202010",
    version=YingyuKouyuXiaozhen202007202010.__version__,
    url="https://github.com/apachecn/yingyu-kouyu-xiaozhen-202007-202010",
    author=YingyuKouyuXiaozhen202007202010.__author__,
    author_email=YingyuKouyuXiaozhen202007202010.__email__,
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
    description="英语口语小镇 2020.7~2020.10",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "yingyu-kouyu-xiaozhen-202007-202010=YingyuKouyuXiaozhen202007202010.__main__:main",
            "YingyuKouyuXiaozhen202007202010=YingyuKouyuXiaozhen202007202010.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

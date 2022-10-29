#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import KaoyanYingyuHuangpishu201606201701
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('KaoyanYingyuHuangpishu201606201701'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="kaoyan-yingyu-huangpishu-201606-201701",
    version=KaoyanYingyuHuangpishu201606201701.__version__,
    url="https://github.com/apachecn/kaoyan-yingyu-huangpishu-201606-201701",
    author=KaoyanYingyuHuangpishu201606201701.__author__,
    author_email=KaoyanYingyuHuangpishu201606201701.__email__,
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
    description="考研英语黄皮书 2016.6~2017.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "kaoyan-yingyu-huangpishu-201606-201701=KaoyanYingyuHuangpishu201606201701.__main__:main",
            "KaoyanYingyuHuangpishu201606201701=KaoyanYingyuHuangpishu201606201701.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

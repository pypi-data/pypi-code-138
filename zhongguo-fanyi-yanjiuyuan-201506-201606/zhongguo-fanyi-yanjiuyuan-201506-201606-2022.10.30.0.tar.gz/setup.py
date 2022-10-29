#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ZhongguoFanyiYanjiuyuan201506201606
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ZhongguoFanyiYanjiuyuan201506201606'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="zhongguo-fanyi-yanjiuyuan-201506-201606",
    version=ZhongguoFanyiYanjiuyuan201506201606.__version__,
    url="https://github.com/apachecn/zhongguo-fanyi-yanjiuyuan-201506-201606",
    author=ZhongguoFanyiYanjiuyuan201506201606.__author__,
    author_email=ZhongguoFanyiYanjiuyuan201506201606.__email__,
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
    description="中国翻译研究院 2015.6~2016.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "zhongguo-fanyi-yanjiuyuan-201506-201606=ZhongguoFanyiYanjiuyuan201506201606.__main__:main",
            "ZhongguoFanyiYanjiuyuan201506201606=ZhongguoFanyiYanjiuyuan201506201606.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

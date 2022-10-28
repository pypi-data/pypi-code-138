#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ZhangxiaoyuShangyeJingdianAnli20170407
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ZhangxiaoyuShangyeJingdianAnli20170407'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="zhangxiaoyu-shangye-jingdian-anli-201704-07",
    version=ZhangxiaoyuShangyeJingdianAnli20170407.__version__,
    url="https://github.com/apachecn/zhangxiaoyu-shangye-jingdian-anli-201704-07",
    author=ZhangxiaoyuShangyeJingdianAnli20170407.__author__,
    author_email=ZhangxiaoyuShangyeJingdianAnli20170407.__email__,
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
    description="张潇雨商业经典案例201704-07",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "zhangxiaoyu-shangye-jingdian-anli-201704-07=ZhangxiaoyuShangyeJingdianAnli20170407.__main__:main",
            "ZhangxiaoyuShangyeJingdianAnli20170407=ZhangxiaoyuShangyeJingdianAnli20170407.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

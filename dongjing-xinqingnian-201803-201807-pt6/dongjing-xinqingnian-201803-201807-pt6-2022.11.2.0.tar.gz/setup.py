#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import DongjingXinqingnian201803201807Pt6
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('DongjingXinqingnian201803201807Pt6'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="dongjing-xinqingnian-201803-201807-pt6",
    version=DongjingXinqingnian201803201807Pt6.__version__,
    url="https://github.com/apachecn/dongjing-xinqingnian-201803-201807-pt6",
    author=DongjingXinqingnian201803201807Pt6.__author__,
    author_email=DongjingXinqingnian201803201807Pt6.__email__,
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
    description="东京新青年 2018.3~2018.7 PT6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "dongjing-xinqingnian-201803-201807-pt6=DongjingXinqingnian201803201807Pt6.__main__:main",
            "DongjingXinqingnian201803201807Pt6=DongjingXinqingnian201803201807Pt6.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)

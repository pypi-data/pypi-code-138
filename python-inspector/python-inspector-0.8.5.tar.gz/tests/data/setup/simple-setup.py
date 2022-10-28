# Copyright (C) 2017-2021 HERE Europe B.V.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# SPDX-License-Identifier: Apache-2.0
# License-Filename: LICENSE

from setuptools import find_packages
from setuptools import setup

setup(
    name="Example-App",
    description="A synthetic test case for OSS Review Toolkit",
    version="2.4.0",
    url="https://example.org/app",
    license="MIT License",
    classifiers=["License :: OSI Approved :: MIT License", "Programming Language :: Python :: 2"],
    python_requires=">2, <=3",
    install_requires=["license-expression>=0.1, <1.2"],
    packages=find_packages(),
)

from setuptools import find_packages, setup

setup(
    name="libcoveofds",
    version="0.1.0",
    author="Open Data Services",
    author_email="code@opendataservices.coop",
    url="https://github.com/Open-Telecoms-Data/lib-cove-ofds",
    project_urls={
        "Documentation": "https://libcoveofds.readthedocs.io/en/latest/",
        "Issues": "https://github.com/Open-Telecoms-Data/lib-cove-ofds/issues",
        "Source": "https://github.com/Open-Telecoms-Data/lib-cove-ofds",
    },
    description="A data review library",
    packages=find_packages(),
    long_description="A data review library",
    python_requires=">=3.8",
    install_requires=[
        "Django>3.2,<3.3",
        "libcoveweb>=0.21.0",
        "libcove>=0.22.0",
    ],
    extras_require={
        "dev": ["pytest", "flake8", "black==22.3.0", "isort", "mypy", "Sphinx"]
    },
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ],
    entry_points="""[console_scripts]
libcoveofds = libcoveofds.cli.__main__:main""",
    include_package_data=True,
)

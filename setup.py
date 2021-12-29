#!/usr/bin/env python3
import setuptools

from pygmail import __version__

with open("README.md") as fh:
    long_description = fh.read()

required_requirements = [
    "click"
]

setuptools.setup(
    name="py-gmail",  # Replace with your own username
    version=__version__,
    author="JunWei Song",
    author_email="sungboss2004@gmail.com",
    description="Python interface for playing Gmail",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krnick/py-gmail",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "pygmail=pygmail.cli:entry_point"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=required_requirements,
)

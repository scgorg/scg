#!/usr/bin/env python3
import setuptools

from scg import __version__

with open("README.md") as fh:
    long_description = fh.read()

required_requirements = [
    "click",
    "pycryptodome"
]

setuptools.setup(
    name="scg",  # Replace with your own username
    version=__version__,
    author="JunWei Song",
    author_email="sungboss2004@gmail.com",
    description="Send custom Gmail with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scgorg/scg",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "scg=scg.cli:entry_point"
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

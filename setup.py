# NOQA: D100

import os

from setuptools import find_packages
from setuptools import setup

def read_file(*paths):  # NOQA: E302
    """Read a file.
    """
    try:
        with open(os.path.join(os.path.dirname(__file__), *paths)) as file:
            return file.read()
    except FileNotFoundError:
        return ""

version = "0.1.0"  # NOQA: E305

long_description = "\n\n".join((
    read_file("README.rst"),
    read_file("CONTRIBUTING.rst"),
    read_file("CHANGES.rst"),
    read_file("LICENSE.srt"),
))

setup(
    name="batlock666.cropscale",
    version=version,
    description="Calculate a crop/scale-filter for ffmpeg.",
    long_description=long_description,
    # get more strings from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Video",
    ],
    keywords="cropscale",
    author="Bert Vanderbauwhede",
    author_email="batlock666@gmail.com",
    url="https://github.com/batlock666/batlock666.cropscale.git",
    license="GPL",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["batlock666"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
    ],
)

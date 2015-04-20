""" The simplest setup.py """

import setuptools

setuptools.setup(
    name="ExhaustiveSearch",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
)

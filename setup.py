#!/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='bmp',
    version='0.0.0',
    description='Python implementation of BMP',
    long_description=readme,
    author='tama@ttk1',
    author_email='tama@ttk1.net',
    url='https://github.com/ttk1/bmpy',
    license=license,
    packages=find_packages(exclude=('test',))
)

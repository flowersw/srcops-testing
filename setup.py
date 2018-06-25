#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# thoth-package-extract
# Copyright(C) 2018 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A foo module for SrcOps-testing."""


import os
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='thoth-srcops-testing',
    version='0.1.0-rc.1',
    zip_safe=False,
    author='Christoph Görn',
    author_email='goern@redhat.com',
    maintainer='Christoph Görn',
    maintainer_email='goern@redhat.com',
    description='This is a test.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['food'],
    url='https://github.com/thoth-station/srcops-testing',
    license='GPLv3+',
    keywords='srcops thoth zuul',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)

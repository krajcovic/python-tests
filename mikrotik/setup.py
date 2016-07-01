#!/usr/bin/python3
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="rosapi_slacker_publish",
    packages=["rosapi_slacker_publish"],
    version="0.0.1",
    description="Universal encoding detector",
    author="Dusan Krajcovic",
    author_email="dusan.krajcovic@gmail.com",
    url="http://krajcovic.info/rosapi/",
    keywords=["mikrotik", "rosapi"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - pre-alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Mikrotik API :: Publish",
    ],
    long_description="""\
Publish rosapi information to slack with slacker module.
-------------------------------------
This version requires Python 3 or later; a Python 2 version is not supported.
"""
)

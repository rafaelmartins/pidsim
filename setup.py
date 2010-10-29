#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import pidsim

setup(
    name = pidsim.__name__,
    version = pidsim.__version__,
    license = pidsim.__license__,
    description = pidsim.__description__,
    author = pidsim.__author__,
    author_email = pidsim.__email__,
    url = pidsim.__url__,
    packages = ['pidsim'],
    package_dir={'pidsim': 'pidsim'},
)

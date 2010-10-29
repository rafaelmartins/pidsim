#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import pidsim

setup(
    name = 'pidsim',
    version = pidsim.__version__,
    license = pidsim.__license__,
    description = pidsim.__description__,
    long_description = open('README.rst').read(),
    author = pidsim.__author__,
    author_email = pidsim.__email__,
    url = pidsim.__url__,
    platforms = 'any',
    packages = ['pidsim'],
    package_dir={'pidsim': 'pidsim'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)


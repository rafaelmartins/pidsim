#!/usr/bin/env python

import warnings
warnings.filterwarnings('ignore')

from sys import path
from os.path import abspath
path.insert(0, abspath('src'))

from setuptools import setup
import controlsystems

setup(
    name=controlsystems.__name__,
    version=controlsystems.__version__,
    license=controlsystems.__license__,
    description=controlsystems.__description__,
    author=controlsystems.__author__,
    author_email=controlsystems.__email__,
    url=controlsystems.__url__,
    packages=[controlsystems.__name__],
    package_dir={
        controlsystems.__name__: 'src/%s' % controlsystems.__name__
    },
)

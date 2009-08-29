#!/usr/bin/env python

import warnings
warnings.filterwarnings('ignore')

from distutils.core import setup
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
        controlsystems.__name__: controlsystems.__name__
    },
)

#!/usr/bin/env python

from setuptools import setup

setup(name='python-controlsystems',
    version='0.2.1',
    license='GPL2',
    description='A python library for study of control systems',
    author=['Rafael G. Martins'],
    author_email=['rafael@rafaelmartins.com'],
    url='http://pycontrolsystems.com/projects/show/controlsystems',
    package_dir={'controlsystems': 'src/controlsystems'},
    packages=['controlsystems'], 
)

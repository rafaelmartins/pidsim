"""Python Control Systems core package

This package implements a basic toolbox for the study of the Control
Systems, using Python.

To use the examples, please initialize this package, using:

    >>> from controlsystems.types import *
    >>> from controlsystems.discretization import *
    >>> from controlsystems.pid_simulation import *
    >>> from controlsystems.error import *

If you need some help with the use, or can help with the development,
please contact the author via email or visit our project website:

http://packages.python.org/controlsystems/

All the help is welcome! :)

"""

#TODO: create unit tests

__all__ = ['types', 'discretization', 'pid_tuning']

__author__ = 'Rafael Goncalves Martins'
__email__ = 'rafael@rafaelmartins.com'

__description__ = 'A Python library for the study of the Control Systems'
__url__ = 'http://packages.python.org/controlsystems/'
__copyright__ = '(c) 2009 %s' % __author__
__license__ = 'GPLv2'

__version__ = '1.0rc3'
__status__ = 'Beta'


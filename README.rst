PIDSIM core package
===================

.. warning::

   This package just have the python modules, not any GUI.

This package implements a basic toolbox for the study of the Control
Systems and the simulation of PID controllers, using Python.

To use the examples, please initialize this package, using::

    >>> from pidsim.core.types import *
    >>> from pidsim.core.discretization import *
    >>> from pidsim.core.pid_simulation import *
    >>> from pidsim.core.error import *

If you need some help with the use, or can help with the development,
please contact the author via email or visit our project website:

http://pidsim.org/

All the help is welcome! :)


Basic installation
~~~~~~~~~~~~~~~~~~

To install, type::

    # python setup.py install

or use pip::

    # pip install pidsim

To build doc (you'll need sphinx), type::

    # make -C doc html


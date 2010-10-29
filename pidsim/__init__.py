# -*- coding: utf-8 -*-
"""
    pidsim
    ~~~~~~

    Main package of pidsim.
    
    This package implements a basic toolbox for the study of the Control
    Systems and simulate PID controllers using Python.

    :copyright: (c) 2009-2010 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

#TODO: write unit tests and docs

__all__ = ['discretization', 'error', 'pid_simulation', 'types']
__author__ = 'Rafael Goncalves Martins'
__email__ = 'rafael@rafaelmartins.eng.br'
__description__ = 'PID Controllers simulator'
__url__ = 'http://pidsim.org/'
__copyright__ = '(c) 2009-2010 %s' % __author__
__license__ = 'GPL-2'
__version__ = '1.0rc3+'


import discretization
import error
import pid_simulation
import types

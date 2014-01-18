# -*- coding: utf-8 -*-
"""
    pidsim.core
    ~~~~~~~~~~~

    Core package of pidsim.

    This package implements a basic toolbox for the study of the Control
    Systems and simulate PID controllers using Python.

    :copyright: 2009-2010 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

#TODO: write unit tests and docs

__all__ = ['discretization', 'error', 'helpers', 'pade', 'pid', 'types']
__author__ = 'Rafael Goncalves Martins'
__email__ = 'rafael@rafaelmartins.eng.br'
__description__ = 'PID Controller simulator (PIDSIM)'
__url__ = 'https://github.com/rafaelmartins/pidsim'
__copyright__ = '(c) 2009-2010 %s' % __author__
__license__ = 'GPL-2'
__version__ = '1.0rc6'


import discretization
import error
import helpers
import pade
import pid
import types

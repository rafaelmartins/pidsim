# -*- coding: utf-8 -*-
"""
    pidsim.core.pid
    ~~~~~~~~~~~~~~~

    PID Controller package.
    
    For a quick reference about PID controllers, see:
    http://wikis.controltheorypro.com/index.php?title=PID_Control
    
    :copyright: 2009-2010 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

__all__ = ['identification', 'tuning']


import identification
import tuning
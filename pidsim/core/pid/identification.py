# -*- coding: utf-8 -*-
"""
    pidsim.core.pid.identification
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    PID Controller identification methods.
    
    This module implements some PID identification methods for simulation, based
    on the reaction curve. Take care to choose a total time after the
    system stabilization for now.
    
    :copyright: 2009-2010 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

__all__ = ['tuning_line']

from pidsim.core.helpers import get_time_near


def tuning_line(t, y):
    """Reaction curve tuning rule"""
    
    k = y[-1]
    
    y28 = 0.28*k
    y63 = 0.632*k
    yp = max(y)
    
    t28 = get_time_near(t, y, y28)
    t63 = get_time_near(t, y, y63)
    
    alpha = (t63 - t28)/(y63 - y28)
    
    t0 = t28 - (y28 * alpha)
    tp = t63 + ((yp - y63) * alpha)
    
    return [t0, t28, t63, tp], [0, y28, y63, yp]

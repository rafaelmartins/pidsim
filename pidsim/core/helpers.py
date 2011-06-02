# -*- coding: utf-8 -*-
"""
    pidsim.core.helpers
    ~~~~~~~~~~~~~~~~~~~

    Helper functions.
    
    :copyright: 2009-2010 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

__all__ = ['get_time_near']


def get_time_near(t, y, point):
    """Get time near
    
    Returns the time 't' of the point 'y' more near of the desired
    point 'point'.
    
    """
    
    tolerance_range = max(y) - min(y)
    
    for i in range(len(y)):
        
        tolerance = abs(y[i] - point)
        
        if tolerance < tolerance_range:
            my_t = t[i]
            tolerance_range = tolerance
    
    return my_t
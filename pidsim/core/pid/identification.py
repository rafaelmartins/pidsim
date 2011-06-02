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

__all__ = ['Alfaro', 'Broida', 'ChenYang', 'Ho', 'Smith', 'Viteckova']

from pidsim.core.helpers import get_time_near


class IdentificationMethod:
    
    point1 = None # in percents
    point2 = None # in percents
    
    def __init__(self, t, y):
        self.t = t
        self.y = y
    
    @property
    def points(self):
        if self.point1 is None or self.point2 is None:
            raise NotImplementedError('You need shouldn\'t instance this ' \
                                      'class directly')
        k = self.y[-1]
        y1 = (float(self.point1)/100) * k
        y2 = (float(self.point2)/100) * k
        t1 = get_time_near(self.t, self.y, y1)
        t2 = get_time_near(self.t, self.y, y2)
        return (t1, y1), (t2, y2)
    
    @property
    def tuning_line(self):
        (t1, y1), (t2, y2) = self.points
        alpha = (t2 - t1)/(y2 - y1)
        yp = max(self.y)
        t0 = t1 - (y1 * alpha)
        tp = t2 + ((yp - y2) * alpha)
        return [t0, t1, t2, tp], [0, y1, y2, yp]


class Alfaro(IdentificationMethod):
    point1 = 25.0
    point2 = 75.0


class Broida(IdentificationMethod):
    point1 = 28.0
    point2 = 40.0


class ChenYang(IdentificationMethod):
    point1 = 33.0
    point2 = 67.0


class Ho(IdentificationMethod):
    point1 = 35.0
    point2 = 85.0


class Smith(IdentificationMethod):
    point1 = 28.2
    point2 = 63.2


class Viteckova(IdentificationMethod):
    point1 = 33.0
    point2 = 70.0


class JahanmiriFallahi(IdentificationMethod):
    point1 = 2.0
    point2 = 70.0
    point3 = 90.0
    
    @property
    def points(self):
        k = self.y[-1]
        y3 = (float(self.point3)/100) * k
        t3 = get_time_near(self.t, self.y, y3)
        a, b = IdentificationMethod.points(self)
        return a, b, (t3, y3)
    
    @property
    def tuning_line(self):
        # XXX: this method is wrong
        (t1, y1), (t2, y2) = self.points
        alpha = (t2 - t1)/(y2 - y1)
        yp = max(self.y)
        t0 = t1 - (y1 * alpha)
        tp = t2 + ((yp - y2) * alpha)
        return [t0, t1, t2, tp], [0, y1, y2, yp]
    

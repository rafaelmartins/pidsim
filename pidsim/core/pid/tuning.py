# -*- coding: utf-8 -*-
"""
    pidsim.core.pid.tuning
    ~~~~~~~~~~~~~~~~~~~~~~

    PID Controller tuning methods.
    
    This module implements some PID tuning methods for simulation, based
    on the reaction curve. Take care to choose a total time after the
    system stabilization for now.
    
    :copyright: 2009-2010 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

#TODO: find the stabilization time
#TODO: error handling
#TODO: improve the documentation

__all__ = [
    'ZieglerNichols',
    'CohenCoon',
    'ChienHronesReswick0',
    'ChienHronesReswick20',
]

from pidsim.core.error import ControlSystemsError


class TuningMethod:
    
    def __init__(self, t, y, i_method):
        self.t = t
        self.y = y
        self.k = y[-1]
        self.ident = i_method(t, y)
    
    @property
    def times(self):
        p1, p2 = self.ident.points
        return p1[0], p2[0]
    
    @property
    def tau(self):
        t1, t2 = self.times
        return 1.5 * (t2 - t1)
    
    @property
    def Tm(self):
        t1, t2 = self.times
        return 1.5 * (t1 - (t2 / 3))
    
    @property
    def gains(self):
        raise NotImplementedError
        

class ZieglerNichols(TuningMethod):

    @property
    def gains(self):
        kp = (1.2 * self.tau) / (self.k * self.Tm)
        Ti = 2 * self.Tm
        Td = self.Tm / 2
        ki = kp / Ti
        kd = kp * Td
        return kp, ki, kd


class CohenCoon(TuningMethod):
    
    @property
    def gains(self):
        R = self.Tm / self.tau
        kp = self.tau / (self.k * self.Tm * ((4/3) + (R / 4)))
        Ti = self.Tm * ((32 + 6*R)/(13 + 8*R))
        Td = 4 / (13 + 8*R)
        ki = kp / Ti
        kd = kp * Td
        return kp, ki, kd


class ChienHronesReswick0(TuningMethod):

    @property
    def gains(self):
        kp = (0.6 * self.tau) / (self.k * self.Tm)
        Ti = self.tau
        Td = self.Tm / 2
        ki = kp / Ti
        kd = kp * Td
        return kp, ki, kd


class ChienHronesReswick20(TuningMethod):
    
    @property
    def gains(self):
        kp = (0.95 * self.tau) / (self.k * self.Tm)
        Ti = 1.4 * self.tau
        Td = 0.47 * self.Tm
        ki = kp / Ti
        kd = kp * Td
        return kp, ki, kd

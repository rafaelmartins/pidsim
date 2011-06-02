# -*- coding: utf-8 -*-
"""
    pidsim.core.approximation
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Implementation of Pade's approximation method.
    
    Reference:
    http://wwwhome.math.utwente.nl/~vajtam/publications/temp00-pade.pdf

    :copyright: 2010 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

__all__ = [
    'Pade1',
    'Pade2',
    'Pade3',
    'Pade4',
    'Pade5',
]

from pidsim.core.types import poly, tf

def Pade1(t):
    """First order Pade approximation"""
    
    num = poly([-t, 2])
    den = poly([t, 2])
    num = num.mult(1.0/den[0])
    den = den.mult(1.0/den[0])
    return tf(num, den)


def Pade2(t):
    """Second order Pade approximation"""
    num = poly([t*t, -6*t, 12])
    den = poly([t*t, 6*t, 12])
    num = num.mult(1.0/den[0])
    den = den.mult(1.0/den[0])
    return tf(num, den)


def Pade3(t):
    """Third order Pade approximation"""
    num = poly([-t*t*t, 12*t*t, -60*t, 120])
    den = poly([t*t*t, 12*t*t, 60*t, 120])
    num = num.mult(1.0/den[0])
    den = den.mult(1.0/den[0])
    return tf(num, den)


def Pade4(t):
    """Fourth order Pade approximation"""
    num = poly([t*t*t*t, -20*t*t*t, 180*t*t, -840*t, 1680])
    den = poly([t*t*t*t, 20*t*t*t, 180*t*t, 840*t, 1680])
    num = num.mult(1.0/den[0])
    den = den.mult(1.0/den[0])
    return tf(num, den)


def Pade5(t):
    """Fifth order Pade approximation"""
    num = poly([-t*t*t*t*t, 30*t*t*t*t, -420*t*t*t, 3360*t*t, -15120*t, 30240])
    den = poly([t*t*t*t*t, 30*t*t*t*t, 420*t*t*t, 3360*t*t, 15120*t, 30240])
    num = num.mult(1.0/den[0])
    den = den.mult(1.0/den[0])
    return tf(num, den)


methods = {
    1: Pade1,
    2: Pade2,
    3: Pade3,
    4: Pade4,
    5: Pade5,
}

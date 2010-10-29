# -*- coding: utf-8 -*-
"""
    pidsim.pid_simulation
    ~~~~~~~~~~~~~~~~~~~~~

    PID Controller simulation methods.
    
    This module implements some PID tuning methods for simulation, based
    on the reaction curve. Take care to choose a total time after the
    system stabilization for now.
    
    For a quick reference about PID controllers, see:
    http://wikis.controltheorypro.com/index.php?title=PID_Control
    
    :copyright: (c) 2009-2010 by Rafael Goncalves Martins
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
    'get_time_near',
    'tuning_rule',
]


def ZieglerNichols(g, sample_time, total_time, n_method):
    """ZieglerNichols tuning method
    
    Returns the 'kp', 'ki' and 'kd' gains to a PID controller, using
    the Ziegler-Nichols tuning method, based on the reaction curve. For
    example (using Euler to discretize)::
    
        >>> g = TransferFunction([1], [1, 2, 3])
        >>> kp, ki, kd = ZieglerNichols(g, 0.01, 10, Euler)
        >>> print kp
        7.25920108978
        >>> print ki
        11.9003296554
        >>> print kd
        1.10702816619
    
    """
    
    t, y = n_method(g, sample_time, total_time)
    
    k = y[-1]
    
    t63 = get_time_near(t, y, 0.632*k)
    t28 = get_time_near(t, y, 0.28*k)
    tau = 1.5*(t63-t28)
    L = 1.5*(t28-(t63/3))
    
    kp = (1.2*tau)/(k*L)
    Ti = 2*L
    Td = L/2
    
    ki = kp/Ti
    kd = kp*Td
    
    return kp, ki, kd


def CohenCoon(g, sample_time, total_time, n_method):
    """CohenCoon tuning method
    
    Returns the 'kp', 'ki' and 'kd' gains to a PID controller, using
    the Cohen-Coon tuning method, based on the reaction curve. For
    example (using Euler to discretize)::
    
        >>> g = TransferFunction([1], [1, 2, 3])
        >>> kp, ki, kd = CohenCoon(g, 0.01, 10, Euler)
        >>> print kp
        5.38204782425
        >>> print ki
        8.56051231163
        >>> print kd
        1.26879134141
    
    """
    
    t, y = n_method(g, sample_time, total_time)
    
    k = y[-1]
    
    t63 = get_time_near(t, y, 0.632*k)
    t28 = get_time_near(t, y, 0.28*k)
    tau = 1.5*(t63-t28)
    L = 1.5*(t28-(t63/3))
    
    R = L/tau
    kp = tau/(k*L*((4/3)+(R/4)))
    Ti = L*((32 + 6*R)/(13 + 8*R))
    Td = 4/(13 + 8*R)
    
    ki = kp/Ti
    kd = kp*Td
    
    return kp, ki, kd


def ChienHronesReswick0(g, sample_time, total_time, n_method):
    """ChienHronesReswick0 tuning method
    
    Returns the 'kp', 'ki' and 'kd' gains to a PID controller, using
    the Chien-Hrones-Reswick (0%) tuning method, based on the reaction
    curve. For example (using Euler to discretize)::
    
        >>> g = TransferFunction([1], [1, 2, 3])
        >>> kp, ki, kd = ChienHronesReswick0(g, 0.01, 10, Euler)
        >>> print kp
        3.62960054489
        >>> print ki
        5.90178950389
        >>> print kd
        0.553514083096
    
    """
    
    t, y = n_method(g, sample_time, total_time)
    
    k = y[-1]
    
    t63 = get_time_near(t, y, 0.632*k)
    t28 = get_time_near(t, y, 0.28*k)
    tau = 1.5*(t63-t28)
    L = 1.5*(t28-(t63/3))
    
    kp = (0.6*tau)/(k*L)
    Ti = tau
    Td = L/2
    
    ki = kp/Ti
    kd = kp*Td
    
    return kp, ki, kd


def ChienHronesReswick20(g, sample_time, total_time, n_method):
    """ChienHronesReswick20 tuning method
    
    Returns the 'kp', 'ki' and 'kd' gains to a PID controller, using
    the Chien-Hrones-Reswick (20%) tuning method, based on the reaction
    curve. For example (using Euler to discretize)::
    
        >>> g = TransferFunction([1], [1, 2, 3])
        >>> kp, ki, kd = ChienHronesReswick20(g, 0.01, 10, Euler)
        >>> print kp
        5.74686752941
        >>> print ki
        6.6746428913
        >>> print kd
        0.823813460341
    
    """
    
    t, y = n_method(g, sample_time, total_time)
    
    k = y[-1]
    
    t63 = get_time_near(t, y, 0.632*k)
    t28 = get_time_near(t, y, 0.28*k)
    tau = 1.5*(t63-t28)
    L = 1.5*(t28-(t63/3))
    
    kp = (0.95*tau)/(k*L)
    Ti = 1.4*tau
    Td = 0.47*L
    
    ki = kp/Ti
    kd = kp*Td
    
    return kp, ki, kd


def get_time_near(t, y, point):
    """Get time near
    
    Auxiliary function.
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


def tuning_rule(t, y):
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
    

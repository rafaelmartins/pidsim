#-*- encoding: utf-8 -*-
#
#       chienhronesreswick0.py
#       
#       Copyright 2009 Rafael G. Martins <rafael@rafaelmartins.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from gettimenear import get_time_near

def ChienHronesReswick0(g, sample_time, total_time, n_method):
    
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

if __name__ == '__main__':
    
    from rk4 import RK4
    from transferfunction import TransferFunction
    
    g = TransferFunction([1], [1, 2, 3])
    
    print ChienHronesReswick0(g, 0.01, 10, RK4)

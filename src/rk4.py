#-*- encoding: utf-8 -*-
#
#       rk4.py
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

from transferfunction import TransferFunction
from statespace import StateSpace
from matrix import Matrix, Zeros, Identity
from error import ControlSystemsError

def RK4(g, sample_time, total_time):
    
    if not isinstance(g, TransferFunction):
        raise ControlSystemsError('Parameter must be a Transfer Function')

    ss = StateSpace(g)
    
    samples = int(total_time/sample_time) + 1
    
    t = [sample_time * a for a in range(samples)]
    
    x = Zeros(ss.a.rows, 1)
    y = []
    
    eye = Identity(ss.a.rows)
    
    a1 = ss.a.mult(sample_time) # A*T
    a2 = ss.b.mult(sample_time) # B*T
    a3 = (ss.a * ss.a).mult(sample_time * sample_time) # A^2*T^2
    a4 = a3.mult(0.5) # (A^2*T^2)/2
    a5 = (ss.a * ss.b).mult(sample_time * sample_time) # A*B*T^2
    a6 = a5.mult(0.5) # (A*B*T^2)/2
    a7 = (ss.a*ss.a*ss.a).mult(sample_time * sample_time * sample_time)
    a8 = a7.mult(0.25)
    a9 = (ss.a*ss.a*ss.b).mult(sample_time * sample_time * sample_time)
    a10 = a9.mult(0.25)
    a11 = a7.mult(0.5)
    a12 = (ss.a*ss.a*ss.a*ss.a).mult(sample_time * sample_time * sample_time * sample_time)
    a13 = a12.mult(0.25)
    a14 = ss.a.mult(sample_time * sample_time)
    a15 = a14*ss.b
    a16 = a9.mult(0.5)
    a17 = (ss.a*ss.a*ss.a*ss.b).mult(sample_time * sample_time * sample_time * sample_time)
    a18 = a17.mult(0.25)
    
    for i in range(samples):
        k1 = a1*x + a2
        k2 = (a1 + a4)*x + a6 + a2
        k3 = (a1 + a4 + a8)*x + a2 + a6 + a10;
        k4 = (a1 + a3 + a11 + a13)*x + a15 +a16 + a18 + a2
        x = x + k1.mult(1.0/6.0) + k2.mult(1.0/3.0) + k3.mult(1.0/3.0) + k4.mult(1.0/6.0)
        y.append((ss.c*x)[0][0] + ss.d[0][0])

    return t, y

if __name__ == '__main__':
   
    g = TransferFunction([1], [1, 2, 3])
    
    print RK4(g, 0.01, 10)

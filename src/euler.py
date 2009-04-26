#-*- encoding: utf-8 -*-
#
#       euler.py
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

def Euler(g, sample_time, total_time):
    
    if not isinstance(g, TransferFunction):
        raise ControlSystemsError('Parameter must be a Transfer Function')

    ss = StateSpace(g)
    
    samples = int(total_time/sample_time) + 1
    
    t = [sample_time * a for a in range(samples)]
    
    x = Zeros(ss.a.rows, 1)
    y = []
    
    eye = Identity(ss.a.rows)
    
    for i in range(samples):
        
        x = ((eye + ss.a.mult(sample_time)) * x) + ss.b.mult(sample_time)
        
        aux = 0
        
        for j in range(ss.c.cols):
            aux += x[j][0] * ss.c[0][j]
        
        y.append(aux)

    return t, y

if __name__ == '__main__':
   
    g = TransferFunction([1], [1, 2, 3])
    
    print Euler(g, 0.01, 10)

#-*- encoding: utf-8 -*-
#
#       statespace.py
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
from matrix import Matrix, Zeros
from error import ControlSystemsError

class StateSpace(object):
    
    def __init__(self, a, b = None, c = None, d = [[0]]):
        
        if isinstance(a, TransferFunction):
            if len(a.num) > len(a.den):
                raise ControlSystemsError('More zeros than poles.')
            
            self.__tf2ss(a)
        else:
            self.__ss(a, b, c, d)
    
    def __ss(self, a, b, c, d):
        
        self.a = Matrix(a)
        self.b = Matrix(b)
        self.c = Matrix(c)
        self.d = Matrix(d)
    
    def __tf2ss(self, tf):
        
        if len(tf.num) == 0 or len(tf.den) == 0:
            raise ControlSystemsError('Invalid Transfer Function')
        
        #preparing A
        order = len(tf.den) - 1
        a = Zeros(order)
        for i in range(order-1):
            for j in range(1, order):
                if (i+1) == j:
                    a[i][j] = 1
        den = tf.den[:]
        den.reverse()
        for i in range(order):
            a[order-1][i] = -den[i]
        
        #preparing B
        b = Zeros(order, 1)
        if len(tf.num) == 1:
            b[order-1][0] = tf.num[0]
        else:
            b[order-1][0] = 1

        #preparing C
        c = Zeros(1, order)
        if len(tf.num) == 1:
            c[0][0] = 1
        else:
            num = tf.num[:]
            num.reverse()
            for i in range(order):
                try:
                    c[0][i] = num[i]
                except IndexError:
                    pass
        
        self.__ss(a, b, c, [[0]])
    
    def __str__(self):
        
        ret = 'State-Space model:\n\nMatrix A:\n'
        ret += str(self.a) + '\n\n'
        ret += 'Matrix B:\n'
        ret += str(self.b) + '\n\n'
        ret += 'Matrix C:\n'
        ret += str(self.c) + '\n\n'
        ret += 'Matrix D:\n'
        ret += str(self.d) + '\n'
        return ret

if __name__ == '__main__':
    
    print StateSpace([
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ],
    [
        [1],
        [2],
        [3],
    ],
    [
        [1,2,3],
    ])
    
    print
    
    print StateSpace(TransferFunction([1], [1, 2, 3]))

#-*- encoding: utf-8 -*-
#
#       transferfunction.py
#       
#       Copyright 2008-2009 Rafael G. Martins <rafael@rafaelmartins.com>
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

from polynomial import Polynomial

class TransferFunction(object):
  
    def __init__(self, num, den):
        self.num = Polynomial(num)
        self.num.var = 's'
        self.den = Polynomial(den)
        self.den.var = 's'
    
    def __str__(self):
        len_max = (len(str(self.num)) > len(str(self.den))) and len(str(self.num)) or len(str(self.den))
        response  = 'Transfer Function:\n\n'
        response += str(self.num).center(len_max) + '\n'
        response += '-' * len_max + '\n'
        response += str(self.den).center(len_max) + '\n'
        return response

    def __mul__(self, tf):
        num = self.num * tf.num
        den = self.den * tf.den
        return TransferFunction(num, den)
    
    def __add__(self, tf):
        num = (self.num*tf.den) + (tf.num*self.den)
        den = self.den * tf.den
        return TransferFunction(num, den)
    
    def __sub__(self, tf):
        num = (self.num*tf.den) - (tf.num*self.den)
        den = self.den * tf.den
        return TransferFunction(num, den)
    
    def simplify(self):
        num = self.num[:]
        den = self.den[:]
        
        mdc = 1
        for i in range(1, max([max(num), max(den)])):
            die = 0
            if len(self.num) == 1:
                mdc = self.num[0]
            else:
                for j in range(len(num)):
                    if num[j] % i != 0:
                        die = 1
                for j in range(len(den)):
                    if den[j] % i != 0:
                        die = 1
                if not die:
                    mdc = i
        return TransferFunction(num, den).div(mdc)
    
    def mult(self, a):
        
        return TransferFunction(self.num.mult(a), self.den.mult(a))
    
    def div(self, a):
        num = self.num[:]
        den = self.den[:]
        
        for i in range(len(num)):
            num[i] /= a
        for i in range(len(den)):
            den[i] /= a
        return TransferFunction(num, den)

tf = TransferFunction

if __name__ == '__main__':
    
    a = TransferFunction([1,2], [1,2,3])
    b = TransferFunction([1], [1,0,0])
    
    print a
    print
    print b
    print
    print a * b
    print
    print a.mult(2)
    

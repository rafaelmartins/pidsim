#!/usr/bin/env python

from polynomial import Polynomial

class TransferFunction(object):
  
    def __init__(self, num, den):
        self.num = Polynomial(num)
        self.den = Polynomial(den)
    
    def __str__(self):
        len_max = (len(str(self.num)) > len(str(self.den))) and len(str(self.num)) or len(str(self.den))
        response  = 'Transfer Function:\n\n'
        response += str(self.num).center(len_max) + '\n'
        response += '-' * len_max + '\n'
        response += str(self.den).center(len_max) + '\n'
        return response

if __name__ == '__main__':
    a = TransferFunction([1,2], [1,2,3])
    print a

#-*- encoding: utf-8 -*-
#
#       polinomyal.py
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

class Polynomial(list):
    
    var = 'x'
    
    def __str__(self):
        poly = self[:]
        poly.reverse()
        response = ''
        for order in range(len(self) - 1, -1, -1): 
            coefficient = poly.pop()
            if coefficient == 0:
                continue
            if order != len(self) - 1:
                if coefficient > 0:
                    response += ' + '
                else:
                    response += ' - '
            if abs(coefficient) > 1 or order == 0:
                response += str(abs(coefficient))
            if order > 0:
                response += self.var
            if order > 1:
                response += '^' + str(order)
        return response
    

    def __add__(self, term):
        
        if not isinstance(term, Polynomial):
            raise ControlSystemsError('Operands must be polynomials')
        
        a = self[:]
        a.reverse()
        b = term[:]
        b.reverse()
        order = (len(a) > len(b)) and len(a) or len(b)
        result = [0 for x in range(order)]
        
        for x in range(order):
            try:
                result[x] += a[x]
            except IndexError:
                pass
            try:
                result[x] += b[x]
            except IndexError:
                pass
        
        result.reverse()
        return Polynomial(result)


    def __sub__(self, term):
        
        term_aux = [-x for x in term]
        return self.__add__(term_aux)
    
    
    def __mul__(self, term):
        
        if not isinstance(term, Polynomial):
            raise ControlSystemsError('Operands must be polynomials')
        
        a = self[:]
        b = term[:]
        result = []
        j = 0
        
        for x in a:
            i = 0
            for y in b:
                result.append((i + j, x * y))
                i += 1
            j += 1
        
        ord_res = 0
        
        for x, y in result:
            if x > ord_res:
                ord_res = x
        
        resp = [0 for x in range(ord_res + 1)]
        
        for x in range(ord_res + 1):
            resp[x] = 0
            for c, d in result:
                if c == x:
                    resp[x] += d
        
        return Polynomial(resp)

poly = Polynomial

if __name__ == '__main__':
    
    a = Polynomial([1,2,3])
    b = Polynomial([2,2,3])
    
    print a
    print b
    print a + b
    print a - b
    print a * b
    

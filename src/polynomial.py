#!/usr/bin/env python

class Polynomial(list):
  
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
                response += 'x'
            if order > 1:
                response += '^' + str(order)
        return response
    

    def __add__(self, term):
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
        a = self[:]
        b = term[:]
        
        ind = 0
        aux = []
        for x in a:
            aux.append((ind, x))
            ind += 1
        a = aux
        
        ind = 0
        aux = []
        for x in b:
            aux.append((ind, x))
            ind += 1
        b = aux
        
        result = []
        
        for ord1, coef1 in a:
            for ord2, coef2 in b:
                result.append((ord1 + ord2, coef1 * coef2))
        
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
        

if __name__ == '__main__':
    a = Polynomial([1,2,3])
    b = Polynomial([1,2,3])
    print a
    print b
    print a * b

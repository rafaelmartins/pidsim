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

if __name__ == '__main__':
    a = Polynomial([1,0,1,5])
    b = Polynomial([2,5])
    print a
    print b
    print a - b

#-*- encoding: utf-8 -*-
#
#       matrix.py
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

from error import ControlSystemsError

class Matrix(list):
    
    def __init__(self, mat):
        
        list.__init__(self, mat)
        self.rows = len(self)
        self.cols = []
        
        for i in range(self.rows):
            
            try:
                if len(self[i]) == self.cols or self.cols == []:
                    self.cols = len(self[i])
                else:
                    raise ControlSystemsError('Invalid Matrix size')
            except:
                raise ControlSystemsError('Invalid Matrix size')

    def __str__(self):
        
        ret = ''
        
        for i in range(self.rows):
            for j in range(self.cols):
                ret += '%s\t' % self[i][j]
            if i < (self.rows - 1):
                ret += '\n'
        
        return ret

    def __call__(self, row, col=None):
        
        if col == None:
            return Matrix([self[row]])
        else:
            return self[row][cow]

    def __add__(self, mat):
        
        rows = self.rows > mat.rows and self.rows or mat.rows
        cols = self.cols > mat.cols and self.cols or mat.cols
        
        res = Zeros(rows, cols)
        
        for i in range(rows):
            for j in range(cols):
                try:
                    res[i][j] += self[i][j]
                except IndexError:
                    pass
                try:
                    res[i][j] += mat[i][j]
                except IndexError:
                    pass
        
        return res
    
    def __sub__(self, mat):
        
        aux = mat.mult(-1)
        return self.__add__(aux)
    
    def __mul__(self, mat):
        
        if not isinstance(mat, Matrix):
            raise ControlSystemsError('Use only matrices when multiplying')
        
        if self.cols != mat.rows:
            raise ControlSystemsError('Invalid Matrices size for multiply')
        
        res = Zeros(self.rows, mat.cols)
        
        for i in range(self.rows):
            for j in range(mat.cols):
                for aux in range(self.cols):
                    res[i][j] += self[i][aux] * mat[aux][j]
        
        return res

    def mult(self, num):
        
        aux = Zeros(self.rows, self.cols)
        
        for i in range(self.rows):
            for j in range(self.cols):
                aux[i][j] = self[i][j] * num

        return aux
    
    def transpose(self):
        
        aux = Zeros(self.cols, self.rows)
        
        for i in range(self.rows):
            for j in range(self.cols):
                aux[j][i] = self[i][j]
        
        return aux

class Zeros(Matrix):
    
    def __init__(self, rows, cols=None):
        
        if cols == None:
            cols = rows
        
        aux = []
        
        for i in range(rows):
            aux.append([])
            for j in range(cols):
                aux[i].append(0)
        
        Matrix.__init__(self, aux)

class Identity(Matrix):
    
    def __init__(self, order):
        
        aux = []
        
        for i in range(order):
            aux.append([])
            for j in range(order):
                if i == j:
                    aux[i].append(1)
                else:
                    aux[i].append(0)
        
        Matrix.__init__(self, aux)


if __name__ == '__main__':
    
    a = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    b = Matrix([
        [2, 3, 4],
        [5, 6, 6],
    ])
    
    c = Matrix([
        [1, 2],
        [3, 4],
    ])

    print a
    print
    print b
    print
    print a + b
    print
    print a - b
    print
    print c * a
    print
    print a.transpose()
    print
    print a.mult(4)
    print
    print Zeros(4)
    print
    print Identity(4)

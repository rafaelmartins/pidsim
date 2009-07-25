"""Data Types for Control Systems

This module implements some data types for Control Systems,like:
Transfer Functions, State-Space models and others.

"""

__all__ = [
    'Polynomial',
    'Matrix', 'ZerosMatrix', 'IdentityMatrix',
    'TransferFunction',
    'StateSpace',
]

#TODO: implement zero-pole data type

from error import ControlSystemsError

class Polynomial(list):
    """Polynomial type
    
    This class implements the Polynomial type, based on Python lists.
    The polinomial object is a list of coeficients, for example:
    
        >>> a = Polynomial([1, 2, 3])
        >>> print a
        x^2 + 2x + 3
    
    """
    
    var = 'x'
    
    def __str__(self):
        """String representation
        
        This method returns the string representation of polynomials,
        like:
        
            x^2 + 2x + 3
        
        """
        
        #TODO: fix bug of first term negative
        
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
        """Operation of addition
        
        This method returns a Polynomial object with the result of the
        addition of 'self' Polynomial and 'term' Polynomial, like:
        
            >>> a = Polynomial([1, 2, 3])
            >>> b = Polynomial([2, 3, 4])
            >>> c = a + b
            >>> print c
            3x^2 + 5x + 7
            >>> type(c)
            <class 'controlsystems.types.Polynomial'>
        
        """
        
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
        """Operation of subtraction
        
        This method returns a Polynomial object with the result of the
        subtraction of 'self' Polynomial and 'term' Polynomial, like:
        
            >>> a = Polynomial([2, 3, 4])
            >>> b = Polynomial([1, 2, 3])
            >>> c = a - b
            >>> print c
            x^2 + x + 1
            >>> type(c)
            <class 'controlsystems.types.Polynomial'>
        
        This method is based on __add__ method
        
        """
        
        term_aux = Polynomial([-x for x in term])
        
        return self.__add__(term_aux)
    
    
    def __mul__(self, term):
        """Operation of multiplication of polynomials
        
        This method returns a Polynomial object with the result of the
        multiplication of 'self' Polynomial and 'term' Polynomial, like:
        
            >>> a = Polynomial([1, 2, 3])
            >>> b = Polynomial([2, 3, 4])
            >>> c = a * b
            >>> print c
            2x^4 + 7x^3 + 16x^2 + 17x + 12
            >>> type(c)
            <class 'controlsystems.types.Polynomial'>
        
        """
        
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


    def __div__(self, term):
        """Operation of division of polynomials
        
        This method returns a Polynomial object with the result of the
        multiplication of 'self' Polynomial and 'term' Polynomial
        
        Not implemented yet.
        
        """
        
        #TODO: implement division of polynomials
        
        if not isinstance(term, Polynomial):
            raise ControlSystemsError('Operands must be polynomials')
        
        if len(term) > len(self):
            raise ControlSystemsError('Invalid sizes to division')
        
        raise NotImplementedError

        
    def mult(self, val):
        """Operation of multiplication between numbers and polynomials
        
        This method returns a Polynomial object with the result of the
        multiplication of 'self' Polynomial and 'val' number, like:
        
            >>> a = Polynomial([1, 2, 3])
            >>> b = a.mult(5)
            >>> print b
            5x^2 + 10x + 15
            >>> type(b)
            <class 'controlsystems.types.Polynomial'>
        
        """
        
        #TODO: check if 'val' is a Real number
        
        x = []
        
        for i in range(len(self)):
            x.append(self[i] * val)
        
        return Polynomial(x)
    
    
    def Zero(self, order):
        """Auxiliary method
        
        This method returns a Polynomial object initialized with zeros,
        like:
        
            >>> a = Polynomial()
            >>> a.Zero(4)
            [0, 0, 0, 0]
        
        """
        
        #TODO: implement it in a better way
        
        zero = []
        
        for i in range(order):
            zero.append(0)
        
        return Polynomial(zero)


class Matrix(list):
    """Matrix type
    
    This class implements the Matrix type, based on Python lists.
    The matrix object is a list of lists and have 2 properties ('cols'
    and 'rows'), that store the sizes of matrix, like:
    
        >>> a = Matrix([
        ...     [1, 2, 3],
        ...     [2, 3, 4],
        ...     [3, 4, 5],
        ... ])
        >>>
        >>> print a
        1    2    3
        2    3    4
        3    4    5
        >>>
        >>> a.rows
        3
        >>> a.cols
        3

    """
    
    def __init__(self, mat):
        """Initialization of Matrix object
        
        This method initialize a Matrix object, calculating values of
        properties 'cols' and 'rows'.
        
        """
        
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
        """String representation
        
        This method returns the string representation of matrices,
        like:
        
            1    2    3
            2    3    4
            3    4    5
        
        """
        
        ret = ''
        
        for i in range(self.rows):
            for j in range(self.cols):
                ret += '%s\t' % self[i][j]
            if i < (self.rows - 1):
                ret += '\n'
        
        return ret


    def __call__(self, row, col=None):
        """Callable object
        
        This method returns a row Matrix object, if a parameter is
        used, and a number, if two parameters are used, like:
        
            >>> a = Matrix([
            ...     [1, 2],
            ...     [3, 4],
            ... ])
            >>>
            >>> b = a(1)
            >>> print b
            3    4
            >>> type(b)
            <class 'controlsystems.types.Matrix'>
            >>>
            >>> c = a(0, 0)
            >>> print c
            1
            >>> type(c)
            <type 'int'>
        
        """
        
        if col == None:
            return Matrix([self[row]])
        else:
            return self[row][col]


    def __add__(self, mat):
        """Operation of addition
        
        This method returns a Matrix object with the result of the
        addition of 'self' MAtrix and 'mat' Matrix, like:
        
            >>> a = Matrix([
            ...     [1, 2],
            ...     [3, 4],
            ... ])
            >>>
            >>> b = Matrix([
            ...     [2, 3],
            ...     [4, 5],
            ... ])
            >>>
            >>> c = a + b
            >>> print c
            3    5
            7    9
            >>> type(c)
            <class 'controlsystems.types.Matrix'>
        
        """
        
        if not isinstance(mat, Matrix):
            raise ControlSystemsError('Operands must be matrices')
        
        rows = self.rows > mat.rows and self.rows or mat.rows
        cols = self.cols > mat.cols and self.cols or mat.cols
        
        res = ZerosMatrix(rows, cols)
        
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
        """Operation of subtraction
        
        This method returns a Matrix object with the result of the
        subtraction of 'self' Matrix and 'mat' Matrix, like:
        
            >>> a = Matrix([
            ...     [2, 3],
            ...     [4, 5],
            ... ])
            >>>
            >>> b = Matrix([
            ...     [1, 2],
            ...     [3, 4],
            ... ])
            >>>
            >>> c = a - b
            >>> print c
            1    1  
            1    1
            >>>
            >>> type(c)
            <class 'controlsystems.types.Matrix'>
        
        This method is based on __add__ method
        
        """
        
        aux = mat.mult(-1)
        
        return self.__add__(aux)
    
    
    def __mul__(self, mat):
        """Operation of multiplication of polynomials
        
        This method returns a Polynomial object with the result of the
        multiplication of 'self' Polynomial and 'term' Polynomial, like:
        
            >>> a = Matrix([
            ...     [1, 2],
            ...     [3, 4],
            ... ])
            >>>
            >>> b = Matrix([
            ...     [2, 3],
            ...     [4, 5],
            ... ])
            >>>
            >>> c = a * b
            >>> print c
            10    13
            22    29
            >>>
            >>> type(c)
            <class 'controlsystems.types.Matrix'>
        
        """
        
        if not isinstance(mat, Matrix):
            raise ControlSystemsError('Operands must be matrices')
        
        if self.cols != mat.rows:
            raise ControlSystemsError('Invalid Matrices size for mult.')
        
        res = ZerosMatrix(self.rows, mat.cols)
        
        for i in range(self.rows):
            for j in range(mat.cols):
                for aux in range(self.cols):
                    res[i][j] += self[i][aux] * mat[aux][j]
        
        return res


    def mult(self, num):
        """Operation of multiplication between numbers and matrices
        
        This method returns a Matrix object with the result of the
        multiplication of 'self' Polynomial and 'num' number, like:
        
            >>> a = Matrix([
            ...     [1, 2],
            ...     [3, 4],
            ... ])
            >>>
            >>> b = a.mult(5)
            >>> print b
            5    10
            15   20
            >>>
            >>> type(b)
            <class 'controlsystems.types.Matrix'>
        
        """
        
        #TODO: check if 'num' is a Real number
        
        aux = ZerosMatrix(self.rows, self.cols)
        
        for i in range(self.rows):
            for j in range(self.cols):
                aux[i][j] = self[i][j] * num

        return aux
    
    def transpose(self):
        """Transpose of matrix
        
        This method returns a Matrix object with the transpose of
        'self' Matrix, like:
        
            >>> a = Matrix([
            ...     [1, 2],
            ...     [3, 4],
            ... ])
            >>>
            >>> b = a.transpose()
            >>> print b
            1    3
            2    4
            >>>
            >>> type(b)
            <class 'controlsystems.types.Matrix'>
        
        """
        
        aux = ZerosMatrix(self.cols, self.rows)
        
        for i in range(self.rows):
            for j in range(self.cols):
                aux[j][i] = self[i][j]
        
        return aux


def ZerosMatrix(rows, cols=None):
    """Matrix of zeros
        
    This method returns a Matrix object with zeros, like:
    
        >>> a = ZerosMatrix(2, 4)
        >>> print a
        0    0    0    0
        0    0    0    0
        >>>
        >>> b = ZerosMatrix(2)
        >>> print b
        0    0
        0    0
        >>>
        >>> type(b)
        <class 'controlsystems.types.Matrix'>
    
    """
    
    if cols == None:
        cols = rows
    
    aux = []
    
    for i in range(rows):
        aux.append([])
        for j in range(cols):
            aux[i].append(0)
    
    return Matrix(aux)


def IdentityMatrix(order):
    """Matrix Identity
        
    This method returns a Matrix object with zeros, and ones only on
    main diagonal, like:
    
        >>> a = IdentityMatrix(4)
        >>> print a
        1    0    0    0
        0    1    0    0
        0    0    1    0
        0    0    0    1
        >>>
        >>> type(a)
        <class 'controlsystems.types.Matrix'>
    
    """
    
    aux = []
    
    for i in range(order):
        aux.append([])
        for j in range(order):
            if i == j:
                aux[i].append(1)
            else:
                aux[i].append(0)
    
    return Matrix(aux)


class TransferFunction(object):
    """TransferFunction type
    
    This class implements the TransferFunction type, based on
    Polynomial type. The transfer function object uses 2 polynomials
    to store numerator and denominator, like:
    
        >>> a = TransferFunction([1], [1, 2, 3])
        >>> print a
        Transfer Function:
        .
        .    1      
        ------------
        s^2 + 2s + 3

    """
    
    def __init__(self, num, den):
        """Initialization of TransferFunction object
        
        This method initialize a TransferFunction object.
        
        """
        
        self.num = Polynomial(num)
        self.num.var = 's'
        
        self.den = Polynomial(den)
        self.den.var = 's'
    
    
    def __str__(self):
        """String representation
        
        This method returns the string representation of matrices,
        like:
        
            Transfer Function:
            .
            .     1      
            ------------
            s^2 + 2s + 3
        
        """
        
        len_max = (len(str(self.num)) > len(str(self.den))) and \
                  len(str(self.num)) or len(str(self.den))
        
        response = 'Transfer Function:\n\n'
        response += str(self.num).center(len_max) + '\n'
        response += '-' * len_max + '\n'
        response += str(self.den).center(len_max) + '\n'
        
        return response


    def __add__(self, tf):
        """Operation of addition
        
        This method returns a TransferFunction object with the result
        of the addition of 'self' TransferFunction and 'tf'
        TransferFunction, like:
        
            >>> a = TransferFunction([1], [1, 2, 3])
            >>> b = TransferFunction([1], [2, 3, 4])
            >>> c = a + b
            >>> print c
            Transfer Function:
            .
            .        3s^2 + 5s + 7         
            ------------------------------
            2s^4 + 7s^3 + 16s^2 + 17s + 12
            .
            >>> type(c)
            <class 'controlsystems.types.TransferFunction'>
        
        """
        
        num = (self.num*tf.den) + (tf.num*self.den)
        den = self.den * tf.den
        return TransferFunction(num, den)
    
    
    def __sub__(self, tf):
        """Operation of subtraction
        
        This method returns a TransferFunction object with the result
        of the subtraction of 'self' TransferFunction and 'tf'
        TransferFunction, like:
        
            >>> a = TransferFunction([1], [1, 2, 3])
            >>> b = TransferFunction([1], [2, 3, 4])
            >>> c = a - b
            >>> print c
            Transfer Function:
            .
            .         s^2 + s + 1          
            ------------------------------
            2s^4 + 7s^3 + 16s^2 + 17s + 12
            .
            >>> type(c)
            <class 'controlsystems.types.TransferFunction'>
        
        """
        
        num = (self.num*tf.den) - (tf.num*self.den)
        den = self.den * tf.den
        
        return TransferFunction(num, den)


    def __mul__(self, tf):
        """Operation of multiplication of polynomials
        
        This method returns a TransferFunction object with the result
        of the multiplication of 'self' Polynomial and 'tf'
        TransferFunction, like:
        
            >>> a = TransferFunction([1], [1, 2, 3])
            >>> b = TransferFunction([1], [2, 3, 4])
            >>> c = a * b
            >>> print c
            Transfer Function:
            .
            .              1               
            ------------------------------
            2s^4 + 7s^3 + 16s^2 + 17s + 12
            .
            >>> type(c)
            <class 'controlsystems.types.TransferFunction'>
        
        """
        
        num = self.num * tf.num
        den = self.den * tf.den
        
        return TransferFunction(num, den)
    
    
    def simplify(self):
        """Simplify Transfer Functions
        
        This method returns a TransferFunction object with the transfer
        function simplified, like:
        
            >>> a = TransferFunction([3], [3, 6, 9])
            >>> print a
            Transfer Function:
            .
            .      3      
            -------------
            3s^2 + 6s + 9
            .
            >>> b = a.simplify()
            >>> print b
            Transfer Function:
            .
            .     1      
            ------------
            s^2 + 2s + 3
            .
            >>> type(b)
            <class 'controlsystems.types.TransferFunction'>
        
        Attention: This method is far from perfect, and don't simplify
        all expressions, but is usable.
        
        """
        
        #TODO: improve this method
        
        num = self.num[:]
        den = self.den[:]
        
        mdc = 1
        
        for i in range(1, int(max([max(num), max(den)]))):
            
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
        """Operation of multiplication between numbers and transfer
        functions
        
        This method returns a TransferFunction object with the result
        of the multiplication of 'self' TransferFunction and 'a' number,
        like:
        
            >>> a = TransferFunction([1], [1, 2, 3])
            >>> b = a.mult(5)
            >>> print b
            Transfer Function:
            .
            .       5       
            ---------------
            5s^2 + 10s + 15
            
            >>> type(b)
            <class 'controlsystems.types.TransferFunction'>
        
        """
        
        #TODO: check if 'a' is a Real number
        
        return TransferFunction(self.num.mult(a), self.den.mult(a))


    def div(self, a):
        """Operation of division of a transfer function per a number
        
        This method returns a TransferFunction object with the result
        of the division of 'self' TransferFunction per a 'a' number,
        like:
        
            >>> a = TransferFunction([3], [3, 6, 9])
            >>> print a
            Transfer Function:
            .
            .      3      
            -------------
            3s^2 + 6s + 9
            .
            >>> b = a.div(3)
            >>> print b
            Transfer Function:
            .
            .     1      
            ------------
            s^2 + 2s + 3
            .
            >>> type(b)
            <class 'controlsystems.types.TransferFunction'>
        
        """
        
        num = self.num[:]
        den = self.den[:]
        
        for i in range(len(num)):
            num[i] /= a
        
        for i in range(len(den)):
            den[i] /= a
        
        return TransferFunction(num, den)


    def feedback_unit(self):
        """Feedback with unit gain
        
        This method returns a TransferFunction object with the result
        of the feedback with unit gain of the transfer function, like:
        
            >>> a = TransferFunction([1], [1, 2, 3])
            >>> b = a.feedback_unit()
            >>> print b
            Transfer Function:
            .
            .         s^2 + 2s + 3        
            -----------------------------
            s^4 + 4s^3 + 11s^2 + 14s + 12
            .
            >>> type(b)
            <class 'controlsystems.types.TransferFunction'>
        
        Attention: This method is far from perfect, and don't simplify
        expressions, but is usable.
        
        """
        
        #TODO: improve this method
        
        aux = TransferFunction([1], [1]) + self
        
        return TransferFunction(self.num * aux.den, self.den * aux.num)


class StateSpace(object):
    """StateSpace type
    
    This class implements the StateSpace type, based on Matrix type.
    The state-space object uses 4 matrices, like:
    
        >>> tf = TransferFunction([1], [1, 2, 3])
        >>> a = StateSpace(tf)
        >>> print a
        State-Space model:
        .
        Matrix A:
        0     1
        -3   -2
        .
        Matrix B:
        0
        1
        .
        Matrix C:
        1    0
        .
        Matrix D:
        0

    """
    
    #TODO: fix D matrix behaviour
    #TODO: improve state-space operations
    
    def __init__(self, a, b = None, c = None, d = [[0]]):
        """Initialization of StateSpace object
        
        This method initialize a StateSpace object, using matrices or
        a TransferFunction object.
        
        """
        
        if isinstance(a, TransferFunction):
            
            if len(a.num) > len(a.den):
                raise ControlSystemsError('More zeros than poles.')
            
            self.__tf2ss(a)
        
        else:
            self.__ss(a, b, c, d)
    
    
    def __ss(self, a, b, c, d):
        """Initialization of StateSpace object using matrices
        
        This method initialize a StateSpace object, using 4 matrices.
        
        """
        
        self.a = Matrix(a)
        self.b = Matrix(b)
        self.c = Matrix(c)
        self.d = Matrix(d)
    
    
    def __tf2ss(self, tf):
        """Initialization of StateSpace object using transfer function
        
        This method initialize a StateSpace object, using a
        TransferFunction object.
        
        """
        
        if len(tf.num) == 0 or len(tf.den) == 0:
            raise ControlSystemsError('Invalid Transfer Function')
        
        #preparing A
        order = len(tf.den) - 1
        a = ZerosMatrix(order)
        for i in range(order-1):
            for j in range(1, order):
                if (i+1) == j:
                    a[i][j] = 1
        den = tf.den[:]
        den.reverse()
        for i in range(order):
            a[order-1][i] = -den[i]
        
        #preparing B
        b = ZerosMatrix(order, 1)
        if len(tf.num) == 1:
            b[order-1][0] = tf.num[0]
        else:
            b[order-1][0] = 1

        #preparing C
        c = ZerosMatrix(1, order)
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
        
        #TODO: fix D
        self.__ss(a, b, c, [[0]])
    
    
    def __str__(self):
        """String representation
        
        This method returns the string representation of state space
        models, like:
        
            State-Space model:
            .
            Matrix A:
            0     1
            -3   -2
            .
            Matrix B:
            0
            1
            .
            Matrix C:
            1    0
            .
            Matrix D:
            0
        
        """
        
        ret = 'State-Space model:\n\nMatrix A:\n'
        ret += str(self.a) + '\n\n'
        ret += 'Matrix B:\n'
        ret += str(self.b) + '\n\n'
        ret += 'Matrix C:\n'
        ret += str(self.c) + '\n\n'
        ret += 'Matrix D:\n'
        ret += str(self.d) + '\n'
        
        return ret

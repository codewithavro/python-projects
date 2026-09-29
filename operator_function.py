import operator

class OperatorFunctions:

    def add(self, a , b) :

        return operator.add(a, b)

    def sub(self, a , b) :

        return operator.sub(a,b)

    def mul(self, a, b):
        return operator.mul(a, b)

    def truediv(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Can't divide by zero")

        return operator.truediv(a, b)

    def floordiv(self, a , b):

      if  b == 0 :
       
       raise ZeroDivisionError("Cannot divide by zero")

      operator.floordiv(a, b)

    def mod(self, a, b) :

         if b == 0 :

           raise ZeroDivisionError("Cannot divide by zero")

         return operator.mod(a, b)

    def pow(self, a, b) :

       return operator.pow(a, b)

    def neg(self, a) :

       return operator.neg(a) 

    def pos(self, a) : 
   
        return operator.pos(a)
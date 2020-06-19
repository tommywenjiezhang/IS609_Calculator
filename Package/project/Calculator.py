import math
class Calculator:
    def add(self,x,y):
        if type(x) is not int or type(y) is not int:
            raise ValueError('Value is not int')
        return x+y
    def minus(self,x,y):
        return y-x
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        if y == 0:
            raise ValueError("Can't be divided by zero")
        return x/y
    def square(self,x):
        return x**2
    def sqrt(self,x):
        return math.sqrt(x)
    
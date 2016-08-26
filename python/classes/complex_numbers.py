#!/bin/python
import math

# this script defines a class for imaginary numbers
# it can operate on two numbers with +,-,*,/
# it can also mod a single imaginary number

# INPUT: Two lines with two integers each
# 2 1
# 5 6
# so the first number is 2+1i and the second is 5+6i

# The program then outputs the numbers after each operation +,-,*,/ mod(a) and mod(b)

class ImNum:
    ''' class that implements imaginary numbers of the form 'a+bi' 
        +, -, *, /, have been overloaded and mod() returns the modulus'''

    real = 0.0
    imag = 0.0

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return "{0:.2f}+{1:.2f}i".format(self.real, self.imag)
        else:
            return "{0:.2f}{1:.2f}i".format(self.real, self.imag)
        
    def __add__(self, other):
        if self.imag + other.imag == 0: # no longer imaginary
            return ImNum(self.real + other.real, 0.0)
        else:
            return ImNum(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        if self.imag - other.imag == 0: # no longer imaginary
            return ImNum(self.real - other.real, 0.0)
        else:
            return ImNum(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        # FOIL a and b, trick, create 2 partial product numbers, then add them together
        pp1 = ImNum(self.real * other.real, self.real * other.imag) # First, Outer
        pp2 = ImNum(self.imag * other.imag * -1, self.imag * other.real) # Last * -1 to handle i^2, Inner
        return pp1 + pp2

    def __truediv__(self, other):
        # multiply top and bottom by conjugate of denominator
        conjugate = ImNum(other.real, other.imag * -1)
        numerator = self * conjugate
        denominator = other * conjugate
        # reduce, i in denominator is now 0 and can be ignored
        quotient = ImNum(numerator.real / denominator.real, numerator.imag / denominator.real)
        return quotient

    def mod(self):
        # mod of a complex number is defined as the square route of a^2 + b^2 where a+bi
        # this is not the best way represent it, but the problem requires this format
        return ImNum(math.sqrt(self.real ** 2 + self.imag ** 2), 0.0)


    
# test the functions
line1 = list(map(float, input().split()))
ia = ImNum(line1[0], line1[1])
line2 = list(map(float, input().split()))
ib = ImNum(line2[0], line2[1])
print(ia + ib)
print(ia - ib)
print(ia * ib)
print(ia / ib)
print(ia.mod())
print(ib.mod())

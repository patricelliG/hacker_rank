#!/bin/python

# given a imaginary number of the form x+ji
# return the polar coordinates 'r' and 'varphi'

import cmath
import math
import re

# get the input and strip out x and y
line = input()
x_and_y = re.split("[-+i]", line)
x_and_y = [x for x in x_and_y if x] # remove whitespace

signs = re.split("[0-9]", line)
signs = [x for x in signs if x] # again...
signs.pop(len(signs) - 1)

# fix, in the event that x does not have a sign
if len(signs) == 1:
    signs.insert(0, '+')

# extract x and y finally
for i in range(2):
    signs[i] += x_and_y[i]

x = float(signs[0])
y = float(signs[1][:-1])

# calculate the results
print(math.sqrt((x**2 + y**2))) # r
print(cmath.phase(complex( x, y))) # varphi

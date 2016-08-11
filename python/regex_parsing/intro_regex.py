#!/bin/python

# script to determin if a number is a float

import re
# get the input
t = int(input())

n = ''
for i in range(t):
	n = str(input())
	print(n)
	#print(bool(re.match("[-+]?[0-9]+[.]{1}[0-9]+$", n)))
	print(bool(re.match("[-+]?[0-9]+.[0-9]+$", n)))

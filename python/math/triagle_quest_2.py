#!/bin/python

# given a postive integer N, print a palindromic triangle of size N
# solution must be in two lines...

for i in range(1, int(input()) + 1): 
	print(str(int('1' * i) ** 2))

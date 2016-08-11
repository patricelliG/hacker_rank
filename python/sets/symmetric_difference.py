#!/bin/python

# this script takes 2 list of integers as input
# it returns the symmetric difference of the two sets

# get input
m = int(input())    # number of ints in the first list
a = list(input().split())   # first list

n = int(input())    # number of ints in the second list
b = list(input().split())   # second list

# arrange the new lists as sets of ints
a = set(map(int, a))
b = set(map(int, b))

# create a list containing the symetric difference
c = set((a.difference(b)).union(b.difference(a)))

# print the symmetic difference in a acending order, one per line
c = list((a.difference(b)).union(b.difference(a)))

for integer in sorted(c):
    print(integer)

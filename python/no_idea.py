#!/bin/python

# There are disjoin sets A and B. The program is given an array of integers.
# For each integer, if the integer is a member of A, our happiness increases by one.
# If the integer is a member of B, our happiness decreases by one.
# Otherwise happiness does not change

# get the input
line1 = input().split()
n = int(line1[0]) # number of ints in array
m = int(line1[1]) # number of ints in sets

array = list(map(int, input().split()))
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

# do the thing...
happiness = 0
for num in array:
    if num in a:
        happiness += 1
    elif num in b:
        happiness -= 1

print(happiness)


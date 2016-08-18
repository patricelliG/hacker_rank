#!/bin/python

# A shop owner has 'x' number of shoes
# a list is given of shoes sizes in inventory
# 'n' customers  will pay 'xi' amound if they get the shoe in their size

from collections import Counter

# get the inputs
x = int(input())
ssl = list(map(int, input().split()))
n = int(input())

# check each customer's demand
size_list = Counter(ssl)
profit = 0

for customer in range(n):
    # get payment and size
    line = list(input().split())
    size = int(line[0])
    payment = int(line[1])
    # check inventory
    if size_list[size] != 0:
        profit += payment
        size_list[size] -= 1

print(profit)


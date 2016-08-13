#!/bin/python

# You are expecting N guests and you already made M cookies.
# You want to distribute all the cookies evenly between your guests
# each guest receives the same number of cookies
# if there are not enough cookies for everyone to receive the same amount,
# you must make some number of additional cookies
# Given N and M, fid and print the minimum number of additional cookies you must make
# 1 <= N, M <= 10^9

import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

if n == 1 or n == m or m % n == 0:
    print(0)
elif n > m:
    print(n - m)
elif n < m:
    divisor = m // n
    extra_cookies = m - n * divisor
    print(n - extra_cookies)
else:
    # something is wrong, return 0
    print(0)

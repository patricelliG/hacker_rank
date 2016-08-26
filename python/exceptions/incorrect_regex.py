#!/bin/python

# A script that determins if a given string is a valid regex
import re
n = int(input()) # the number of test strings

for strings in range(n):
    try:
        regex = str(input())
        re.match(regex, "")
    except:
        print("False")
    else:
        print("True")

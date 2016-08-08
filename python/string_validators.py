#!/bin/python

# a simple script testing string validators

# get input string
string = str(input())

# define checks for each type of validator
alphanum = False
alphabet = False
digits = False
lower = False
upper = False

# check for each type of string validators
for char in string:
    if alphanum == False:
        if char.isalnum():
            alphanum = True
    if alphabet == False:
        if char.isalpha():
            alphabet = True
    if digits == False:
        if char.isdigit():
            digits = True
    if lower == False:
        if char.islower():
            lower = True
    if upper == False:
        if char.isupper():
            upper = True

# print the results
print(alphanum)
print(alphabet)
print(digits)
print(lower)
print(upper)



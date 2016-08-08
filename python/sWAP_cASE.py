#!/bin/python

# This script takes a string and reverses to case of each character in the string

#  get the string
string = str(input())

# reverse the casing
new_string = []
for character in string:
    if character.isupper():
        new_string.append(character.lower())
    elif character.islower():
        new_string.append(character.upper())
    else:
        new_string.append(character)
        
print(''.join(new_string))



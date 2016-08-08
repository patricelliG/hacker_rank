#!/bin/python

# a program that finds the number of times a substring appears in a given string

# get the string and sub string, s and ss accordingly
s = str(input())
ss = str(input())
times = 0 # number of times the substring appears

# check for the substring
for char in range(len(s)):
    if s[char] == ss[0]:
        if char + len(ss) <= len(s) and s[char:char+(len(ss))] == ss:
            times += 1 

print(times)



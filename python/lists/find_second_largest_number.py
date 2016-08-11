#!/bin/python

# a script that finds the second largest number in a list
# inputs: first line is the number of arguments
# second line is the list, each element seperated by spaces

# get the inputs
num_ints = input()
int_string = input()

# remove duplicates from the list

int_string = list(set(int_string.split()))

# convert the string to ints and sort the string
int_list = sorted(list(map(int, int_string)))

# return the second largest number
print(int_list[-2])




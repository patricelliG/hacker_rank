#!/bin/python

# this script is a simple exercise in set functions discard, remove, and pop.

# get the inputs
n = int(input())
s = set(list(map(int, input().split())))
num_commands = int(input())

# run each command on the set, commands can be pop, remove, or discard
for i in range(num_commands):
    line = list(map(str, input().split()))
    command = line[0]

    if command == "pop":
        s.pop()
    elif command == "remove":
        s.remove(int(line[1]))
    elif command == "discard":
        s.discard(int(line[1]))
    else:
        exit(1) # some other command was issued

print(sum(s))



#!/bin/python
# a simple program meant to demostrate the functinoality of exception handeling

n = int(input())

for pair in range(n):
    try:
        line = list(map(int, input().split()))
        a = line[0]
        b = line[1]
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

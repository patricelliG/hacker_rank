#!/bin/python

# a program that takes the x, y, z of a cuboid and returns all points in which satisfy the following
# X + Y + Z must not = N
# new_list_name = [ <what to do to each element> for <element name> in <old_list>]

# get the coords
x_range = int(input())
y_range = int(input())
z_range = int(input())

# get n
n = int(input())

# create a list of all the points
points = []

for x in range(x_range + 1):
    for y in range(y_range + 1):
        for z in range(z_range + 1):
            points.append([x, y, z])

# make a new list of good points
good_points = []
[good_points.append(point) for point in points if point[0] + point[1] + point[2] != n]
print(good_points)

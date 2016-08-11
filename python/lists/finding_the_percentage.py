#!/bin/python

# this program takes the following input
# n, the number of students
# student math physics chemistry percentages

# the program then stores this data in a dictionary
# a user can enter a student's name
# the program then outputs the average percentage marks obtained by the student
# the percentage is corrected by 2 decimal places

# get the data
student_scores = {}
num_students = int(input())

for student in range(num_students):
    line = list(input().split())
    student_scores[str(line[0])] = (float(line[1]), float(line[2]), float(line[3]))


# get the student name in which to calculate scores
sname = input()

# calculate the average scores for the student
print("{:0.2f}".format((student_scores[sname][0] + student_scores[sname][1] + student_scores[sname][2]) / 3))


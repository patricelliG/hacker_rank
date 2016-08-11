#!/bin/python

# get the names and grade of the students in a list

num_students = input()
student_data = []

for student in range(int(num_students)):
    student_name = input()
    student_grade = float(input())
    student_data.append([student_name, student_grade])

# make a list of student grade only
grades = []
[grades.append(student[1]) for student in student_data ]
grades = list(set(grades))
grades.sort()

# make a list of students with the second lowest grade
slgs = []
[slgs.append(student) for student in student_data if student[1] == grades[1]]

# print the result sorting by name
slgs.sort(key=lambda x:(x[0]))
for student in slgs:
    print(student[0])


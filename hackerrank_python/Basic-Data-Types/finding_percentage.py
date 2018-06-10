# Finding the percentage
#
# Task
# You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
#
# Input Format
#
# The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
#
# Output Format
#
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

# Solution
x = int(input())
students_data  = []
for i in range(x):
    data = input().split()
    students_data.append(data)
name_student = input()
m = [data for data in students_data if data[0] == name_student][0]
avg_marks = (float(m[1]) + float(m[2]) + float(m[3])) / 3
print("{0:.2f}".format(avg_marks))

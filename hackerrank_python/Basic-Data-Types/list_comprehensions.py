# List Comprehensions
#
# Task
# You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the code if we dont use list comprehensions in Python.
#
# Input Format
#
# Four integers X,Y,Z and N each on four separate lines, respectively.
#
#
#
# Solution
x = int(input())
y = int(input())
z = int(input())
n = int(input())
result = [[X,Y,Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X+Y+Z != n]
print(result)

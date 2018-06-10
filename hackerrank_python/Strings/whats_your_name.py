# What's Your Name?
#
# Task
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.
#
# Input Format
#
# The first line contains the first name, and the second line contains the last name.
#
# Constraints
#
# The length of the first and last name ≤ 10 .
#
# Output Format
#
# Print the output as mentioned above.
#
# Solution
s1 = str(input())
s2 = str(input())
print("Hello {0} {1}!. You just delved into Python".format(s1,s2))

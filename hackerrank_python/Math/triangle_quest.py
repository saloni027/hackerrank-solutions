# Triangle Quest
#
# Task
# You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:
#
# 1
# 22
# 333
# 4444
# ......
# Can you do it using only arithmetic operations, a single for loop and print statement?
#
# Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.
#
# Note: Using anything related to strings will give a score of 0.
#
# Input Format
#
# A single line containing integer, N.
#
# Output Format
#
# Print N-1 lines as explained above.
#
# Solution
for i in range(1,int(input())):
    print(((pow(10,i) - 1 ) // 9 ) * i)

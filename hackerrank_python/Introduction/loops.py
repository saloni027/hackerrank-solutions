#Loops

# Task
# Read an integer N. For all non-negative integers i < N , print i^2. See the sample for details.
#
# Input Format
#
# The first and only line contains the integer,N .
#
# Output Format
#
# Print N lines, one corresponding to each i.

#Solution

N = int(input())
for i in range(0,N):
    print(i*i)

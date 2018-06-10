# Find the Runner-Up Score!
#
# Task
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
#
# Input Format
#
# The first line contains n. The second line contains an array A[]  of n integers each separated by a space.
#
# Output Format
#
# Print the runner-up score.
#
# Solution
n = int(input())
arr = [int(i) for i in input().split()]
arr = list(set(arr))
arr.sort()
print(arr[-2])

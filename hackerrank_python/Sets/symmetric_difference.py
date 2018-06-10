# Symmetric Difference
#
# Task
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
#
# Input Format
#
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.
#
# Output Format
#
# Output the symmetric difference integers in ascending order, one per line.
#
# Solution
n = int(input())
s1 = set(int(i) for i in input().split())
m = int(input())
s2= set(int(i) for i in input().split())

result = sorted((s1.difference(s2)).union(s2.difference(s1)))
for i in result:
    print(i)

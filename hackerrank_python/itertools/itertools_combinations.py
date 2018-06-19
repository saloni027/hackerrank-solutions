# itertools.combinations()
#
# Task
# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
#
# Input Format
# A single line containing the string S and integer value k separated by a space.
#
# Output Format
# Print the different combinations of string S on separate lines.
#
# Solution
from itertools import combinations

s,k = input().split()
s = sorted(s)
for i in range(1,int(k) + 1):
    for j in combinations(s,i):
                print(''.join(j))

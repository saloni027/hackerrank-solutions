# itertools.permutations()
#
# Task
# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
#
# Input Format
# A single line containing the space separated string S and the integer value k.
#
# Output Format
# Print the permutations of the string S on separate lines.
#
# Solution
from itertools import permutations
s,k = input().split()
l = sorted(list(permutations(s,int(k))))
for elm in l:
    print(''.join(elm))

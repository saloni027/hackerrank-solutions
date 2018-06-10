# Check Strict Superset
#
# Task
# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
#
# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
#
# A strict superset has at least one element that does not exist in its subset.
#
# Input Format
#
# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next n lines contains the space separated elements of the other sets.
#
# Output Format
#
# Print True if set A is a strict superset of all other N sets. Otherwise, print False.
#
# Solution
set1 = set(int(i) for i in input().split())
k = int(input())
result = True
for j in range(k):
    s = set(int(i) for i in input().split())
    if not s.issubset(set1):
        result = False
    if len(s) >= len(set1):
        result = False

print(result)

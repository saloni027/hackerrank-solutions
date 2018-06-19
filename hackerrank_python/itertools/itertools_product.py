# itertools.product()
#
# Task
# You are given a two lists A and B. Your task is to compute their cartesian product AXB.
#
# Input Format
# The first line contains the space separated elements of list A.
# The second line contains the space separated elements of list B.
#
# Both lists have no duplicate integer elements.
#
# Output Format
# Output the space separated tuples of the cartesian product.
#
# Solution
import itertools
a = list(set(int(i) for i in input().split()))
b = list(set(int(i) for i in input().split()))
for elem in list(itertools.product(a,b)):
    print(elem,end=' ')

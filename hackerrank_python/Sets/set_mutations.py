# Set Mutations
#
# Task
# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
#
# Your task is to execute those operations and print the sum of elements from set A.
#
# Input Format
#
# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2 * N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.
#
# Output Format
#
# Output the sum of elements in set A.
#
# Solution
n1 = int(input())
s1 = set(int(i) for i in input().split())
n = int(input())
for i in range(n):
    args = input().split()
    k = set(int(i) for i in input().split())
    if args[0] == "intersection_update":
        s1.intersection_update(k)
    if args[0] == "update":
        s1.update(k)
    if args[0] == "symmetric_difference_update":
        s1.symmetric_difference_update(k)
    if args[0] == "difference_update":
        s1.difference_update(k)
print(sum(s1))

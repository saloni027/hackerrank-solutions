# No Idea!
#
# Task
# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i belongs to A, you add 1 to your happiness. If i belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
#
# Input Format
#
# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.
#
# Output Format
#
# Output a single integer, your total happiness.
#
# Solution
nums = map(int,input().split())
arr = [int(i) for i in input().split()]
set1 = set([int(i) for i in input().split()])
set2 = set([int(i) for i in input().split()])
count = 0
for i in arr:
    if i in set1:
        count+=1
    if i in set2:
        count-=1
print(count)

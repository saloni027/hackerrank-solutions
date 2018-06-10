# Set .discard(),.remove() & .pop()
#
# Task
# You have a non-empty set s, and you have to execute N commands given in N lines.
#
# The commands will be pop, remove and discard.
#
# Input Format
#
# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.
#
# Output Format
#
# Print the sum of the elements of set s on a single line.
#
# Solution
n = int(input())
s = set(map(int,input().split()))
t = int(input())
for i in range(t):
    args = input().split()
    if args[0] == "pop":
        s.pop()
    elif args[0] == "remove":
        s.remove(int(args[1]))
    elif args[0] == "discard":
        s.discard(int(args[1]))
print(sum(s))

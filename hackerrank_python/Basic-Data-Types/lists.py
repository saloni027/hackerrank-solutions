#Lists

#Task
# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Input Format
#
# The first line contains an integer,n , denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

# Output Format
#
# For each command of type print, print the list on a new line.

#Solution

T = int(input())

L = []
for t in range(T):
    args = input().split(" ")
    if args[0] == "append":
        L.append(int(args[1]))
    elif args[0] == "insert":
        L.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        L.remove(int(args[1]))
    elif args[0] == "pop":
        L.pop()
    elif args[0] == "sort":
        L.sort()
    elif args[0] == "reverse":
        L.reverse()
    elif args[0] == "print":
        print (L)

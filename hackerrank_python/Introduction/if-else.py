# Python If-Else

# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format
#
# A single line containing a positive integer, .
#
# Output Format
#
# Print Weird if the number is weird; otherwise, print Not Weird.

#Solution
if __name__ == '__main__':
    n = int(input())

    if n%2 == 1:
        print("Weird")
    else:
        if n in range(2,6):
            print('Not Weird')
        elif n in range(6,21):
            print('Weird')
        else:
            print('Not Weird')

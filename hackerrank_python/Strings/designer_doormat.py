# Designer Door Mat
#
# Task
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# 1)Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
# 2)The design should have 'WELCOME' written in the center.
# 3)The design pattern should only use |, . and - characters.
#
# Input Format
#
# A single line containing the space separated values of N and M.
#
# Output Format
#
# Output the design pattern.
#
# Solution
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print(('.|.'*i).center(M,'-'))
print('WELCOME'.center(M,'-'))
for i in range(N-2,-1,-2):
    print(('.|.'*i).center(M,'-'))

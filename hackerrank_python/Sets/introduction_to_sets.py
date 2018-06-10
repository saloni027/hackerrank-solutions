# Introduction to Sets
#
# Task
# Now, let's use our knowledge of sets and help Mickey.
#
# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
#
# Formula used: Average = Sum of Distinct Heights/Total Number of Heights.
#
# Input Format
#
# The first line contains the integer, N, the total number of plants.
# The second line contains the N space separated heights of the plants.
#
# Output Format
#
# Output the average height value on a single line.
#
# Solution
def average(array):
    s = set(array)
    avg = sum(s) / len(s)
    return avg

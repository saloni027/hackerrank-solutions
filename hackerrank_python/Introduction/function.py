#Write a function

# Task
# You are given the year, and you have to write a function to check if the year is leap or not.
#
# Note that you have to complete the function and remaining code is given as template.
#
# Input Format
#
# Read y, the year that needs to be checked.
#
# Output Format
#
# Output is taken care of by the template. Your function must return a boolean value (True/False)

#Solution
def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

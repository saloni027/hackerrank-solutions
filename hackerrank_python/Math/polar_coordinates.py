# Polar Coordinates
#
# Task
# You are given a complex z. Your task is to convert it to polar coordinates.
#
# Input Format
#
# A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.
#
# Output Format
#
# Output two lines:
# The first line should contain the value of r.
# The second line should contain the value of phase.
#
# Solution
import math
import cmath
c = complex(input())
r = abs(c)
ph = cmath.phase(c)
print(r)
print(ph)

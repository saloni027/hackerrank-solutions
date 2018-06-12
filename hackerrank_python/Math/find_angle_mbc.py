# Find Angle MBC
#
# Task
# /_ABC = 90°
# Point M is the midpoint of hypotenuse AC.
#
# You are given the lengths AB and BC.
# Your task is to find /_MBC  in degrees.
#
# Input Format
#
# The first line contains the length of side AB.
# The second line contains the length of side BC.
#
# Output Format
#
# Output /_MBC in degrees.
#
# Note: Round the angle to the nearest integer.
#
# Solution
import math
ab = float(input())
bc = float(input())
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm
angle_mbc_radian = math.acos(bc/(2 * mc))
angle_mbc_degree = int(round((180 * angle_mbc_radian) / math.pi ))
result = str(angle_mbc_degree) + "°"
print(result)

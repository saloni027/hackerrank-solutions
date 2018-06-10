# String Validators
#
# Task
# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
#
# Input Format
#
# A single line containing a string .
#
# Output Format
#
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
#
# Solution
S = input()
print("True" if len([s for s in S if s.isalnum()]) > 0 else "False")
print("True" if len([s for s in S if s.isalpha()]) > 0 else "False")
print("True" if len([s for s in S if s.isdigit()]) > 0 else "False")
print("True" if len([s for s in S if s.islower()]) > 0 else "False")
print("True" if len([s for s in S if s.isupper()]) > 0 else "False")

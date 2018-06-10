# Capitalize!
#
# Task
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
#
# Input Format
#
# A single line of input containing the full name, S.
#
# Output Format
#
# Print the capitalized string, S.
#
# Solution
def capitalize(string):
    split_string = string.split(' ')
    final_string = [n.capitalize() for n in split_string]
    return ' '.join(final_string)

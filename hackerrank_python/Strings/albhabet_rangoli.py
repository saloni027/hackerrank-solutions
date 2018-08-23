# Alphabet Rangoli
#
# Task
# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# Input Format
#
# Only one line of input containing N, the size of the rangoli.


# Output Format
#
# Print the alphabet rangoli in the format explained above.


# Solution
import string
n = int(input())
alphabet_list = list(string.ascii_lowercase[:n])
alphabet_list.reverse()
width = n * 4 - 3
for i in range(1,n+1):
    left_part = "".join(alphabet_list[0:i])
    right_part = "".join(reversed(left_part[:-1]))
    print('-'.join(left_part + right_part).center(width,'-'))
for j in reversed(range(1,n)):
    left_part = "".join(alphabet_list[0:j])
    right_part = "".join(reversed(left_part[:-1]))
    print('-'.join(left_part + right_part).center(width,'-'))

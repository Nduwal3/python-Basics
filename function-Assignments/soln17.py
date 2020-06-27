"""
 Write a Python program to find if a given string starts with a given character 
using Lambda. 
"""

character_to_be_checked = 'a'

is_valid = lambda input_string: input_string.startswith(character_to_be_checked)

def check_initial_char(input_string):
    if is_valid(input_string):
        print("{} starts with {}".format(input_string , character_to_be_checked))
    else:
        print("{} does not starts with {}".format(input_string , character_to_be_checked))

check_initial_char('apple')
check_initial_char('cat')

    
"""
Write a Python program to check whether a given string is number or not 
using Lambda. 
"""
is_number = lambda string_input: string_input.isnumeric()

def check_is_numeric(input_string):
    if(is_number(input_string)):
        print("the string is a number")
    else:
        print("the string is not a number")

check_is_numeric("50")
check_is_numeric("python")
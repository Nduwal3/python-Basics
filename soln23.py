"""
Write a Python program to check a list is empty or not. 
"""

def is_list_empty(input_list):
    if len(input_list) <= 0:
        print("The list is empty")
    else:
        print("The list is not empty")

is_list_empty([])
is_list_empty([1, 2, 3, 4])
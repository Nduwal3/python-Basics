"""
Write a Python function to check whether a number is in a given range. 
"""

def is_in_range():
    lower_range = 10
    upper_range = 100
    num = int(input("Enter a number to check if it is in a given range:: "))
    if num in range(lower_range , upper_range):
        return True
    else:
        return False

if(is_in_range()):
    print("the number is in given range")
else:
    print("not in the range")
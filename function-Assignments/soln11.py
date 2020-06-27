"""
Write a Python program to create a lambda function that adds 15 to a given 
number passed in as an argument, also create a lambda function that multiplies 
argument x with argument y and print the result. 
"""

add_15 = lambda num: num + 15
print(add_15(10))

multiply = lambda param1 , param2: param1 * param2 
print(multiply(4, 6))

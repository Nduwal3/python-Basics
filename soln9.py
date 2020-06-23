"""
Write a Python program to change a given string to a new string where the first 
and last chars have been exchanged
"""
input_string = input("enter a string:::  ")
last_char = input_string[-1]
last_char_replaced = input_string.replace(input_string[-1] , input_string[0])
updated_string = last_char_replaced.replace(last_char_replaced[0], last_char, 1)
print(updated_string)
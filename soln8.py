"""
8. Write a Python program to remove the nth index character from a nonempty 
string
"""
try:
    stringInput = input('Enter a string:::  ')
    index_of_char_to_be_removed = int(input('Enter index of char to be removed::: '))
except ValueError:
    print('value Error! Entered number is not valid')
else:
    print(stringInput.replace(stringInput[index_of_char_to_be_removed] , ''))
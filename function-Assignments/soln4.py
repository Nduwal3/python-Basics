"""
Write a Python program to reverse a string. 
Sample String : "1234abcd" 
Expected Output : "dcba4321" 
"""

def create_string_reverse(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

string_reversed = create_string_reverse("1234abcd")
print(string_reversed)
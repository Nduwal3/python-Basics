"""
Write a Python program to insert a given string at the beginning of all items in 
a list. 
Sample list : [1,2,3,4], string : emp 
Expected output : ['emp1', 'emp2', 'emp3', 'emp4'] 
"""

def insert_char_at_beginning(input_string):
    x = lambda a : input_string + str(a)
    sample_list = [1, 2, 3, 4]
    new_list = list(map(x , sample_list ))
    print(new_list)   

insert_char_at_beginning('emp')

    
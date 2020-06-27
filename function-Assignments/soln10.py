"""
 Write a Python program to print the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
Expected Result : [2, 4, 6, 8] 
"""

def get_even_number(input_list):
    even_list = filter(lambda x: x % 2 == 0 , input_list)
    print(list(even_list))

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
get_even_number(sample_list)
"""
Write a Python program to sort a list of tuples using Lambda. 
"""

list_of_tuples = [(1,2), (9,8), (6,8), (5,3), (7,7)]

sorted_list_of_tuples = lambda input_list: sorted(input_list)
print(sorted_list_of_tuples(list_of_tuples))
"""
Write a Python function that takes a list and returns a new list with unique 
elements of the first list. 
Sample List : [1,2,3,3,3,3,4,5] 
Unique List : [1, 2, 3, 4, 5] 
"""

def remove_duplicates(input_list):
    unique_num_list = []
    for num in input_list:
        if num not in unique_num_list:
            unique_num_list.append(num)
    return unique_num_list

sample_list = [1,2,3,3,3,3,4,5] 
print(remove_duplicates(sample_list))

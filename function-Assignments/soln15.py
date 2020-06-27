"""
Write a Python program to filter a list of integers using Lambda. 
"""
odd_nums = [1, 3, 5, 7, 9]

filter_num = lambda x: x in odd_nums

def filter_list(input_list):
    filtered_list = filter(filter_num, input_list)
    print(list(filtered_list))

sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_list(sample_list)

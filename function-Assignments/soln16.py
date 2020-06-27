"""
Write a Python program to square and cube every number in a given list of 
integers using Lambda. 
"""

def calc_square_and_cube(input_list):
    square_list = map(lambda num: num * num, input_list)
    cube_list = map(lambda num: num ** 3, input_list)
    print(list(square_list))
    print(list(cube_list))

sample_list = [1, 3, 5, 7, 9]
calc_square_and_cube(sample_list)
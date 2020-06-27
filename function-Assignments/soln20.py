"""
Write a Python program to find intersection of two given arrays using 
Lambda. 
"""

intersection = lambda arr1, arr2: set(arr1).intersection(arr2)

def get_intersection(list1 , list2):
    print(intersection(list1 , list2))

test_list1 = [1, 2, 3, 4, 5]
test_list2 = [2, 4, 6, 8, 10]

get_intersection(test_list1 , test_list2)

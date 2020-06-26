"""
 Write a Python program to check whether all dictionaries in a list are empty or 
not. 
Sample list : [{},{},{}] 
Return value : True 
Sample list : [{1,2},{},{}] 
Return value : False 
"""

def check_empty_dictionaries(sample_list):
    is_empty = False
    for item in sample_list:
        if item:
            is_empty = False
            break
        else:
            is_empty = True
    print(is_empty)

sample_list1 = [{},{},{}]
sample_list2 = [{},{1,2},{}]
check_empty_dictionaries(sample_list1)
check_empty_dictionaries(sample_list2)

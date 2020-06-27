"""
 Write a Python function that accepts a string and calculate the number of 
upper case letters and lower case letters. 
Sample String : 'The quick Brow Fox' 
Expected Output : 
No. of Upper case characters : 3 
No. of Lower case Characters : 12 
"""

def count_string_lower_and_upper_case(input_string):
    count_upper_case = 0
    count_lower_case = 0
    for char in input_string:
        if char.isupper():
            count_upper_case += 1
        elif  char.islower():
            count_lower_case += 1
        else:
            continue
    return count_upper_case , count_lower_case

upper_case_count, lower_case_count = count_string_lower_and_upper_case('The quick Brow Fox')
print("No. of Upper case characters : {}".format(upper_case_count))
print("No. of Lower case characters : {}".format(lower_case_count))

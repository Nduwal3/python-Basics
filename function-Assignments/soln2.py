"""
Write a Python function to sum all the numbers in a list. 
Sample List : (8, 2, 3, 0, 7) 
Expected Output : 20 
"""

def calculate_sum(input_list):
    return sum(input_list)

sample_list = [8, 2, 3, 0, 7]
sum = calculate_sum(sample_list)
print(sum)
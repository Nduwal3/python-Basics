"""
Write a Python script to print a dictionary where the keys are numbers 
between 1 and 15 (both included) and the values are square of keys 
Sample Dictionary 
"""


start_point = 1
end_point = 15 + 1
sample_dict = {}
for n in range(start_point , end_point):
    sample_dict[n] = n ** 2
print(sample_dict)
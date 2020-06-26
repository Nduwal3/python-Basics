"""
Write a Python program to multiply all the items in a dictionary. 
"""

my_dict = {'1':5,'2':-5,'3':3}
result  = 1 
for key in my_dict.values():
    result = result * key
print("total product:: {} ".format(result))
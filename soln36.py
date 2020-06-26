"""
Write a Python program to sum all the items in a dictionary. 
"""

my_dict = {1:5,2:-5,3:3}
result  = 0
for key , value in my_dict.items():
    result = result + key + value
print("total Sum:: {} ".format(result))
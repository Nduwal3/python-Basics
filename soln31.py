"""
Write a Python program to iterate over dictionaries using for loops. 
"""

my_dict = {
    "name" : "jack",
    "gender": "male",
    "email": "jack@j.com",
    "address" : "bhaktapur"
    }
for key , value in my_dict.items():
    print('{} : {}'.format(key , value))

for key in my_dict.keys():
    print('key : {}'.format(key))

for value in my_dict.values():
    print('values : {}'.format(value))
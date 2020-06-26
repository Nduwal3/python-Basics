"""
Write a Python script to check whether a given key already exists in a 
dictionary. 
"""

key_to_be_checked = input("enter the key to be checked:::: ")
my_dict = {
    "name" : "jack",
    "gender": "male",
    "email": "jack@j.com",
    "address" : "bhaktapur"}
if key_to_be_checked in my_dict.keys():
    print("key already exists")
else:
    print("key doesnt exists")
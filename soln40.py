"""
Write a Python program to add an item in a tuple. 
"""

# since python tuples are immutable we cannot append or remove item from a tuple. 
# but we can achive it by converting the tuple into a list and again converting the list back to a tuple

my_tuple = ('ram', 37, "ram@r.com")
my_list = list(my_tuple)
my_list.append(4)
my_tuple = tuple(my_list)
print(my_tuple)
"""
Write a Python program to remove an item from a tuple. 
"""


# since python tuples are immutable we cannot append or remove item from a tuple. 
# but we can achive it by converting the tuple into a list and again converting the list back to a tuple

my_tuple = ('ram', 37, "ram@r.com")
my_list = list(my_tuple)
my_list.remove(37)
my_tuple = tuple(my_list)
print(my_tuple)
"""
Write a Python program to slice a tuple.
"""

# since python tuples are immutable we cannot append or remove item from a tuple. 
# but we can achive it by converting the tuple into a list and again converting the list back to a tuple

my_tuple = ('ram', 37, "ram@r.com" , "983259855" , "bhaktapur" , "Nepal")
my_list = list(my_tuple)
my_list = my_list[2: 4]
my_tuple = tuple(my_list)
print(my_tuple)
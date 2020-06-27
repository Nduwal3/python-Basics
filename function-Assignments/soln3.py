"""
Write a Python function to multiply all the numbers in a list. 
Sample List : (8, 2, 3, -1, 7) 
Expected Output : -336 
"""

def multiply_item(input_list):
    product = 1
    for item in input_list:
        product = product * item
    return product

my_list = [8, 2, 3, -1, 7]
item_prodcuts = multiply_item(my_list)
print(item_prodcuts)


"""
Write a Python program to create a function that takes one argument, and 
that argument will be multiplied with an unknown given number. 
"""

import random

def multiply_with_random_num(num):
    random_num = random.randint(1,100)
    # print(random_num)
    product = num * random_num
    print(product)

multiply_with_random_num(5)
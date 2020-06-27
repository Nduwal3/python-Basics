"""
Write a Python function to calculate the factorial of a number (a non-negative 
integer). The function accepts the number as an argument. 
"""

def calc_factorial(num):
    factorial = 1
    for i in range(num, 0, -1):
        factorial *= i  
    print(factorial) 

calc_factorial(5)
"""
Write a Python function that takes a number as a parameter and check the 
number is prime or not. 
Note : A prime number (or a prime) is a natural number greater than 1 and that 
has no positive divisors other than 1 and itself. 
"""

def check_prime(num):
    is_prime = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
            else:
                is_prime = True
    return is_prime

num = 16
if(check_prime(num)):
    print("the number is prime")
else:
    print("the number is not prime")
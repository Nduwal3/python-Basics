"""
Write a Python program to create Fibonacci series upto n using Lambda.
"""

def create_fibonacci_series(num):
    fibonacci = lambda number: number if number <= 1 else fibonacci(number - 1) + fibonacci(number - 2)
    listOfFibonacciNumbers = list(map(fibonacci, range(0, num)))
    print(listOfFibonacciNumbers)

create_fibonacci_series(7)

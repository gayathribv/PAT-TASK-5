"""

Use Python's Lambda function to create a fibonacci series from 1 to 50
First trying with normal for loop

"""
import functools
from functools import reduce
fibonacci = lambda number: number if number <= 1 else fibonacci(number - 1) + fibonacci(number - 2);
listOfFibonacciNumbers = list(map(fibonacci, range(0,10,1)));
print(listOfFibonacciNumbers);

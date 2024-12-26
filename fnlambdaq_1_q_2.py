"""
Q1 .Present the expected output for the code piece given below
The lambda function takes in the iterable data and applies the expression x > 4
returns the result (elements of data array greater than 4)
The filter function will Filter the list, and return a new array with only
the values returned by lambda function
The list function creates a list of the results returned by filter 
"""

data= [10, 501, 22, 37, 100, 999, 87, 351 ]
result =filter(lambda x:x>4, data)
print(list(result))


"expected output of code for q1"
"""
>>> print(list(result))
>>> [10, 501, 22, 37, 100, 999, 87, 351]
"""



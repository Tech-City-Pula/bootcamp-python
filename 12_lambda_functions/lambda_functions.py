"""
Lambda functions in Python are like quick, one-time-use tools that you make on the spot. They're small anonymous functions defined with the lambda keyword. Lambda functions can take any number of arguments, but they can only have one expression, which is evaluated and returned. You'd use a lambda function when you need a simple function for a short period of time, and you're typically not going to reuse it. They are handy for simple operations in methods that expect a function as an argument, like sorted(), map(), filter(), etc.
"""

# define a lambda function to add two numbers
add = lambda x, y: x + y

# use the lambda function
result = add(5, 3)

# a list of tuples
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]

# sort the list by the second item in each tuple
pairs.sort(key=lambda pair: pair[1])

numbers = [1, 2, 3, 4, 5, 6]

# Filter out even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# create a new list with each number squared
squared_numbers = list(map(lambda x: x ** 2, numbers))
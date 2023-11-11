# Exercise 1: Write a lambda function that multiplies a number by itself (squares it) and apply it to the number 8.

square = lambda x: x * x

eight_squared = square(8)

print(eight_squared)

# Exercise 2: Create a list of numbers from 1 to 5, and use a lambda function with map to increment each number in the list. Print the resulting list of numbers.

numbers = [1, 2, 3, 4, 5]

incremented_numbers = [number for number in map(lambda number: number + 1, numbers)]

print(incremented_numbers)
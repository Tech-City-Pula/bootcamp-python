# Exercise 1: Create a variable named age and assign your age to it. Then print a sentence using this variable like "I am X years old" where X is the age variable.

age = 27

print(f"I am {age} years old")

# Exercise 2: Swap the values of two variables. Start with a = 10 and b = 20, and end up with a = 20 and b = 10 without using direct assignment (i.e., without just doing a = 20).

a = 10
b = 20

print(a, b)

temp = b # 20
a = temp # 20
b = a # 10

print(a, b)

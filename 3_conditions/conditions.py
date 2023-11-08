"""
Conditions in Python are like making a decision based on a question. You ask a question that can be answered as either "True" or "False" and then tell the computer what to do in each case. For example, using an if statement, you can check if a number is greater than another: if number > 10:. This means "if the number is greater than 10, do the following." You can also use else to specify what should happen if the condition is not true. Conditions help your program make choices and take different actions based on the data it has.
"""

favorite_number_as_string = input("what's your favorite number?\n")
x = int(favorite_number_as_string)

if x > 50:
    print(f"{x} is greater than 50")
elif 0 < x <= 50:
    print(f"{x} is between 0 and 50")
elif x == 0:
    print(f"{x} is exactly 0")
else:
    print(f"{x} is less than 0")
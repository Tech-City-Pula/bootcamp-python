# Exercise 1: Use the random module to generate a random number between 1 and 100, then print it.
from random import randint

print(randint(1, 100))

# Exercise 2: Import the datetime module and print the current date in the format "Year-Month-Day".
from datetime import datetime

print(datetime.now().strftime("%y-%m-%d"))
# Exercise 1: Write an if statement to check if a number stored in a variable is even or odd. Print an appropriate message for each case.
number = 4

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Exercise 2: Ask the user to input a word and check if that word is "Python". If it is, print "You guessed the right word!", otherwise print "Try again!".

word = input("enter a word\n")

if word == "Python":
    print("You guessed the right word!")
else:
    print("Try again!")
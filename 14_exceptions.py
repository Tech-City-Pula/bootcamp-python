try:
    x = int(input("What's your favorite number?\n"))

    if x > 50:
        print("x is greater than 50")
    elif 0 < x <= 50:
        print("x is between 0 and 50")
    elif x == 0:
        print("x is exactly 0")
    else:
        print("x is less than 0")
except ValueError:
    print("You did not enter a valid number.")
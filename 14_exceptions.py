"""
Exceptions in Python are like alerts that pop up when something goes wrong in your program. When Python encounters an error, it "throws" an exception—an object that contains information about the problem. This interrupts your program's normal flow of control, and if not properly handled, it will cause your program to crash. To manage these errors, you can use try and except blocks. You put the code that might cause an error in a try block, and then you write except blocks to catch and handle the exception if it happens. This way, you can deal with problems gracefully in your code.
"""

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
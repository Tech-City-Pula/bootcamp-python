# Exercise 1: Write a try/except block to handle a FileNotFoundError when trying to open a file that does not exist. The except block should print a friendly error message.

filename = "./does_not_exist.txt"

try:
    with open(filename, "r") as file:
        line = file.readline()
        print(line)
except FileNotFoundError:
    print(f"file \"{filename}\" does not exists")

# Exercise 2: Modify the division program from earlier so that it handles any type of Exception by printing "An error occurred", but also add an else block that prints "No errors occurred" if there were no issues.

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("No errors occurred. The result is:", result)

divide_numbers(2, 0)
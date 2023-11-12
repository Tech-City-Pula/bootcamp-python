import os
from functools import wraps

CURRENT_DIRECTORY = os.getcwd()

def add_whitespace():
    print('\n\n\n')

def clear_screen(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Run the function
        result = func(*args, **kwargs)

        add_whitespace()

        input("press enter key to continue")
        # Clear the screen (for macOS and Linux)
        os.system('clear')
        return result

    return wrapper

def template(question):
    return (
f"""{question}
> """
    )

def prompt(question):
    answer = input(template(question))

    return answer


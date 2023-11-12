from util import clear_screen, prompt, CURRENT_DIRECTORY
import os
import json


BIRTHDAYS_FILENAME = os.path.join(CURRENT_DIRECTORY, "storage/birthdays.json")

birthdays = {}

try:
    with open(BIRTHDAYS_FILENAME, 'r') as file:
        birthdays = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print("no birthdays file found, creating new one")
    with open(BIRTHDAYS_FILENAME, 'w') as file:
        json.dump(birthdays, file)
        

@clear_screen
def view():
    if len(birthdays) > 0:
        for friend in birthdays:
            birthday = birthdays[friend]
            print(f"{friend}: {birthday}")
    else:
        print("no birthdays :(")

    

@clear_screen
def add():
    name = prompt("enter friend's name:")
    dob = prompt("enter friends date of birth:")

    birthdays[name] = dob

    print(f"added {name} ({dob})!")

def save():
    with open(BIRTHDAYS_FILENAME, 'w') as file:
        json.dump(birthdays, file)
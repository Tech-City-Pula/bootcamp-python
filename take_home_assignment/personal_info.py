from util import clear_screen, prompt, CURRENT_DIRECTORY
import json
import os

PERSONAL_INFO_FILENAME = os.path.join(CURRENT_DIRECTORY, "storage/personal_info.json")

personal_info = {}

try:
    with open(PERSONAL_INFO_FILENAME, 'r') as file:
        personal_info = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print("no personal info file found, creating new one")

    with open(PERSONAL_INFO_FILENAME, 'w') as file:
        json.dump(personal_info, file)


@clear_screen
def view():
    if len(personal_info) > 0:
        for property in personal_info:
            info = personal_info[property]
            print(f"{property}: {info}")
    else:
        print("no personal info :(")
    

@clear_screen
def add():
    property = prompt('enter property:')
    value = prompt('enter value:')

    personal_info[property] = value

    print(f"{property} set to {value}!")

@clear_screen
def update():
    for property in personal_info:
        print(property)

    property = prompt("enter property name for property you'd like to update:")

    try:
        previous = personal_info[property]
        value = prompt("what do you want to change it to?")
        personal_info[property] = value
        print(f"{previous} updated to {value}!")
    except KeyError:
        print('invalid key')
    


@clear_screen
def delete():
    for property in personal_info:
        print(property)

    property = prompt("enter property name for property you'd like to delete:")

    try:
        del personal_info[property]

        print(f"{property} deleted!")
    except KeyError:
        print('invalid key')

def save():
    with open(PERSONAL_INFO_FILENAME, 'w') as file:
        json.dump(personal_info, file)
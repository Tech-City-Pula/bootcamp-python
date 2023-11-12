from util import prompt, add_whitespace
import birthdays
import personal_info
import tasks
import os

current_directory = os.getcwd()

def clear_screen():
    os.system('clear')

def quit_program():
    print("saving birthdays...")
    birthdays.save()
    print("saved birthdays!")
    print("saving tasks...")
    tasks.save()
    print("saved tasks!")
    print("saving personal_info...")
    personal_info.save()
    print("saved personal_info!")
    print("exiting...")
    exit()

commands = {
    # general
    "q": {
        "description": "Quit the program",
        "command": quit_program
    },

    # tasks
    "vt": {
        "description": "View all tasks",
        "command": tasks.view
    },
    "at": {
        "description": "Add a new task",
        "command": tasks.add
    },
    "ct": {
        "description": "Complete a task",
        "command": tasks.complete
    },

    # personal info
    "vp": {
        "description": "View personal info",
        "command": personal_info.view
    },
    "ap": {
        "description": "Add personal info",
        "command": personal_info.add
    },
    "up": {
        "description": "Update personal info",
        "command": personal_info.update
    },
    "dp": {
         "description": "Delete personal info",
        "command": personal_info.delete
    },

    # birthdays
    "vb": {
        "description": "View friend's birthdays",
        "command": birthdays.view
    },
    "ab": {
        "description": "Add friend's birthday",
        "command": birthdays.add
    }
}

def run():
    for key in commands:
        description = commands[key]["description"]
        print(f"{key}: {description}")

    add_whitespace()

    command_key = prompt("enter command:")
    normalized_key = command_key.strip().lower()

    try:
        command = commands[normalized_key]["command"]

        add_whitespace()

        command()

    except KeyError:
        print(f"invalid key {normalized_key}")


while True:
    run()



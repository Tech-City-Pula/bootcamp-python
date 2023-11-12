from util import clear_screen, prompt, CURRENT_DIRECTORY
import os
import json

TASKS_FILENAME = os.path.join(CURRENT_DIRECTORY, "storage/tasks.json")

tasks = []

try:
    with open(TASKS_FILENAME, 'r') as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
        print("no tasks file found, creating new one")

        with open(TASKS_FILENAME, 'w') as file:
            json.dump(tasks, file)

@clear_screen
def view():
    if len(tasks) > 0:
        for task in tasks:
            title, completed = task['title'], task['completed']
            completed_emoji = "✅" if completed else "❌"
            
            print(f"{title} - {completed_emoji}")
    else:
        print('no tasks :)')

@clear_screen    
def add():
    title = prompt('give me a title:')

    tasks.append({
        "title": title,
        "completed": False
    })

    print(f"{title} added!")


@clear_screen
def complete():
    for index in range(len(tasks)):
        task = tasks[index]
        title, completed = task['title'], task['completed']

        completed_emoji = "✅" if completed else "❌"

        print(f"- {index} - {title} {completed_emoji}")
        
    index = prompt('which task would you like to complete?')

    try:
        task = tasks[int(index)]
        task['completed'] = True

        print(f"{task['title']} completed!")
    except IndexError:
        print(f"invalid index {index}")

def save():
    with open(TASKS_FILENAME, 'w') as file:
        json.dump(tasks, file)
"""
Dictionaries in Python are like a real-life dictionary where you look up a word (a "key") to find its definition (a "value"). They are created with curly braces {} containing pairs of keys and values, like my_dict = {'name': 'Alice', 'age': 25}. To access the value, you use the key like this: my_dict['name'] would give you 'Alice'. You can change values, add new pairs, or remove them. Dictionaries are great when you want to associate items with a meaningful label instead of just a position in a list.
"""

# dict
player = {
    "username": "hackerman",
    "level": 1337,
    "items": ["sword", "shield"],
    "stats": {
        "health_points": 100,
        "mana": 72,
        "strength": 10,
        "intelligence": 25
    }
}

# access field
username = player['username']

# access nested field
health_points = player["stats"]['health_points']

# update field
player["level"] = 1338

# add new field
player["guild"] = "Warriors of Light"

# delete field
del player["guild"]

# checking if field exists
if "health_points" in player["stats"]:
    print("Health points:", player["stats"]["health_points"])

# looping over all top-level keys
for key in player:
    print(key, ":", player[key])
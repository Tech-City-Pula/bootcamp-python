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
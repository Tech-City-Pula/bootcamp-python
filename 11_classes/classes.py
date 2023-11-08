"""
Classes in Python are like blueprints for creating objects—a class defines the shape and behaviors of all instances of that type. Imagine a class as a recipe that you can use to make similar yet distinct batches of cookies. Each batch, while made from the same recipe, can have unique characteristics like the number of chips or the size of the cookies. Classes bundle data and functionality together and are a fundamental part of Python's approach to object-oriented programming (OOP).
"""

# define player class
class Player:
    def __init__(self, username, level, items, stats):
        self.username = username
        self.level = level
        self.items = items
        self.stats = stats

    def greet(self):
        print(f"Hello, {self.username}! You are at level {self.level}.")

    def attack(self):
        print(f"{self.username} attacks with a power of {self.stats['strength']}!")

    def get_stats(self):
        return self.stats

# player dict from before
player_info = {
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

# create a Player instance
player = Player(
    username=player_info["username"],
    level=player_info["level"],
    items=player_info["items"],
    stats=player_info["stats"]
)

# use the Player methods
player.greet()       
player.attack()      
stats = player.get_stats()
print(stats)

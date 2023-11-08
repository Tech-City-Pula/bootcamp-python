"""
Data structures in Python are different ways of organizing and storing data so that it can be used efficiently. Think of them like different types of containers in a kitchen. Some common Python data structures are:

Lists: Like a row of jars on a shelf, each with an item inside. You can add, remove, or change the items.
Tuples: Like a fixed pack of items, you cannot change them once you've put them together.
Dictionaries: Like a file cabinet, where each drawer has a label and contains specific items. You can find items quickly by their labels.
Sets: Like a basket of fruit where you don't care about the order and you don't have duplicates.
Each structure has its own methods and uses depending on what you need to do with your data.
"""

# list
basket = ["apples", "grapes"]

# set
unique_items_in_basket = set(basket)

# tuple
pula_coordinates = (44.8666, 13.8496)

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

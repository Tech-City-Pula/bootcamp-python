"""
Lists in Python are like a line of baskets where you can put things in order, change them, or take them out. You create a list by putting items inside square brackets [], separated by commas. For example, fruits = ["apple", "banana", "cherry"] is a list of fruits. You can access list items by their position in the line (which starts at 0), so fruits[0] is "apple". You can also add more items, remove items, or sort the list. Lists are versatile and are used often in Python programs.
"""

# list
basket = ["apples", "grapes"]

# add items to list
basket.append("bananas")
basket.append("oranges")

# access certain list item
apples = basket[0]

# get the length of the list (i.e. count of items that are inside of the list)
basket_count = len(basket)

# loop over a list using indexes
for index in range(basket_count):
    item = basket[index]
    print(f"{index}: {item}")

items_to_add_to_basket = ["pears", "peaches", "mushrooms", "carrots", "celery", "avocados", "potatos", "onions", "salad", "tomatoes"]

# loop over list items without using indexes
for item in items_to_add_to_basket:
    basket.append(item)


# use an array method to do the same
basket.extend(items_to_add_to_basket)

# check if item exists inside the array
if "apples" in basket:
    print("we have apples!")
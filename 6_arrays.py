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


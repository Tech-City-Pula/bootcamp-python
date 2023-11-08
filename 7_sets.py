"""
Sets in Python are like a bag where you throw in items without worrying about the order, and each item can only appear once; it's a collection with no duplicates. You make a set with curly braces {} or the set() function, like this: my_set = {1, 2, 3} or my_set = set([1, 2, 3]). Unlike lists, sets can't have two items that are the same, and you can't get items by their position. Sets are useful when you need to keep track of unique items and you're not concerned with the order they're in.
"""


my_basket = ["apples", "grapes"]

my_basket.append("apples")
my_basket.append("apples")
my_basket.append("apples")
my_basket.append("apples")
my_basket.append("apples")
my_basket.append("apples")
my_basket.append("apples")
my_basket.append("apples")
my_basket.append("apples")
my_basket.append("apples")

unique_fruits_in_my_basket = set(my_basket)

my_friends_basket = {"apples", "oranges"}

# unique fruits in both baskets together
print(unique_fruits_in_my_basket.union(my_friends_basket))

# fruits i have that my friend doesn't
print(unique_fruits_in_my_basket.difference(my_friends_basket))

# fruits we have in common
print(unique_fruits_in_my_basket.intersection(my_friends_basket))

# checking if a fruit is in basket
if "apples" in my_friends_basket:
    print("my friend has apples!")
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
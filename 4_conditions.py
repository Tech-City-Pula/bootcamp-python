favorite_number_as_string = input("what's your favorite number?\n")
x = int(favorite_number_as_string)

if x > 50:
    print(f"{x} is greater than 50")
elif 0 < x <= 50:
    print(f"{x} is between 0 and 50")
elif x == 0:
    print(f"{x} is exactly 0")
else:
    print(f"{x} is less than 0")
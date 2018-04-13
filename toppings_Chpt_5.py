# loop to check for special items with an if statement and a for loot
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers': 
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# check if a list is empty

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers': 
            print("Sorry, we are out of green peppers right now.")
        else:
            print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# check to ensure requested toppings are in the list

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")


# ordinal numbers
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    elif number == 4:
        print(str(number) + "th")
    elif number == 5:
        print(str(number) + "th")
    elif number == 6:
        print(str(number) + "th")
    elif number == 7:
        print(str(number) + "th")
    elif number == 8:
        print(str(number) + "th")
    elif number == 9:
        print(str(number) + "th")
# types of pizza 
pizzas = ["plain", "pepperoni", "grandma"]
friend_pizzas = pizzas[:]
pizzas.append("sausage")
friend_pizzas.append("meatball")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
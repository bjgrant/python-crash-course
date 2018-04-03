# List of motorcycle brands.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# Replace first element
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
# adds a new element to the end of the list
motorcycles.append('ducati')
print(motorcycles)
# Creates an empty list
motorcycles = []
# adds each element one by one
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#inserts a new item into the list at the first index
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# deletes the first item in the list
del motorcycles[0]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# deletes the second item in the list
del motorcycles[1]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# Pop an item from a list
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles = ['honda', 'yamaha', 'suzuki']
# Pops an item by index
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# Removes an item by name
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# remove and item by name and use the variable to explain why we removed it
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
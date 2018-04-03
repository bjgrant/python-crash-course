# lists chapter 3 

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# access first element
print(bicycles[0])
# Capitalize first letter of the first element
print(bicycles[0].title())
# Print second element
print(bicycles[1])
# Print fourth element
print(bicycles[3])
# Print last element
print(bicycles[-1])
# Using the a list item in a variable
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message) 
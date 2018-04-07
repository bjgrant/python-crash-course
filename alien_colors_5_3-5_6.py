# if statment to test if color is green
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
# this time the if statement is false
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
# if else block using alien color 
if alien_color == 'green':
    points = 5
else:
    points = 10
print("You just earned " + str(points) + " points!")
# The if is true here
alien_color = 'green'
if alien_color == 'green':
    points = 5
else:
    points = 10
print("You just earned " + str(points) + " points!")
#make an if-else chain out if it
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
print("You just earned " + str(points) + " points!")
# first elif is true
alien_color = 'yellow'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
print("You just earned " + str(points) + " points!")
# second elif is true
alien_color = 'red'
alien_color = 'yellow'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
print("You just earned " + str(points) + " points!")
# If-elif chain that determines person stage in life
age = 5
if age < 2:
    stage = "baby"
elif age <= 3:
    stage = "toddler"
elif age <= 12:
    stage = 'kid'
elif age <= 19:
    stage = 'teenager'
elif age <= 64:
    stage = 'adult'
elif age >= 65:
    stage = 'senior'

print("The persons stage in life is " + stage + ".")

# series of if statements
fruits = ['pear', 'orange', "apple", 'lime', 'grapefruit' ]

if 'tangerine' in fruits:
    print("You must love tangerines!")
if 'pear' in fruits:
    print("You must love pears!")
if 'apple' in fruits:
    print("You must love apples!")
if 'pineapple' in fruits:
    print("You must love pineapples!")
if 'grapefruit' in fruits:
    print("You must love grapefruits!")






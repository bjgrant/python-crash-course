#list of players
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print the first 3 players (slice)
print(players[0:3])
# print players 2 -4
print(players[1:4])
# print the first 4 players
print(players[:4])
# start at player 3
print(players[2:])
# print the last 3 players on the list
print(players[-3:])
# loop through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
#copy a list to a new list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# add a new food to each list
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# 4-10 slices 
# print first three items
print("The first three items in the players list are: " + str(players[:3]))
# Print middle three names
print("The middle three items in the players list are: " + str(players[1:4]))
# print the last three names 
print("The last three items in the players list are" + str(players[-3:]))
# 4-12 More loops
for foods in my_foods:
    print(foods)
for foods in friend_foods:
    print(foods)
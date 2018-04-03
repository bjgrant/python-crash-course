# List of people to have dinner with
guests = ["Buddy Neilson", "Ben Franklin", "Aidan Grant"]
# invite guests to dinner
print(guests[0] + " please join us for a dinner to remember.")
print(guests[1] + " please join us for a dinner to remember.")
print(guests[2] + " please join us for a dinner to remember.")
# Remove someone who cannot make it
cannot_attend = guests.pop(1)
print(cannot_attend)
# Add replacement guest 
guests.insert(1, "John Adams") 
print(guests)
# Print a message to each guest
print(guests[0] + " please join us for a dinner to remember.")
print(guests[1] + " please join us for a dinner to remember.")
print(guests[2] + " please join us for a dinner to remember.")
# add more guests
guests.insert(0, "Reggie White")
guests.insert(2, "Richard Petty")
guests.append("Burt Reynolds")
# print a message inviting the guests
print(guests[0] + " please join us for a dinner to remember, we found a bigger table!")
print(guests[1] + " please join us for a dinner to remember, we found a bigger table!")
print(guests[2] + " please join us for a dinner to remember, we found a bigger table!")
print(guests[3] + " please join us for a dinner to remember, we found a bigger table!")
print(guests[4] + " please join us for a dinner to remember, we found a bigger table!")
print(guests[5] + " please join us for a dinner to remember, we found a bigger table!")
# Now we only have space for two people
print("Due to unforseen circumstances our space is now limited.")
# Pop users on by one and print a message letting them know
print(guests.pop() + " sorry but we ran out of space, lets have dinner some other time.")
print(guests.pop() + " sorry but we ran out of space, lets have dinner some other time.")
print(guests.pop() + " sorry but we ran out of space, lets have dinner some other time.")
print(guests.pop() + " sorry but we ran out of space, lets have dinner some other time.")
print(guests)
# Let the two remaining guests know they are still invited
print(guests[0] + " the dinner is still on!")
print(guests[1] + " the dinner is still on!")
del guests[1]
del guests[0]
print(guests)
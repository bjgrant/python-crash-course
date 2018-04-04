# Basic for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
magicians = ['alice', 'david', 'carolina']
# Print a message to each magician
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    # print another statement to each magician
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# Print a statement at the end
print("Thank you, everyone. That was a great magic show!")
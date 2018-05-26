# poll of multiple people in dictonary form

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() +
    ".")

# Look through to print everyones favorite language

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

# print all of the keys in a dictonary with a for loop

for name in favorite_languages.keys():
    print(name.title())

# loop through dictonary and use an if statement to match a key in a varible

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + 
            favorite_languages[name].title() + "!")

# checking if a person took the poll

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
# print the names sorted alphabetically

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")

# print the values

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# print the languages without duplicates using set

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# check if people have taken poll, print message based on that status
people = ['bob', 'jen', 'ammie', 'sarah', 'bubba']

for person in people:
    if person in favorite_languages.keys():
        print(person + ", thank you for taking the poll.")
    elif person not in favorite_languages.keys():
        print(person + ", please take our poll.")
        




    



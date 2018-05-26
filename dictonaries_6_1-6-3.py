# store infomation on a person in a dictonary and print the info

person = {'first_name': 'Johnny',
    'last_name': 'Wishbone',
    'age': 45,
    'city': 'Beverly Hills',

}

print(person)

# Make a dictionary of favorite numbers and print each one

favorite_numbers = {
    "ammie": 42,
    'popa': 43,
    'lobster': 101,
    'bubba': 28,
    'Johnny': -1,
    }

print(favorite_numbers)

# create a glossary and print it

glossary = {
    '>': 'greater than',
    '<': 'less than',
    'list': 'collection of entities',
    'python': 'programming language',
    'boolean': 'true or false',
    'sorted': 'sorts alphabetically',
    'set': 'creates a unique list',
    'keys()': 'accesses the keys in a dictionary',
    'values()': 'accesses the values in a dictionary',
    'if': "checks if something is true",
}

for key, value in glossary.items():
    print(key + " means " + value + ".")


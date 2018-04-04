# create a loop that counts to 20
#numbers = list(range(1,21))
#for number in numbers:
#    print(number)
# Create a list of one to a million and print each number
#numbers = list(range(1,1000001))
#for number in numbers:
#    print(number)
# commented the above code because to stop 1 millions numbers from being displayed
# it will run if uncommented

# list of 1,000,000 numbers
'''numbers = list(range(1,1000001))
# Min number in list
print(str(min(numbers)))
# Max number in list
print(str(max(numbers)))
# Sum of the numbers in the list
print(str(sum(numbers)))
# make a list of odd numbers between 1 - 20
numbers = list(range(1,21,2))
for number in numbers:
    print(number) '''
# List of multiples 3 to 30
numbers = [3,6,9,12,15,18,21,24,27,30]
for number in numbers:
    print(number)
numbers = []
for value in range(1,11):
    number = value**3
    numbers.append(number)
    print(number)
print(numbers)
# first 10 cubes list comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)

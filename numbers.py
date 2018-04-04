# Generate a series of numbers
for value in range(1,5):
    print(value)
# Generate 1 - 5, buy using the range 1 -6
for value in range(1,6):
    print(value)
# use range() to create a list of numbers
numbers = list(range(1,6))
print(numbers)
# tell range to skip odd numbers
# the second 2 tells python to add 2 to the first value until it hits the second value
even_numbers = list(range(2,11,2))
print(even_numbers)
# squares of 1 - 10 
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
# more concise code of the above
# No reason to store the square in a temporary variable
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
# min, max and sum functions, they do exactly what you think they do
digits = list(range(0,10))
print("Digits: " + str(digits) + "\n")
print("Min: " + str(min(digits)) + "\n")
print("Max: " + str(max(digits)) + "\n")
print("Sum: " + str(sum(digits)))
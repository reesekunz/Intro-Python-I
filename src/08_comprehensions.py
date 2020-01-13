"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
for x in range(5):  # outer loop range 0-4
    y.append(x + 1)  # Add 1 to each value so its 1 -5

print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
for x in range(10):  # outer loop range 0-9
    y.append(x**3)  # take the ^3 of every value being looped through 0-9

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

# loop through a and convert each index (x) to uppercase
y = [x.upper() for x in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

input_numbers = input("Enter comma-separated numbers: ").split(',')
# integer_input_numbers = int(input_numbers)
# What do you need between the square brackets to make it work?
y = [int(input_numbers)]
for x in input_numbers:
    if x % 2 == 0:
        y.append(x)
print(y)

# Method 2
# input_number = input("Enter number: ")
# modulus = int(input_number) % 2
# if modulus != 0:
#     print("odd number")
# else:
#     print("even number")

# Method 3 (brute force lol)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# y = []
# for x in numbers:
#     if x % 2 == 0:
#         y.append(x)

# print(y)

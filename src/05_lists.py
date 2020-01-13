# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# in terminal: python -> x = [1,2,3] -> dir(x) will tell you all available methods
# ex: help(x.pop) or help(x.append), etc.

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)  # insert 4 to end of array x
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x = x+y  # Combines array x with array y
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)  # removes 8 from combined array
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)  # at index 5, insert 99
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000
# Iterate through array x and multiply each value by 1000
new_array = [x * 1000 for x in x]
print(new_array)

# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# OR

for num in y:
    x.append(num)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)  # at index 5, insert 99
# could also do x.insert(-1, 99)
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000

for num in x:
    print(num*1000)

 # OR


# mutiply_values = [number * 1000 for number in x]
# print(mutiply_values)

# OR

# mutiply_values_two = []
# for number in x:
#     value = number * 1000
#     mutiply_values_two.append(value)

# print(mutiply_values_two)

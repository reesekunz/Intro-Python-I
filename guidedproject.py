''' Intro to Python I - Guided Project
    This document contains examples for CS Intro to Python, module 1. Examples
    focus on Python syntax & semantics plus the usage of lists, dicts, sets,
    and tuples.
'''
# Lists = like arrays in javascript ()
array = [1, 2, 8, 10, 2]
# Dictionaries = like objects in javascript {key:value} pairs
person = {"name": "joe", "age": 35, "city": "Phoenix"}
print(person["name"]) # Accessing a value in a dictionary
print(person["age"]) # Dictionaries arent ordered so cant access with [0] index
# Tuples - immutable (cant be changed)
students = ("student1", "student2")
# Sets = Only one that cant have duplicates, also unordered so can't access with index [0]
users = {342432, 12312321, 123132, 1111} # no key value pairs, just elements separated by commas 

### Questions 
# How do we print something to the console?
print("Hello, world!")
print('"Hello world", said Austen')  # Example with quotes
print("Aren't you excited to learn Python")  # Example with apostrophe


# With f-strings? - f string Inserts variable data in strings
name = "Reese"
print("Hello " + name)  # avoid this
print(f"Hello, {name}")  # f string (do this)

# Given an "out" string length 4, such as "<<>>", and a word, return a new
# string where the word is in the middle of the out string, e.g. "<<word>>".
# (from CodingBat)


def make_out_word(out, word):
    # [0:2] is the same as [:2], just saying to start at index 0 or beginning
    return out[0:2] + word + out[2:]

    # pass - tells function to do nothing function can run without errors) - good placeholder to use when outlining something


print(make_out_word('<<>>', 'Yay'))  # → '<<Yay>>'
print(make_out_word('<<>>', 'WooHoo'))  # → '<<WooHoo>>'
print(make_out_word('[[]]', 'word'))  # → '[[word]]'


# Given an array of ints length 3, return the sum of all the elements.
# (from CodingBat)

def sum3(nums):
    return sum(nums)  # could also do nums[0] + numbs[1] + nums[2]
                      # lists in python = array in javascript


print(sum3([1, 2, 3]))  # → 6
print(sum3([5, 11, 2]))  # → 18
print(sum3([7, 0, 0]))  # → 7

# Return the sum of the numbers in the array, except ignore sections of numbers
# starting with a 6 and extending to the next 7 (every 6 will be followed by at
# least one 7). Return 0 for no numbers.
# (from CodingBat)


def sum67(nums):
#1. establish what we are returning - returning the sum (decide if you print, return, etc.)
    sum = 0 # initialize sum at 0
    skip = False # initialize skip (going to turn it to True if its a 6)
    for x in nums: # loop through nums array 
        if x == 6: # which numbers do we care about? 6 and 7
            skip = True           # ignore until we find a 7 - remove? 
        elif x == 7:
             skip = False      # start adding again if find a 7
        else: 
            if skip is False: # same as if skip == False, but cleaner
                sum += x
            
    return sum
    
 
print(sum67([1, 2, 2])) # → 5
print(sum67([1, 2, 2, 6, 99, 99, 7])) # → 5 - ignore 6, 99, 99 to get to 7
print(sum67([1, 1, 6, 7, 2])) # → 4 - ignore 6 to get to 7



# Create a new list containing the squares of all values in `numbers`with a
# list comprehension
numbers = [1, 2, 3, 4, 5]
print(numbers)

squares = [x*x for x in numbers]
print("squares", squares)
# SAME AS 
squares_two = []
for x in numbers:
    squares_two.append(x*x)
print("squares_two", squares_two)
# We can also use list comprehensions to filter!
# Create a new list containing only the even values of `numbers`
even_numbers = [x for x in numbers if x % 2 == 0] # add x to list if x in numbers if divisible by 2
print("even numbers", even_numbers)
# SAME AS
even_numbers_two = []
for x in numbers:
    if x % 2 == 0: # if number is divisible by 2
        even_numbers_two.append(x)
print("even numbers two", even_numbers_two)

# Can you use pieces of both of the above examples to...
# Create a new list containing only the names that start with `s` so that they
# are properly capitalized (regardless of how the name originally appears)
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
print(names)

start_with_s = [x.capitalize() for x in names if x[0].lower() == "s" ]
print(start_with_s)

# SAME AS
start_with_s_two = [] # initialize new array
for x in names: # loop through names array
    if x[0].lower() == "s": # Filter through array to find "s", convert to lower case to keep what youre looking for consistent
        start_with_s_two.append(x.capitalize()) # Add new (capitalized) value to list
print(start_with_s_two)

    

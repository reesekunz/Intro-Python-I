# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def changeX():
    global x  # now prints 99
    x = 99


changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(x)


# This nested function has a similar problem.

y = 120


def inner():
    y = 999
    print("from inner", y)


inner()
# This prints 120. What do we have to change in inner() to get it to print
# 999? Google "python nested function scope".
print("from outer", y)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Write a function is_even that will return true if the passed-in number is even.


def is_even(num):
    if num % 2 == 0:  # even
        return True
    else:
        return False  # odd


print(is_even(num))


# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even_two(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")


print(is_even_two(num))

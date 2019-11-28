import math
# Create a function called func_a, which prints a message.
# Call the function.
# Assign the function object as a value to the variable b, without calling the function.
# Now call the function using the variable b.


def func_a():
    print('aaaaaaaaaa')


func_a()
b = func_a
b()

# Create a function called hypotenuse, which takes two numbers as parameters and prints the square root of the sum of
# their squares.
# Call this function with two floats.
# Call this function with two integers.
# Call this function with one integer and one float.


def hypotenuse(a, b):
    print(math.sqrt(a**2 + b**2))


hypotenuse(2, 3)
hypotenuse(12.3, 45.6)
hypotenuse(12, 34)
hypotenuse(12, 34.5)

# Rewrite the hypotenuse function from exercise 2 so that it returns a value instead of printing it.Add exception
# handling so that the function returns None if it is called with parameters of the wrong type.
# Call the function with two numbers, and print the result.
# Call the function with two strings, and print the result.
# Call the function with a number and a string, and print the result.


def hypotenuse_A(a, b):
    try:
        return math.sqrt(a ** 2 + b ** 2)
    except TypeError:
        return None


print(hypotenuse_A(12, 34))
print(hypotenuse_A("12", "34"))
print(hypotenuse_A(12, "34"))


def fibonacci(n):
    current, next = 0, 1

    for i in range(n):
        current, next = next, current + next

    return current


print(fibonacci(4))

# Write a recursive function which calculates the factorial of a given number.Use exception
# handling to raise an appropriate exception if the input parameter is not a positive integer,
# but allow the user to enter floats as long as they are whole numbers.

# Factorial(n!)
# For n>0,
# n! = 1×2×3×4×...×n
# For n=0,
# 0! = 1
# Recursive factorial formula
# n! = n×(n-1)!


def factorial(n):
    ni = int(n)

    if ni != n or ni <= 0:
        raise ValueError("%s is not a positive integer." % n)

    if ni == 1:
        return 1

    return ni * factorial(ni - 1)


print(factorial(5))

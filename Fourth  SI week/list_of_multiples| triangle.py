# In this simple exercise, you will build a program that takes a value, integer, and returns a list of its multiples up
# to another value, limit. If limit is a multiple of integer, it should be included as well. There will only ever be
# positive integers passed into the function, not consisting of 0. The limit will always be higher than the base.

# For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the
# multiples of 2 up to 6.

# If you can, try writing it in only one line of code.


def find_multiples(integer, limit):
    number = 0
    multiple_list = []
    while limit > number:
        number += integer
        multiple_list.append(number)
    return multiple_list


# def find_multiples(integer, limit):
#     return list(range(integer, limit+1, integer))


# Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built
# with the sides of given length and false in any other case.
# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)

# def is_triangle(a, b, c):
#     a, b, c = sorted([a, b, c])
#     return a + b > c

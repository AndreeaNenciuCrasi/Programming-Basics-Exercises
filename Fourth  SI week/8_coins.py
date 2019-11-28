# I found this interesting interview question just today:

# 8 coins are given where all the coins have equal weight, except one. The odd one weights less than the others,
# not being of pure gold. In the worst case, how many iterations are actually needed to find the odd one out on a
# two plates scale.

# I am asking you then to tell me what is the minimum amount of weighings it will take to measure n coins in every
# possible occurrence (including worst case scenario, ie: without relying on luck at all).

# n is guaranteed to be a positive integer.

# Tip: being able to think recursively might help here :p

# Note: albeit this is more clearly a logical than a coding problem, do not underestimate (or under-rank) the kata
# for requiring not necessarily wizard-class coding skills: a good coder is a master of pattern recognition and subsequent
# optimization ;)

# from math import ceil, log


# def how_many_measurements(n):
#     return ceil(log(n, 3))

# def how_many_measurements(n):
#     if n > 1:
#         return 1 + how_many_measurements(n/3)
#     return 0

# import math


# def how_many_measurements(n):
#     if n == 1:
#         return 0
#     if n == 2 or n == 3:
#         return 1
#     if n == 4:
#         return 2
#     return how_many_measurements(math.ceil(n/3)) + 1

def how_many_measurements(n):
    nr_measurements = 0
    while n > 1:
        n = n / 3
        nr_measurements += 1
    return nr_measurements


print(how_many_measurements(1))
print(how_many_measurements(2))
print(how_many_measurements(3))
print(how_many_measurements(8))
print(how_many_measurements(100))

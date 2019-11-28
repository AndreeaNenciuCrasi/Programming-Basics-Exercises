# Create a function add(n)/Add(n) which returns a function that always adds n to any number

# Note for Java: the return type and methods have not been provided to make it a bit more challenging.

# add_one = add(1)
# add_one(3)  # 4

# add_three = add(3)
# add_three(3) # 6


def add(n):
    return lambda x: x + n


# def add(n):
#     def _add(m):
#         return m + n
#     return _add


# Agent 47, you have a new task! Among citizens of the city X are hidden 2 dangerous criminal twins. You task is to
# identify them and eliminate!

# Given an array of integers, your task is to find two same numbers and return one of them, for example in array
# [2, 3, 6, 34, 7, 8, 2] answer is 2.

# If there are no twins in the city - return None or the equivilent in the langauge that you are using.


def elimination(arr):
    for i in arr:
        if arr.count(i) == 2:
            return i


# def elimination(arr):
#     seen = set()
#     for elem in arr:
#         if elem in seen:
#             return elem
#         seen.add(elem)

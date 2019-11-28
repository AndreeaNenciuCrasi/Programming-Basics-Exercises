# Your task is to find the first element of an array that is not consecutive.

# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's
# the first non-consecutive number.

# If the whole array is consecutive then return null or Nothing.

# The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be
# unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be
# either too!


def first_non_consecutive(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] - arr[i + 1] != -1:
            return arr[i + 1]
        i += 1

# def first_non_consecutive(arr):
#     for b in range(len(arr) - 1):
#         if arr[b + 1] - arr[b] != 1:
#             return arr[b + 1]

# def first_non_consecutive(arr):
#     for i, a in enumerate(arr):
#         if 0 < i < len(arr) + 1 and a != arr[i-1] + 1:
#             return a

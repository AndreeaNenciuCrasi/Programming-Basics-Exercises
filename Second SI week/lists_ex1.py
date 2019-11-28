# Create a list a which contains the first three odd positive integers and a list b which contains the first three
# even positive integers.
# Create a new list c which combines the numbers from both lists (order is unimportant).
# Create a new list d which is a sorted copy of c, leaving c unchanged.
# Reverse d in-place.
# Set the fourth element of c to 42.
# Append 10 to the end of d.
# Append 7, 8 and 9 to the end of c.
# Print the first three elements of c.
# Print the last element of d without using its length.
# Print the length of d.
a = [1, 3, 5]
b = [2, 4, 6]
c = [1, 3, 5] + [2, 4, 6]
d = sorted(c)
d.append(10)
c.extend([7, 8, 9])
print(d)
print(c)
c[3] = 42
print(c[:3])
print(d[-1])
print(len(d))

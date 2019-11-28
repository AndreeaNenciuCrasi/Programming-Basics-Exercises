# Create a tuple a which contains the first four positive integers and a tuple b which contains
# the next four positive integers.
# Create a tuple c which combines all the numbers from a and b in any order.
# Create a tuple d which is a sorted copy of c.
# Print the third element of d.
# Print the last three elements of d without using its length.
# Print the length of d.
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = b + a
print(c)
d = sorted(c)
print(d)
print(d[2])
print(d[-3:])
print(len(d))

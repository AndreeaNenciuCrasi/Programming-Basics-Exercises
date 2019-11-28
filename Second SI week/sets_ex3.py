# Create a set a which contains the first four positive integers and a set b which contains
# the first four odd positive integers.
# Create a set c which combines all the numbers which are in a or b(or both).
# Create a set d which contains all the numbers in a but not in b.
# Create a set e which contains all the numbers in b but not in a.
# Create a set f which contains all the numbers which are both in a and in b.
# Create a set g which contains all the numbers which are either in a or in b but not in both.
# Print the number of elements in c.
a = {1, 2, 3, 4}
b = {1, 3, 5, 7}
c = (a | b)
print(c)
d = (a - b)
print(d)
e = (b - a)
print(e)
f = (a & b)
print(f)
g = (a ^ b)
print(g)
print(len(c))

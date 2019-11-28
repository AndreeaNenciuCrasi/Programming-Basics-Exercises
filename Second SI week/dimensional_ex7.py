# Create a list a which contains three tuples. The first tuple should contain a single element, the second two elements
# and the third three elements.
# Print the second element of the second element of a.
# Create a list b which contains four lists, each of which contains four elements.
# Print the last two elements of the first element of b.
a = [(1),
     (1, 2),
     (1, 2, 3)]
print(a[1][1])
b1 = [[1, 2, 3, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4], ]
print(b1[0][-2:])
b = [
    list(range(10)),
    list(range(10, 20)),
    list(range(20, 30)),
    list(range(30, 40)),
]

print(b[0][1:-1])

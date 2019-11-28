# Convert a list which contains the numbers 1, 1, 2, 3 and 3, and convert it to a tuple a.Convert a to a list b. Print its length.
# Convert b to a set c. Print its length.Convert c to a list d. Print its length.Create a range which starts at 1 and ends at 10. Convert it to a list e.
# Create the directory dict from the previous example. Create a list t which contains all the key-value pairs from the dictionary as tuples.
# Create a list v of all the values in the dictionary.
# Create a list k of all the keys in he dictionary.
# Create a string s which contains the word "antidisestablishmentarianism". Use the sorted function on it. What is
# the output type? Concatenate the letters in the output to a string s2.
# Split the string "the quick brown fox jumped over the lazy dog" into a list w of individual words.
a = [1, 1, 2, 3, 3]
a_tuple = tuple(a)
b = list(a_tuple)
c = set(b)
d = list(c)
e = list(range(1, 11))
dic = {
    'Name':	'Telephone number',
    'Jane Doe': '+ 27 555 5367',
    'John Smith': '+ 27 555 6254',
    'Bob Stone': '+ 27 555 5689'}
t = list(tuple(dic.items()))
v = list(dic.values())
k = list(dic.keys())
print(a_tuple, b,  c, d, e, t, v, k)
s = "antidisestablishmentarianism"
s1 = sorted(list(s))
s2 = ''.join(s1)
print(s2)
w = "the quick brown fox jumped over the lazy dog".split()
print(w)

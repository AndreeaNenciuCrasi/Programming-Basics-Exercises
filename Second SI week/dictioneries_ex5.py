# Create a dict directory which stores telephone numbers(as string values), and populate it with these key-value pairs:
dic = {
    'Name':	'Telephone number',
    'Jane Doe': '+ 27 555 5367',
    'John Smith': '+ 27 555 6254',
    'Bob Stone': '+ 27 555 5689'}
# 'Change Jane’s number to + 27 555 1024 }

# Add a new entry for a person called Anna Cooper with the phone number + 27 555 3237

# Print Bob’s number.

# Print Bob’s number in such a way that None would be printed if Bob’s name were not in the dictionary.

# Print all the keys. The format is unimportant, as long as they’re all visible.

# Print all the values.
print(dic)
dic['Jane Doe'] = '+ 27 555 1024'
print(dic)
dic['Anna Cooper'] = '+ 27 555 3237'
print(dic)
print(dic['Bob Stone'])
print(dic.get("Bob Stone", None))
print(dic.keys())
print(dic.values())
print(dic.items())

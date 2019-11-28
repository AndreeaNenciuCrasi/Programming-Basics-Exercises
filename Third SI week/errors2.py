# person = {}

# for prop in ["name", "surname", "age", "height", "weight"]:
#     person[prop] = input("Please enter your %s: " % prop)

# Now there is no unnecessary duplication. We can easily change the string that we use as a prompt, or add more code
# to execute for each property – we will only have to edit the code in one place, not in five places. To add another
# property, all we have to do is add another name to the list.

# Exercise 7
# Modify the example above to include type conversion of the properties: age should be an integer, height and weight
# should be floats, and name and surname should be strings.

person = {}

properties = [
    ("name", str),
    ("surname", str),
    ("age", int),
    ("height", float),
    ("weight", float),
]


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as ie:
        print("The list has no element at index %d." % index)
        raise ie


print_list_element(properties, 2)

for property, p_type in properties:
    valid_value = None

    while valid_value is None:
        try:
            value = input("Please enter your %s: " % property)
            valid_value = p_type(value)
        except ValueError as ve:
            print(ve)
            # print("Could not convert %s '%s' to type %s. Please try again." %
            #       (property, value, p_type.__name__))

    person[property] = valid_value

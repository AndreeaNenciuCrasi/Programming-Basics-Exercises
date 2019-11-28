# Query string is a way to serialize object, which is used in HTTP requests. You may see it in URL:

# codewars.com/kata/search/?q=querystring
# The part q=querystring represents that parameter q has value querystring. Also sometimes querystring used in HTTP POST
# body:

# POST /api/users
# Content-Type: application/x-www-form-urlencoded

# username=warrior&kyu=1&age=28
# The string username=warrior&kyu=1&age=28 represents an entity (user in this example) with username equals warrior,
# kyu equals 1 and age equals 28. The entity may be represented as object:

# {
#   "username": "warrior",
#   "kyu": 1,
#   "age": 28
# }
# Sometimes there are more than one value for property:

# {
#   "name": "shirt",
#   "colors": [ "white", "black" ]
# }
# Then it represents as repeated param:

# name=shirt&colors=white&colors=black
# So, your task is to write a function that convert an object to query string:

# to_query_string({"bar": [2, 3], "foo": 1}) // = > "bar=2&bar=3&foo=1"


def to_query_string(data):
    final_string = ''
    for key, value in sorted(data.items()):
        if isinstance(value, list):
            for i in value:
                final_string += key + "=" + str(i) + '&'
        else:
            final_string += key + "=" + str(value) + '&'
    return final_string[:-1]


print(to_query_string({"bar": 34, "foo": 46}))
print(to_query_string({"bar": [2, 1], "foo": [3, 4]}))
print(to_query_string({"a": "Z", "b": "Y", "c": "X",
                       "d": "W", "e": "V", "f": "U", "g": "T"}))

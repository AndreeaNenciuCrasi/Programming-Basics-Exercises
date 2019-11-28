# Write logging configuration for a program which logs to a file called log.txt and discards all logs less important
# than INFO.
# Rewrite the second program from exercise 2 so that it uses this logging configuration instead of printing messages to
# the console (except for the first print statement, which is the purpose of the function).
# Do the same with the third program from exercise 2.
import logging

dict = {"listname1": [1, 2, 3],
        "listname2": [2, 3, 4],
        "listname3": [3, 4, 5],
        "listname4": [4, 5, 6],
        "listname5": [5, 6, 7],
        "listname6": [6, 7, 8], }

properties = [
    ("name", str),
    ("surname", str),
    ("age", int),
    ("height", float),
    ("weight", float),
]

logging.basicConfig(filename='log.txt', level=logging.INFO)


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        logging.error("The list has no element at index %d." % index)


def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
    except KeyError:
        thedict[listname] = []
        logging.info("Created %s." % listname)
    else:
        logging.info("%s already has %d elements." % (listname, len(l)))
    finally:
        thedict[listname].append(element)
        logging.info("Added %s to %s." % (element, listname))


add_to_list_in_dict(dict, "listname4", 10)
print(dict)
print_list_element(properties, 2)

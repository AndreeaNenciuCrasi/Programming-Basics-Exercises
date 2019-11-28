dict = {"listname1": [1, 2, 3],
        "listname2": [2, 3, 4],
        "listname3": [3, 4, 5],
        "listname4": [4, 5, 6],
        "listname5": [5, 6, 7],
        "listname6": [6, 7, 8], }


def add_to_list_in_dict(thedict, listname, element):
    # if listname in thedict:
    #     l = thedict[listname]
    #     print("%s already has %d elements." % (listname, len(l)))
    # else:
    #     thedict[listname] = []
    #     print("Created %s." % listname)

    # thedict[listname].append(element)

    # print("Added %s to %s." % (element, listname))
    try:
        l = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(l)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


add_to_list_in_dict(dict, "listname10", 10)

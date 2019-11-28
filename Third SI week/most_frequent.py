def most_frequent(mylist):
    '''
    Check what is the most frequent number in an array. If there are multiple such numbers, 
    return the largest one. 

    >>> most_frequent([3, 3, 3, 2, 2, 2, 4, 4])
    3
    >>> most_frequent([3, 3, 3, 2, 2, 2, 2, 4, 4])
    2
    >>> most_frequent([3, 3, 3, 2, 2, 2, 2, 4, 4, 4, 4])
    4
    >>> most_frequent([3, 3, 3, 3, 2, 2, 2, 2, 4, 4, 4, 4])
    4
    '''
    count_values = []
    sorted_list = []
    for l in mylist:
        count_values.append((l, mylist.count(l)))

    sorted_list = sorted(list(set(count_values)),
                         key=lambda t: t[1], reverse=True)

    if sorted_list[0][1] == sorted_list[1][1]:
        if sorted_list[0][0] >= sorted_list[1][1]:
            return sorted_list[0][0]
        else:
            return sorted_list[1][0]
    else:
        return sorted_list[0][0]


# print(most_frequent([3, 3, 3, 2, 2, 2, 2, 4, 4, 4, 4]))

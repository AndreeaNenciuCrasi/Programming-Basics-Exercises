# Given a set of numbers, return the additive inverse of each.Each positive becomes negatives, and the negatives
# become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.


def invert(lst):
    invert_list = []
    if lst == []:
        return lst
    else:
        for number in lst:
            number = str(number)
            if '-' in number:
                nr_list = []
                final_list = []
                nr_list = list(number)
                nr_list.pop(0)
                final_list = ''.join(nr_list)
                invert_list.append(int(final_list))
            else:
                invert_list.append(int('-' + number))
        return invert_list

    print(invert([100, -200, 376, -4, 5]))


# def invert(lst):
#     return [-x for x in lst]


# def invert(lst):
#     return list(map(lambda x: -x, lst))

# def invert(lst):
#     i = 0
#     inv = []
#     while i < len(lst):
#         inv.append(lst[i] * -1)
#         i += 1
#     return inv

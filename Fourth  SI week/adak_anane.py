# The Arara are an isolated tribe found in the Amazon who count in pairs. For example one to eight is as follows:

# 1 = anane
# 2 = adak
# 3 = adak anane
# 4 = adak adak
# 5 = adak adak anane
# 6 = adak adak adak
# 7 = adak adak adak anane
# 8 = adak adak adak adak

# Take a given number and return the Arara's equivalent.

# e.g.

# count_arara(3) # -> 'adak anane'

# count_arara(8) # -> 'adak adak adak adak'


def count_arara(n):
    count1 = 'anane'
    count2 = 'adak'
    count = ''
    if n == 1:
        return 'anane'
    elif n == 2:
        return 'adak'
    else:
        if n % 2 == 0:
            div = n // 2
            count = (div-1) * (count2 + ' ') + count2
        else:
            div = n // 2
            count = (div-1) * (count2 + ' ') + count2 + ' ' + count1

    return count

# def count_arara(n):
#     return " ".join(['adak']*(n//2) + ['anane']*(n%2))

# def count_arara(n):
#     adak = n / 2
#     anane = n % 2
#     return (adak * "adak " + anane * "anane").rstrip()


# from itertools import chain, repeat
# def count_arara(n):
#     twos = repeat('adak', n / 2)
#     one = repeat('anane', n % 2)
#     return ' '.join(chain(twos, one))

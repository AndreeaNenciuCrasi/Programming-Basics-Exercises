def cyclic_rotation(string, n):
    '''
    Calculate a cyclic rotation of a string,move the last N elements from the end to the beginning. 

    >>> cyclic_rotation('abcde', 2)
    'deabc'

    >>> cyclic_rotation('abcdeabcdeeeeee', 6)
    'eeeeeeabcdeabcd'
    '''
    n_string = []
    n_string.extend([string[-n:], string[:-n]])
    print("'" + ''.join(n_string) + "'")


cyclic_rotation('abcde', 2)

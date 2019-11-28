def word_lengths(sentence):
    '''
    Returns a list with lengths of all words in a sentence.

    >>> word_lengths('Hello world')
    [5, 5]
    >>> word_lengths('Once upon a midnight dreary')
    [4, 4, 1, 8, 6]
    '''

    words = sentence.split()
    return [(len(word)+1) for word in words]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

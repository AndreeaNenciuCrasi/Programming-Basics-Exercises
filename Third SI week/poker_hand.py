def poker_hand(string):
    '''
    Function that will score a poker hand. The function will take an array 5 numbers and return a string based 
    on what is inside.

    >>> poker_hand('11111')
    five
    >>> poker_hand('22223')
    four
    >>> poker_hand('11123')
    three
    >>> poker_hand('22334')
    twopairs
    >>> poker_hand('12234')
    pair
    >>> poker_hand('11222')
    fullhouse
    >>> poker_hand('12346')
    nothing
    '''
    hand = list(string)
    if len(string) == 5:
        if hand.count('1') == 5 and set(hand) & set(['1', '1', '1', '1', '1']) == {'1'}:
            print('five')
        if hand.count('2') == 4 and set(hand) & set(['2', '2', '2', '2', '3']) == {'2', '3'}:
            print('four')
        if hand.count('1') == 3 and set(hand) & set(['1', '1', '1', '2', '3']) == {'1', '2', '3'}:
            print('three')
        if hand.count('2') == 2 and hand.count('3') == 2 and set(hand) & set(['2', '2', '3', '3', '4']) == {'2', '3', '4'}:
            print('twopairs')
        if hand.count('2') == 2 and set(hand) & set(['1', '2', '2', '3', '4']) == {'1', '2', '3', '4'}:
            print('pair')
        if hand.count('1') == 2 and hand.count('2') == 3 and set(hand) & set(['1', '1', '2', '2', '2']) == {'1', '2'}:
            print('fullhouse')
        if set(hand) & set(['1', '2', '3', '4', '6']) == {'1', '2', '3', '4', '6'}:
            print('nothing')
    else:
        print('Not a valid string.')


# poker_hand('11111')
# poker_hand('22223')
# poker_hand('11123')
# poker_hand('22334')
# poker_hand('12234')
# poker_hand('11222')
# poker_hand('12346')

# Mount the Bowling Pins!
# Task:
# Did you ever play Bowling? Short: You have to throw a bowl into 10 Pins arranged like this:


# I I I I  # each Pin has a Number:    7 8 9 10
#  I I I                                4 5 6
#   I I                                  2 3
#    I                                    1

# You will get an Array with Numbers, e.g.: [3,5,9] and remove them from the field like this:


# I I   I
#  I   I
#   I
#    I

# Return a string with the current field.

# Note that:
# String.prototype.replace() is not allowed!

# You begin a new line with \n
# Each Line must be 7 chars long
# Fill the missing pins with a whitespace


def bowling_pins(arr):
    matrix = ['7', ' ', '8', ' ', '9', ' ', '10', ' ', '4', ' ', '5', ' ', '6',
              ' ', ' ', ' ', '2', ' ', '3', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ']
    i = 0
    while i < len(matrix):
        for nr in arr:
            if matrix[i] == str(nr):
                matrix[i] = ' '
        i += 1
    print(matrix)
    j = 0
    while j < len(matrix):
        if matrix[j] != ' ':
            matrix[j] = 'I'
        j += 1
    print(matrix)
    string_1 = ''
    string_2 = ''
    string_3 = ''
    string_4 = ''
    for a in range(7):
        string_1 += matrix[a]
    for b in range(7, 14):
        string_2 += matrix[b]
    for c in range(14, 21):
        string_3 += matrix[c]
    for d in range(21, 28):
        string_4 += matrix[d]

    return string_1 + '\n' + string_2 + '\n' + string_3 + '\n' + string_4


print(bowling_pins([2, 3, 4, 5]))

# pins = "{7} {8} {9} {10}\n" + \
#         " {4} {5} {6} \n" + \
#          "  {2} {3}  \n" + \
#           "   {1}   "

# def bowling_pins(arr):
#     return pins.format(*(" " if i in arr else "I" for i in range(11)))

# def bowling_pins(arr):
#     pins = [7,8,9,10,4,5,6,2,3,1]
#     pins_after= []
#     for pin in pins:
#         if pin in arr:
#             pins_after.append(' ')
#         else:
#             pins_after.append('I')


#     return '{} {} {} {}\n {} {} {} \n  {} {}  \n   {}   '.format(*pins_after)

# def bowling_pins(empty):
#   raw =     ['I ', 'I ', 'I ', 'I\n', ' I', ' I ', 'I \n', '  I ', 'I  \n', '   I   ']
#   replace = ['  ', '  ', '  ', ' \n', '  ', '   ', '  \n', '    ', '   \n', '       ']
#   order = [7, 8, 9, 10, 4, 5, 6, 2, 3, 1]

#   return ''.join([replace[x] if order[x] in empty else raw[x] for x in xrange(10)])


# def bowling_pins(arr):

#     dict = {1:"I", 2:"I", 3:"I", 4:"I", 5:"I", 6:"I", 7:"I", 8:"I", 9:"I", 10:"I"}
#     for number in arr:
#         dict[number] = " "

#     bowling_pin_str = "{} {} {} {}\n {} {} {} \n  {} {}  \n   {}   ".format(dict[7], dict[8], dict[9], dict[10], dict[4], dict[5], dict[6], dict[2], dict[3], dict[1])
#     return bowling_pin_str

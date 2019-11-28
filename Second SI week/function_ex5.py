import math
# Rewrite the calculator function from exercise 4 so that it takes any number of number parameters as well as the same
# optional keyword parameters.The function should apply the operation to the first two numbers, and then apply it again
# to the result and the next number, and so on.For example, if the numbers are 6, 4, 9 and 1 and the operation is
# subtraction the function should return 6 - 4 - 9 - 1. If only one number is entered, it should be returned unmodified.
# If no numbers are entered, raise an exception.

ADD, SUB, MUL, DIV = range(4)


def calculator(operation=ADD, output_format=float, *args):
    if not args:
        raise ValueError('No number was entered.')

    result = args[0]

    for n in args[1:]:
        if operation == ADD:
            result += n
        elif operation == SUB:
            result -= n
        elif operation == MUL:
            result *= n
        elif operation == DIV:
            result /= n
        else:
            raise ValueError('False operation')

    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = math.round(result)
    else:
        raise ValueError('Type must be float or int')
    return result


print(calculator(SUB, float, 6, 4, 9, 1))

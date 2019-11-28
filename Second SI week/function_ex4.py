import math
# Write a function called calculator. It should take the following parameters: two numbers, an arithmetic operation
# (which can be addition, subtraction, multiplication or division and is addition by default), and an output format
# (which can be integer or floating point, and is floating point by default). Division should be floating-point division.

# The function should perform the requested operation on the two input numbers, and return a result in the requested
# format (if the format is integer, the result should be rounded and not just truncated). Raise exceptions as appropriate
# if any of the parameters passed to the function are invalid.

# Call the function with the following sets of parameters, and check that the answer is what you expect:

# 2, 3.0
# 2, 3.0, output format is integer
# 2, 3.0, operation is division
# 2, 3.0, operation is division, output format is integer

ADD, SUB, MUL, DIV = range(4)


def calculator(a, b, operation=ADD, output_format=float):
    if operation == ADD:
        result = a + b
    elif operation == SUB:
        result = a - b
    elif operation == MUL:
        result = a * b
    elif operation == DIV:
        result = a / b
    else:
        raise ValueError('False operation')

    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = math.round(result)
    else:
        raise ValueError('Type must be float or int')
    return result


print(calculator(2, 3.0))
print(calculator(2, 3.0, DIV))

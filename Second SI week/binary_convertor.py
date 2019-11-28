def decimal_to_binary(n):
    if(n > 1):
        decimalToBinary(n//2)
    print(str(n % 2) + ' ')


def binary_to_decimal(n):
    decimal = 0
    i = 0
    while n != 0:
        a = n % 10
        decimal = decimal + a * (2 ** i)
        n = n // 10
        i += 1
    print(decimal)


def binary_decimal_convertor(number, system):
    if system == 2:
        decimalToBinary(number)
    elif system == 10:
        binary_to_decimal(number)


binary_decimal_convertor(101000, 10)



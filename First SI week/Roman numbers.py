# Write a program which takes a natural number (written in Arabic numerals, greater than zero and # less than 4000), and then prints it in Roman form. For example, after input 94 your program 
# should print XCIV or xciv, and after input 611, your program should print DCXI or dcxi.


def int_to_roman(input):
    if 0 < input < 4000:
        ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        result = []
        for i in range(len(ints)):
            count = int(input / ints[i])
            result.append(nums[i] * count)
            input -= ints[i] * count
    return ''.join(result)

print(int_to_roman(2050))
print(int_to_roman(3150))

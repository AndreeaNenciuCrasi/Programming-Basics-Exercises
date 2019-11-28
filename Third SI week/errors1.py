import math


def myfunction(x, y):
    return x + y


print("Hello!")

mark = 4
arriving = True
flag = True
if mark >= 50:
    print("You passed!")

if arriving:
    print("Hi!")
else:
    print("Bye!")

if flag:
    print("Flag is set!")

# dividend = float(input("Please enter the dividend: "))
# divisor = float(input("Please enter the divisor: "))
# quotient = dividend / divisor
# quotient_rounded = math.round(quotient)

product = 1
for i in range(1, 10):
    product *= i
print(product)

sum_squares = 0
for i in range(10):
    i_sq = i**2
    sum_squares += i_sq
print(sum_squares)

nums = 0
for num in range(10):
    nums += num
print(nums)

n = None
while n is None:
    try:
        s = input("Please enter an integer: ")
        n = int(s)
    except ValueError:
        print("%s is not an integer." % s)

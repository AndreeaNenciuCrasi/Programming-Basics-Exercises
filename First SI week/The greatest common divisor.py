# Write a program which takes two numbers from a command line and prints the greatest common 
# divisor of them.

x = int(input("First number: "))
y = int(input("Second number: "))

def gcd(a, b):

    t = min(a, b)

    while a % t != 0 or b % t != 0:
        t -= 1

    return t

print(gcd(x,y))

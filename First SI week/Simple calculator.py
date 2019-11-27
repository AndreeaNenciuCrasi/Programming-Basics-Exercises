# Write a calculator script that waits for the user to enter a number, then a sign (plus, minus, 
# multiplication and division), then a number again. After the 2nd number input, the script should # calculate the addition or subtraction and print it out. Then the program should run again with 
# asking for the first number.

nr1 = input('Enter a number (or a letter to exit): ')

if nr1.isalpha():
    print('Exit')
else:
    operation = input('Enter an operation (+,-,*,/): ')
    nr2 = int(input('Enter another number: '))
    result = 0
    if operation == '+':
        result = int(nr1) + nr2
    if operation == '-':
        result = int(nr1) - nr2
    if operation == '*':
        result = int(nr1) * nr2
    if operation == '/':
        result = int(nr1) / nr2
    print('Result: ', result)

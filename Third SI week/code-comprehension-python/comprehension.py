import random  # import random module

'''
    Guess in maximum 6 attempts a number from 1 to 20
'''

guesses_taken = 0  # assign 0 to guesses_taken variable

print('Hello! What is your name?')  # print message
myName = input()  # assign the user input to myName variable

# generate a number between 1 and 20 and assign the value to number variable
number = random.randint(1, 20)

# print message, concatenate strings with user input
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guesses_taken < 6:  # as long as the value of guesses_taken is less than 6
    print('Take a guess.')  # ask for user input
    guess = input()  # assign the user input to guess variable
    guess = int(guess)  # change guess value from str to int

    guesses_taken += 1  # add 1 to guesses_taken value

    if guess < number:  # if the value of guess is less than the value of number
        print('Your guess is too low.')  # print message

    if guess > number:  # if the value of guess is greater than the value of number
        print('Your guess is too high.')  # print message

    if guess == number:  # if the value of guess is equal than the value of number
        break  # stop the while loop

if guess == number:  # if the value of guess is equal than the value of number
    # change guesses_taken value from int to str
    guesses_taken = str(guesses_taken)
    print('Good job, ' + myName + '! You guessed my number in ' +
          guesses_taken + ' guesses!')  # print message, concatenate strings with variables

if guess != number:  # if the value of guess is different from value of number
    number = str(number)  # change number value from int to str
    # print message, concatenate strings with variables
    print('Nope. The number I was thinking of was ' + number)

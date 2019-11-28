import random


def get_user_input(min_number, max_number):
    guess = int(input("Enter an integer from " +
                      str(min_number) + " to " + str(max_number) + " : "))
    while guess not in range(min_number, max_number + 1):
        guess = int(input("Enter an integer from " +
                          str(min_number) + " to " + str(max_number) + " : "))
    return guess


def guess_number(count, min_number, max_number):
    list_of_random_numbers = []
    for i in range(count):
        list_of_random_numbers.append(
            random.randint(min_number, max_number))

    for number in list_of_random_numbers:
        guess = 0
        while number != guess:
            guess = get_user_input(min_number, max_number)
            if guess < number:
                print("guess is low")
            elif guess > number:
                print("guess is high")
        print("you guessed it!")


def main():
    first_play = guess_number(10, 1, 99)
    print(first_play)
    second_play = guess_number(10, 1, 49)
    print(second_play)


if __name__ == '__main__':
    main()

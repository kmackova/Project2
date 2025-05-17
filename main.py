import random

def test_guess(input_string: str) -> bool:
    """
    Test if the user input (guess number) meets the given requirements.
    """
    guess_ok = True
    if input_string:
        if input_string[0] == "0":
            print ("The first digit can't be 0.")
            guess_ok = False
        if input_string.isnumeric() == False:
            print("The number should include just numeric characters.")
            guess_ok = False
        if len(input_string) != 4:
            print("The number should have 4 digits.")
            guess_ok = False
        if len(set(input_string)) != len(input_string):
            print("There should be no duplicite digits in the number.")
            guess_ok = False
    else:
        guess_ok = False
    return guess_ok

def get_guess() -> tuple:
    """
    Ask for user input (guess number) until it is correct (i.e. test_guess function returns True).
    Return tuple including integers (digits of the guess number).
    """
    guess_input = ""
    while test_guess(guess_input) == False:
        guess_input = input()
    return tuple(int(digit) for digit in guess_input)

def count_bulls(secret_tuple: tuple, guess_tuple: tuple) -> int:
    """
    Count bulls, i.e. the user guessed both the correct digit and its correct position.
    """
    bulls_counter = 0
    for digit_secret, digit_guess in zip(secret_tuple, guess_tuple):
        if digit_secret == digit_guess:
            bulls_counter +=1     
    return bulls_counter

def count_cows(secret_tuple: tuple, guess_tuple: tuple, number_of_bulls: int) -> int:
    """
    Count cows, i.e. the user guessed the correct digit but on a differnt position.
    """
    cows_counter = - number_of_bulls
    for digit_secret in secret_tuple:
        if digit_secret in guess_tuple:
            cows_counter +=1
    return cows_counter

def bulls_msg(bulls_number: int) -> str:
    if bulls_number == 1:
        return "1 bull"
    else:
        return f"{bulls_number} bulls"

def cows_msg(cows_number: int) -> str:
    if cows_number == 1:
        return "1 cow"
    else:
        return f"{cows_number} cows"

def sep_line():
    print("-" * 47)

digit_1 = random.randint(1, 9)
available_digits = list(range(0, 10))
available_digits.remove(digit_1)
digits_2to4 = random.sample(available_digits, k = 3)

secret_number = tuple([digit_1] + digits_2to4)


# to tam nema byt :)
for i in secret_number:
    print(i, end="")
else:
    print()


print("Hi there!")
sep_line()
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
sep_line()
print("Enter a number:")
sep_line()

guess_counter = 0
bulls = 0

while bulls < 4:
    guess = get_guess()
    guess_counter += 1
    bulls = count_bulls(secret_number, guess)
    if bulls < 4:
        cows = count_cows(secret_number, guess, bulls)
        print(f"{bulls_msg(bulls)}, {cows_msg(cows)}")
        sep_line()
else:
    print(f"Correct, you've guessed the right number\nin {guess_counter} guesses!")
    sep_line()
    print("That's amazing!")
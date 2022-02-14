# Guess the secret number the computer has selected

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low!')
        elif guess > random_number:
            print('Sorry, guess again. Too high')

    print(f'Yay, congrats. You have guessed the number {random_number}')

# Row the computer guesses a number you're thinking of

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Wow, the computer guessed your number, {guess}, correctly!')

computer_guess(10)
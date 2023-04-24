import random

def guess(number):
    random_number = random.randrange(1,21,2)
    guess = 0
    while guess != random_number:
        # guess = int(input(f'Guess an odd number between 1 and {number}: '))
        guess = int(input('Guess an odd number between 1 and {}: '.format(number)))
        if guess > random_number:
            print('guess again, number is too high')
        elif guess < random_number:
            print('guess again, number is too low')

    print(f'Great!!! You guessed the number {random_number} right!!!')

guess(20)
"""
The guesser game..Computer thinks of a number and guess it in x options.
use random to make the number
"""

import random
key = 0
print('Hi! What is your name?')
name = input()
number = random.randint(1, 50)
print('Well, ' + name + ', I am thinking of a number between 1 and 50.')
while key < 6:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)
    key = key + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    key = str(key)
    print('Good job, ' + name + '! You guessed my number in ' + key + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
    

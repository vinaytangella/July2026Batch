#Fun project #1
"""
    p1 - Guess a number - hint
    computer - picks a number - hint
    computer checks the number you guessed against the picked number
    matching - congrats! it took you n times to guess correct bumber
    less - you picked a small number
    more - you picked bigger number
    keep track of guesses
"""
import random

picked_number = random.randint(1,10)

success = False
counter = 0

#conditon is true or false not false - true

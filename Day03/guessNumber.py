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

guessed_number = input('please enter a number: ')
print(guessed_number)

picked_number = random.randint(1,10)
while (this condition runs until the picked_number == guessed_number is satisfied, keep track of count incrementing every time)
    if picked_number == guessed_number:
        print("Congratulations! Your number matched with the picked number.")
    elif picked_number < guessed_number:
    
        print("Your picked number is less")
    else:
        print("Your picked number is more")
        
    count= i++

print("your number matched on ")

print(picked_number)
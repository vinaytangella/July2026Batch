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
picked_num = random.randint(1, 20)
count = 0
while True:
    guessed_num = int(input("Enter your guess: "))
    count = count + 1
    if guessed_num == picked_num:
        print(f"Congratulations! Your guess matched on attempt number {count}")
        break
    elif guessed_num < picked_num:
        print("Your number is smaller. Try again!")
    else:
        print("Your number is larger. Try again!")
import random

number = random.randint(1, 10)

count = 0

while True:
    guess = int(input("Enter a number: "))
    count = count + 1

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("You won")
        print("Attempts:", count)
        break
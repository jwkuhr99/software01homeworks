import random

def guess_the_number():
    number_to_guess = random.randint(1,10)
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        user_guess = int(input("Your guess: "))
        if user_guess <1 or user_guess > 10:
            print("\nPlease enter a number between 1 and 10.")
            continue
        if user_guess < number_to_guess:
            print("\nHigher!")
        elif user_guess > number_to_guess:
            print("\nLower!")
        else:
            print("\nCorrect! That was the number. :))")
            break

guess_the_number()
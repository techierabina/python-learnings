import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    tries = 0
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            tries += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {tries} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()

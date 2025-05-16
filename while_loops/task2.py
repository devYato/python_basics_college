import numpy as np

random_numbers = np.random.randint(1, 10) 
find = False
number_of_guesses = 0
print("Welcome to the number guessing game!")
while not find:
    user_guess = int(input("Guess the number (1-10): "))
    number_of_guesses += 1
    if user_guess == random_numbers:
        print("Congratulations! You found the number.")
        find = True
    else:
        print("Try again.")

print(f"You found the number in {number_of_guesses} guesses.")

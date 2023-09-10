# Number Guessing Game where the system generates a random number for a user
# Import random 
import random

while True:
    print("Welcome to the number guessing game.")
    print("To begin, please input a range (1-100):")
    lower_range = int(input("Please select the lower bound of your range: "))
    upper_range = int(input("Please select the upper bound of your range: "))

    generated_number = random.randint(lower_range, upper_range)
    print(f"The system has generated a number. The number is {generated_number}")
    
    attempts = 0
    
    while True:
        user_guess = int(input("Please input your guess: "))
        attempts += 1

        if user_guess != generated_number:
            print("You guessed incorrectly. Try again!")
            if user_guess < generated_number:
                print("You guessed lower than the generated number.")
            elif user_guess > generated_number:
                print("You guessed higher than the generated number.")
        else:
            print(f"You guessed correctly in {attempts} attempts!")
            break

    play_again = input("Would you like to play again? (Yes/No): ")
    if play_again.lower() != 'yes':
        print("Thank you for playing!")
        break           
        
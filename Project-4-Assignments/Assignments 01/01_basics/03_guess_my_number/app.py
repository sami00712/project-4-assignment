import random

def main():
    secret_number = random.randint(0, 99)
    user_guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

    while user_guess != secret_number:
        if user_guess > secret_number:
            print("Your guess is too high")
        elif user_guess < secret_number:
            print("Your guess is too low")
        
        # Move this line INSIDE the loop so the user can guess again
        user_guess = int(input("Enter a new number: "))

    # If the loop exits, that means the guess is correct
    print("Congrats!!! The number was:", secret_number)

if __name__ == "__main__":
    main()

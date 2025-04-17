import random

def guess(x):
    random_number = random.randint(1, x)
    guess =0
    while guess != random_number:
        user_input = input(f" Guess a number between 1 and {x}:")

        if user_input.strip() == "":
            print("⚠️  Input cannot be empty! Please enter a number.")
            continue
        if not user_input.isdigit():
            print("⚠️   Invalid input! Please enter a valid number.")
            continue

        guess = int(user_input)

        if guess < random_number:
            print('❌ Too low. Try again.')

        elif guess > random_number:
            print('❌ Too high. Try again.')

    print(f"🎉 Yay, congrats! You guessed the number {random_number} correctly!")

guess(10)

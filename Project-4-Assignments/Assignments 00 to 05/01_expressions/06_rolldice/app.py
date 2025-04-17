import random

num_sides = 6

def main():
    # roll the dice
    die1 : int = random.randint(1, num_sides)
    die2 : int = random.randint(1, num_sides)

    Total :int = die1 + die2
    print(f"🎲 Dice have {num_sides} sides.")
    print(f"🎲 First die: {die1}")
    print(f"🎲 Second die: {die2}")
    print(f"🎲 Total of two dice: {Total}")

if __name__ == "__main__":
    main()
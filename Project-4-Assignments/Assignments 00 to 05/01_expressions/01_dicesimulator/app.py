import random

die_sides = 6

def roll_dice():
    """
    Roll a die and return the result
    """
    die1 : int = random.randint(1, die_sides)
    die2 : int  = random.randint(1, die_sides)
    total: int = die1 + die2
    print("Total Of Two Dice:", total)

def main():
    die1 : int = 20
    print("die1 in main() starts as:" + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print ("die1 in main() is :" + str(die1) )

if __name__ == "__main__":
    main()
    


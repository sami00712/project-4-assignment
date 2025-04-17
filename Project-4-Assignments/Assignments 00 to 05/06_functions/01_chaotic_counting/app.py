import random  # Import random module

DONE_LIKELIHOOD = 0.3  # 30% chance of stopping at each step

def chaotic_counting():
    for i in range(10):  # Loop runs up to 10 times
        curr_num = i + 1  # Convert 0-based index to 1-based counting
        if done():  # Check if counting should stop
            return  # Exit function early if done() returns True
        print(curr_num)  # Print the current number

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:  # Generate a random number and compare
        return True  # Stop counting
    return False  # Continue counting

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Start the chaotic counting
    print("I'm done")  # Print message after counting stops

if __name__ == "__main__":
    main()

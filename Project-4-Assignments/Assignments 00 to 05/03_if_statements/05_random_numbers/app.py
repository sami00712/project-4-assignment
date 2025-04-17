import random  # Import the random library

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    for _ in range(N_NUMBERS):  # Loop 10 times
        num = random.randint(MIN_VALUE, MAX_VALUE)  # Generate a random number between 1 and 100
        print(num, end=" ")  # Print the number on the same line with a space
    
    print()  # Move to a new line after printing all numbers

if __name__ == '__main__':
    main()

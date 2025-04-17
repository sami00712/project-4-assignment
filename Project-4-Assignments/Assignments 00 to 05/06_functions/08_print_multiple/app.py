def print_multiple(message: str, repeats: int):
    """
    Prints the given message the specified number of times.
    """
    for _ in range(repeats):  
        # Loop repeats times
        print(message, end=" ")  


def main():
    message = input("Please type a message: ")  # Get message from user
    repeats = int(input("Enter a number of times to repeat your message: "))  # Get repeat count
    print_multiple(message, repeats)  # Call function

if __name__ == '__main__':
    main()

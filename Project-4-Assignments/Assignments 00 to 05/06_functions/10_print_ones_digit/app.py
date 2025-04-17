def print_ones_digit(num: int):
    """
    Prints the ones digit of the given number.
    """
    ones_digit = num % 10  # Get the remainder when divided by 10
    print("The ones digit is", ones_digit)


def main():
    num = int(input("Enter a number: "))  # Get user input and convert to integer
    print_ones_digit(num)  # Call the function to print the ones digit

if __name__ == '__main__':
    main()

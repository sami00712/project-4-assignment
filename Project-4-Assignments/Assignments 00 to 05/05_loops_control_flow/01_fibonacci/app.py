MAX_TERM_VALUE: int = 10000  # Maximum limit for Fibonacci numbers

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)  # Print the current Fibonacci term
        term_after_next = curr_term + next_term  # Compute next term
        curr_term = next_term  # Move to next term
        next_term = term_after_next  # Update next term

if __name__ == '__main__':
    main()  # Run the program

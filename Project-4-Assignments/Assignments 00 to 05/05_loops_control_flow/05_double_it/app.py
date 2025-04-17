def main():
    # Step 1: Ask for user input
    curr_value = int(input("Enter a number: "))

    # Step 2: Double the value until it reaches 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the number
        print(curr_value, end=" ")  # Print on the same line
    
# Step 3: Run the main function
if __name__ == "__main__":
    main()

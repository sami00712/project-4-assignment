def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:  # Check if the number is even
            count += 1  # Increment count

    return count  # ✅ Return instead of print

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Create an empty list to store integers
    user_input = input("Enter an integer or press enter to stop: ")  
    while user_input != "":  # Keep reading until user presses enter
        lst.append(int(user_input))  # Convert input to int and add to list
        user_input = input("Enter an integer or press enter to stop: ")  

    return lst  # Return the final list

def main():
    lst = get_list_of_ints()
    even_count = count_even(lst)  # Call count_even() and store the result
    print(f"Number of even numbers: {even_count}")  # ✅ Print here

if __name__ == '__main__':
    main()

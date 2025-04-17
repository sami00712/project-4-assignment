def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])  # Prints the first element of the list

def get_last_element(lst):
    """
    Prints the last element of a provided list.
    """
    print(lst[-1])  # Prints the last element of the list using negative indexing

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)  # Adds the entered element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst  # Returns the final list

def main():
    lst = get_lst()  # Get user input for the list
    get_first_element(lst)  # Print the first element of the list
    get_last_element(lst)  # Print the last element of the list

if __name__ == '__main__':
    main()

import math

def main():
    # get input from user
    ab : float = float(input("Enter the length of side AB: "))
    ac : float = float(input("Enter the length of side AC: "))

    bc : float = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: ", str(bc))

if __name__ == "__main__":  
    main()




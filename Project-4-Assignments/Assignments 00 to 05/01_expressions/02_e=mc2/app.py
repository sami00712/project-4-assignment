c : int = 299792458 

def main():
    mass_in_kgs: float = float(input("Enter the value of mass in kgs :\t"))
    # now apply the formula
    energy = mass_in_kgs * c** 2

    print("E = m*c**2....")
    print("m =" + str(mass_in_kgs)  + "kg")
    print("C = " + str(c) + "m/s")

    print(str(energy) + " joules of energy!  ")

if __name__ == "__main__":
    main()
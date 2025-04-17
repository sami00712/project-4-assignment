# planet_names = {
#     "Mercury": 0.376,
#     "Venus": 0.889,
#     "Mars": 0.378,
#     "Jupiter": 2.36,
#     "Saturn": 1.081,
#     "Uranus": 0.815,
#     "Neptune": 1.14
# }

# def main():
#     earth_weight = float(input("enter a  weight :"))
#     planet_name = input("enter a planet :")

#     planet_weight = earth_weight * planet_names[planet_name]

#     print("your weight in {planet_name} is " + str( planet_weight))

# if __name__ == '__main__':
#     main()


    # or


def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ").strip().lower()

    if planet == "mercury":
        planet_weight = earth_weight * 0.376
    elif planet == "venus":
        planet_weight = earth_weight * 0.889
    elif planet == "mars":
        planet_weight = earth_weight * 0.378
    elif planet == "jupiter":
        planet_weight = earth_weight * 2.36
    elif planet == "saturn":
        planet_weight = earth_weight * 1.081
    elif planet == "uranus":
        planet_weight = earth_weight * 0.815
    elif planet == "neptune":
        planet_weight = earth_weight * 1.14
    else:
        print("Invalid planet name.")
        return

    print(f"The equivalent weight on {planet.capitalize()}: {round(planet_weight, 2)}")

# Run the program only when executed directly
if __name__ == "__main__":
    main()

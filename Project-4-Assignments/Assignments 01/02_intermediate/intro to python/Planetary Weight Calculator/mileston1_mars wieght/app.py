MARS_MULTIPLE = 0.378

def main():
    earth_weight = float(input(" Enter a Enter a weight on Earth:"))

    mars_weight = earth_weight * MARS_MULTIPLE

    round_mars_weight = round(mars_weight, 2)

    print(" the equivalent weight on Mars : " + str(round_mars_weight))


if __name__ == "__main__":
    main()

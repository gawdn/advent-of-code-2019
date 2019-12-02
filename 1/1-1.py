def calculate_fuel_required(mass):
    """
    Calculates the fuel required for a module given it's mass
    """
    return (mass//3) - 2


if __name__ == "__main__":
    with open("../1.in", "r") as masses:
        total_fuel = 0
        for mass in masses:
            total_fuel += calculate_fuel_required(int(mass))

    print(total_fuel)

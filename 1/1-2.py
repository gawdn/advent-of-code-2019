def calculate_fuel_required(mass):
    """
    Calculates the fuel required for a module given it's mass
    """
    return (mass//3) - 2


if __name__ == "__main__":
    with open("1.in", "r") as masses:
        total_fuel = 0
        for mass in masses:
            # Fuel for an individual module
            module_fuel = 0
            fuel_required = int(mass)

            # Account for the weight of the fuel
            while fuel_required > 0:
                fuel_required = calculate_fuel_required(fuel_required)

                # don't add negative amounts
                if fuel_required > 0:
                    module_fuel += fuel_required

            total_fuel += module_fuel

    print(total_fuel)

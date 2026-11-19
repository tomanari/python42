#!/usr/bin/env python3
class PlantError(Exception):
    def __init__(self, plant_name):
        super().__init__(f"Invalid plant name to water: '{plant_name}'")


def water_plant(name):
    if name != name.capitalize():
        raise PlantError(name)
    print(f"Watering {name}: [OK]")


def test_valid_watering_system(plants):
    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant.capitalize())
    finally:
        print("Closing watering system")


def test_invalid_watering_system(plants):
    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as p:
        print(f"Caught PlantError: {p}")
        print("... ending tests and returning to main")
    finally:
        print("Closing watering system")


def main():
    print("=== Garden Watering System ===\n")
    i = 0
    plants = []
    while True:
        plant = str(input(f"Enter plant {i + 1} or type")
                    ("exit to leave program: "))
        if plant.lower() == "exit":
            break
        plants.append(plant)
        i += 1
    test_valid_watering_system(plants)
    test_invalid_watering_system(plants)


if __name__ == "__main__":
    main()

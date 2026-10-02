#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message="A general error ocurred"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def check_health(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")

def check_water(w_level: int) -> None:
    if w_level <= 0:
        raise WaterError("Not enough water in the tank")

def test_cheker() -> None:
    print("Testing PlantError...")
    try:
        check_health(is_wilting=True)
    except PlantError as p:
        print(f"Caught PlantError: {p}\n")
    print("Testing WaterError...")
    try:
        check_water(w_level=0)
    except WaterError as w:
        print(f"Caught PlantError: {w}\n")
    print("Testing catching all garden errors...")
    g_errors = [PlantError("The tomato plant is wilting!"),
                WaterError("Not enough water in the tank")]
    for g in g_errors:
        try:
            raise g
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custon Garden Errors Demo ===")
    test_cheker()

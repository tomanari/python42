#!/usr/bin/env python3
def ft_garden_intro(plant: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant.capitalize()}\nHeight: {height}cm\nAge: "
          "{age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("rose", 15, 21)

#!/usr/bin/env python3

def ft_garden_intro(name: str, height: int, age: int):
    print("=== Welcome to My Garden")
    print(f"Plant: {name.capitalize()}\nHeight: {height} cm\nAge: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("Rose", 34, 26)
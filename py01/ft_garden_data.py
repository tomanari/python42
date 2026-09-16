#!/usr/bin/env python3
class Plant:
    def __init__(self, plant, height, age):
        self.plant = plant
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.plant.capitalize()}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Plant("rose", 15, 21).show()
    Plant("cactus", 45, 61).show()
    Plant("sunflower", 58, 33).show()

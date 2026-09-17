#!/usr/bin/env python3
class Plant:
    def __init__(self, plant, height, age_day, grow_rate):
        self.plant = plant
        self.height = height
        self.age_day = age_day
        self.grow_rate = grow_rate

    def grow(self):
        self.height += self.grow_rate
        return self

    def age(self):
        self.age_day += 1
        return self

    def show(self):
        print(f"{self.plant.capitalize()}: {self.height}cm, "
              f"{self.age_day} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("rose", 25, 30, 0.7)
    oak = Plant("oak", 200, 365, 0.8)
    cactus = Plant("cactus", 5, 90, 0.05)
    sunflower = Plant("sunflower", 80, 45, 2)
    fern = Plant("fern", 15, 120, 0.2)
    plants = [rose, oak, cactus, sunflower, fern]
    for i in range(0, 5):
        print("Created: ", end="")
        plants[i].show()

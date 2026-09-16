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
        print(f"{self.plant.capitalize()}: {self.height}cm, {self.age_day} days old")
    
    
if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose =  Plant("rose", 15, 21, 0.5)
    rose.show()
    total_g = 0
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow().age().show()
        total_g += rose.grow_rate
    print(f"Growth this week: {total_g}cm")

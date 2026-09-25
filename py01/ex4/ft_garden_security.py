#!/usr/bin/env python3
class Plant:
    def __init__(self, plant, height, age_day, grow_rate):
        if height < 0:
            print(f"{plant.capitalize()}: Error, height can't be negative")
            height = 0
        if age_day < 0:
            print(f"{plant.capitalize()}: Error, age can't be negative")
            age_day = 0

        self.plant = plant
        self._height = height
        self._age_day = age_day
        self._grow_rate = grow_rate

    def grow(self):
        self._height += self._grow_rate
        return self

    def age(self):
        self._age_day += 1
        return self

    def show(self):
        print(f"{self.plant.capitalize()}: {self._height}cm, "
              f"{self._age_day} days old\n")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age_day

    def set_height(self, height):
        if height < 0:
            print(f"{self.plant.capitalize()}: Error, height can't be "
                  f"negative\nHeight update rejected")
            print(f"\nCurrent state: {self.plant.capitalize()}: "
                  f"{self.get_height()}cm, {self.get_age()} days old")
        else:
            self._height = height
            print(f"Height updated: {self.get_height()}cm")

    def set_age(self, age_day):
        if age_day < 0:
            print(f"{self.plant.capitalize()}: Error, age can't be "
                  f"negative\nAge update rejected")
            print(f"\nCurrent state: {self.plant.capitalize()}: "
                  f"{self.get_height()}cm, {self.get_age()} days old")
        else:
            self._age_day = age_day
            print(f"Age updated: {self.get_age()} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 15, 30, 0.7)
    oak = Plant("oak", 200, 365, 0.8)
    cactus = Plant("cactus", 5, 90, 0.05)
    sunflower = Plant("sunflower", 80, 45, 2)
    fern = Plant("fern", 15, 120, 0.2)
    plants = [rose]
    for i in range(0, len(plants)):
        print("Plant created: ", end="")
        plants[i].show()
    rose.set_height(25)
    rose.set_age(-2)

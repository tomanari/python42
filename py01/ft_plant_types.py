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
        print(f"{self.plant.capitalize()}: {round(self._height)}cm, "
              f"{self._age_day} days old")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age_day

    def set_height(self, height):
        if height < 0:
            print(f"{self.plant.capitalize()}: Error, height can't be "
                  "negative\nHeight update rejected")
            print(f"\nCurrent state: {self.plant.capitalize()}: "
                  f"{self.get_height()}cm, {self.get_age()} days old")
        else:
            self._height = height
            print(f"Height updated: {self.get_height()}cm")

    def set_age(self, age_day):
        if age_day < 0:
            print(f"{self.plant.capitalize()}: Error, age can't be "
                  "negative\nAge update rejected")
            print(f"\nCurrent state: {self.plant.capitalize()}: "
                  f"{self.get_height()}cm, {self.get_age()} days old\n")
        else:
            self._age_day = age_day
            print(f"Age updated: {self.get_age()} days")

class Flower(Plant):
    def __init__(self, plant, height, age_day, grow_rate, color):
        super().__init__(plant, height, age_day, grow_rate)
        self.color = color
        self.has_bloomed = False

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed == False:
            print(f"{self.plant.capitalize()} has not bloomed yet\n")
        else:
            print(f"{self.plant.capitalize()} is blooming beautifully!\n")

    def bloom(self):
        print(f"[asking the {self.plant.capitalize()} to bloom]")
        self.has_bloomed = True

class Tree(Plant):
    def __init__(self, plant, height, age_day, grow_rate, trunk_diameter):
        super().__init__(plant, height, age_day, grow_rate)
        self.trunk_diameter = trunk_diameter
        self.has_shade = False

    def show(self):
        super().show()
        if self.has_shade == True:
            print(f"Tree{self.plant.capitalize()} now produces a shade of "
                  f"{self.trunk_diameter}cm long and {self.trunk_diameter}"
                  "cm wide!\n")

    def produce_shade(self):
        print(f"[asking the {self.plant.capitalize()} to produce shade]")
        self.has_shade = True

class Vegetable(Plant):
    def __init__(self, plant, height, age_day, grow_rate, harvest_season):
        super().__init__(plant, height, age_day, grow_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self):
        super().show()
        print(f"Harvest Season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age_grow(self, days):
        print(f"[make {self.plant.lower()} grow and age for {days} days]")
        for i in range(0, days):
            super().grow()
            super().age()
            self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("rose", 15, 30, 0.7, "red")
    oak = Plant("oak", 200, 365, 0.8)
    cactus = Plant("cactus", 5, 90, 0.05)
    sunflower = Plant("sunflower", 80, 45, 2)
    fern = Vegetable("tomato", 15, 120, 0.2,"April")
    plants = [rose]

    fern.show()
    fern.age_grow(20)
    fern.show()

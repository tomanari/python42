#!/usr/bin/env python3
def show_statistics(plant):
    plant.display_statistics()


class Plant:
    @staticmethod
    def year_old(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown Plant", 0, 0, 0)

    class PlantStats():
        def __init__(self):
            self._grow_ct = 0
            self._age_ct = 0
            self._show_ct = 0

        def display(self):
            print(f"Stats: {self._grow_ct} grow, {self._age_ct} age, "
                  f"{self._show_ct} show")

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
        self._stats = self.PlantStats()

    def grow(self):
        self._height += self._grow_rate
        self._stats._grow_ct += 1
        return self

    def age(self):
        self._age_day += 1
        self._stats._age_ct += 1
        return self

    def show(self):
        print(f"{self.plant.capitalize()}: {round(self._height)}cm, "
              f"{self._age_day} days old")
        self._stats._show_ct += 1

    def display_statistics(self):
        self._stats.display()

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
        if self.has_bloomed is False:
            print(f"{self.plant.capitalize()} has not bloomed yet\n")
        else:
            print(f"{self.plant.capitalize()} is blooming beautifully!")

    def bloom(self):
        print(f"[asking the {self.plant.capitalize()} to bloom]")
        self.has_bloomed = True


class Seed(Flower):
    def __init__(self, plant, height, age_day, grow_rate, color):
        super().__init__(plant, height, age_day, grow_rate, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}\n")


class Tree(Plant):
    def __init__(self, plant, height, age_day, grow_rate, trunk_diameter):
        super().__init__(plant, height, age_day, grow_rate)
        self.trunk_diameter = trunk_diameter
        self.has_shade = False
        self._stats._shade_ct = 0

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        if self.has_shade is True:
            print(f"Tree {self.plant.capitalize()} now produces a shade of "
                  f"{self._height}cm long and {self.trunk_diameter}"
                  "cm wide!\n")

    def produce_shade(self):
        print(f"[asking the {self.plant.capitalize()} to produce shade]")
        self.has_shade = True
        self._stats._shade_ct += 1

    def display_statistics(self):
        super().display_statistics()
        print(f"{self._stats._shade_ct} shade")


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

    rose = Seed("rose", 15, 30, 0.7, "red")
    oak = Tree("oak", 200, 365, 0.8, 60)
    cactus = Plant("cactus", 5, 90, 0.05)
    fern = Vegetable("tomato", 15, 120, 0.2, "April")

    rose.show()
    rose.age()
    rose.bloom()
    rose.grow()
    rose.show()

    oak.show()
    oak.produce_shade()
    oak.show()

    print("\n=== Statistics ===")
    show_statistics(rose)
    show_statistics(cactus)
    show_statistics(fern)
    show_statistics(oak)

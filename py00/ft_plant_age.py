def plant_age():
    age = int(input("Enter plant age: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")


plant_age()
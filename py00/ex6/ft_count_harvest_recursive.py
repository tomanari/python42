def count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_day(day):
        if day > days:
            print("Harvest Day!")
            return

        print(f"Day {day}")
        count_day(day + 1)

    count_day(1)


count_harvest_recursive()

def ft_seed_inventory(seed_type: str, quantity: int, unit: str)-> None:
    unit = unit.lower()
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: {quantity} square meters")
    else:
       print("Unknown unit type")
        
ft_seed_inventory("nada", 4, "sei la")
ft_seed_inventory("Strawberry", 25, "packets")
ft_seed_inventory("Lettuce", 8, "area")   
ft_seed_inventory("carots", 250, "grams")
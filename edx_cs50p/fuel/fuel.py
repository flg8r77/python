def main():
    fuel = get_fraction("Fraction: ")

    print(fuel_left(fuel))

def get_fraction(prompt):
    while True:
        fraction = input(prompt)
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                raise ValueError
            return (x / y)
        except (ValueError, ZeroDivisionError):
            pass

def fuel_left(fuel):
    fuel_left = round(fuel * 100)
    if fuel_left <= 1:
        fuel_left = "E"
    elif fuel_left >= 99:
        fuel_left = "F"
    else:
        fuel_left = f'{fuel_left}%'
    return fuel_left

if __name__ == "__main__":
    main()
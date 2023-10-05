def main():
    user_input = input("Fraction: ")
    pct = convert(user_input)
    print(guage(pct))
    sys.exit(0)

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y and y != 0:
        raise ValueError()
    elif y == 0:
        raise ZeroDivisionError
    else:
        return int(x/y * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f'{percentage}%'

if __name__ == "__main__":
    main()

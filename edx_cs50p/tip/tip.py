def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollars_string):
    rv = dollars_string.split("$")[1]
    return float(rv)

def percent_to_float(percent_string):
    rv = percent_string.split("%")[0]
    return float(rv) / 100

main()
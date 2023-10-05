def main():
    time_input = input("What time is it? ").strip()
    converted_time = (convert(time_input))

    if 7.00 <= converted_time <= 8.00:
        print("breakfast time")
    elif 12.00 <= converted_time <= 13.00:
        print("lunch time")
    elif 18.00 <= converted_time <= 19.00:
        print("dinner time")
    else:
        pass

def convert(time):
    hr, min = time.split(":")
    rv = float(hr) + (float(min) / 60)
    return round(rv, 2)

if __name__ == "__main__":
    main()
def main():

    valid_months = {
        "January": 1,
        "Feburary": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        date_in = input("Date: ")

        if date_in.count("/") == 2:
            d = date_in.split("/")

            try:
                ds = [int(i) for i in d]
            except ValueError:
                continue
            else:
                if 1 <= ds[0] <= 12 and 1 <= ds[1] <= 31 and len(str(ds[2])) == 4:
                    print_date(ds[0], ds[1], ds[2])
                else:
                    continue

        elif date_in.count(" ") == 2:
            d = date_in.split(" ")

            try:
                month = valid_months[d[0]]
            except KeyError:
                continue

            if d[1].endswith(","):
                try:
                    day = int(d[1].rstrip(","))
                except ValueError:
                    continue
            else:
                continue

            if 1 <= day <= 31:
                pass
            else:
                continue

            try:
                year = int(d[2])
            except ValueError:
                continue

            if len(str(year)) == 4:
                pass
            else:
                continue

            print_date(month, day, year)

        else:
            continue

def print_date(m, d, y):
    print(f'{y}-{m:02}-{d:02}')
    exit()

if __name__ == "__main__":
    main()
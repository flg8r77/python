import sys
import csv
from tabulate import tabulate

def main():
    table = []
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif "." not in sys.argv[1] or sys.argv[1].split(".")[1] != "csv":
        sys.exit("Not a CSV file")
    else:
        pass

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table, headers="keys", tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()
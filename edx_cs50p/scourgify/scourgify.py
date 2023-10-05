import sys
import csv

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        pass

    try:
        with open(sys.argv[1], 'r') as read_file, open(sys.argv[2], 'w') as write_file:
            reader = csv.reader(read_file)
            new_headers = ["first", "last", "house"]
            writer = csv.DictWriter(write_file, fieldnames=new_headers)
            writer.writeheader()
            next(reader)
            new_data = []
            for row in reader:
                first = row[0].split(",")[1].lstrip()
                last = row[0].split(",")[0].lstrip()
                house = row[1]
                writer.writerow(dict({'first': first, 'last': last, 'house': house}))

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')


if __name__ == "__main__":
    main()
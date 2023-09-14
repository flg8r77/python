import csv
import sys
import os

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few arguments. Provide input and output csv file name")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    else:
        pass

    try:
        with open(sys.argv[1], 'r') as read_file, open(sys.argv[2], 'w') as write_file:
            reader = csv.DictReader(read_file)
            header_list = reader.fieldnames
            writer = csv.DictWriter(write_file, fieldnames=header_list)
            next(reader)
            writer.writeheader()
            for row in sorted(reader, key=lambda reader: ( int(reader["Founded"]), int(reader["Number of employees"]) )):
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Cannot find file {sys.argv[1]}")

if __name__ == "__main__":
    main()
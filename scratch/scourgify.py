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
            writer.writeheader() #write out the header to the output file before data lines get written
            next(reader) #skip the header from getting processed in the for loop below
            for row in reader:
                first = row[0].split(",")[1].lstrip()
                last = row[0].split(",")[0].lstrip()
                house = row[1]
                #create the dict that will be the row that gets written by csv.DictWriter to the output file
                writer.writerow(dict({'first': first, 'last': last, 'house': house}))

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')


""" for row in sorted(reader, key=lambda row: (int(row["Founded"]), row["Country"])):
            writer.writerow(row) """


if __name__ == "__main__":
    main()
import sys

def main():
    lines = []
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif "." not in sys.argv[1] or sys.argv[1].split(".")[1] != "py":
        sys.exit("Not a Python file")
    else:
        pass

    try:
        with open(sys.argv[1]) as file:
            number_of_lines = 0
            for line in file:
                if line.lstrip().startswith("#") or line.lstrip() == "":
                    pass
                else:
                    number_of_lines += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(number_of_lines)

if __name__ == "__main__":
    main()
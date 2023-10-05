def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):

# check to ensure plate length is between 2 and 6
    if 2 <= len(plate) <= 6 and plate.isalpha():
        return True
    elif 2 <= len(plate) <= 6:
        length_check = "passed"
    else:
        return False

# Check to ensure first two letters of plate are alphabets
    if len(plate) == 2 and plate[:2].isalpha():
        return True
    elif plate[:2].isalpha():
        first_two_check = "passed"
    else:
        return False

# check to ensure plate has only alphabets or numbers
    if plate.isalnum():
        alphanum_check = "passed"
    else:
        return False

# check to ensure plate does not have numbers in the middle and the first number is not 0
    number_of_digits = 0

    for c in plate:
        if c.isdigit():
            number_of_digits += 1

    lookup_index = - number_of_digits

    try:
        if int(plate[lookup_index]) == 0:
            return False
    except ValueError:
        return False

    if plate[lookup_index:].isnumeric():
         number_check = "passed"
    else:
        return False

    if length_check == "passed" and first_two_check == "passed" and alphanum_check == "passed" and number_check == "passed":
        return True
    else:
        return False



if __name__ == "__main__":
    main()

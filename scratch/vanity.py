def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(in_str):
    if lencheck(in_str) and first2(in_str) and alphanumonly(in_str) and number_check(in_str):
        return True
    else:
        return False

# check to ensure length is between 2 and 6
def lencheck(input_str):
    if 2 <= len(input_str) <= 6:
        return True
    else:
        return False

# Check to ensure first two letters are alphabets
def first2(input_str):
    for i in range(2):
        if input_str[i].isalpha():
            pass
        else:
            return False
    return True

# check to ensure plate has only alphabets or numbers
def alphanumonly(input_str):
    if input_str.isalnum():
        return True
    else:
        return False

# check to ensure plate does not have numbers in the middle and the first number is not 0
def number_check(input_str):
    if input_str.isalpha():
        return True

    number_of_digits = 0
    for c in input_str:
        if c.isdigit():
            number_of_digits += 1

    lookup_index = - number_of_digits
    if int(input_str[lookup_index]) == 0:
        return False

    for i in range(number_of_digits):
        if input_str[lookup_index].isdigit():
            pass
        else:
            return False
        lookup_index += 1
    return True

if __name__ == "__main__":
    main()

'''
Decimal to Binary

Write a program that converts a decimal (base 10) number to binary (base 2). Read the
decimal number from the user as an integer and then use the division algorithm shown
below to perform the conversion. When the algorithm completes, result contains the
binary representation of the number. Display the result, along with an appropriate
message.

Algorithm

Let result be an empty string
Let q represent the number to convert
repeat
    Set r equal to the remainder when q is divided by 2
    Convert r to a string and add it to the beginning of result
    Divide q by 2, discarding any remainder, and store the result back into q
until q is 0

'''

def main():

    while True:
        try:
            number_in = int(input("Enter a positive number: "))
            if number_in < 0:
                raise ValueError
        except ValueError:
            continue
        else:
            break
    
    binary_number = ''
    q = number_in
    while q != 0:
        r = q % 2
        binary_number = str(r) + binary_number
        q = q // 2
    
    print(f'Binary representation of {number_in} is {binary_number}')

if __name__ == "__main__":
    main()
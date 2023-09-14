'''
Binary to Decimal

Write a program that converts a binary (base 2) number to decimal (base 10). Your
program should begin by reading the binary number from the user as a string. Then
it should compute the equivalent decimal number by processing each digit in the
binary number. Finally, your program should display the equivalent decimal number
with an appropriate message.
'''


def main():
    while True:
        try:
            binary_number = input("Enter a binary number (base 2): ").strip()
            for c in binary_number:
                if c != "0" and c != "1":
                    raise ValueError
        except ValueError:
            continue
        else:
            break

    decimal_value = 0    
    for i in range(0,len(binary_number)):
        index = -1 * (i + 1)
        value = int(binary_number[index]) * pow(2, i)
        decimal_value += value
    
    print(f'Decimal value of binary number {binary_number} is {decimal_value}')


if __name__ == "__main__":
    main()
import sys
def main():
    binary = ""

    decimal = int(input("Enter a positive integer: "))
    q = decimal
    while q != 0:
        r = str(q % 2)
        binary = r + binary
        q = int(q / 2)

    print(f'Binary of {decimal} is {binary}')

if __name__ == "__main__":
    main()




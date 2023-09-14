import sys

def main():
    running_avg = 0
    numbers_given = 0
    while True:
        try:
            value = int(input("Enter a positive integer (0 to quit): "))
        except ValueError:
            continue
        else:
            if value < 0:
                continue
            elif value == 0:
                sys.exit(f'Final running_average = {running_avg}')
            else:
                numbers_given += 1
                running_avg = ( running_avg + value ) / numbers_given
                print(f'Current {running_average} = {running_avg:0.2f}')
                

if __name__ == "__main__":
    main()
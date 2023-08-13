'''
Write a program that reads integers from the user and stores them in a list. Your
program should continue reading values until the user enters 0. Then it should display
all of the values entered by the user (except for the 0) in ascending order, with one
value appearing on each line. Use either the sort method or the sorted function
to sort the list.
'''

import sys
def main():
    results = []
    while True:
        try:
            value = int(input("Enter an integer (0 to quit): "))
        except ValueError:
            continue
        else:
            if value == 0:
                break
            else:
                results.append(value)
    
    results.sort()
    for item in results:
        print(item)

if __name__ == "__main__":
    main()

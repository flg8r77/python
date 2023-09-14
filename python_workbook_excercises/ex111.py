
'''
 Write a program that reads integers from the user and stores them in a list. Use 0 as
 a sentinel value to mark the end of the input. Once all of the values have been read
 your program should display them (except for the 0) in reverse order, with one value
 appearing on each line.
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
    
    reverse = sorted(results, key=lambda x: x, reverse=True)
    for item in reverse:
        print(item)

if __name__ == "__main__":
    main()

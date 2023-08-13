'''
Create a program that reads integers from the user until a blank line is entered. Once
all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers. Within
each group the numbers should be displayed in the same order that they were entered
by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
should display each value on its own line.
'''


import sys

def main():
    negative_list = []
    zero_list = []
    positive_list = []

    while True:
        try:
            value = input("Enter an integer (blank line to quit): ")
            if value == "":
                break
            else:
                value = int(value)
        except ValueError:
            continue
        else:
            if value < 0:
                negative_list.append(value)
            elif value == 0:
                zero_list.append(value)
            else:
                positive_list.append(value)

    print(negative_list + zero_list + positive_list)

if __name__ == "__main__":
    main()

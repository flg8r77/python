'''
When analysing data collected as part of a science experiment it may be desirable
to remove the most extreme values before performing other calculations. Write a
function that takes a list of values and an non-negative integer, n, as its parameters.
The function should create a new copy of the list with the n largest elements and the
n smallest elements removed. Then it should return the new copy of the list as the
function’s only result. The order of the elements in the returned list does not have to
match the order of the elements in the original list.

Write a main program that demonstrates your function. It should read a list of
numbers from the user and remove the two largest and two smallest values from it by
calling the function described previously. Display the list with the outliers removed,
followed by the original list. Your program should generate an appropriate error
message if the user enters less than 4 values.
'''


import sys

def main():
    original_list = get_input()
    outlier = get_outlier()
    if len(original_list) < 2*outlier:
        sys.exit("Not enough elements in the list to discard outliers. Exiting..")
    
    print(remove_outliers(original_list, outlier))

def get_input():
    rv = []
    while True:
        value_raw = input("Enter an integer value (enter 'quit' when done): ")
        if value_raw == 'quit':
            return rv
        else:
            try:
                value_int = int(value_raw)
            except ValueError:
                continue
            rv.append(value_int)

def get_outlier():
    while True:
        try:
            outliers = int(input("How many smallest and largest outliers should be discarded? "))
            if outliers < 0:
                raise ValueError
        except ValueError:
            continue
        else:
            return outliers
        
def remove_outliers(list_in, outlier):
    rv = list_in
    rv_sorted = sorted(rv, key=lambda x: x)
    for i in range(outlier):
        rv_sorted.pop(0)
    for i in range(outlier):
        rv_sorted.pop()
    return rv_sorted




if __name__ == "__main__":
    main()

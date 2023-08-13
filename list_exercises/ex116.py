'''
An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.

Write a function that determines whether or not a positive integer is perfect. Your
function will take one parameter. If that parameter is a perfect number then your
function will return True. Otherwise it will return False. In addition, write a main
program that uses your function to identify and display all of the perfect numbers
between 1 and 10,000. Import your solution to Exercise 115 when completing this
task.
'''



def main():
    start_range = 1
    end_range = 30001
    perfect_numbers = []
    for number in range(start_range, end_range):
        is_perfect = perfect_number(number)
        if is_perfect:
            perfect_numbers.append(number)
        else:
            pass
    if len(perfect_numbers) > 0:
        print(f'Following are the perfect numbers between {start_range} and {end_range - 1}:')
        for i in perfect_numbers:
            print(i)
    else:
        print("No perfect numbers found in the given range")


def perfect_number(perfect_number_candidate):
    pd_list = proper_divisor(perfect_number_candidate)
    pd_sum = 0
    for i in range(len(pd_list)):
        pd_sum += pd_list[i]
    if pd_sum == perfect_number_candidate:
        return True
    else:
        return False

def proper_divisor(number):
    rv = []
    for i in range (1, number):
        if number % i == 0:
            rv.append(i)
        else:
            continue
    return rv

if __name__ == "__main__":
    main()

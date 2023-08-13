'''
The prime factorization of an integer, n, can be determined using the following steps:

Initialize factor to 2
While factor is less than or equal to n do
    If n is evenly divisible by factor then
        Conclude that factor is a factor of n
        Divide n by factor using floor division
    Else
    Increase factor by 1

    Write a program that reads an integer from the user. If the value entered by the
user is less than 2 then your program should display an appropriate error message.
Otherwise your program should display the prime numbers that can be multiplied
together to compute n, with one factor appearing on each line. For example:
'''

def main():

    while True:
        try:
            number_in = int(input("Enter an integers (2 or greater): "))
            if number_in < 2:
                raise ValueError
        except ValueError:
            continue
        else:
            break

    factor = 2
    factor_list = []
    while factor <= number_in:
        if number_in % factor == 0:
            factor_list.append(factor)
            number_in = number_in // factor
        else:
            factor += 1
    
    for item in factor_list:
        print(item)

if __name__ == "__main__":
    main()
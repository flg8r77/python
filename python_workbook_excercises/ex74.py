'''
Write a program that implements Newton’s method to compute and display the
square root of a number, x, entered by the user. The algorithm for Newton’s method
follows:

	Read x from the user
	Initialize guess to x/2
	While guess is not good enough do

Update guess to be the average of guess and x/guess
When this algorithm completes, guess contains an approximation of the square
root of x. The quality of the approximation depends on how you define “good
enough”. In the author’s solution, guess was considered good enough when the
absolute value of the difference between guess ∗ guess and x was less than or equal
to 10−12
'''

def main():

    while True:
        try:
            number_in = int(input("Enter an integer: "))
        except ValueError:
            continue
        else:
            break

    guess = number_in / 2

    while not (((guess * guess) - number_in) <= pow(10, -12)):
        guess = (guess + (number_in / guess)) / 2

    print(f'Approximation of the square root of {number_in} is {guess:.2f}')

if __name__ == "__main__":
    main()

'''
Greatest common divisor

The greatest common divisor of two positive integers, n and m, is the largest number,
d, which divides evenly into both n and m. There are several algorithms that can be
used to solve this problem, including:

	Initialize d to the smaller of m and n.
	While d does not evenly divide m or d does not evenly divide n do
		Decrease the value of d by 1
	Report d as the greatest common divisor of n and m

Write a program that reads two positive integers from the user and uses this algorithm
to determine and report their greatest common divisor.

'''
def main():
    
	n = get_positive_number()
	m = get_positive_number(another=True)

	if m < n:
		d = m
	else:
		d = n
	
	while ((m % d != 0) or (n % d != 0)):
		d = d - 1
	
	print(f'Greatest common divisor of {m} and {n} is {d}')


def get_positive_number(another=False):
	while True:
		if another == False:
			try:
				number_in = int(input("Enter a positive integer: "))
			except ValueError:
				continue
			else:
				return number_in
		else:
			try:
				number_in = int(input("Enter another positive integer: "))
			except ValueError:
				continue
			else:
				return number_in
			
if __name__ == "__main__":
	main()
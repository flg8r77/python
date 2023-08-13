'''
A string is a palindrome if it is identical forward and backward. For example “anna”,
“civic”, “level” and “hannah” are all examples of palindromic words. Write a program
that reads a string from the user and uses a loop to determine whether or not it is a
palindrome. Display the result, including a meaningful output message.

'''

import sys

def main():
	
	while True:
		input_string = input("Enter a String (Only alphabets allowed): ").strip().casefold()
		if input_string.isalpha():
			break
		else:
			continue
    
	palidrome = ispalidrome(input_string)

	if palidrome:
		print(f'{input_string} is a Palidrome')
	else:
		print(f'{input_string} is not a Palidrome')

def ispalidrome(string):
	for i in range(0, len(string)):
		if string[i] == string[-(i + 1)]:
			continue
		else:
			return False
	return True

if __name__ == "__main__":
    main()

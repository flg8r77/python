'''
There are numerous phrases that are palindromes when spacing is ignored. Examples
include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
among many others. Extend your solution to Exercise 75 so that it ignores spacing
while determining whether or not a string is a palindrome. For an additional challenge,
further extend your solution so that is also ignores punctuation marks and treats
uppercase and lowercase letters as equivalent.
'''

from ex75 import ispalidrome
import string

def main():
	
	while True:
		try:
			string_in = input("Enter a string of words: ").strip().casefold()
			string_in = "".join(string_in.split())
			string_in = string_in.translate(str.maketrans('', '', string.punctuation))
			print(string_in)
			if string_in.isalpha():
				break
			else:
				raise ValueError
		except ValueError:
			continue
		else:
			pass

	if ispalidrome(string_in):
		print('String entered is a Palidrome')
	else:
		print('String entered is not a Palidrome')

if __name__ == "__main__":
	main()
 

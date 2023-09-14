'''
In this exercise you will create a program that identifies all of the words in a
string entered by the user. Begin by writing a function that takes a string as
its only parameter. Your function should return a list of the words in the string
with the punctuation marks at the edges of the words removed. The punctu-
ation marks that you must consider include commas, periods, question marks,
hyphens, apostrophes, exclamation points, colons, and semicolons. Do not remove
punctuation marks that appear in the middle of a word, such as the apostrophes
used to form a contraction. For example, if your function is provided with the
string "Contractions include: don’t, isn’t, and wouldn’t."
then your function should return the list ["Contractions", "include",
"don’t", "isn’t", "and", "wouldn’t"].

Write a main program that demonstrates your function. It should read a string from
the user and then display all of the words in the string with the punctuation marks
removed. You will need to import your solution to this exercise when completing
Exercises 118 and 167. As a result, you should ensure that your main program only
runs when your file has not been imported into another program.
'''

def main():
    input_string = input("Input a string: ")
    punctuation_stripped = remove_punctuation(input_string)
    print(punctuation_stripped)
    for word in punctuation_stripped:
        print(f'{word} ', end="")
    print("")

def remove_punctuation(string_in):
    punctuation = ",.?-'!:;"
    rv = []
    temp = string_in.strip().split()
    for word in temp:
        rv.append(word.rstrip(punctuation))
    return rv

if __name__ == "__main__":
    main()


    

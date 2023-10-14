'''
Many people do not use capital letters correctly, especially when typing on small
devices like smart phones. To help address this situation, you will create a function
that takes a string as its only parameter and returns a new copy of the string that has
been correctly capitalized. In particular, your function must:

• Capitalize the first non-space character in the string,
• Capitalize the first non-space character after a period, exclamation mark or question
mark, and
• Capitalize a lowercase “i” if it is preceded by a space and followed by a space,
period, exclamation mark, question mark or apostrophe.

Implementing these transformations will correct most capitalization errors. For
example, if the function is provided with the string “what time do i have to be there?
what’s the address? this time i’ll try to be on time!” then it should return the string
“What time do I have to be there? What’s the address? This time I’ll try to be on
time!”. Include a main program that reads a string from the user, capitalizes it using
your function, and displays the result.
'''

def main():

    s1 = "what time do i have to be there? what's the address? this time i'll try to be on time!"
    print(capitalize_it(s1))
    
def capitalize_it(s):
    inlist = s.split()
    outlist = []
    for i in range(0, len(inlist)):
        if i == 0:
            outlist.append(inlist[i].capitalize())
        elif inlist[i - 1].endswith(".") or inlist[i - 1].endswith("!") or inlist[i - 1].endswith("?"):
            outlist.append(inlist[i].capitalize())
        elif inlist[i].startswith("i") and len(inlist[i]) == 1:
            outlist.append(inlist[i].capitalize())
        elif inlist[i].startswith("i") and len(inlist[i]) > 1:
            if inlist[i][1] == "." or inlist[i][1] == "!" or inlist[i][1]== "?" or inlist[i][1] == "'":
                outlist.append(inlist[i].capitalize())
            else:
                outlist.append(inlist[i])
        else:
            outlist.append(inlist[i])

    outstring = ""
    for word in outlist:
        outstring = f'{outstring} {word}'

    return outstring.strip()

if __name__ == "__main__":
    main()

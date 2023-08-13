'''
In this exercise, you will create a program that reads words from the user until the
user enters a blank line. After the user enters a blank line your program should dis-
play each word entered by the user exactly once. The words should be displayed in
the same order that they were first entered. For example, if the user enters:

first
second
first
third
second

then your program should display:

first
second
third
'''

def main():
    wrds_gvn = []
    while True:
        wrd_gvn = input("Enter a word (leave blank to quit): ")
        if wrd_gvn == "":
            break
        else:
            wrds_gvn.append(wrd_gvn)
    
    print(wrds_gvn)
    unq_lst = get_unq(wrds_gvn)
    print(unq_lst)
        

def get_unq(list_in):
    seen = []
    for x in range(len(list_in)):
        if list_in[x] not in seen:
            seen.append(list_in[x])
    return seen

if __name__ == "__main__":
    main()

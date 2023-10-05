def main():
    message_in = input("Input: ")
    print(shorten(message_in))

def shorten(input_str):
    vlist = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    rv = ""
    for c in input_str:
        if c in vlist:
            rv = rv + ""
        else:
            rv = rv + c
    return rv

if __name__ == "__main__":
    main()
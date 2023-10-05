def main():
    message = input("")
    print(convert(message))


def convert(inputstring):
    words = inputstring.split(" ")
    print(words)
    rv = ""
    for word in words:
        if word == ":)":
            rv += "🙂" + " "
        elif word == ":(":
            rv += "😰" + " "
        elif word == ":/":
            rv += "🙄" + " "
        elif word == "lol":
            rv += "🤣" + " "
        else:
            rv += word + " "
    return rv.lstrip()

main()

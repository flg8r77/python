def main():

    import sys
    from pyfiglet import Figlet

    figlet = Figlet()

    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid usage")

    elif len(sys.argv) == 1:
        input_str = get_input()
        print(figlet.renderText(input_str))

    elif len(sys.argv) == 3 and ( sys.argv[1] != "-f" and sys.argv[1] != "--font" ):
        sys.exit("Invalid usage")

    elif len(sys.argv) == 3 and sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")

    else:
        figlet.setFont(font=sys.argv[2])
        input_str = get_input()
        print(figlet.renderText(input_str))

def get_input():
    return input("Input: ")

if __name__ == "__main__":
    main()
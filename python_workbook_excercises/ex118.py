def main():

    in_string = user_input()
    print(in_string)


def user_input():
    while True:
        try:
            user_input = input("Enter a test string (no numbers allowed): ").strip()
            for word in user_input.split():
                if word.strip(",.?-'!:;").isalpha:
                    continue
                else:
                    raise ValueError
        except ValueError:
            continue
        else:
            return user_input

if __name__ == "__main__":
    main()
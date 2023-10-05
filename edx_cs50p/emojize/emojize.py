def main():
    import emoji

    input_str = input("Input: ")

    print(emoji.emojize(input_str, language='alias'))


if __name__ == "__main__":
    main()
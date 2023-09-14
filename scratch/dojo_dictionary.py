def main():
    original_dict = {"one": 1, "two": 2, "three": 3}

    reversed_dict = {}

    for key, value in original_dict.items():
        reversed_dict[value] = key
    
    print(reversed_dict)

if __name__ == "__main__":
    main()


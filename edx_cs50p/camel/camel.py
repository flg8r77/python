def main():
    camel = input("camelCase: ")
    if camel.islower():
        print(camel)
    else:
        print(f'snake_case: {camel_to_snake(camel)}')

def camel_to_snake(input_string):
    rv = ""
    for c in input_string:
        if c.isupper():
            rv = rv + "_" + c
        else:
            rv = rv + c
    return rv.lower()

if __name__ == "__main__":
    main()

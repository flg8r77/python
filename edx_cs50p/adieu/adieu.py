def main():

    import inflect

    p = inflect.engine()

    list_of_names = []

    while True:
        try:
            name = input("Name: ").strip()
        except EOFError:
            break
        else:
            list_of_names.append(name)

    print("Adieu, adieu, to " + p.join(list_of_names))

if __name__ == "__main__":
    main()

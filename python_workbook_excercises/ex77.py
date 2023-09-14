def main():
    rows = list(range(1, 11))
    columns = list(range(1, 11))
    print(" ", end='')
    for row in rows:
        print(f'\t{row}', end='')
    print("")
    for column in columns:
        print(column, end='')
        for row in rows:
            print(f'\t{column * row}', end='')
        print("")


if __name__ == "__main__":
    main()

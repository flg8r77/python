def main ():

    total = 0

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while True:
        menu_item = get_menu_item()
        try:
            item_value = menu[menu_item]
        except KeyError:
            continue

        total = total + item_value
        print(f'Total: ${total:.2f}')

def get_menu_item():

    while True:
        try:
            return input("Item: ").casefold().title()
        except ValueError:
            continue
        except EOFError:
            exit_program()

def exit_program():
    print("\n")
    exit()

if __name__ == "__main__":
    main()
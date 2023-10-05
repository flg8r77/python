def main():
    grocery_list = {}
    while True:
        grocery_item = get_grocery_item()
        if grocery_item == 128:
            output_and_end(grocery_list)
        else:
            try:
                grocery_item_quantity = grocery_list[grocery_item]
                grocery_item_quantity += 1
                grocery_list[grocery_item] = grocery_item_quantity
            except KeyError:
                grocery_list[grocery_item] = 1

def get_grocery_item():
    while True:
        try:
            item = input("").upper()
            if item.replace(" ", "").isalpha():
                return item
            else:
                raise ValueError
        except EOFError:
            return 128
        except ValueError:
            continue

def output_and_end(dict_in):
    keylist = list(dict_in.keys())
    keylist.sort()
    for key in keylist:
        print(f'{dict_in[key]} {key}')
    exit()

if __name__ == "__main__":
    main()
import sys

#dict with beer and carbs/ounce
beer = {
    "michelob ultra": 0.22,
    "yuengling flight": 0.22,
    "yuengling light": 0.27,
    "natural light": 0.27,
    "lone star": 1.00
}


def main():
    beer_name = input("which beer: ")
    if beer_name not in beer.keys():
        sys.exit("sorry this beer not supported")
    
    try:
        serving_size = int(input("beer ounces per serving: "))
    except ValueError:
        sys.exit("serving size should be number of ounces")
    
    
    while True:
        try:
            number_of_servings = int(input(f'How many {serving_size}oz serving did you have?: '))
        except ValueError:
            print("serving size must be a number")
            continue
        else:
            break
                                                                        

    print(f'Carbs consumed is: {beer[beer_name] * serving_size * number_of_servings:,.2f} grams')


if __name__ == "__main__":
    main()

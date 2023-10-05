import random

def main():
    level = get_level()

    wrongs = 0
    for i in range(9):
        num1, num2 = generate_integer(level)
        strikes = 0
        while True:
            try:
                answer = int(input(f'{num1} + {num2} = '))
            except ValueError:
                if strikes == 2:
                    print(f'{num1} + {num2} = {num1 + num2}')
                    wrongs += 1
                    break
                else:
                    strikes += 1
                    print("EEE")
                    continue
            else:
                if answer == num1 + num2:
                        break
                elif answer != num1 + num2 and strikes == 2:
                    print("EEE")
                    print(f'{num1} + {num2} = {num1 + num2}')
                    wrongs += 1
                    break
                else:
                    strikes += 1
                    print("EEE")
                    continue
    print(f'Score: {10 - wrongs}')

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level != 1 and level != 2 and level != 3:
                continue
            else:
                return level

def generate_integer(level):
    if level == 1:
        range_start = 0
        range_end = (10**level) - 1
    else:
        range_start = 10**(level - 1)
        range_end = (10**level) - 1

    n1 = random.randint(range_start, range_end)
    n2 = random.randint(range_start, range_end)
    return n1, n2



if __name__ == "__main__":
    main()
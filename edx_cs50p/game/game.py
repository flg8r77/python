import sys
import random

def main():


    level = get_level()

    secret = random.randint(1, level)
    guess(secret)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level <= 0:
                continue
            else:
                return level

def guess(number):
    while True:
        try:
            user_guess = int(input("Guess: "))
        except ValueError:
            continue
        else:
            if user_guess < number:
                print("Too small!")
                continue
            elif user_guess > number:
                print("Too large!")
                continue
            else:
                exit("Just right!")

if __name__ == "__main__":
    main()
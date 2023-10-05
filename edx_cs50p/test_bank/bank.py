def main():
    greeting = input("Greeting: ").strip()
    fine = value(greeting)

    print(f'${fine}')

def value(greeting):
    if greeting.startswith("hello") or greeting.startswith("Hello") or greeting.startswith("HELLO"):
        return 0
    elif greeting.startswith("h") or greeting.startswith("H"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
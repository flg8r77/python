def main():
    amount_due = 50
    total_in = 0
    while total_in < 50:
        coin_in = insert_coin(amount_due)
        amount_due = amount_due - coin_in
        total_in = total_in + coin_in
    print(f'Change Owed: {total_in - 50}')

def insert_coin(amt_due):
    print(f"Amount Due: {amt_due}")
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        return coin
    else:
        return 0


if __name__ == "__main__":
    main()
    
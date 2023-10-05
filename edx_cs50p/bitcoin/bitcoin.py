import requests
import sys
import json

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
# Adding some random comments
    try:
        coins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        sys.exit("could not pull bitcoin price from coindesk")

    price = r.json()["bpi"]["USD"]["rate_float"]

    print(f'${coins * price:,.4f}')

if __name__ =="__main__":
    main()
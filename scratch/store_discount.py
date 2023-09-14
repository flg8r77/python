import csv
from tabulate import tabulate

def main():
    header_list = ["Price", "Discount", "New Price"]
    price_list = [4.95, 9.95, 14.95, 19.95, 24.95]
    merch = []

    for price in price_list:
        discount = round(price * 0.60, 2)
        new_price = round(price - discount, 2)
        merch.append(dict({'Price': price, 'Discount': discount, 'New Price': new_price}))
    
    print(tabulate(merch, headers="keys", tablefmt="fancy_grid"))

    with open("dataout/store_discount.csv", 'w') as write_file:
        writer = csv.DictWriter(write_file, fieldnames=header_list)
        writer.writeheader()
        for row in merch:
            writer.writerow(row)
    

if __name__ == "__main__":
    main()
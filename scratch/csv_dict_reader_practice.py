import csv
from tabulate import tabulate


def main():
        
    with open("./csv/organizations-100.csv") as read_file, open("./csv/organization_sorted_Founded_country.csv", 'w') as write_file:
        reader = csv.DictReader(read_file)
        header_list = reader.fieldnames
        writer = csv.DictWriter(write_file, fieldnames=header_list)
        writer.writeheader()
        for row in sorted(reader, key=lambda row: (int(row["Founded"]), row["Country"])):
            writer.writerow(row)
            

            

    #print(list_sorted)
    #print(tabulate(list_sorted, headers="keys", tablefmt="fancy_grid"))


    
"""     with open("Organizations_headcount.txt", "a") as file:
       for org in sorted(orgs, key=lambda org: int(org["Headcount"]), reverse=True):
            file.write(f'Name: {org["Name"]}\nHeadcount: {org["Headcount"]}\n\n') """


if __name__ == "__main__":
    main()
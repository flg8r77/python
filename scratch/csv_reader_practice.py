import csv
    
def main():

    orgs = []
     
    with open("organizations-100.csv") as file:
        contents = csv.reader(file)
        for row in contents:
            orgs.append({"Org_ID": row[1], "name": row[2]})
            

    for org in sorted(orgs, key=lambda org: org["name"]):
        print(f'{org["name"]} has an Org_ID of {org["Org_ID"]}')



if __name__ == "__main__":
    main()
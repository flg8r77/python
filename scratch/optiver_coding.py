import sys
csv_input = sys.stdin.read()
from string import digits

# Enter your code here. The csv input has been populated for you into a string, csv_input. Print output to STDOUT
list = []
mydata = csv_input.splitlines()
#print(mydata)
for item in mydata:
    list.append(item.split(","))
list.pop(0)
print(list)
sorted_list = sorted(list, key=lambda x: (x[0], x[2]))
print("date,exchange,total_bytes")
for item in sorted_list:
    print(f"{item[0]},{item[2].rstrip(digits)},{item[4]}")

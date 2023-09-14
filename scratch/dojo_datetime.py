import datetime
from tabulate import tabulate

def main():

    info = []
#Documentation link :   https://docs.python.org/3/library/datetime.html

    in_here = datetime.datetime.now()
    in_utc = datetime.datetime.utcnow()

    info.append(dict({"location": "here", "current_time": in_here }))
    info.append(dict({"location": "utc", "current_time": in_utc }))
    print(tabulate(info, headers="keys", tablefmt="fancy_grid"))

    print(in_here.toordinal())
    print(in_here.timestamp())

if __name__ == "__main__":
    main()
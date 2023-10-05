import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    sys.tracebacklimit = None
    matches = re.search(r"^(\d\d?):?(\d\d)? (\w+) to (\d\d?):?(\d\d)? (\w+)$", s)
    if matches:
        if matches.group(2) != None and ( int(matches.group(2)) < 0 or int(matches.group(2)) > 59 ):
            raise ValueError("minutes have to be between 0-59")
        if matches.group(5) != None and ( int(matches.group(5)) < 0 or int(matches.group(5)) > 59 ):
            raise ValueError("minutes have to be between 0-59")
        if int(matches.group(1)) < 0 or int(matches.group(1)) > 12:
            raise ValueError("Hours have to be between 0-12")
        if int(matches.group(4)) < 0 or int(matches.group(4)) > 12:
            raise ValueError("Hours have to be between 0-12")
        if matches.group(3) != "AM" and matches.group(3) != "PM":
            raise ValueError("Only AM or PM allowed")
        if matches.group(6) != "AM" and matches.group(6) != "PM":
            raise ValueError("Only AM or PM allowed")

        #start hour value in 24hr format
        if matches.group(1) == "12" and matches.group(3) == "AM":
            start_hr = 0
        elif matches.group(1) == "12" and matches.group(3) == "PM":
            start_hr = 12
        elif matches.group(3) == "AM":
            start_hr = int(matches.group(1))
        else:
            start_hr = int(matches.group(1)) + 12

        #start min value
        if matches.group(2) != None:
            start_min = int(matches.group(2))
        else:
            start_min = 0

        #stop hour value in 24hr format
        if matches.group(4) == "12" and matches.group(6) == "AM":
            stop_hr = 0
        elif matches.group(4) == "12" and matches.group(6) == "PM":
            stop_hr = 12
        elif matches.group(6) == "AM":
            stop_hr = int(matches.group(4))
        else:
            stop_hr = int(matches.group(4)) + 12

        #stop min value
        if matches.group(5) != None:
            stop_min = int(matches.group(5))
        else:
            stop_min = 0
        rv = f"{start_hr:02d}:{start_min:02d} to {stop_hr:02d}:{stop_min:02d}"
        return rv

    else:
        raise ValueError("incorrect time format entered")
        sys.exit()

if __name__ == "__main__":
    main()
import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    matches = re.search(r"^([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)$", ip)
    if not matches:
        return False
    else:
        for octet in matches.groups():
            if int(octet) < 0 or int(octet) > 255:
                return False
        return True

if __name__ == "__main__":
    main()

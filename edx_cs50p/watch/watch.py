import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):

    matches = re.search(r"^.+https?.+(?:www)?.*youtube\.com/embed/(\w+).*$", s)
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None

    #matches2 = re.search(r"^.*youtube\.com/embed/(\w+).*$", s)
    #print(matches2.groups())

if __name__ == "__main__":
    main()
import sys
import re
import os

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments\nUsage: youtubedl_namefix.py <directory path>")
    else:
        folder = sys.argv[1]

    try:
        list_of_files = os.listdir(folder)
    except FileNotFoundError:
        sys.exit(f'Could not find the directory: \t{folder}')
    else:
        pass

    for filename in list_of_files:
        match = re.match(r'^.*(-\w*\d*)\.mp\d$', filename)
        if match:
            newfilename = filename.replace(match.groups(0)[0], '')
            src = f"{folder}/{filename}"
            dst = f"{folder}/{newfilename}"
            #print(f"{src} -----> {dst}")
            os.rename(src, dst)
        else:
            print(filename)

if __name__ == "__main__":
    main()

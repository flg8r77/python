import sys
import os
import json

def main():
    filename = input("Filename (or Fully qualified path): ")
    try:
        with open(filename) as read_file:
            jo = json.load(read_file)
            print(json.dumps(jo, indent=4))
    except FileNotFoundError:
        sys.exit(f'File {filename} not found!')
    
if __name__ == "__main__":
    main()

    
            
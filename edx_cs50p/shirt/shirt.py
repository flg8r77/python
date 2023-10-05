import sys
import os
from PIL import Image

def main():

    valid_extensions = [".jpg", ".jpeg", ".png"]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.splitext(sys.argv[1])[1].casefold() not in valid_extensions or os.path.splitext(sys.argv[2])[1].casefold() not in valid_extensions:
        sys.exit("Invalid input")
    elif os.path.splitext(sys.argv[1])[1].casefold() != os.path.splitext(sys.argv[2])[1].casefold():
        sys.exit("Input and output have different extensions")
    else:
        pass


    shirt = Image.open("shirt.png")
    before_img = Image.open("before1.jpg")
    print(f'shirt size: {shirt.size}')
    print(f'before_img size: {before_img.size}')







if __name__ == "__main__":
    main()
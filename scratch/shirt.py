import sys
import os
from PIL import Image, ImageOps

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
    try:
        photo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f'File {sys.argv[1]} not found')
    shirt = Image.open("/home/ze/zedata/code/python/jpeg/shirt.png")
    size = shirt.size
    photo_resized = ImageOps.fit(photo, size)
    photo_resized.paste(shirt,shirt)
    photo_resized.save(sys.argv[2])
    



if __name__ == "__main__":
    main()
import sys
import csv
import os
from PIL import Image, ImageOps
def main():
    #conditions before able to try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    ffile = sys.argv[1]
    sfile = sys.argv[2]

    # valid extension
    validext = ('.jpg', '.png', '.jpeg')
    first_ext= os.path.splitext(ffile)[1].lower()
    second_ext = os.path.splitext(sfile)[1].lower()
    

    if first_ext not in validext:
        sys.exit("wrong extension")
    elif second_ext not in validext :
        sys.exit("wrong extension")
    if first_ext != second_ext:
        sys.exit("input and output doesn't have the same extension")


    try:
        with Image.open('shirt.png') as img:
            photo = Image.open(ffile)
            photo = ImageOps.fit(photo, img.size)
            photo.paste(img, img)
            photo.save(sfile)
    except :
        exit(1)
if __name__ == "__main__":
    main()

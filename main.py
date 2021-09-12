import os
import re
import sys
from PIL import Image, ImageEnhance


def main():
    """
    Entry point for code.
    """
    for infile in sys.argv[1:]:
        hero = create_hero(infile=infile)
        if hero is not None:
            try:
                os.remove(infile)
                print(f"{hero} haves been created, and source file removed")
            except Exception as err:
                print(err)


def create_hero(infile: str) -> str:
    """
    Create a hero image for use on samkenney.com blog.

    args:
        infile: (str)
            The path to the file to crop.

    returns: (str)
        The path of the new cropped file.
    """
    size = 740, 740
    outfile = re.search("(.*)\.[a-zA-Z]{3,4}", infile)[1] + "-hero.png"

    im = Image.open(infile)
    width = im.size[0]
    if width >= 740:
        im.thumbnail(size, Image.ANTIALIAS)
        sharpen = ImageEnhance.Sharpness(im)
        sharpen.enhance(1.5).save(outfile, "PNG")
        return outfile
    else:
        print("Main image must be at least 740px wide")


if __name__ == "__main__":
    main()

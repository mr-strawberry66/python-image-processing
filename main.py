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
    outfile = re.search("(.*)\.[a-zA-Z]{3,4}", infile)[1] + "-hero.png"

    im = Image.open(infile)
    width = im.size[0]
    height = im.size[1]
    aspect = width / float(height)
    required_width = 640
    required_height = 350
    required_aspect = required_width / float(required_width)

    if aspect > required_aspect:
        new_width = int(required_aspect * height)
        offset = (width - new_width) / 2
        resize = (offset, 0, width - offset, height)
    else:
        new_height = int(width / required_aspect)
        offset = (height - new_height) / 2
        resize = (0, offset, width, height - offset)

    im.crop(resize).resize((required_width, required_height), Image.ANTIALIAS)
    sharpen = ImageEnhance.Sharpness(im)
    sharpen.enhance(1.5).save(outfile, "PNG")
    return outfile


if __name__ == "__main__":
    main()

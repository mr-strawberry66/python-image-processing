import os
import re
import sys
from PIL import Image, ImageEnhance

REQUIRED_WIDTH = 640
REQUIRED_HEIGHT = 350


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
    required_aspect = REQUIRED_WIDTH / float(REQUIRED_WIDTH)

    if width >= REQUIRED_WIDTH:
        if aspect > required_aspect:
            new_width = int(required_aspect * height)
            offset = (width - new_width) / 2
            resize = (0, 0, width - (offset * 2), height)
        else:
            new_height = int(width / required_aspect)
            offset = (height - new_height) / 2
            resize = (0, 0, width, height - (offset * 2))

        hero = im.crop(resize).resize(
            (REQUIRED_WIDTH, REQUIRED_HEIGHT), resample=Image.ANTIALIAS
        )
        sharpen = ImageEnhance.Sharpness(hero)
        sharpen.enhance(1.5).save(outfile, "PNG")
        return outfile
    else:
        print("Image must be at least 640px wide")


if __name__ == "__main__":
    main()

# Python image processing for my blog
*(Version 1.0)*

This is a toolkit used to prepare images for my blog posts. As of V1.0, it will take a main image in `png` or `jpg` format, then create a suitably sized hero image.

## How to use
*   Create a virtualenv using [Python virtualenv](https://docs.python.org/3/library/venv.html) `virtualenv venv --prompt "name of env"`
*   Install requirements using `pip install -r requirements.txt`.
*   Run the script with `python3 main.py [path/to/your/image/here.png]`.

## Notes
*   The main image must have the correct naming convention, ie, `article-name.file-format`.

    For example, `face-recognition.jpeg`, or `notes.png`.

*   The input file must be either `png`, `jpg`, or `jpeg`.

*   The output files will always be `.png` files.

*   The output files will be written to the same directory as the input file

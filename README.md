# ASCII Image Converter

Convert images to ASCII art using Python.

## Installation

Clone this repository.
Install the required packages:

```bash
pip install pillow numpy
```

## Usage

Be sure to have the image to be converted in the same folder of the script

```python
from ascii_image_converter import to_ascii

# Convert an image to ASCII art
to_ascii("image.jpg", (640, 300))  # Optional: provide (width, height) to resize
```

## TODO

 - Validate the path entry

 - Maybe an easier way to run the function

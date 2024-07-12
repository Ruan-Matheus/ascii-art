from PIL import Image, ImageOps
import numpy as np
from math import ceil


def map_brightness(value: int) -> int:
    brightness_set = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    interpolation = ceil(np.interp(value, [0,255], [0, len(brightness_set) - 1]))
    return brightness_set[interpolation]
    


def to_ascii(image_path: str, size: tuple[int, int] = None) -> None:
    resized = False
    if size:
        with Image.open(image_path) as im:
            # Not dealing with actuals paths
            ImageOps.fit(im, size).save("resized_" + image_path)
            resized = True

    if resized:
        image_path = "resized_" + image_path

    with Image.open(image_path) as im:
        px = im.load()
        lux = []

        print(im.format, im.size, im.mode)

        width, height = im.size

        for i in range(height):
            row = []
            for j in range(width):
                avg_brightness = int(sum(px[j, i]) / 3)  # Calculate average brightness
                row.append(map_brightness(avg_brightness))   # Map to ASCII character
            lux.append("".join(row))  # Add the row to lux

    # Print the resulting ASCII art
    for row in lux:
        print(row)


if __name__ == "__main__":
    to_ascii("image.jgp", (800, 600))

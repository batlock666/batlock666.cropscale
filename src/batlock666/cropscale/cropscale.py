# NOQA: D100

import math

DEFAULT_SAR_WIDTH = 1
DEFAULT_SAR_HEIGHT = 1
DEFAULT_WANTED = [
    (512, 384),
    (640, 360),
    (720, 300),
    (720, 324),
    (720, 360),
]

def cropscale_filter(  # NOQA: D103, E302
    width, height,
    sar_width=DEFAULT_SAR_WIDTH,
    sar_height=DEFAULT_SAR_HEIGHT,
    wanted=DEFAULT_WANTED,
):
    result = []

    adj_width = width
    adj_height = height

    if (sar_width > sar_height) and sar_height:
        adj_width *= sar_width / sar_height
        adj_width = int(adj_width)
        adj_width += adj_width % 2
    elif (sar_width < sar_height) and sar_width:
        adj_height *= sar_height / sar_width
        adj_height = int(adj_height)
        adj_height += adj_height % 2

    if (adj_width != width) or (adj_height != height):
        result.append(f"setsar=0,scale={adj_width}:{adj_height}")

        width = adj_width
        height = adj_height

    best_fit = 0
    crop_width, crop_height = 0, 0
    scale_width, scale_height = 0, 0

    for (wanted_width, wanted_height) in wanted:
        divisor = math.gcd(wanted_width, wanted_height)
        min_width = 2 * wanted_width // divisor
        min_height = 2 * wanted_height // divisor

        multiplier = width // min_width
        if ((min_height * multiplier) > height):
            multiplier = height // min_height

        new_fit = (min_width * multiplier) * (min_height * multiplier)
        if new_fit > best_fit:
            best_fit = new_fit

            crop_width = min_width * multiplier
            crop_height = min_height * multiplier
            scale_width = wanted_width
            scale_height = wanted_height

    if (crop_width != width) or (crop_height != height):
        result.append(f"crop={crop_width}:{crop_height}")
    if (scale_width != crop_width) or (scale_height != crop_height):
        result.append(f"scale={scale_width}:{scale_height}")

    return ",".join(result)

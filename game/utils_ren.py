from typing import Optional

from renpy.display.im import Image
from renpy.display.pgrender import Surface
import renpy

reputation: int

"""renpy
init python:
"""


def get_registered_image_size(image_name: str) -> tuple[Optional[int], Optional[int]]:
    image: Optional[Image] = renpy.exports.get_registered_image(image_name)
    if image is None:
        raise ValueError(f"Displayable {image_name} not found")
    if isinstance(image, renpy.display.transform.Transform):
        raise NotImplementedError("Transforms are not supported")
    pysurface: Surface = renpy.display.im.cache.get(image)
    return pysurface.get_size()


def get_image_size(image_path: str) -> tuple[int, int]:
    return renpy.display.im.load_surface(image_path).get_size()


def search_store(name: str) -> None:
    for key in store.__dict__:
        if name in key:
            print(key)


def interpolate_color_to_white(hex_color: str, factor: float) -> str:
    factor = min(max(factor, 0.0), 1.0)

    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    r_white = int(r + (255 - r) * (1 - factor))
    g_white = int(g + (255 - g) * (1 - factor))
    b_white = int(b + (255 - b) * (1 - factor))

    return f"#{r_white:02x}{g_white:02x}{b_white:02x}"

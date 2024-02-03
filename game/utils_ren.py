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

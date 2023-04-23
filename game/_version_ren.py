"""renpy
python early:
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from renpy import config
    import renpy.exports as renpy


def is_patreon() -> bool:
    return not config.enable_steam


def is_deluxe() -> bool:
    return is_patreon()

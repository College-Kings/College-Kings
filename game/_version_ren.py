from renpy import config
import renpy.exports as renpy

"""renpy
python early:
"""


def is_patreon() -> bool:
    return not config.enable_steam


def is_deluxe() -> bool:
    return is_patreon()

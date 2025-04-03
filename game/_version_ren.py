from renpy import config

"""renpy
python early:
"""


def is_patreon() -> bool:
    return not config.enable_steam


def is_deluxe() -> bool:
    return is_patreon()

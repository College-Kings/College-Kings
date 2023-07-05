import math
import os
from typing import Any

from renpy import config, store, ui
import renpy.exports as renpy

"""renpy
init python:
"""


def write_console(data: object) -> None:
    with open("console.txt", "w") as f:
        f.write(str(data))


def open_deluxe_folder() -> None:
    import webbrowser

    path: str = os.path.join(config.basedir, "deluxe_content")
    webbrowser.open("file:///" + path)


def label_callback(label_name: str, is_reached_from_jump: bool) -> None:
    if label_name.startswith("_"):
        return

    try:
        store.label_history
    except AttributeError:
        store.label_history = []

    if not isinstance(store.label_history, list):
        store.label_history = list(store.label_history)

    if not store.label_history or store.label_history[-1] != label_name:
        store.label_history.append(label_name)


def write_scene_lines_to_file() -> None:
    file_line: tuple[str, str] = renpy.get_filename_line()  # type: ignore
    with open(os.path.join(config.basedir, "game_log.txt"), "a") as f:
        f.write(f"{file_line}\n")


def get_distance_between_two_points(
    point_1: tuple[int, int], point_2: tuple[int, int]
) -> int:
    return int(((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5)


def get_angle_between_two_points(
    point_1: tuple[int, int], point_2: tuple[int, int]
) -> float:
    return math.atan2(point_2[1] - point_1[1], point_2[0] - point_1[0]) * (
        180 / math.pi
    )


def set_dict_values(dict_: dict[Any, Any], value: Any = True) -> None:
    for key in dict_:
        dict_[key] = value


inf_adj = ui.adjustment()
inf_adj.value = float("inf")

renpy.add_layer("foreground", above="master")  # type: ignore

"""renpy
init 100 python:
"""

if store.config_debug:
    config.interact_callbacks.append(write_scene_lines_to_file)  # type: ignore

config.overlay_screens.append("free_roam_tutorial")  # type: ignore

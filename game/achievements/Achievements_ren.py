from dataclasses import dataclass
from typing import ClassVar

path_builder: bool
_in_replay: bool

"""renpy
init python:
"""


@dataclass
class Achievement:
    all_achievements: ClassVar[dict[str, "Achievement"]] = {}

    _id: str
    _description: str
    _hidden: bool = False
    _hide_description: bool = False

    @property
    def id(self) -> str:
        return self._id

    @property
    def description(self) -> str:
        return self._description

    @property
    def hidden(self) -> bool:
        return self._hidden

    @hidden.setter
    def hidden(self, value: bool) -> None:
        self._hidden = value

    @property
    def hide_description(self) -> bool:
        return self._hide_description

    @property
    def display_name(self) -> str:
        return self.id.replace("_", " ")

    def register(self) -> "Achievement":
        self.all_achievements[self.id] = self

        # Add achievements to renpy/steam
        achievement.register(self.id)  # type: ignore
        achievement.sync()  # type: ignore
        return self

    def grant(self) -> None:
        if path_builder or _in_replay:
            return

        renpy.show(self.id, [show_achievement])  # type: ignore
        achievement.grant(self.id)  # type: ignore
        achievement.sync()  # type: ignore

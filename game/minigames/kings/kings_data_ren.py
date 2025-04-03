from dataclasses import dataclass

"""renpy
init python:
"""


@dataclass
class KingsData:
    drinks: int = 0

    def drink(self) -> None:
        self.drinks += 1

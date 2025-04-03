init python:
    class Fight:
        def __init__(
            self, player: "PlayableCharacter", opponent: "NonPlayableCharacter", end_label: str
        ):
            self.player = player
            self.opponent = opponent
            self.end_label = end_label

            self.stats: dict[str, dict[str, int]] = {
                player.name: {
                    "guards_broken": 0,
                    "damage_dealt": 0,
                    "damage_blocked": 0,
                    "damage_taken": 0,
                },
                opponent.name: {
                    "guards_broken": 0,
                    "damage_dealt": 0,
                    "damage_blocked": 0,
                    "damage_taken": 0,
                },
            }

            self.move_list: list[dict[str, list[FightMoves]]] = []

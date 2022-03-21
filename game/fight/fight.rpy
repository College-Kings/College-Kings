init python:
    class Fight:
        def __init__(self, player, opponent, end_label):
            self.player = player
            self.opponent = opponent
            self.end_label = end_label

            self.stats = {
                player.name: {
                    "guards_broken": 0,
                    "damage_dealt": 0,
                    "damage_blocked": 0,
                    "damage_taken": 0
                },
                opponent.name: {
                    "guards_broken": 0,
                    "damage_dealt": 0,
                    "damage_blocked": 0,
                    "damage_taken": 0
                }
            }

            self.move_list = []
            
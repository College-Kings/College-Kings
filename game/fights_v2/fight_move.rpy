init python:

    # class FightStance(Enum):
    #     DEFENSE = 0
    #     NEUTRAL = 1
    #     AGGRESSIVE = 2

    class FightMove:
        moves = []

        def __init__(self, name, description, damage, accuracy, stamina_cost, stance, effect, jump_to, images=None):
            self.name = name
            self.description = description
            self.damage = damage
            self.accuracy = accuracy
            self.stamina_cost = stamina_cost
            self.stance = stance
            self.effect = effect
            self.jump_to = jump_to
            self.images = images
        

            FightMove.moves.append(self)

        def copy(self, images):
            return self.__class__(self.name, self.description, self.damage, self.accuracy, self.stamina_cost, self.stance, self.effect, self.jump_to, images)

define HOOK = FightMove(
    name="Hook",
    description="A devastating attack to your opponent's head.",
    damage=10,
    accuracy=70,
    stamina_cost=4,
    stance=2,
    effect="|> Aggressive Stance",
    jump_to="player_hook_v2"
)

define JAB = FightMove(
    name="Jab",
    description="Attack with a quick jab straight to the chin.",
    damage=5,
    accuracy=80,
    stamina_cost=2,
    stance=1,
    effect="|> Neutral Stance",
    jump_to="player_jab_v2"
)

define TRASHTALK = FightMove(
    name="Trash Talk",
    description="Trash talk your opponent to shake their confidence.",
    damage=0,
    accuracy=0,
    stamina_cost=2,
    stance=2,
    effect="|> Neutral Stance",
    jump_to="player_trash_talk_v2"
)

define GUARDUP = FightMove(
    name="Guard Up",
    description="End your turn with your guard up.",
    damage=0,
    accuracy=0,
    stamina_cost=4,
    stance=0,
    effect="|> Defensive Stance",
    jump_to="player_guard_up_v2"
)

define ENDTURN = FightMove(
    name="End Turn",
    description="End your turn and retain up to 2 stamina",
    damage=0,
    accuracy=0,
    stamina_cost=0,
    stance=0,
    effect="|> Keep Current Stance",
    jump_to="opponent_attack_v2"
)

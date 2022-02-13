init python:
    class FightMove:
        moves = []

        def __init__(self, name, description, damage, stamina_cost, stance, images=None):
            self.name = name
            self.description = description
            self.damage = damage
            self.stamina_cost = stamina_cost
            self.stance = stance
            self.images = images

            FightMove.moves.append(self)

        def copy(self, images):
            return self.__class__(self.name, self.description, self.damage, self.stamina_cost, self.stance, images)

    define HOOK = FightMove(
        name="Hook",
        description="Attack with a devastating hook to your opponent's face.",
        damage=10,
        stamina_cost=4,
        stance=FightStance.AGGRESSIVE
    )

    define JAB = FightMove(
        name="Jab",
        description="Attack with a quick jab straight to the chin.",
        damage=5,
        stamina_cost=2,
        stance=FightStance.NEUTRAL
    )

    define TRASHTALK = FightMove(
        name="Trash Talk",
        description="Trash talk your opponent to shake their confidence.",
        damage=0,
        stamina_cost=2,
        stance=FightStance.NEUTRAL
    )

    define GUARDUP = FightMove(
        name="Guard Up",
        description="Trash talk your opponent to shake their confidence.",
        damage=0,
        stamina_cost=4,
        stance=FightStance.DEFENSE
    )

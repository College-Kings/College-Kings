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


    ## COPY THISE STEVE!
    define HOOK = FightMove(
        name="Hook",
        description="Blah Blah Blah",
        damage=5,
        stamina_cost=6,
        stance=FightStance.AGGRESSIVE
    )

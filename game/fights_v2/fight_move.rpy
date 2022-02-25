init offset = 1
init python:
    class BaseMove:
        def __init__(self, name, description, stamina_cost, ideal_stance, end_stance, effect="", stance_bonus=None):
            self.name = name
            self.description = description
            self.stamina_cost = stamina_cost
            self.ideal_stance = ideal_stance
            self.end_stance = end_stance
            self.effect = effect


    class FightMove(BaseMove):
        DAMAGE_DICT = {
            FightStance.AGGRESSIVE: 5,
            FightStance.DEFENSIVE: -5,
            FightStance.FORWARD: 0,
            FightStance.SOLID: 0
        }

        def __init__(self, name, description, damage, stamina_cost, ideal_stance, end_stance, effect="", images=None):
            BaseMove.__init__(self, name, description, stamina_cost, ideal_stance, end_stance, effect)
            self.damage = damage
            self.images = images

        def copy(self, images):
            return self.__class__(self.name, self.description, self.damage, self.stamina_cost, self.ideal_stance, self.end_stance, self.effect, images)


define BODY_HOOK = FightMove(
    name="Body Hook",
    description="A devastating attack to your opponent's body",
    damage=5,
    stamina_cost=2,
    ideal_stance=FightStance.FORWARD,
    end_stance=FightStance.SOLID,
    effect="|> Solid stance"
)

define JAB = FightMove(
    name="Jab",
    description="Attack with a quick jab straight to the chin.",
    damage=10,
    stamina_cost=3,
    ideal_stance=FightStance.AGGRESSIVE,
    end_stance=FightStance.FORWARD,
    effect="|> Forward Stance"
)

define HOOK = FightMove(
    name="Hook",
    description="A devastating attack to your opponent's head.",
    damage=15,
    stamina_cost=4,
    ideal_stance=FightStance.FORWARD,
    end_stance=FightStance.AGGRESSIVE,
    effect="|> Aggressive Stance"
)

define KICK = FightMove(
    name="Kick",
    description="A devastating attack to your opponent's body.",
    damage=20,
    stamina_cost=5,
    ideal_stance=FightStance.SOLID,
    end_stance=FightStance.FORWARD,
    effect="|> Forward Stance"
)

define END_TURN = BaseMove(
    name="End Turn",
    description="End your turn and retain up to 2 stamina",
    stamina_cost=0,
    ideal_stance=None,
    end_stance=None,
    effect="|> Keep Current Stance"
)

define TURTLE = BaseMove(
    name="Turtle",
    description="End turn and set stance to Defensive",
    stamina_cost=4,
    ideal_stance=FightStance.SOLID,
    end_stance=FightStance.DEFENSIVE,
    effect="|> Defensive Stance"
)

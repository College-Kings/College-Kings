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

        def __repr__(self):
            return self.name.upper().replace(' ', '_')


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


    class SpecialMove(FightMove):
        pass


define BODY_HOOK = FightMove(
    name="Body Hook",
    description="A devastating attack to your opponent's body",
    damage=1,
    stamina_cost=2,
    ideal_stance=FightStance.FORWARD,
    end_stance=FightStance.SOLID,
    effect="+20% Damage to next attack this turn"
)

define JAB = FightMove(
    name="Jab",
    description="Attack with a quick jab straight to the chin.",
    damage=2,
    stamina_cost=3,
    ideal_stance=FightStance.AGGRESSIVE,
    end_stance=FightStance.FORWARD,
    effect="Next Attack this turn ignores guard"
)

define HOOK = FightMove(
    name="Hook",
    description="A devastating attack to your opponent's head.",
    damage=3,
    stamina_cost=4,
    ideal_stance=FightStance.FORWARD,
    end_stance=FightStance.AGGRESSIVE,
    effect="Opp has -2 Stamina at the start of their next turn if not blocked [[Once per turn]]"
)

define KICK = FightMove(
    name="Kick",
    description="A devastating attack to your opponent's body.",
    damage=4,
    stamina_cost=5,
    ideal_stance=FightStance.SOLID,
    end_stance=FightStance.FORWARD,
    effect="+20% Damage if used with exactly 6 Stamina left"
)

define END_TURN = BaseMove(
    name="End Turn",
    description="End your turn and retain up to 2 stamina",
    stamina_cost=0,
    ideal_stance=None,
    end_stance=None,
    effect="Save up to 2 Stamina to use next turn."
)

define TURTLE = BaseMove(
    name="Turtle",
    description="End turn and set stance to Defensive",
    stamina_cost=4,
    ideal_stance=FightStance.SOLID,
    end_stance=FightStance.DEFENSIVE,
    effect="+1 Guard"
)

define HEADBUTT = SpecialMove(
    name="Headbutt",
    description="",
    damage=2,
    stamina_cost=2,
    ideal_stance=FightStance.AGGRESSIVE,
    end_stance=FightStance.SOLID,
    effect="If you used \"Turtle\" last turn, deal +30% more Damage"
)

define OVERHAND_PUNCH = SpecialMove(
    name="Overhand Punch",
    description="",
    damage=3,
    stamina_cost=3,
    ideal_stance=FightStance.FORWARD,
    end_stance=FightStance.AGGRESSIVE,
    effect="Breaks Guard and deals 100% Damage if it's at 30% or less"
)

define UPPERCUT = SpecialMove(
    name="Uppercut",
    description="",
    damage=4,
    stamina_cost=4,
    ideal_stance=FightStance.AGGRESSIVE,
    end_stance=FightStance.FORWARD,
    effect="If Opponents's Will is 20% or less, this attack deals +50% Damage"
)

define SUCKER_PUNCH = SpecialMove(
    name="Sucker Punch",
    description="",
    damage=5,
    stamina_cost=5,
    ideal_stance=FightStance.SOLID,
    end_stance=FightStance.FORWARD,
    effect="50% Damage bypasses Guard"
)
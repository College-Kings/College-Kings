init offset = 1
init python:
    class TurnMove:
        __metaclass__ = ABCMeta

        def __repr__(self):
            return "<{}>".format(self.__class__.__name__)


    class BaseAttack:
        __metaclass__ = ABCMeta

        DAMAGE_DICT = {
            FightStance.AGGRESSIVE: 5,
            FightStance.DEFENSIVE: -5,
            FightStance.FORWARD: 0,
            FightStance.SOLID: 0
        }

        def __repr__(self):
            return "<{}>".format(self.__class__.__name__)


    class SpecialMove:
        __metaclass__ = ABCMeta

        @abstractmethod
        def is_sensitive(self, target, attacker):
            pass

        def __repr__(self):
            return "<{}>".format(self.__class__.__name__)


    class EndTurn(TurnMove):
        def __init__(self):
            self.name = "End Turn"
            self.description = "End your turn and retain up to 2 stamina"
            self.stamina_cost = 0
            self.ideal_stance = None
            self.end_stance = None
            self.effect = "Save up to 2 Stamina to use next turn."

        def __repr__(self):
            return "<{}>".format(self.__class__.__name__)


    class Turtle(TurnMove):
        def __init__(self):
            self.name = "Turtle"
            self.description = "End turn and set stance to Defensive"
            self.stamina_cost = 4
            self.ideal_stance = FightStance.SOLID
            self.end_stance = FightStance.DEFENSIVE
            self.effect = "+1 Guard"

        def __repr__(self):
            return "<{}>".format(self.__class__.__name__)


    class BodyHook(BaseAttack):
        def __init__(self, images):
            self.images = images
            
            self.name = "Body Hook"
            self.description = "A devastating attack to your opponent's body"
            self.damage = 1
            self.stamina_cost = 2
            self.ideal_stance = FightStance.FORWARD
            self.end_stance = FightStance.SOLID
            self.effect = "+20% Damage to next attack this turn"


    class Jab(BaseAttack):
        def __init__(self, images):
            self.images = images
            
            self.name = "Jab"
            self.description = "Attack with a quick jab straight to the chin."
            self.damage = 2
            self.stamina_cost = 3
            self.ideal_stance = FightStance.AGGRESSIVE
            self.end_stance = FightStance.FORWARD
            self.effect = "Next Attack this turn ignores guard"


    class Hook(BaseAttack):
        def __init__(self, images):
            self.images = images
            
            self.name = "Hook"
            self.description = "A devastating attack to your opponent's head."
            self.damage = 3
            self.stamina_cost = 4
            self.ideal_stance = FightStance.FORWARD
            self.end_stance = FightStance.AGGRESSIVE
            self.effect = "Opp has -2 Stamina at the start of their next turn if not blocked [[Once per turn]]"


    class Kick(BaseAttack):
        def __init__(self, images):
            self.images = images

            self.name = "Kick"
            self.description = "A devastating attack to your opponent's body."
            self.damage = 4
            self.stamina_cost = 5
            self.ideal_stance = FightStance.SOLID
            self.end_stance = FightStance.FORWARD
            self.effect = "+20% Damage if used with exactly 6 Stamina left"

    
    class Headbutt(SpecialMove):
        def __init__(self, images):
            self.images = images

            self.name = "Headbutt"
            self.description = ""
            self.damage = 2
            self.stamina_cost = 2
            self.ideal_stance = FightStance.AGGRESSIVE
            self.end_stance = FightStance.SOLID
            self.effect = "If you used \"Turtle\" last turn, deal +30% more Damage"

        def is_sensitive(self, target, attacker):
            return fight.stats[target.name]["guards_broken"] >= 3


    class OverhandPunch(SpecialMove):
        def __init__(self, images):
            self.images = images

            self.name = "Overhand Punch"
            self.description = ""
            self.damage = 3
            self.stamina_cost = 3
            self.ideal_stance = FightStance.FORWARD
            self.end_stance = FightStance.AGGRESSIVE
            self.effect = "Breaks Guard and deals 100% Damage if it's at 30% or less"

        def is_sensitive(self, target, attacker):
            return fight.stats[attacker.name]["guards_broken"] >= 3


    class Uppercut(SpecialMove):
        def __init__(self, images):
            self.images = images

            self.name = "Uppercut"
            self.description = ""
            self.damage = 4
            self.stamina_cost = 4
            self.ideal_stance = FightStance.AGGRESSIVE
            self.end_stance = FightStance.FORWARD
            self.effect = "If Opponents's Will is 20% or less, this attack deals +50% Damage"

        def is_sensitive(self, target, attacker):
            return fight.stats[attacker.name]["damage_dealt"] >= 40


    class SuckerPunch(SpecialMove):
        def __init__(self, images):
            self.images = images

            self.name = "Sucker Punch"
            self.description = ""
            self.damage = 5
            self.stamina_cost = 5
            self.ideal_stance = FightStance.SOLID
            self.end_stance = FightStance.FORWARD
            self.effect = "50% Damage bypasses Guard"

        def is_sensitive(self, target, attacker):
            return fight.stats[attacker.name]["damage_taken"] >= 40
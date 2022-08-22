init 10 python:
    class TurnMove:
        def __init__(self):
            self.name = ""
            self.ideal_stance: Optional[FightStance] = None

        def __repr__(self):
            return f"<{self.__class__.__name__}>"


    class BaseAttack:
        DAMAGE_DICT = {
            FightStance.AGGRESSIVE: 5,
            FightStance.DEFENSIVE: -5,
            FightStance.FORWARD: 0,
            FightStance.SOLID: 0,
        }

        def __init__(self):
            self.name = ""
            self.ideal_stance: Optional[FightStance] = None

        def __repr__(self):
            return f"<{self.__class__.__name__}>"


    class SpecialMove(ABC):
        def __init__(self):
            self.name = ""
            self.ideal_stance: Optional[FightStance] = None

        @abstractmethod
        def is_sensitive(
            self, fight: "Fight", target: "BasePlayer", attacker: "BasePlayer"
        ) -> bool:
            ...

        @abstractmethod
        def check_level_1_stance_bonus(
            self, fight: "Fight", target: "BasePlayer", attacker: "BasePlayer"
        ) -> bool:
            ...

        @abstractmethod
        def check_level_2_stance_bonus(
            self, fight: "Fight", target: "BasePlayer", attacker: "BasePlayer"
        ) -> bool:
            ...

        @abstractmethod
        def check_level_3_stance_bonus(
            self, fight: "Fight", target: "BasePlayer", attacker: "BasePlayer"
        ) -> bool:
            ...

        def __repr__(self):
            return f"<{self.__class__.__name__}>"


    FightMoves = Union[TurnMove, BaseAttack, SpecialMove]


    class EndTurn(TurnMove):
        def __init__(self):
            self.name = "End Turn"
            self.description = "End your turn and retain up to 2 stamina"
            self.stamina_cost = 0
            self.ideal_stance = None
            self.end_stance = None
            self.effect = "Save up to 2 Stamina to use next turn."


    class Turtle(TurnMove):
        def __init__(self):
            self.name = "Turtle"
            self.description = "End turn and set stance to Defensive"
            self.stamina_cost = 4
            self.ideal_stance = FightStance.SOLID
            self.end_stance = FightStance.DEFENSIVE
            self.effect = "+1 Guard"


    class BodyHook(BaseAttack):
        def __init__(self, images: dict[str, str]):
            self.images = images

            self.name = "Body Hook"
            self.description = "A devastating attack to your opponent's body"
            self.damage = 1
            self.stamina_cost = 2
            self.ideal_stance = FightStance.FORWARD
            self.end_stance = FightStance.SOLID
            self.effect = "+20% Damage to next attack this turn"


    class Jab(BaseAttack):
        def __init__(self, images: dict[str, str]):
            self.images = images

            self.name = "Jab"
            self.description = "Attack with a quick jab straight to the chin."
            self.damage = 2
            self.stamina_cost = 3
            self.ideal_stance = FightStance.AGGRESSIVE
            self.end_stance = FightStance.FORWARD
            self.effect = "Next Attack this turn ignores guard"


    class Hook(BaseAttack):
        def __init__(self, images: dict[str, str]):
            self.images = images

            self.name = "Hook"
            self.description = "A devastating attack to your opponent's head."
            self.damage = 3
            self.stamina_cost = 4
            self.ideal_stance = FightStance.FORWARD
            self.end_stance = FightStance.AGGRESSIVE
            self.effect = "Opp has -2 Stamina at the start of their next turn if not blocked [[Once per turn]]"


    class Kick(BaseAttack):
        def __init__(self, images: dict[str, str]):
            self.images = images

            self.name = "Kick"
            self.description = "A devastating attack to your opponent's body."
            self.damage = 4
            self.stamina_cost = 5
            self.ideal_stance = FightStance.SOLID
            self.end_stance = FightStance.FORWARD
            self.effect = "+20% Damage if used with exactly 5 Stamina left"


    class Headbutt(SpecialMove):
        def __init__(self, images: dict[str, str]):
            self.images = images

            self.name = "Headbutt"
            self.description = ""
            self.damage = 2
            self.stamina_cost = 2
            self.ideal_stance = FightStance.AGGRESSIVE
            self.end_stance = FightStance.SOLID
            self.effect = 'If you used "Turtle" last turn, deal +30% more Damage'

        def is_sensitive(self, fight: Fight, target: BasePlayer, attacker: BasePlayer):
            return fight.stats[target.name]["guards_broken"] >= 3

        def check_level_1_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ):
            return isinstance(fight.move_list[-2][attacker.name][-1], Turtle)

        def check_level_2_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ):
            return target.guard == 0

        def check_level_3_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ):
            return not fight.move_list[-1][attacker.name]


    class OverhandPunch(SpecialMove):
        def __init__(self, images: dict[str, str]):
            self.images = images

            self.name = "Overhand Punch"
            self.description = ""
            self.damage = 3
            self.stamina_cost = 3
            self.ideal_stance = FightStance.FORWARD
            self.end_stance = FightStance.AGGRESSIVE
            self.effect = "Breaks Guard and deals 100% Damage if it's at 30% or less"

        def is_sensitive(self, fight: Fight, target: BasePlayer, attacker: BasePlayer):
            return fight.stats[attacker.name]["guards_broken"] >= 3

        def check_level_1_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ) -> bool:
            return target.guard <= BasePlayer.MAX_GUARD * 0.3

        def check_level_2_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ) -> bool:
            raise NotImplementedError()

        def check_level_3_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ) -> bool:
            raise NotImplementedError()


    class Uppercut(SpecialMove):
        def __init__(self, images: dict[str, str]):
            self.images = images

            self.name = "Uppercut"
            self.description = ""
            self.damage = 4
            self.stamina_cost = 4
            self.ideal_stance = FightStance.AGGRESSIVE
            self.end_stance = FightStance.FORWARD
            self.effect = (
                "If Opponents's Will is 20% or less, this attack deals +50% Damage"
            )

        def is_sensitive(self, fight: Fight, target: BasePlayer, attacker: BasePlayer):
            return fight.stats[attacker.name]["damage_dealt"] >= 40

        def check_level_1_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ):
            return target.health <= target.max_health * 0.2

        def check_level_2_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ) -> bool:
            raise NotImplementedError()

        def check_level_3_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ):
            return not fight.move_list[-1][attacker.name]


    class SuckerPunch(SpecialMove):
        def __init__(self, images: dict[str, str]):
            self.images = images

            self.name = "Sucker Punch"
            self.description = ""
            self.damage = 5
            self.stamina_cost = 5
            self.ideal_stance = FightStance.SOLID
            self.end_stance = FightStance.FORWARD
            self.effect = "50% Damage bypasses Guard"

        def is_sensitive(self, fight: Fight, target: BasePlayer, attacker: BasePlayer):
            return fight.stats[attacker.name]["damage_taken"] >= 40

        def check_level_1_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ):
            return True

        def check_level_2_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ):
            return True

        def check_level_3_stance_bonus(
            self, fight: Fight, target: BasePlayer, attacker: BasePlayer
        ):
            return True

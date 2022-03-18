init python:
    class FightQuirk:
        __metaclass__ = ABCMeta

        quirks = []

        @abstractmethod
        def effect(self):
            pass


    class SeeingRed(FightQuirk):
        def __init__(self, name):
            self.name = name

        def effect(self):
            pass


    class TheGreatEqualizer(FightQuirk):
        def __init__(self, name):
            self.name = name

        def effect(self, target, attacker):
            if target.health > attacker.health:
                return 0.8
            elif target.health < attacker.health:
                return 1.2
            else:
                return 1.0

    
    class InTheZone(FightQuirk):
        def __init__(self, name):
            self.name = name

        def effect(self, attacker, move):
            if attacker.stance == move.ideal_stance:
                return 1.2
            else:
                return 0.8

    
    class Backlash(FightQuirk):
        def __init__(self, name):
            self.name = name

        def effect(self):
            pass


    class DoubleTime(FightQuirk):
        def __init__(self, name):
            self.name = name

        def effect(self):
            pass

    
    class AllIn(FightQuirk):
        def __init__(self, name):
            self.name = name

        def effect(self):
            pass
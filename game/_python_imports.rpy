python early:
    import os
    import random
    from enum import Enum

    class SmartEnum(Enum):
        def __lt__(self, other):
            if not isinstance(other, self.__class__):
                raise TypeError("{} must be of type {}.".format(other, self.__class__.__name__))

            return self.value < other.value

        def __le__(self, other):
            if not isinstance(other, self.__class__):
                raise TypeError("{} must be of type {}.".format(other, self.__class__.__name__))

            return self.value <= other.value

        def __gt__(self, other):
            if not isinstance(other, self.__class__):
                raise TypeError("{} must be of type {}.".format(other, self.__class__.__name__))

            return self.value > other.value

        def __ge__(self, other):
            if not isinstance(other, self.__class__):
                raise TypeError("{} must be of type {}.".format(other, self.__class__.__name__))

            return self.value >= other.value


    def weighted_choice(choices, size=1, probability=None):
        probability = tuple(int(round(x, 2) * 100) for x in probability)

        weighted_choices = []
        for c, p in zip(choices, probability):
            weighted_choices += [c] * p

        return renpy.random.choice(weighted_choices)

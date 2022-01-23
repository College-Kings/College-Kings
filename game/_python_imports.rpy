python early:
    import os
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
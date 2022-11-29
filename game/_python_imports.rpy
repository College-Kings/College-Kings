python early:
    import datetime
    import math
    import os
    import random
    import re
    import requests
    from abc import ABC, abstractmethod
    from dataclasses import dataclass
    from enum import Enum
    from typing import Any, Callable, ClassVar, Optional, Union


    class SmartEnum(Enum):
        """
        Extention of the enum class that adds comparison opperations
        """

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

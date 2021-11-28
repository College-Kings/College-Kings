init python:
    class PlayableCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self, profile_picture):
            self.profile_picture = profile_picture

            self.money = 0
            self.inventory = Inventory()

            self.quirks = {
                "animal_lover": False,
                "boomer": False,
                "hardass": False,
                "pop_culture": False,
                "prankster": False,
                "quirk_sensitive_stomach": False
                "quirk_tough_tummy": False,
                "quirk_hunter": False,
                "quirk_not_hunter": False,
            }

            self.relationships = set()
            self.girlfriends = set()

        def add_item(self, item):
            if item.cost > self.money:
                raise UnhandledTranscribingError("{} price is higher then user money".format(item.name))

            self.inventory.items.append(item)

        def has_item(self, item):
            return (item in self.inventory.items)


init offset = 1

default mc = PlayableCharacter(profile_pictures[0])

default quirk_sensitive_stomach = False
default quirk_tough_tummy = False
default quirk_hunter = False
default quirk_not_hunter = False
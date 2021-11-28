init python:
    class PlayableCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self, profile_picture):
            self.profile_picture = profile_picture

            self.money = 0
            self.inventory = Inventory()

            self.quirks = {
                "animal_lover": 0,
                "boomer": 0,
                "hardass": 0,
                "pop_culture": 0,
                "prankster": 0
                "quirk_sensitive_stomach": 0
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
default quirk_hunter = False
init python:
    class PlayableCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self, profile_picture):
            self.profile_picture = profile_picture

            self.username = self.name
            self.money = 0
            self.inventory = Inventory()

            self.quirks = {
                "animal_lover": False,
                "boomer": False,
                "hardass": False,
                "pop_culture": False,
                "prankster": False,
                "sensitive_stomach": False,
                "tough_tummy": False,
                "hunter": False,
                "not_hunter": False,
            }

            self.relationships = set()
            self.girlfriends = set()

        @property
        def name(self):
            return store.name

        def add_item(self, item):
            if item.cost > self.money:
                raise UnhandledTranscribingError("{} price is higher then user money".format(item.name))

            self.inventory.items.append(item)

        def has_item(self, item):
            return (item in self.inventory.items)


init offset = 1

default mc = PlayableCharacter(profile_pictures[0])
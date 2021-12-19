init python:
    class PlayableCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self, profile_picture):
            self.profile_picture = profile_picture

            self.username = self.name
            self.money = 0
            self.inventory = Inventory()

            self.relationships = set()
            self.girlfriends = set()

        @property
        def name(self):
            return store.name

        def has_item(self, item):
            return (item in self.inventory)


init offset = 1

default mc = PlayableCharacter(profile_pictures[0])
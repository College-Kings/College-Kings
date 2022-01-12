init python:
    class PlayableCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self):
            self.username = self.name
            self.money = 0
            self.inventory = Inventory()
            self.detective = None

            self.relationships = set()
            self.girlfriends = set()

        @property
        def name(self):
            return store.name

        @property
        def profile_picture(self):
            return profile_pictures[0]

        def has_item(self, item):
            return (item in self.inventory)


init offset = 1

default mc = PlayableCharacter()
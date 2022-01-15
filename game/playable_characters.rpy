init python:
    class PlayableCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self):
            self.username = self.name
            self.money = 0
            self.inventory = Inventory()
            self.detective = None
            self._profile_picture = profile_pictures[0]

            self.relationships = set()
            self.girlfriends = set()

        @property
        def name(self):
            return store.name

        @property
        def profile_picture(self):
            return profile_pictures[0]

        @profile_picture.setter
        def profile_picture(self, value):
            self._profile_picture = value

        def __after_load__(self):
            attrs = vars(self).copy()

            self.__init__()

            for var, value in attrs.items():
                setattr(self, var, value)
                

        def has_item(self, item):
            return (item in self.inventory)


init offset = 1

default mc = PlayableCharacter()
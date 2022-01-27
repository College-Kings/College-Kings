init python:
    class PlayableCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self, username=None):
            if username is None: self.username = self.name
            else: self.username = username

            self._profile_picture = profile_pictures[0]
            self._fighter = None

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

        @profile_picture.setter
        def profile_picture(self, value):
            self._profile_picture = value

        @property
        def fighter(self):
            return self._fighter
        
        @fighter.setter
        def fighter(self, value):
            self._fighter = value

        def __after_load__(self):
            attrs = vars(self).copy()

            self.__init__()

            for var, value in attrs.items():
                try: setattr(self, var, value)
                except AttributeError: continue
                
        def has_item(self, item):
            return (item in self.inventory)

init 1:
    default mc = PlayableCharacter()
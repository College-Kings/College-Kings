init python:
    class PlayableCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self, username=None):
            if username is None: self.username = self.name
            else: self.username = username

            self._profile_pictures = None
            self._fighter = None

            self.profile_picture = self.profile_pictures[0]
            self.money = 0
            self.inventory = Inventory()
            self.detective = None
            self.relationships = set()
            self.girlfriends = set()

        @property
        def name(self):
            return store.name
                
        @property
        def profile_pictures(self):
            if self._profile_pictures is not None:
                return self._profile_pictures

            DIRECTORY = os.path.join(config.basedir, "game", "images", "nonplayable_characters", "profile_pictures")

            self._profile_pictures = []
            for root, dirs, files in os.walk(DIRECTORY):
                self._profile_pictures.extend(os.path.join(root, file).replace(os.sep, '/') for file in files if file.startswith("mc"))

            return self._profile_pictures

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
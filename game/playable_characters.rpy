init python:
    class PlayableCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self, username: Optional[str] = None):
            self._username = username
            self._profile_picture = None
            self._fighter = None

            self.money = 0
            self.inventory = Inventory()
            self.detective = None
            self.relationships: set[NonPlayableCharacter] = set()
            self.girlfriends: set[NonPlayableCharacter] = set()
            self.frat = None

        @property
        def name(self):
            return store.name

        @property
        def username(self):
            try:
                if self._username is not None:
                    return self._username
            except AttributeError:
                pass

            return self.name

        @username.setter
        def username(self, value: str):
            self._username = value

        @property
        def profile_picture(self):
            if (
                (not hasattr(self, "_profile_picture"))
                or (self._profile_picture is None)
                or (not os.path.exists(os.path.join(config.gamedir, self._profile_picture)))
            ):
                return self.profile_pictures[0]

            return self._profile_picture

        @profile_picture.setter
        def profile_picture(self, value: str):
            self._profile_picture = value

        @property
        def profile_pictures(self):
            return [
                file
                for file in renpy.list_files()
                if file.startswith(f"images/characters/mc/")
            ]

        @property
        def fighter(self):
            return self._fighter

        @fighter.setter
        def fighter(self, value: BasePlayer):
            self._fighter = value

        def has_item(self, item: Item):
            return item in self.inventory

init 1:
    default mc = PlayableCharacter()

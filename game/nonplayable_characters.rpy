init python:
    class Relationship(Enum):
        FRIEND = 0
        FWB = 1
        GIRLFRIEND = 2
        AWKWARD = 3
        BRO = 4
        DATE = 5
        FORGIVE = 6
        FUN = 7
        HANGOUT = 8
        KISS = 9
        LIKES = 10
        LOYAL = 11
        MAD = 12
        PUBLIC = 13
        SAD = 14
        STRIKES = 15
        SUSPICIOUS = 16
        TAMED = 17
        TRUST = 18


    class NonPlayableCharacter:
        """
        Custom character class primarily used for managing all the character specific function of the game.

        Attributes:
            name (str): The display name for the character
            profile_picture (str): The file name for the characters profile picture, located in "images/nonplayable_characters/profile_pictures/"
        """

        def __init__(self, name):
            self.name = name
            self.name = name.replace(" ", "_")

            self._messenger = None
            self._simplr = None

            self.stats = {
                "Competitive": None,
                "Vindictive": [],
                "Talkative": None
            }

            self.points = 0
            self._relationship = Relationship.FRIEND

        @property
        def relationship(self):
            try: return self._relationship
            except AttributeError: return Relationship.FRIEND

        @relationship.setter
        def relationship(self, value):
            self._relationship = value
            
            if value == Relationship.GIRLFRIEND:
                mc.relationships.add(self)
                mc.girlfriends.add(self)

            elif value == Relationship.FWB:
                try: mc.relationships.remove(self)
                except KeyError: pass
                mc.relationships.add(self)

            else:
                try:
                    mc.relationships.remove(self)
                    mc.girlfriends.remove(self)
                except KeyError: pass

        @property
        def messenger(self):
            if self._messenger is None:
                self._messenger = Contact(self.name, self.profile_picture)
                messenger.contacts.append(self.messenger)
            return self._messenger

        @messenger.setter
        def messenger(self, value):
            self._messenger = value

        @property
        def simplr(self):
            if self._simplr is None:
                self._simplr = SimplrContact(self.name)
                simplr_pendingContacts.append(self._simplr)
            return self._simplr

        @simplr.setter
        def simplr(self, value):
            self._simplr = value

        @property
        def profile_picture(self):
            return "images/nonplayable_characters/profile_pictures/{}.webp".format(self.name.lower())

        def kill(self):
            # Check Competitive stat
            if self.stats["Competitive"] and len(v12s7_killList) < 3:
                self.points -= 1
            elif not self.stats["Competitive"] and len(v12s7_killList) < 3:
                self.points += 1

            # Check Vindictive stat
            for character in self.stats["Vindictive"]:
                if character in v12s7_killList:
                    self.points += 1
                else:
                    self.points -= 1

            # Check Talkative stat
            if self.stats["Talkative"] and self in v12s7_endtalkList:
                self.points += 1
            elif self.stats["Talkative"]:
                self.points -= 1
            elif not self.stats["Talkative"] and self in v12s7_endtalkList:
                self.points -= 1

            # Add character to kill list
            if self != cameron: # Except Cameron, because he's not playing
                v12s7_killList.add(self)

        def reset_points(self):
            self.points = 0

default chloe = NonPlayableCharacter("Chloe")
default amber = NonPlayableCharacter("Amber")
default penelope = NonPlayableCharacter("Penelope")
default riley = NonPlayableCharacter("Riley")
default lindsey = NonPlayableCharacter("Lindsey")
default lauren = NonPlayableCharacter("Lauren")
default emily = NonPlayableCharacter("Emily")
default ms_rose = NonPlayableCharacter("Ms Rose")
default nora = NonPlayableCharacter("Nora")
default aubrey = NonPlayableCharacter("Aubrey")
default ryan = NonPlayableCharacter("Ryan")
default imre = NonPlayableCharacter("Imre")
default chris = NonPlayableCharacter("Chris")
default charli = NonPlayableCharacter("Charli")
default cameron = NonPlayableCharacter("Cameron")
default josh = NonPlayableCharacter("Josh")
default julia = NonPlayableCharacter("Julia")
default evelyn = NonPlayableCharacter("Evelyn")
default autumn = NonPlayableCharacter("Autumn")
default sebastian = NonPlayableCharacter("Sebastian")
default grayson = NonPlayableCharacter("Grayson")
default jenny = NonPlayableCharacter("Jenny")
default mr_lee = NonPlayableCharacter("Mr Lee")

default beth = NonPlayableCharacter("Beth")
default iris = NonPlayableCharacter("Iris")
default samantha = NonPlayableCharacter("Samantha")
default emmy = NonPlayableCharacter("Emmy")

default wolf = NonPlayableCharacter("Wolf")
default trainer = NonPlayableCharacter("Trainer")
default buyer = NonPlayableCharacter("Buyer")

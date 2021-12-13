init python:
    class Relationship(Enum):
        FRIEND = 0
        HANGOUT = 1
        DATE = 2
        LIKES = 3
        KISS = 4
        FWB = 5
        TAMED = 6
        GIRLFRIEND = 7
        AWKWARD = 10
        BRO = 11
        FORGIVE = 12
        FUN = 13
        LOYAL = 14
        MAD = 15
        TRUST = 16

    class NonPlayableCharacter:
        """
        Custom character class primarily used for managing all the character specific function of the game.

        Attributes:
            name (str): The display name for the character
            profile_picture (str): The file name for the characters profile picture, located in "images/nonplayable_characters/profile_pictures/"
        """

        def __init__(self, name, username=None):
            self.name = name
            self.name = name.replace(" ", "_")
            
            if username is None:
                self._username = name
            else:
                self._username = username

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
        def username(self):
            try:
                if self._username is not None:
                    return self._username
            except AttributeError: pass

            return self.name

        @username.setter
        def username(self, value):
            self._username = value

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

        def __after_load__(self):
            try: messenger = self._messenger
            except AttributeError: messenger = None
            try: simplr = self._simplr
            except AttributeError: simplr = None
            try: stats = self.stats
            except AttributeError: stats = { "Competitive": None, "Vindictive": [], "Talkative": None }
            try: points = self.points
            except AttributeError: points = 0
            try: relationship = self._relationship
            except AttributeError: relationship = Relationship.FRIEND

            self.__init__(self.name, self.username)

            self._messenger = messenger
            self._simplr = simplr
            self.stats = stats
            self.points = points
            self._relationship = relationship

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

default chloe = NonPlayableCharacter("Chloe", "Chloe101")
default amber = NonPlayableCharacter("Amber", "Amber_xx")
default penelope = NonPlayableCharacter("Penelope", "Penelopeeps")
default riley = NonPlayableCharacter("Riley", "RileyReads")
default lindsey = NonPlayableCharacter("Lindsey", "LindsLou")
default lauren = NonPlayableCharacter("Lauren", "LoLoLauren")
default emily = NonPlayableCharacter("Emily", "emilyyyy")
default ms_rose = NonPlayableCharacter("Ms Rose")
default nora = NonPlayableCharacter("Nora", "Nora_12")
default aubrey = NonPlayableCharacter("Aubrey", "Aubs123")
default ryan = NonPlayableCharacter("Ryan", "Ryanator")
default imre = NonPlayableCharacter("Imre", "BadBoyImre")
default chris = NonPlayableCharacter("Chris", "Chriscuit")
default charli = NonPlayableCharacter("Charli", "CharliAndTheCockFactory")
default cameron = NonPlayableCharacter("Cameron", "Cameroon")
default josh = NonPlayableCharacter("Josh", "Josh80085")
default julia = NonPlayableCharacter("Julia")
default evelyn = NonPlayableCharacter("Evelyn") #Relationship progression: DATE, LIKES, KISS
default autumn = NonPlayableCharacter("Autumn", "Its_Fall")
default sebastian = NonPlayableCharacter("Sebastian", "Big Seb")
default grayson = NonPlayableCharacter("Grayson", "G-rayson")
default jenny = NonPlayableCharacter("Jenny")
default mr_lee = NonPlayableCharacter("Mr Lee")

default adam = NonPlayableCharacter("Adam", "A.D.A.M.")
default mason = NonPlayableCharacter("Mason", "Mason_Mas")
default elijah = NonPlayableCharacter("Elijah", "Elijah_Woods")
default kim = NonPlayableCharacter("Kim", "KimPlausible")
default caleb = NonPlayableCharacter("Caleb", "Aleb")
default parker = NonPlayableCharacter("Parker")
default kai = NonPlayableCharacter("Kai", "KaiCriesWith2Ply")
default aaron = NonPlayableCharacter("Aaron", "DoubleARon")
default naomi = NonPlayableCharacter("Naomi", "NaomiXMarie")
default lews_official = NonPlayableCharacter("LewsOfficial")

default beth = NonPlayableCharacter("Beth")
default iris = NonPlayableCharacter("Iris")
default samantha = NonPlayableCharacter("Samantha", "SamFromSpaceJam")
default emmy = NonPlayableCharacter("Emmy")
default aryssa = NonPlayableCharacter("Aryssa") #Relationship progression: LIKES
defauly kourtney = NonPlayableCharacter("Kourtney") #Relationship progression: LIKES

default wolf = NonPlayableCharacter("Wolf")
default trainer = NonPlayableCharacter("Trainer")
default buyer = NonPlayableCharacter("Buyer")
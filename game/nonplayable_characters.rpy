init python:
    class Relationship(Enum):
        MAD = -4
        THREATEN = -3
        MAKEFUN = -2
        AWKWARD = -1
        FRIEND = 0
        MOVE = 1
        DATE = 2
        LIKES = 3
        TRUST = 4
        BRO = 5
        KISS = 6
        FWB = 7
        LOYAL = 8
        TAMED = 9
        GIRLFRIEND = 10

        def __lt__(self, other):
            if not isinstance(other, Relationship):
                raise TypeError("Relation {} must be of type Relationship.".format(other))

            return self.value < other.value

        def __le__(self, other):
            if not isinstance(other, Relationship):
                raise TypeError("Relation {} must be of type Relationship.".format(other))

            return self.value <= other.value

        def __gt__(self, other):
            if not isinstance(other, Relationship):
                raise TypeError("Relation {} must be of type Relationship".format(other))

            return self.value > other.value

        def __ge__(self, other):
            if not isinstance(other, Relationship):
                raise TypeError("Relation {} must be of type Relationship".format(other))

            return self.value >= other.value


    class NonPlayableCharacter:
        """
        Custom character class primarily used for managing all the character specific function of the game.

        Attributes:
            name (str): The display name for the character
            profile_picture (str): The file name for the characters profile picture, located in "images/nonplayable_characters/profile_pictures/"
        """

        Characters = {}

        def __init__(self, name, username=None):
            self.name = name
            self._username = name if username is None else username

            self._messenger = None
            self._simplr = None

            self.stats = {
                "Competitive": None,
                "Vindictive": [],
                "Talkative": None
            }

            self.points = 0
            self._relationship = Relationship.FRIEND

            NonPlayableCharacter.Characters[name] = self

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
            if not isinstance(value, Relationship):
                raise TypeError("{} must be of type Relationship".format(value))

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
            try: self._messenger
            except AttributeError: self._messenger = None

            if self._messenger is None:
                self._messenger = Contact(self.name, self.profile_picture)
                messenger.contacts.append(self.messenger)
            return self._messenger

        @messenger.setter
        def messenger(self, value):
            self._messenger = value

        @property
        def simplr(self):
            try: self._simplr
            except AttributeError: self._simplr = None

            if self._simplr is None:
                self._simplr = SimplrContact(self.name)
                simplr_pendingContacts.append(self._simplr)
            return self._simplr

        @simplr.setter
        def simplr(self, value):
            self._simplr = value

        @property
        def profile_picture(self):
            return "images/nonplayable_characters/profile_pictures/{}.webp".format(self.name.replace(' ', '_').lower())

        def __after_load__(self):
            attrs = vars(self).copy()

            self.__init__(self.name)

            for var, value in attrs.items():
                try: setattr(self, var, value)
                except AttributeError: continue

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


    def nonplayable_character_setup():
        beth.simplr
        iris.simplr
        samantha.simplr
        emmy.simplr


default aaron = NonPlayableCharacter("Aaron", "DoubleARon")
default adam = NonPlayableCharacter("Adam", "A.D.A.M.")
default amber = NonPlayableCharacter("Amber", "Amber_xx") # Relationship progression: FRIEND, KISS, FWB
default aryssa = NonPlayableCharacter("Aryssa") # Relationship progression: FRIEND, LIKES
default aubrey = NonPlayableCharacter("Aubrey", "Aubs123") # Relationship progression: MAD, FRIEND, FWB, TAMED
default autumn = NonPlayableCharacter("Autumn", "Its_Fall") # Relationship progression: MAD, FRIEND, KISS
default beth = NonPlayableCharacter("Beth")
default buyer = NonPlayableCharacter("Buyer")
default caleb = NonPlayableCharacter("Caleb", "Aleb")
default cameron = NonPlayableCharacter("Cameron", "Cameroon") # Relationship progression: FRIEND, BRO
default candy = NonPlayableCharacter("Candy") # Relationship progression: FRIEND, LIKES, FWB
default charli = NonPlayableCharacter("Charli", "CharliAndTheCockFactory")
default chloe = NonPlayableCharacter("Chloe", "Chloe101") # Relationship progression: MAD, FRIEND, FWB, GIRLFRIEND
default chris = NonPlayableCharacter("Chris", "Chriscuit") # Relationshp progression: MAD, FRIEND
default dean = NonPlayableCharacter("Dean")
default elijah = NonPlayableCharacter("Elijah", "Elijah_Woods") # Relationship progression: MAKEFUN, FRIEND
default emily = NonPlayableCharacter("Emily", "emilyyyy") # Relationship progression: FRIEND, FWB
default emmy = NonPlayableCharacter("Emmy") # Relationship progression: FRIEND, LIKES, FWB
default evelyn = NonPlayableCharacter("Evelyn") # Relationship progression: FRIEND, MOVE, DATE, LIKES, KISS
default grayson = NonPlayableCharacter("Grayson", "G-rayson")
default imre = NonPlayableCharacter("Imre", "BadBoyImre") # Relationship progression: MAD, FRIEND
default iris = NonPlayableCharacter("Iris")
default jenny = NonPlayableCharacter("Jenny") # Relationship progression: AWKWARD, FRIEND, FWB
default josh = NonPlayableCharacter("Josh", "Josh80085") # Relationship progression: MAD, FRIEND
default julia = NonPlayableCharacter("Julia")
default kai = NonPlayableCharacter("Kai", "KaiCriesWith2Ply")
default kim = NonPlayableCharacter("Kim", "KimPlausible")
default kourtney = NonPlayableCharacter("Kourtney") # Relationship progression: FRIEND, LIKES
default lauren = NonPlayableCharacter("Lauren", "LoLoLauren") # Relationship progression: MAD, FRIEND, MOVE, KISS, GIRLFRIEND
default lews_official = NonPlayableCharacter("LewsOfficial")
default lindsey = NonPlayableCharacter("Lindsey", "LindsLou") # Relationship progression: FRIEND, KISS, FWB
default mason = NonPlayableCharacter("Mason", "Mason_Mas")
default mr_lee = NonPlayableCharacter("Mr Lee")
default ms_rose = NonPlayableCharacter("Ms Rose") # Relationship progression: THREATEN, FRIEND, KISS, FWB
default naomi = NonPlayableCharacter("Naomi", "NaomiXMarie") # Relationship progression: FRIEND, FWB
default nora = NonPlayableCharacter("Nora", "Nora_12") # Relationship progression: MAD, FRIEND, MOVE, LIKES, FWB
default parker = NonPlayableCharacter("Parker")
default penelope = NonPlayableCharacter("Penelope", "Penelopeeps") # Relationship progression: FRIEND, LIKES, LOYAL
default riley = NonPlayableCharacter("Riley", "RileyReads") # Relationship progression: FRIEND, MOVE, LIKES, FWB, LOYAL
default ryan = NonPlayableCharacter("Ryan", "Ryanator")
default samantha = NonPlayableCharacter("Samantha", "SamFromSpaceJam") # Relationship progression: FRIEND, MOVE, FWB
default satin = NonPlayableCharacter("Satin") # Relationship progression: FRIEND, FWB
default sebastian = NonPlayableCharacter("Sebastian", "Big Seb")
default trainer = NonPlayableCharacter("Trainer")
default wolf = NonPlayableCharacter("Wolf")

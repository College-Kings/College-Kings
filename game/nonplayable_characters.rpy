init python:
    class Frat(Enum):
        APES = 0
        WOLVES = 1


    class Relationship(SmartEnum):
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


    class NonPlayableCharacter:
        """
        Custom character class primarily used for managing all the character specific function of the game.

        Attributes:
            name (str): The display name for the character
            profile_picture (str): The file name for the characters profile picture, located in "images/characters/"
        """

        characters: dict[str, "NonPlayableCharacter"] = {}

        def __init__(self, name: str, username: Optional[str] = None):
            self.name = name
            self._username = name if username is None else username

            self._messenger = None
            self._simplr = None
            self._relationship = Relationship.FRIEND
            self._fighter = None

            self.points = 0
            self.stats = {
                "Competitive": None,
                "Vindictive": [],
                "Talkative": None
            }

            NonPlayableCharacter.characters[name] = self

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
        def relationship(self):
            try:
                return self._relationship
            except AttributeError:
                return Relationship.FRIEND

        @relationship.setter
        def relationship(self, value: Relationship):
            if not isinstance(value, Relationship):
                raise TypeError(f"{value} must be of type Relationship")

            self._relationship = value

            if value == Relationship.GIRLFRIEND:
                mc.relationships.add(self)
                mc.girlfriends.add(self)

            elif value == Relationship.FWB:
                try:
                    mc.relationships.remove(self)
                except KeyError:
                    pass
                mc.relationships.add(self)

            else:
                try:
                    mc.relationships.remove(self)
                    mc.girlfriends.remove(self)
                except KeyError:
                    pass

        @property
        def messenger(self):
            try:
                self._messenger
            except AttributeError:
                self._messenger = None

            if self._messenger is None:
                self._messenger = Contact(self)
                messenger.contacts.append(self.messenger)
            return self._messenger

        @messenger.setter
        def messenger(self, value: "Contact"):
            self._messenger = value

        @property
        def simplr(self):
            try: self._simplr
            except AttributeError: self._simplr = None

            if self._simplr is None:
                self._simplr = SimplrContact(self)
                simplr_app.pending_contacts.append(self._simplr)
            return self._simplr

        @simplr.setter
        def simplr(self, value):
            self._simplr = value

        @property
        def fighter(self):
            return self._fighter

        @fighter.setter
        def fighter(self, value: BasePlayer):
            self._fighter = value

        @property
        def profile_picture(self):
            try:
                return self.profile_pictures[0]
            except IndexError:
                raise IndexError(f"{self.name} has no profile pictures")

        @property
        def profile_pictures(self):
            if self.name.lower() == "ms_rose":
                self.name = "Ms Rose"

            return [
                file
                for file in renpy.list_files()
                if file.startswith(f"images/characters/{self.name.lower()}/")
            ]

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

        chloe.stats["Competitive"] = True
        chloe.stats["Vindictive"] = [nora]

        amber.stats["Competitive"] = amber.stats["Talkative"] = True
        amber.stats["Vindictive"] = [riley]

        riley.stats["Competitive"] = riley.stats["Talkative"] = True

        lindsey.stats["Competitive"] = lindsey.stats["Talkative"] = True
        lindsey.stats["Vindictive"] = [chloe]

        emily.stats["Talkative"] = False

        nora.stats["Talkative"] = True
        nora.stats["Vindictive"] = [chris, chloe]

        aubrey.stats["Competitive"] = True

        ryan.stats["Vindictive"] = [imre]

        imre.stats["Competitive"] = False
        imre.stats["Vindictive"] = [ryan]

        chris.stats["Competitive"] = chris.stats["Talkative"] = False

        charli.stats["Competitive"] = True
        charli.stats["Talkative"] = False

        josh.stats["Competitive"] = True


default aaron = NonPlayableCharacter(_("Aaron"), _("DoubleARon"))
default adam = NonPlayableCharacter(_("Adam"), _("A.D.A.M."))
default amber = NonPlayableCharacter(_("Amber"), _("Amber_xx")) # Relationship progression: FRIEND, KISS, FWB
default aryssa = NonPlayableCharacter(_("Aryssa")) # Relationship progression: FRIEND, LIKES
default aubrey = NonPlayableCharacter(_("Aubrey"), _("Aubs123")) # Relationship progression: MAD, FRIEND, FWB, TAMED
default autumn = NonPlayableCharacter(_("Autumn"), _("Its_Fall")) # Relationship progression: MAD, FRIEND, KISS
default beth = NonPlayableCharacter(_("Beth"))
default buyer = NonPlayableCharacter(_("Buyer"))
default caleb = NonPlayableCharacter(_("Caleb"), _("Aleb"))
default cameron = NonPlayableCharacter(_("Cameron"), _("Cameroon")) # Relationship progression: FRIEND, BRO
default candy = NonPlayableCharacter(_("Candy")) # Relationship progression: FRIEND, LIKES, FWB
default charli = NonPlayableCharacter(_("Charli"), _("CharliAndTheCockFactory"))
default chloe = NonPlayableCharacter(_("Chloe"), _("Chloe101")) # Relationship progression: MAD, FRIEND, FWB, GIRLFRIEND
default chris = NonPlayableCharacter(_("Chris"), _("Chriscuit")) # Relationshp progression: MAD, FRIEND
default dean = NonPlayableCharacter(_("Dean"))
default elijah = NonPlayableCharacter(_("Elijah"), _("Elijah_Woods")) # Relationship progression: MAKEFUN, FRIEND
default emily = NonPlayableCharacter(_("Emily"), _("emilyyyy")) # Relationship progression: FRIEND, FWB
default emmy = NonPlayableCharacter(_("Emmy")) # Relationship progression: FRIEND, LIKES, FWB
default evelyn = NonPlayableCharacter(_("Evelyn")) # Relationship progression: FRIEND, MOVE, DATE, LIKES, KISS
default grayson = NonPlayableCharacter(_("Grayson"), _("G-rayson"))
default imre = NonPlayableCharacter(_("Imre"), _("BadBoyImre")) # Relationship progression: MAD, FRIEND
default iris = NonPlayableCharacter(_("Iris"))
default jenny = NonPlayableCharacter(_("Jenny")) # Relationship progression: AWKWARD, FRIEND, FWB
default josh = NonPlayableCharacter(_("Josh"), _("Josh80085")) # Relationship progression: MAD, FRIEND
default julia = NonPlayableCharacter(_("Julia"))
default kai = NonPlayableCharacter(_("Kai"), _("KaiCriesWith2Ply"))
default kim = NonPlayableCharacter(_("Kim"), _("KimPlausible"))
default kourtney = NonPlayableCharacter(_("Kourtney")) # Relationship progression: FRIEND, LIKES
default lauren = NonPlayableCharacter(_("Lauren"), _("LoLoLauren")) # Relationship progression: MAD, FRIEND, MOVE, KISS, GIRLFRIEND
default lews_official = NonPlayableCharacter(_("LewsOfficial"))
default lindsey = NonPlayableCharacter(_("Lindsey"), _("LindsLou")) # Relationship progression: FRIEND, KISS, FWB
default mason = NonPlayableCharacter(_("Mason"), _("Mason_Mas"))
default mr_lee = NonPlayableCharacter(_("Mr Lee"))
default ms_rose = NonPlayableCharacter(_("Ms Rose")) # Relationship progression: THREATEN, FRIEND, KISS, FWB
default naomi = NonPlayableCharacter(_("Naomi"), _("NaomiXMarie")) # Relationship progression: FRIEND, FWB
default nora = NonPlayableCharacter(_("Nora"), _("Nora_12")) # Relationship progression: MAD, FRIEND, MOVE, LIKES, FWB
default parker = NonPlayableCharacter(_("Parker"))
default penelope = NonPlayableCharacter(_("Penelope"), _("Penelopeeps")) # Relationship progression: FRIEND, LIKES, LOYAL
default polly = NonPlayableCharacter(_("Polly"))
default riley = NonPlayableCharacter(_("Riley"), _("RileyReads")) # Relationship progression: FRIEND, MOVE, LIKES, FWB, LOYAL
default ryan = NonPlayableCharacter(_("Ryan"), _("Ryanator"))
default samantha = NonPlayableCharacter(_("Samantha"), _("SamFromSpaceJam")) # Relationship progression: FRIEND, MOVE, FWB
default satin = NonPlayableCharacter(_("Satin")) # Relationship progression: FRIEND, FWB
default sebastian = NonPlayableCharacter(_("Sebastian"), _("Big Seb"))
default tom = NonPlayableCharacter(_("Tom"))
default trainer = NonPlayableCharacter(_("Trainer"))
default wolf = NonPlayableCharacter(_("Wolf"))

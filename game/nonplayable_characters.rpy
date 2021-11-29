init python:
    class NonPlayableCharacter:
        """
        Custom character class primarily used for managing all the character specific function of the game.

        Attributes:
            name (str): The display name for the character
            profile_picture (str): The file name for the characters profile picture, located in "images/nonplayable_characters/profile_pictures/"
        """

        def __init__(self, name, profile_picture):
            self.name = name
            self.name = name.replace(" ", "_")
            self.profile_picture = "images/nonplayable_characters/profile_pictures/{}".format(profile_picture)

            self._messenger = None
            self._simplr = None

            self.stats = {
                "Competitive": None,
                "Vindictive": [],
                "Talkative": None
            }

            self.points = 0
            self._relationship = False
            self._girlfriend = False

        @property
        def relationship(self):
            return self._relationship

        @relationship.setter
        def relationship(self, value):
            self._relationship = value
            if value:
                mc.relationships.add(self)
            else:
                mc.relationships.remove(self)

        @property
        def girlfriend(self):
            return self._girlfriend

        @girlfriend.setter
        def girlfriend(self, value):
            self._girlfriend = value
            if value:
                mc.girlfriends.add(self)
            else:
                mc.girlfriends.remove(self)

        @property
        def messenger(self):
            if self._messenger is None:
                self._messenger = Contact(self.name, self.profile_picture, locked)
                contacts.append(self.messenger)
            return self._messenger

        @property
        def simplr(self):
            if self._simplr is None:
                self._simplr = SimplrContact(self.name)
                simplr_pendingContacts.append(self._simplr)
            return self._simplr

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

default chloe = NonPlayableCharacter("Chloe", "chloe.webp", messenger=True)
default amber = NonPlayableCharacter("Amber", "amber.webp", messenger=True)
default penelope = NonPlayableCharacter("Penelope", "penelope.webp", messenger=True)
default riley = NonPlayableCharacter("Riley", "riley.webp", messenger=True)
default lindsey = NonPlayableCharacter("Lindsey", "lindsey.webp", messenger=True)
default lauren = NonPlayableCharacter("Lauren", "lauren.webp", messenger=True)
default emily = NonPlayableCharacter("Emily", "emily.webp", messenger=True)
default ms_rose = NonPlayableCharacter("Ms Rose", "ms_rose.webp")
default nora = NonPlayableCharacter("Nora", "nora.webp", messenger=True)
default aubrey = NonPlayableCharacter("Aubrey", "aubrey.webp", messenger=True)
default ryan = NonPlayableCharacter("Ryan", "ryan.webp", messenger=True)
default imre = NonPlayableCharacter("Imre", "imre.webp", messenger=True)
default chris = NonPlayableCharacter("Chris", "chris.webp")
default charli = NonPlayableCharacter("Charli", "charlie.webp")
default cameron = NonPlayableCharacter("Cameron", "cameron.webp")
default josh = NonPlayableCharacter("Josh", "josh.webp", messenger=True)
default julia = NonPlayableCharacter("Julia", "julia.webp", messenger=True)
default evelyn = NonPlayableCharacter("Evelyn", "evelyn.webp")
default autumn = NonPlayableCharacter("Autumn", "autumn.webp", messenger=True)
default sebastian = NonPlayableCharacter("Sebastian", "sebastian.webp", messenger=True)
default grayson = NonPlayableCharacter("Grayson", "grayson.webp", messenger=True)
default jenny = NonPlayableCharacter("Jenny", "jenny.webp", messenger=True)
default mr_lee = NonPlayableCharacter("Mr Lee", "lee.webp")

default beth = NonPlayableCharacter("Beth", "beth.webp", simplr=True)
default iris = NonPlayableCharacter("Iris", "iris.webp", simplr=True)
default samantha = NonPlayableCharacter("Samantha", "samantha.webp", simplr=True)
default emmy = NonPlayableCharacter("Emmy", "emmy.webp", simplr=True)

default wolf = NonPlayableCharacter("Wolf", "wolf.webp")
default trainer = NonPlayableCharacter("Trainer", "trainer.webp")
default buyer = NonPlayableCharacter("Buyer", "buyer.webp")

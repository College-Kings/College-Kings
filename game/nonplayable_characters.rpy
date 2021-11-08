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

            self.stats = {
                "Competitive": None,
                "Vindictive": [],
                "Talkative": None
            }

            self.points = 0
            self.opinion = None

        def create_contact(self, profile_picture, locked=True):
            self.messenger = Contact(self.name, self.profile_picture, locked)
            contacts.append(self.messenger)
        
        def create_simplr(self, condition="True"):
            self.simplr = SimplrContact(self.name, condition)

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

init offset = 1

default chloe = NonPlayableCharacter("Chloe", "chloe.webp")
default amber = NonPlayableCharacter("Amber", "amber.webp")
default penelope = NonPlayableCharacter("Penelope", "penelope.webp")
default riley = NonPlayableCharacter("Riley", "riley.webp")
default lindsey = NonPlayableCharacter("Lindsey", "lindsey.webp")
default lauren = NonPlayableCharacter("Lauren", "lauren.webp")
default emily = NonPlayableCharacter("Emily", "emily.webp")
default ms_rose = NonPlayableCharacter("Ms Rose", "ms_rose.webp")
default nora = NonPlayableCharacter("Nora", "nora.webp")
default aubrey = NonPlayableCharacter("Aubrey", "aurbrey.webp")
default ryan = NonPlayableCharacter("Ryan", "ryan.webp")
default imre = NonPlayableCharacter("Imre", "imre.webp")
default chris = NonPlayableCharacter("Chris", "chris.webp")
default charli = NonPlayableCharacter("Charli", "charlie.webp")
default cameron = NonPlayableCharacter("Cameron", "cameron.webp")
default josh = NonPlayableCharacter("Josh", "josh.webp")
default julia = NonPlayableCharacter("Julia", "Julia.webp")
default evelyn = NonPlayableCharacter("Evelyn", "evelyn.webp")
default autumn = NonPlayableCharacter("Autumn", "autumn.webp")
default sebastian = NonPlayableCharacter("Sebastian", "sebastian.webp")
default grayson = NonPlayableCharacter("Grayson", "grayson.webp")
default jenny = NonPlayableCharacter("Jenny", "jenny.webp")

default beth = NonPlayableCharacter("Beth", "beth.webp")
default iris = NonPlayableCharacter("Iris", "iris.webp")
default samantha = NonPlayableCharacter("Samantha", "samantha.webp")
default emmy = NonPlayableCharacter("Emmy", "emmy.webp")
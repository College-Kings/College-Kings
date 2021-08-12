init python:
    class CustomCharacter:
        """
        Custom character class primarily used for the murder mystery game in v12s7

        Attributes:
            name (str): The display name for the character
        """

        def __init__(self, name):
            self.name = name

            self.stats = {
                "Competitive": None,
                "Vindictive": [],
                "Talkative": None
            }

            self.points = 0
            self.opinion = None

        def kill(self):
            # Check Competitive stat
            if self.stats["Competitive"] == True and len(v12s7_killList) < 3:
                self.points -= 1
            elif self.stats["Competitive"] == False and len(v12s7_killList) < 3:
                self.points += 1

            # Check Vindictive stat
            for character in self.stats["Vindictive"]:
                if character in v12s7_killList:
                    self.points += 1
                else:
                    self.points -= 1

            # Check Talkative stat
            if self.stats["Talkative"] == True:
                self.points += 1
            elif self.stats["Talkative"] == False:
                self.points -= 1

            # Add character to kill list
            if not self == cameron: #except Cameron, because he's not playing :D
                v12s7_killList.append(self)

        def resetPoints(self):
            self.points = 0
        
default chloe = CustomCharacter("Chloe")
default amber = CustomCharacter("Amber")
default penelope = CustomCharacter("Penelope")
default riley = CustomCharacter("Riley")
default lindsey = CustomCharacter("Lindsey")
default lauren = CustomCharacter("Lauren")
default samantha = CustomCharacter("Samantha")
default emily = CustomCharacter("Emily")
default ms_rose = CustomCharacter("Ms Rose")
default nora = CustomCharacter("Nora")
default aubrey = CustomCharacter("Aubrey")
default ryan = CustomCharacter("Ryan")
default imre = CustomCharacter("Imre")
default chris = CustomCharacter("Chris")
default charli = CustomCharacter("Charli")
default cameron = CustomCharacter("Cameron")
default josh = CustomCharacter("Josh")


default contact_Emily = Contact("Emily", "emilyprofilepic.webp")
default contact_Lauren = Contact("Lauren", "laurenprofilepic.webp")
default contact_Julia = Contact("Julia", "juliaprofilepic.webp")
default contact_Ryan = Contact("Ryan", "ryanprofilepic.webp")
default contact_Josh = Contact("Josh", "joshprofilepic.webp")
default contact_Aubrey = Contact("Aubrey", "aubreyprofilepic.webp")
default contact_Chloe = Contact("Chloe", "chloeprofilepic.webp")
default contact_Evelyn = Contact("Evelyn", "evelynprofilepic.webp")
default contact_Amber = Contact("Amber", "amberprofilepic.webp")
default contact_Penelope = Contact("Penelope", "penelopeprofilepic.webp")
default contact_Riley = Contact("Riley", "rileyprofilepic.webp")
default contact_Autumn = Contact("Autumn", "autumnprofilepic.webp")
default contact_Imre = Contact("Imre", "imreprofilepic.webp")
default contact_Sebastian = Contact("Sebastian", "sebastianprofilepicture.webp")
default contact_Grayson = Contact("Grayson", "graysonprofilepicture.webp")
default contact_Lindsey = Contact("Lindsey", "lindseyprofilepic.webp")
default contact_Jenny = Contact("Jenny", "jennyprofilepicture.webp")

default simplr_Beth = SimplrContact("Beth", "bethProfilePicture.webp", "bethProfilePictureLarge.webp")
default simplr_Iris = SimplrContact("Iris", "irisProfilePicture.webp", "irisProfilePictureLarge.webp")
default simplr_Samantha = SimplrContact("Samantha", "samanthaProfilePicture.webp", "samanthaProfilePictureLarge.webp")
default simplr_Emmy = SimplrContact("Emmy", "emmyProfilePicture.webp", "emmyProfilePictureLarge.webp")
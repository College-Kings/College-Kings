init python:
    class MainCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self):
            self.money = 0
            self.inventory = Inventory()

        def add_item(self, item):
            if item.cost > self.money:
                raise UnhandledTranscribingError("{} price is higher then user money".format(item.name))

            self.inventory.items.append(item)

        def has_item(self, item):
            return (item in self.inventory.items)


    class CustomCharacter:
        """
        Custom character class primarily used for the murder mystery game in v12s7

        Attributes:
            name (str): The display name for the character
            profile_picture (str): The relative path for this character's profile picture
        """

        def __init__(self, name):
            self.name = name

            self.name = name.replace(" ", "_")

            self.stats = {
                "Competitive": None,
                "Vindictive": [],
                "Talkative": None
            }

            self.points = 0
            self.opinion = None


        def create_contact(profile_picture, locked=True):
            self.messenger = Contact(self.name, profile_picture, locked)

        
        def create_simplr(profile_picture, large_profile_picture, condition="True"):
            self.simplr = SimplrContact(self.name, profile_picture, large_profile_picture, condition)


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
            if self.stats["Talkative"] == True and self in v12s7_endtalkList:
                self.points += 1
            elif self.stats["Talkative"] == True:
                self.points -= 1
            elif self.stats["Talkative"] == False and self in v12s7_endtalkList:
                self.points -= 1

            # Add character to kill list
            if self != cameron: # Except Cameron, because he's not playing
                v12s7_killList.add(self)


        def reset_points(self):
            self.points = 0

init offset = 1

default mc = MainCharacter()
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


# default contact_Emily = Contact("Emily", "emilyprofilepic.webp")
# default contact_Lauren = Contact("Lauren", "laurenprofilepic.webp")
# default contact_Julia = Contact("Julia", "juliaprofilepic.webp")
# default contact_Ryan = Contact("Ryan", "ryanprofilepic.webp")
# default contact_Josh = Contact("Josh", "joshprofilepic.webp")
# default contact_Aubrey = Contact("Aubrey", "aubreyprofilepic.webp")
# default contact_Chloe = Contact("Chloe", "chloeprofilepic.webp")
# default contact_Evelyn = Contact("Evelyn", "evelynprofilepic.webp")
# default contact_Amber = Contact("Amber", "amberprofilepic.webp")
# default contact_Penelope = Contact("Penelope", "penelopeprofilepic.webp")
# default contact_Riley = Contact("Riley", "rileyprofilepic.webp")
# default contact_Autumn = Contact("Autumn", "autumnprofilepic.webp")
# default contact_Imre = Contact("Imre", "imreprofilepic.webp")
# default contact_Sebastian = Contact("Sebastian", "sebastianprofilepicture.webp")
# default contact_Grayson = Contact("Grayson", "graysonprofilepicture.webp")
# default contact_Lindsey = Contact("Lindsey", "lindseyprofilepic.webp")
# default contact_Jenny = Contact("Jenny", "jennyprofilepicture.webp")
# default contact_Nora = Contact("Nora", "noraprofilepicture.webp")

# default simplr_Beth = SimplrContact("Beth", "bethProfilePicture.webp", "bethProfilePictureLarge.webp")
# default simplr_Iris = SimplrContact("Iris", "irisProfilePicture.webp", "irisProfilePictureLarge.webp")
# default simplr_Samantha = SimplrContact("Samantha", "samanthaProfilePicture.webp", "samanthaProfilePictureLarge.webp")
# default simplr_Emmy = SimplrContact("Emmy", "emmyProfilePicture.webp", "emmyProfilePictureLarge.webp")
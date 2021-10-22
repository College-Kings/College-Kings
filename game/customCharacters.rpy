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

        def __init__(self, name, profile_picture):
            self.name = name
            self.profile_picture = "images/phone/messages/profile_pictures/{}".format(profile_picture)

            self.name = name.replace(" ", "_")
            
            # self.messenger = Contact(name, profile_picture)

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
            if self.stats["Talkative"] == True and self in v12s7_endtalkList:
                self.points += 1
            elif self.stats["Talkative"] == True:
                self.points -= 1
            elif self.stats["Talkative"] == False and self in v12s7_endtalkList:
                self.points -= 1

            # Add character to kill list
            if self != cameron: #except Cameron, because he's not playing :D
                v12s7_killList.add(self)

        def resetPoints(self):
            self.points = 0

init offset = 1

default mc = MainCharacter()
default chloe = CustomCharacter("Chloe", "chloeprofilepic.webp")
default amber = CustomCharacter("Amber", "chloeprofilepic.webp")
default penelope = CustomCharacter("Penelope", "chloeprofilepic.webp")
default riley = CustomCharacter("Riley", "chloeprofilepic.webp")
default lindsey = CustomCharacter("Lindsey", "chloeprofilepic.webp")
default lauren = CustomCharacter("Lauren", "chloeprofilepic.webp")
default samantha = CustomCharacter("Samantha", "chloeprofilepic.webp")
default emily = CustomCharacter("Emily", "chloeprofilepic.webp")
default ms_rose = CustomCharacter("Ms Rose", "chloeprofilepic.webp")
default nora = CustomCharacter("Nora", "chloeprofilepic.webp")
default aubrey = CustomCharacter("Aubrey", "chloeprofilepic.webp")
default ryan = CustomCharacter("Ryan", "chloeprofilepic.webp")
default imre = CustomCharacter("Imre", "chloeprofilepic.webp")
default chris = CustomCharacter("Chris", "chloeprofilepic.webp")
default charli = CustomCharacter("Charli", "chloeprofilepic.webp")
default cameron = CustomCharacter("Cameron", "chloeprofilepic.webp")
default josh = CustomCharacter("Josh", "chloeprofilepic.webp")


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
default contact_Nora = Contact("Nora", "noraprofilepicture.webp")

default simplr_Beth = SimplrContact("Beth", "bethProfilePicture.webp", "bethProfilePictureLarge.webp")
default simplr_Iris = SimplrContact("Iris", "irisProfilePicture.webp", "irisProfilePictureLarge.webp")
default simplr_Samantha = SimplrContact("Samantha", "samanthaProfilePicture.webp", "samanthaProfilePictureLarge.webp")
default simplr_Emmy = SimplrContact("Emmy", "emmyProfilePicture.webp", "emmyProfilePictureLarge.webp")
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
        Custom character class primarily used for managing all the character specific function of the game.
            - Messenger
            - Simplr
            - Murder Mystery

        Attributes:
            name (str): The display name for the character
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


        def create_contact(self, profile_picture, locked=True):
            self.messenger = Contact(self.name, profile_picture, locked)
            contacts.append(self.messenger)

        
        def create_simplr(self, condition="True"):
            self.simplr = SimplrContact(self.name, condition)


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
default julia = CustomCharacter("Julia")
default evelyn = CustomCharacter("Evelyn")
default autumn = CustomCharacter("Autumn")
default sebastian = CustomCharacter("Sebastian")
default grayson = CustomCharacter("Grayson")
default jenny = CustomCharacter("Jenny")

default beth = CustomCharacter("Beth")
default iris = CustomCharacter("Iris")
default samantha = CustomCharacter("Samantha")
default emmy = CustomCharacter("Emmy")
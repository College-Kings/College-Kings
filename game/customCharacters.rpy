init python:
    class CustomCharacter:
        def __init__(self, name):
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

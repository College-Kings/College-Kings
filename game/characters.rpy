init python:
    class Character(ADVCharacter):
        def __init__(self, name, kind=None, **properties):
            ADVCharacter.__init__(self, name, kind, **properties)

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
            

# Declare characters used by this game. The color argument colorizes the name of the character.
default narrator = Character (None, what_outlines=[ (2, "#000") ])
default u = Character("[name]", who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ju = Character("Julia", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default car = Character("Car", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ca = Character("Cameron", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ma = Character("Mason", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default aut = Character("Autumn", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default em = Character("Emily", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default an = Character("Mrs. Anderson", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ch = Character("Chris", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default no = Character("Nora", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ry = Character("Ryan", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ro = Character("Ms. Rose", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default la = Character("Lauren", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ri = Character("Riley", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default el = Character("Elijah", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default imre = Character("Imre", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default au = Character("Aubrey", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default sam = Character("Sam", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default karen = Character("Karen", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default jo = Character("Josh", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default courtney = Character("Courtney", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default jeremy = Character("Jeremy", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default katy = Character("Katy", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default sarah = Character("Sarah", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default gr = Character("Grayson", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default cl = Character("Chloe", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default tom = Character("Tom", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default tut = Character("Tutorial", who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default lee = Character("Mr. Lee", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ben = Character("Benjamin", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ehr = Character("Dr. Ehrmantraut", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default pe = Character("Penelope", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ev = Character("Evelyn", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default aa = Character("Aaron", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default sec = Character("Security Guard", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default li = Character("Lindsey", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default unknown = Character("Unknown", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default uber = Character("Uber Driver", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default clerk = Character("Clerk", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default am = Character("Amber", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ki = Character("Kim", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ad = Character("Adam", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default co = Character("Counselor", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 6.0
default waiter = Character("Waiter", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default host = Character("Host", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default poet1 = Character("Lisa", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default poet2 = Character("Martin", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default sa = Character("Samantha", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default guya = Character("Peter", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default guyb = Character("Harry", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default finn = Character("Finn", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default guyd = Character("Perry", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default se = Character("Sebastian", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default guyc = Character("Marcus", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default matt = Character("Matt", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 7.0
default cal = Character("Caleb", who_color="#83d81c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
default coop = Character("Cooper", who_color="#11af68", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
default kai = Character("Kai", who_color="#1caedb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
default wes = Character("Wesley", who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape
default par = Character("Parker", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape
default rg1 = Character("Angelica", who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default rg2 = Character("Elisa", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default nerd = Character("Nerd", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default xav = Character("Xavier", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default jax = Character("Jaxon", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default teach = Character("Teacher", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default class1 = Character("Class", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 8.0
default de = Character("The Dean", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default je = Character("Joe", who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ann = Character("Speaker Announcement", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default empl = Character("Employee", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 9.0
default unkfem = Character("Female voice", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 10.0
default jen = Character("Jenny", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default mrr = Character("Mr. Rose", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default be = Character("Ben", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default jer = Character("Jerry", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default dg1 = Character("Rachel", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default dg2 = Character("Eleanor", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default dg3 = Character("Karen", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default dg4 = Character("Rebecca", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 11.0
default art = Character("Art Director", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default air = Character("Airport Host", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ran = Character("Rancher", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default hor = Character("Horse", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default dun = Character("Duncan", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default bartender = Character("Bartender", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default foxy = Character("Foxy", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default ericka = Character("Ericka", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default jane = Character("Jane", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default candy = Character("Candy", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default mana = Character("Manager", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default driver = Character("Driver", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default sus = Character("Susan", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default jud = Character("Judge", who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default charli = Character("Charli", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default csa = Character("Sales Rep", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default dennis = Character("Dennis", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default bank = Character("Bank Teller", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 12.0
default robber = Character("Robber", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
default fwait = Character("French Waitress", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

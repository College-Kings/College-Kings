init python:
    class Detective(Enum):
        PROFESSIONAL = 0
        PSYCHOLOGIST = 1
        LOOSE_CANNON = 2


    class Clue:
        def __init__(self, name, image, opinion=""):
            self.name = name
            self.image = image
            self.opinion = opinion


    class Location:
        def __init__(self, name, image="", opinion=""):
            self.name = name
            self.image = image

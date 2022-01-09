init python:
    class Detective(Enum):
        PROFESSIONAL = 0
        PSYCHOLOGIST = 1
        LOOSE_CANNON = 2


    class Clue:
        def __init__(self, name, image):
            self.name = name
            self.image = image


    class Location:
        def __init__(self, name, image=""):
            self.name = name
            self.image = image

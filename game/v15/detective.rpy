init python:
    class Detective(Enum):
        PROFESSIONAL = 0
        PSYCHOLOGIST = 1
        LOOSE_CANNON = 2


    class Clue:
        def __init__(self, informant, description, opinion=""):
            self.informant = informant
            self.description = description
            self.opinion = opinion

            renpy.show_screen("detective_popup", message="Clue found!")


    class Location:
        def __init__(self, name, image, opinion=""):
            self.name = name
            self.image = image
            self.opinion = opinion

            renpy.show_screen("detective_popup", message="Location found!")

init python:
    class Checklist:
        def __init__(self):
            self.checklist = []

        def __getitem__(self, index):
            return self.checklist[index]

        def __iter__(self):
            return iter(self.checklist)

        def add_item(self, name):
            self.checklist.append(ChecklistItem(name))

        def reset(self):
            self.checklist = []


    class ChecklistItem:
        def __init__(self, name):
            self.name = name

            self.completed = False


screen checklist_icon():
    tag checklist

    imagebutton:
        idle "icon"
        hover "icon_hover"
        action Show("checklist")


screen checklist():
    tag checklist
    
    vbox:
        for item in checklist:
            text item.name:
                if item.completed:
                    color "#0f0"
                else:
                    color "#fff"
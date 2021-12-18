init python:
    class ChecklistItem:
        def __init__(self, name):
            self.name = name

            self.complete = False


    class Checklist:
        def __init__(self):
            self.items = []

        def __getitem__(self, index):
            return self.items[index]

        def __iter__(self):
            return iter(self.items)

        def add_item(self, name):
            self.items.append(ChecklistItem(name))

        def reset(self):
            self.items = []


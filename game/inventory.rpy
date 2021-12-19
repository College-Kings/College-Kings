init python:
    class Inventory:
        """Inventory class used to manage MC virtual storage"""

        def __init__(self):
            self.items = []

        def __contains__(self, item):
            return item in self.items

        def __getitem__(self, index):
            return self.items[index]

        def __iter__(self):
            return iter(self.items)

        def add_item(self, item):
            self.items.append(item)

        def reset(self):
            self.items = []

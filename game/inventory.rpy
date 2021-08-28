init python:
    class Inventory:
        """Inventory class used to manage MC virtual storage"""

        def __init__(self):
            self.items = []

        def add_item(self, item):
            self.items.append(item)


    class Item:
        """Item class used to repersent an interactable Item
        
        Attributes:
            name (str): Display name of the item
        """
        def __init__(self, name):
            self.name = name


default honey = Item("Honey")
default butt_plug = Item("Butt Plug")
default spankers = Item("Spankers")
default cuffs = Item("Cuffs")
default feather = Item("Feather")
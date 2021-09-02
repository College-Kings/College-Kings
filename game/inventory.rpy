init python:
    class Inventory:
        """Inventory class used to manage MC virtual storage"""

        def __init__(self):
            self.items = []
            

    class Item:
        """Item class used to repersent an interactable Item
        
        Attributes:
            name (str): Display name of the item
            cost (int): Amount item costs in dollars 
        """

        def __init__(self, name, cost):
            self.name = name
            self.cost = cost


default honey = Item("Honey", 15)
default butt_plug = Item("Butt Plug", 30)
default spankers = Item("Spankers", 50)
default cuffs = Item("Cuffs", 10)
default feather = Item("Feather", 15)
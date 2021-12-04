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
            return self.items

        def reset(self):
            self.items = []


    class Item:
        """Item class used to repersent an interactable Item
        
        Attributes:
            name (str): Display name of the item
            cost (int): Amount item costs in dollars 
        """

        def __init__(self, name, cost, idle_image=None, hover_image=None, insensitive_image=None):
            self.name = name
            self.cost = cost
            self.idle_image = idle_image
            self.hover_image = hover_image
            self.insensitive_image = insensitive_image


default honey = Item("Honey", 15, "images/v13/Scene35/sex_shop/honey.webp", "images/v13/Scene35/sex_shop/honey_hover.webp", "images/v13/Scene35/sex_shop/honey_insensitive.webp")
default butt_plug = Item("Butt Plug", 30, "images/v13/Scene35/sex_shop/butt_plug.webp", "images/v13/Scene35/sex_shop/butt_plug_hover.webp", "images/v13/Scene35/sex_shop/butt_plug_insensitive.webp")
default spankers = Item("Spankers", 50, "images/v13/Scene35/sex_shop/spanker.webp", "images/v13/Scene35/sex_shop/spankers_hover.webp", "images/v13/Scene35/sex_shop/spankers_insensitive.webp")
default cuffs = Item("Cuffs", 10, "images/v13/Scene35/sex_shop/cuffs.webp", "images/v13/Scene35/sex_shop/cuffs_hover.webp", "images/v13/Scene35/sex_shop/cuffs_insensitive.webp")
default feather = Item("Feather", 15, "images/v13/Scene35/sex_shop/feather.webp", "images/v13/Scene35/sex_shop/feather_hover.webp", "images/v13/Scene35/sex_shop/feather_insensitive.webp")
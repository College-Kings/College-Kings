init python:
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


# v13
define honey = Item(
    "Honey",
    cost=15,
    idle_image="images/v13/Scene 35/sex_shop/honey.webp",
    hover_image="images/v13/Scene 35/sex_shop/honey_hover.webp",
    insensitive_image="images/v13/Scene 35/sex_shop/honey_insensitive.webp",
)
define butt_plug = Item(
    "Butt Plug",
    cost=30,
    idle_image="images/v13/Scene 35/sex_shop/butt_plug.webp",
    hover_image="images/v13/Scene 35/sex_shop/butt_plug_hover.webp",
    insensitive_image="images/v13/Scene 35/sex_shop/butt_plug_insensitive.webp"
)
define spankers = Item(
    "Spankers",
    cost=50,
    idle_image="images/v13/Scene 35/sex_shop/spanker.webp",
    hover_image="images/v13/Scene 35/sex_shop/spankers_hover.webp",
    insensitive_image="images/v13/Scene 35/sex_shop/spankers_insensitive.webp"
)
define cuffs = Item(
    "Cuffs",
    cost=10,
    idle_image="images/v13/Scene 35/sex_shop/cuffs.webp",
    hover_image="images/v13/Scene 35/sex_shop/cuffs_hover.webp",
    insensitive_image="images/v13/Scene 35/sex_shop/cuffs_insensitive.webp"
)
define feather = Item(
    "Feather",
    cost=15,
    idle_image="images/v13/Scene 35/sex_shop/feather.webp",
    hover_image="images/v13/Scene 35/sex_shop/feather_hover.webp",
    insensitive_image="images/v13/Scene 35/sex_shop/feather_insensitive.webp"
)

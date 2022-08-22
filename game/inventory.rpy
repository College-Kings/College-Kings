init python:
    @dataclass
    class Item:
        name: str
        cost: int
        idle_image: Optional[str] = None
        hover_image: Optional[str] = None
        insensitive_image: Optional[str] = None


    class Inventory:
        """Inventory class used to manage MC virtual storage"""

        def __init__(self):
            self.items: list[Item] = []

        def __contains__(self, item: Item):
            return item in self.items

        def __getitem__(self, index: int):
            return self.items[index]

        def __setitem__(self, index, value):
            self.items[index] = value

        def __iter__(self):
            return iter(self.items)

        def add_item(self, item: Item):
            self.items.append(item)

        def reset(self):
            self.items = []


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

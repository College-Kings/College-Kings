init python:
    class PlayableCharacter:
        """Main Character class is used to create the MC character model"""

        def __init__(self):
            self.money = 0
            self.inventory = Inventory()

        def add_item(self, item):
            if item.cost > self.money:
                raise UnhandledTranscribingError("{} price is higher then user money".format(item.name))

            self.inventory.items.append(item)

        def has_item(self, item):
            return (item in self.inventory.items)


default mc = PlayableCharacter()
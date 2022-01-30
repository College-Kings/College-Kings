init python:
    class Application:
        def __init__(self, name, image, home_screen, locked=False):
            self.name = name
            self._image = "images/phone/{}".format(image)
            self.home_screen = home_screen
            self.locked = locked
            
            self.contacts = []
            self.notification = False

        @property
        def image(self):
            if self.notification:
                return os.path.splitext(self._image)[0] + "Notification" + os.path.splitext(self._image)[1]
            return self._image

        @image.setter
        def image(self, value):
            self._image = value

        def unlock(self):
            self.locked = False

default messenger = Application("Messages", "messages/appAssets/messagesIcon.webp", "messenger_contacts")
default stats_app = Application("Stats", "stats/appAssets/statsIcon.webp", "stats", locked=True)
default achievement_app = Application("Achievements", "achievements/appAssets/achievementsIcon.webp", "achievements")
default kiwii = Application("Kiwii", "kiwii/appAssets/kiwiiIcon.webp", "kiwiiApp", locked=True)
default simplr_app = Application("Simplr", "simplr/appAssets/simplrIcon.webp", "simplr_app", locked=True)
default relationship_app = Application("Relationships", "relationships_icon.webp", "relationship_screen", locked=False)
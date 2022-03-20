init python:
    class Application:
        def __init__(self, name, *args, **kwargs):
            self.name = name
            self.home_screen = "{}_home".format(self.name.lower())
            
            self.contacts = []

        @property
        def image(self):
            return "images/phone/{}/app-assets/icon{}.webp".format(self.name.lower(), "-notification" if self.notification else "")

        @property
        def notification(self):
            return False

    
    class Messenger(Application):
        def __init__(self):
            Application.__init__(self, "Messenger")

        @property
        def notification(self):
            return any(contact.notification for contact in self.contacts)

default messenger = Messenger()
default stats_app = Application("KCT", "stats/appAssets/statsIcon.webp", "stats", locked=True)
default achievement_app = Application("Achievements", "achievements/appAssets/achievementsIcon.webp", "achievements")
default kiwii = Application("Kiwii", "kiwii/appAssets/kiwiiIcon.webp", "kiwiiApp", locked=True)
default simplr_app = Application("Simplr", "simplr/appAssets/simplrIcon.webp", "simplr_app", locked=True)
default relationship_app = Application("Relationships", "relationships/appAssets/relationships_icon.webp", "relationship_app", locked=False)
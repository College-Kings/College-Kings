init python:
    class Application:
        def __init__(self, name, *args, **kwargs):
            self.name = name
            self.home_screen = "{}_home".format(self.name.lower())
            
            self.notification = False
            self.contacts = []

        @property
        def image(self):
            return "images/phone/{}/app-assets/icon{}.webp".format(self.name.lower(), "-notification" if self.notification else "")

        def unlock(self):
            if self not in phone.applications:
                phone.applications.append(self)

    
    class Messenger(Application):
        def __init__(self):
            super(Messenger, self).__init__("Messenger")

        @property
        def notification(self):
            return any(contact.notification for contact in self.contacts)

        @notification.setter
        def notification(self, value):
            pass


    class Simplr(Application):
        def __init__(self):
            super(Simplr, self).__init__("Simplr")

            self.pending_contacts = []

        @property
        def notification(self):
            return any(contact.notification for contact in self.contacts)

        @notification.setter
        def notification(self, value):
            pass


default messenger = Messenger()
default stats_app = Application("KCT")
default achievement_app = Application("Achievements")
default kiwii = Application("Kiwii")
default simplr_app = Simplr()
default relationship_app = Application("Relationships", "relationships/appAssets/relationships_icon.webp", "relationship_app", locked=False)
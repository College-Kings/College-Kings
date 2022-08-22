init python:
    class Application:
        def __init__(self, name: str):
            self.name = name
            self.home_screen = f"{self.name.lower()}_home"

            self.notification = False
            self.contacts: list[Contact] = []

        @property
        def image(self):
            if self.notification:
                return f"images/phone/{self.name.lower()}/app-assets/icon-notification.webp"
            else:
                return f"images/phone/{self.name.lower()}/app-assets/icon.webp"

        def unlock(self):
            if self not in phone.applications:
                phone.applications.append(self)


    class Messenger(Application):
        def __init__(self):
            super().__init__("Messenger")

        @property
        def notification(self):
            return any(contact.notification for contact in self.contacts)

        @notification.setter
        def notification(self, value: Any):
            pass


    class Simplr(Application):
        def __init__(self):
            super().__init__("Simplr")

            self.pending_contacts = []

        @property
        def notification(self):
            return any(contact.notification for contact in self.contacts)

        @notification.setter
        def notification(self, value: Any):
            pass


    class Kiwii(Application):
        def __init__(self):
            super().__init__("Kiwii")

        @staticmethod
        def get_message(kiwii_obj: Union["KiwiiComment", "KiwiiPost"]):
            usernames = [mention.username for mention in kiwii_obj.mentions]

            message = ", @".join(usernames)
            if usernames:
                message = (
                    f"{{color=#3498DB}}{{b}}@{message}{{/b}}{{/color}} {kiwii_obj.message}"
                )
            else:
                message = kiwii_obj.message

            return message

        @staticmethod
        def toggle_liked(kiwii_obj: Union["KiwiiComment", "KiwiiPost"]):
            kiwii_obj.liked = not kiwii_obj.liked

            if kiwii_obj.liked:
                kiwii_obj.numberLikes += 1
            else:
                kiwii_obj.numberLikes -= 1


default messenger = Messenger()
default stats_app = Application("KCT")
default achievement_app = Application("Achievements")
default kiwii = Kiwii()
default simplr_app = Simplr()
default relationship_app = Application("Relationships")
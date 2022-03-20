init python:
    class SimplrContact(Contact):
        """
        The Contact class for Simplr. Used to manage and create messages for simplr characters.

        Attributes:
            name (str): The display name for the character
            profile_picture (str): The relative path for this character's contact profile picture
            condition (str): A string repersenting a python condition which deems if the character unlocks 
        """

        def __init__(self, name):
            self.name = name
            self.condition = True

            self._notification = False

            for (dirpath, dirname, filenames) in os.walk(os.path.join(contacts_file_path, name.lower(), "large_profile_pictures")):
                self.large_profile_pictures = ["images/nonplayable_characters/{}/large_profile_pictures/{}".format(name.lower(), filename) for filename in filenames]

            self.sent_messages = []
            self.pending_messages = []

            simplr_app.unlock()

        @property
        def notification(self):
            if not self.sent_messages and not self.pending_messages:
                return False
            
            if self.replies:
                return True

            return self._notification

        @notification.setter
        def notification(self, value):
            self._notification = value

        @property
        def profile_picture(self):
            return "images/nonplayable_characters/{0}/{0}_profile_picture.webp".format(self.name.lower())

        def removeContact(self):
            simplr_app.pending_contacts.pop(0)

        def likedContact(self):
            self.removeContact()

            if self.condition:
                simplr_app.contacts.append(self)
            
        def newMessage(self, message, force_send=False):
            message = Message(self, message)

            # Moves contact to the top when recieving a new message
            if self in simplr_app.contacts:
                simplr_app.contacts.insert(0, simplr_app.contacts.pop(simplr_app.contacts.index(self)))

            # Add message to queue
            if not force_send:
                self.pending_messages.append(message)
            else:
                self.pending_messages = []
                self.sent_messages.append(message)
            
            return message

        def newImgMessage(self, img, force_send=False):
            message = ImageMessage(self, img)

            # Moves contact to the top when recieving a new message
            if self in simplr_app.contacts:
                simplr_app.contacts.insert(0, simplr_app.contacts.pop(simplr_app.contacts.index(self)))

            # Add message to queue
            if not force_send:
                self.pending_messages.append(message)
            else:
                self.pending_messages = []
                self.sent_messages.append(message)

            return message

        def addReply(self, message, func=None):
            reply = Reply(message, func)

            # Append reply to last sent message
            try:
                if self.pending_messages:
                    self.pending_messages[-1].replies.append(reply)
                else:
                    self.sent_messages[-1].replies.append(reply)
            except IndexError:
                message = self.newMessage("", force_send=True)
                message.replies.append(reply)

        def addImgReply(self, image, func):
            reply = ImgReply(image, func)

            # Append reply to last sent message
            try:
                if self.pending_messages:
                    self.pending_messages[-1].replies.append(reply)
                else:
                    self.sent_messages[-1].replies.append(reply)
            except Exception:
                self.newMessage("", force_send=True)
                self.pending_messages[-1].replies.append(reply)

        def getMessage(self, message):
            for msg in self.sent_messages:
                try:
                    if message == msg.message:
                        return msg
                except AttributeError:
                    if message == msg.image:
                        return msg
            return False


screen simplr_home():
    tag phone_tag
    python:
        try: simplr_contact = simplr_app.pending_contacts[0]
        except IndexError: simplr_contact = None

    use base_phone:

        default image_path = "images/phone/simplr/app-assets/"

        frame:
            background image_path + "background.webp"
            
            # Top UI
            imagebutton:
                pos (340, 100)
                idle image_path + "message-icon.webp"
                hover image_path + "message-icon-hover.webp"
                action Show("simplr_contacts")

            if simplr_contact is not None:
                frame:
                    background simplr_contact.large_profile_pictures[0]
                    xysize (370, 593)
                    xalign 0.5
                    ypos 200
                    
                    hbox:
                        align (0.5, 1.0)
                        yoffset -10
                        spacing 10

                        imagebutton:
                            idle image_path + "like-button-idle.webp"
                            hover image_path + "like-button-hover.webp"
                            action Function(simplr_contact.likedContact)

                        imagebutton:
                            idle image_path + "no-button-idle.webp"
                            hover image_path + "no-button-hover.webp"
                            action Function(simplr_contact.removeContact)

            else:
                text "No new profiles to show...\nYou can however still chat with your matches!\n\nBe sure to check back soon!":
                    style "simplr_no_more_profiles"
                    align (0.5, 0.5)
                    xsize 340


screen simplr_contacts():
    tag phone_tag

    default image_path = "images/phone/simplr/app-assets/"

    use base_phone:
        frame:
            background image_path + "simplr_contacts_background.webp"
            xysize (433, 918)

            viewport:
                mousewheel True
                draggable True
                pos (11, 134)
                xysize (416, 709)

                vbox:
                    spacing 5

                    null height 10

                    for contact in simplr_app.contacts:
                        button:
                            action [Function(renpy.retain_after_load), SetField(contact, "notification", False), Show("simplr_messenger", contact=contact)]
                            ysize 80

                            add Transform(contact.profile_picture, size=(65, 65)) xpos 20 yalign 0.5
                            
                            text contact.name style "nametext" xpos 100 yalign 0.5

                            if contact.notification:
                                add "contact_notification" align (1.0, 0.5) xoffset -25


screen simplr_messenger(contact):
    tag phone_tag
    modal True

    default image_path = "images/phone/simplr/app-assets/"

    python:
        yadj.value = yadjValue

    use base_phone:
        frame:
            background image_path + "conversation-background.webp"
            xysize (433, 918)

            hbox:
                pos (41, 62)
                ysize 93
                spacing 15

                imagebutton:
                    idle "back_button"
                    action [Hide("message_reply"), Show("simplr_home")]
                    yalign 0.5

                add Transform(contact.profile_picture, size=(65, 65)) yalign 0.5

                text contact.name style "nametext" yalign 0.5

            viewport:
                yadjustment yadj
                mousewheel True
                pos (11, 157)
                xysize (416, 686)

                vbox:
                    spacing 5

                    null height 5

                    for message in contact.sent_messages:
                        frame:
                            padding (50, 50)

                            if isinstance(message, Message) and message.message.strip():
                                background "message_background"

                                text message.message  style "message_text"

                            elif isinstance(message, ImageMessage):
                                background "message_background"

                                imagebutton:
                                    idle Transform(message.image, ysize=216)
                                    action Show("phone_image", img=message.image)

                            elif isinstance(message, Reply):
                                background "message_background"

                                text message.message style "message_text"

                            elif isinstance(message, ImgReply):
                                background "message_background"

                                imagebutton:
                                    idle Transform(message.image, ysize=216)
                                    action Show("phone_image", img=message.image)

            if contact.replies:
                fixed:
                    xysize (416, 63)
                    ypos 780

                    imagebutton:
                        idle "reply_button_idle"
                        hover image_path + "reply-button-hover.webp"
                        selected_idle image_path + "reply-button-hover.webp"
                        action Show("message_reply", contact=contact)
                        align (0.5, 0.5)

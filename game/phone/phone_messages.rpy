init python:
    class Contact:
        def __init__(self, user: Union["PlayableCharacter", "NonPlayableCharacter"]):
            self.user = user
            self.sent_messages: list[BaseMessage] = []
            self.pending_messages: list[BaseMessage] = []
            self._notification: bool = False

        @property
        def notification(self):
            if not self.sent_messages and not self.pending_messages:
                return False

            if self.replies:
                return True

            try:
                return self._notification
            except AttributeError:
                return False

        @notification.setter
        def notification(self, value: bool):
            self._notification = value

        @property
        def replies(self) -> list[BaseReply]:
            try:
                self.sent_messages
            except AttributeError:
                self.sent_messages = []

            try:
                return self.sent_messages[-1].replies
            except IndexError:
                return []

        def new_message(self, content: str, force_send: bool = False):
            message = Message(self, content)

            # Moves contact to the top when recieving a new message
            try:
                messenger.contacts.insert(
                    0, messenger.contacts.pop(messenger.contacts.index(self))
                )
            except ValueError:
                messenger.contacts.insert(0, self)

            # Add message to queue
            if self.replies and not force_send:
                self.pending_messages.append(message)
            else:
                self.pending_messages = []
                self.sent_messages.append(message)

            self.notification = True

            return message

        def new_image_message(self, image: str, force_send: bool = False):
            message = ImageMessage(self, image)

            # Moves contact to the top when recieving a new message
            try:
                messenger.contacts.insert(
                    0, messenger.contacts.pop(messenger.contacts.index(self))
                )
            except ValueError:
                messenger.contacts.insert(0, self)

            # Add message to queue
            if not force_send:
                self.pending_messages.append(message)
            else:
                self.pending_messages = []
                self.sent_messages.append(message)

            self.notification = True

            return message

        def add_reply(
            self,
            content: str,
            func: Optional[Callable[[], None]] = None,
            new_message: bool = False,
            disabled: bool = False,
        ):
            reply = Reply(content, func)

            # Append reply to last sent message
            try:
                if self.pending_messages:
                    self.pending_messages[-1].replies.append(reply)
                elif self.sent_messages:
                    self.sent_messages[-1].replies.append(reply)
                else:
                    message = self.new_message("", force_send=True)
                    message.replies.append(reply)
            except IndexError:
                message = self.new_message("", force_send=True)
                message.replies.append(reply)

            self.notification = True

        def add_image_reply(
            self,
            content: str,
            func: Optional[Callable[[], None]] = None,
            newMessage: bool = False,
            disabled: bool = False,
        ):
            reply = ImgReply(content, func)

            # Append reply to last sent message
            try:
                if newMessage:
                    message = self.new_message("")
                    message.replies.append(reply)
                elif self.pending_messages:
                    self.pending_messages[-1].replies.append(reply)
                else:
                    self.sent_messages[-1].replies.append(reply)
            except IndexError:
                message = self.new_message("", force_send=True)
                message.replies.append(reply)

            self.notification = True

        def selected_reply(self, reply: BaseReply):
            self.sent_messages.append(reply)
            self.sent_messages[-1].reply = reply
            self.sent_messages[-1].replies = []

            if reply.func is not None:
                reply.func()
                reply.func = None

            # Send next queued message(s)
            try:
                while not self.replies:
                    self.sent_messages.append(self.pending_messages.pop(0))
            except IndexError:
                pass

        def unlock(self):
            if self not in messenger.contacts:
                messenger.contacts.append(self)  # type: ignore
            self.locked = False

        def find_message(self, message: str):
            for msg in self.sent_messages:
                if hasattr(msg, "content") and message == msg.content:
                    return msg
                elif hasattr(msg, "message") and message == msg.message:
                    return msg
                elif hasattr(msg, "image") and message == msg.image:
                    return msg
            return False

        ## Backwards compatibility
        def newMessage(self, message: str, force_send: bool = False):
            return self.new_message(message, force_send)

        def newImgMessage(self, image: str, force_send: bool = False):
            return self.new_image_message(image, force_send)

        def addReply(
            self,
            message: str,
            func: Optional[Callable[[], None]] = None,
            newMessage: bool = False,
            disabled: bool = False,
        ):
            return self.add_reply(message, func, newMessage)

        def addImgReply(
            self,
            image: str,
            func: Optional[Callable[[], None]] = None,
            newMessage: bool = False,
            disabled: bool = False,
        ):
            return self.add_image_reply(image, func, newMessage)


screen messenger_home():
    tag phone_tag

    default image_path = "images/phone/messenger/app-assets/"

    use base_phone:
        frame:
            background image_path + "home-background.webp"
            xysize (433, 918)

            viewport:
                mousewheel True
                draggable True
                pos (11, 134)
                xysize (416, 709)

                vbox:
                    spacing 5

                    null height 10

                    for contact in messenger.contacts:
                        button:
                            action [Function(renpy.retain_after_load), Show("messager", contact=contact)]
                            ysize 80

                            add Transform(contact.user.profile_picture, xysize=(65, 65)) xpos 20 yalign 0.5
                            
                            text contact.user.name style "nametext" xpos 100 yalign 0.5

                            if contact.notification:
                                add "contact_notification" align (1.0, 0.5) xoffset -25

    if config_debug:
        for contact in messenger.contacts:
            if contact.notification:
                timer 0.1 action [Function(renpy.retain_after_load), Show("messager", contact=contact)]


screen messager(contact=None):
    tag phone_tag
    modal True

    default image_path = "images/phone/messenger/app-assets/"

    python:
        contact.notification = False

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
                    action [Hide("message_reply"), Show("messenger_home")]
                    yalign 0.5

                add Transform(contact.user.profile_picture, xysize=(65, 65)) yalign 0.5

                text contact.user.name style "nametext" yalign 0.5

            viewport:
                yadjustment inf_adj
                mousewheel True
                pos (11, 157)
                xysize (416, 686)

                vbox:
                    spacing -25

                    null height 25

                    for message in contact.sent_messages:
                        frame:
                            padding (50, 50)

                            if isinstance(message, Message) and message.message.strip():
                                background "message_background"

                                text message.message  style "message_text"

                            elif isinstance(message, ImageMessage):
                                background "message_background"

                                imagebutton:
                                    idle Transform(message.image, zoom=0.15)
                                    action Show("phone_image", img=message.image)

                            elif isinstance(message, Reply):
                                background "reply_background"
                                xalign 1.0

                                text message.message  style "reply_text"

                            elif isinstance(message, ImgReply):
                                background "reply_background"
                                xalign 1.0

                                imagebutton:
                                    idle Transform(message.image, zoom=0.15)
                                    action Show("phone_image", img=message.image)

                    null height 75

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

    if kiwii_firstTime:
        timer 0.01 action Show("kiwiiPopup")

    if config_debug:
        if contact.replies:
            timer 0.1 repeat True action Show("message_reply", contact=contact)
        else:
            timer 0.1 repeat True action [Hide("message_reply"), Show("phone")]
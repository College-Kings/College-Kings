init python:
    class Contact:
        def __init__(self, name, locked=True):
            self.name = name
            self.locked = locked
            self.sent_messages = []
            self.pending_messages = []

        @property
        def profile_picture(self):
            return "images/nonplayable_characters/profile_pictures/{}.webp".format(self.name.replace(' ', '_').lower())

        @property
        def replies(self):
            try: self.sent_messages
            except AttributeError: self.sent_messages = []

            try:
                return self.sent_messages[-1].replies
            except IndexError: return []

        def new_message(self, message, force_send=False):
            message = Message(self, message)

            # Moves contact to the top when recieving a new message
            messenger.contacts.insert(0, messenger.contacts.pop(messenger.contacts.index(self)))

            # Add message to queue
            if self.replies and not force_send:
                self.pending_messages.append(message)
            else:
                self.pending_messages = []
                self.sent_messages.append(message)

            self.unlock()
            messenger.notification = True
            
            return message

        def new_image_message(self, img, force_send=False):
            message = ImageMessage(self, img)

            try: contacts.insert(0, contacts.pop(contacts.index(self))) # Moves contact to the top when recieving a new message
            except Exception: pass

            # Add message to queue
            if not force_send:
                self.pending_messages.append(message)
            else:
                self.pending_messages = []
                self.sent_messages.append(message)

            self.unlock()
            messenger.notification = True

            return message

        def add_reply(self, message, func=None, new_message=False, disabled=False):
            reply = Reply(message, func, disabled)

            # Append reply to last sent message
            try:
                if new_message:
                    self.newMessage("")
                    message.replies.append(reply)
                elif self.pending_messages:
                    self.pending_messages[-1].replies.append(reply)
                else:
                    self.sent_messages[-1].replies.append(reply)
            except IndexError:
                message = self.newMessage("", force_send=True)
                message.replies.append(reply)

            self.unlock()

        def add_image_reply(self, img, func=None, newMessage=False, disabled=False):
            reply = ImgReply(img, func, disabled)

            # Append reply to last sent message
            try:
                if newMessage:
                    message = self.newMessage("")
                    message.replies.append(reply)
                elif self.pending_messages:
                    self.pending_messages[-1].replies.append(reply)
                else:
                    self.sent_messages[-1].replies.append(reply)
            except IndexError:
                message = self.newMessage("", force_send=True)
                message.replies.append(reply)

            self.unlock()

        def selected_reply(self, reply):
            self.sent_messages.append(reply)
            self.sent_messages[-1].reply = reply
            self.sent_messages[-1].replies = []

            try:
                reply.func()
                reply.func = None
            except TypeError:
                pass

            # Send next queued message(s)
            try:
                while not self.replies:
                    self.sent_messages.append(self.pending_messages.pop(0))
            except IndexError: pass

            # Check if all replies been sent
            if not any([contact.replies for contact in messenger.contacts]):
                messenger.notification = False

        def unlock(self):
            if self not in messenger.contacts:
                messenger.contacts.append(self)
            self.locked = False

        def find_message(self, message):
            for msg in self.sent_messages:
                try:
                    if message == msg.message:
                        return msg
                except AttributeError:
                    if message == msg.image:
                        return msg
            return False

        ## Backwards compatibility
        def newMessage(self, message, force_send=False):
            return self.new_message(message, force_send)

        def newImgMessage(self, img, force_send=False):
            return self.new_image_message(img, force_send)

        def addReply(self, message, func=None, newMessage=False, disabled=False):
            return self.add_reply(message, func, newMessage, disabled)

        def addImgReply(self, img, func=None, newMessage=False, disabled=False):
            return self.add_image_reply(img, func, newMessage, disabled)


    class Message:
        def __init__(self, contact, message):
            self.contact = contact
            self.message = message
            self.replies = []
            self.reply = None


    class ImageMessage:
        def __init__(self, contact, image):
            self.contact = contact
            self.image = image
            self.replies = []
            self.reply = None


    class Reply:
        def __init__(self, message, func=None, disabled=False):
            self.message = message
            self.func = func
            self.disabled = disabled


    class ImgReply:
        def __init__(self, image, func=None, disabled=False):
            self.image = image
            self.func = func
            self.disabled = disabled


screen messenger_contacts():
    tag phone_tag

    use base_phone:

        add "images/phone/contacts_screen.webp" at truecenter

        fixed:
            xysize(375, 78)
            pos(772, 168)

            text "Messages" align(0.1, 0.5) style "phonetext"

        vpgrid:
            cols 1
            mousewheel True
            draggable True
            scrollbars "vertical"
            xysize (375, 663)
            pos (772, 247)

            for contact in messenger.contacts:
                if not contact.locked:
                    fixed:
                        xysize(375, 74)
                        
                        add contact.profile_picture yalign 0.5 xpos 20

                        text contact.name style "nametext" yalign 0.5 xpos 100

                        if contact.replies:
                            add "images/contactmsgnot.webp" yalign 0.5 xpos 275

                        imagebutton:
                            idle "images/contactbutton.webp" align(0.5, 0.5)
                            action [Function(renpy.retain_after_load), Show("messager", contact=contact)]


screen messager(contact=None):
    tag phone_tag
    zorder 200
    modal True

    python:
        yadj.value = yadjValue

    use base_phone:

        add "images/msg.webp" at truecenter ## Messenger Screen Background

        fixed:
            xysize(375, 112)
            xalign 0.5
            ypos 168

            imagebutton:
                idle "images/msgarrow.webp"
                action [Show("messenger_contacts"), Hide("messenger_reply")]
                yalign 0.5

            vbox:
                align (0.5, 0.5)

                if hasattr(contact, "profile_picture"):
                    add contact.profile_picture xalign 0.5
                else:
                    add contact.profilePicture xalign 0.5

                text contact.name style "nametext"

        viewport:
            yadjustment yadj
            mousewheel True
            pos (773, 282)
            xysize (374, 550)

            vbox:
                xsize 374
                spacing 5

                null height 5

                for message in contact.sent_messages:
                    if isinstance(message, Message) and message.message.strip():
                        textbutton message.message style "msgleft"
                    elif isinstance(message, ImageMessage):
                        imagebutton:
                            idle Transform(message.image, size=(307, 173))
                            style "msgleft"
                            action Show("phone_image", img=message.image)
                    elif isinstance(message, Reply):
                        textbutton message.message style "msgright"
                    elif isinstance(message, ImgReply):
                        imagebutton:
                            idle Transform(message.image, size=(307, 173))
                            style "msgright"
                            action Show("phone_image", img=message.image)

        if contact.replies:
                hbox:
                    xalign 0.5
                    ypos 855

                    textbutton "Reply":
                        style "replybox"
                        action Show("messenger_reply", contact=contact)

    if kiwii_firstTime:
        timer 0.01 action Show("kiwiiPopup")


screen messenger_reply(contact=None):
    zorder 200

    vbox:
        xpos 1200
        yalign 0.84
        spacing 15

        for reply in contact.replies:
            if isinstance(reply, Reply):
                textbutton reply.message:
                    if reply.disabled:
                        style "reply_disabled"
                        text_style "replies_style_text"
                    else:
                        style "replies_style"
                        action [Hide("messenger_reply"), Function(contact.selected_reply, reply)]

            elif isinstance(reply, ImgReply):
                imagebutton:
                    idle Transform(reply.image, zoom=0.15)
                    if reply.disabled:
                        style "reply_disabled"
                    else:
                        style "replies_style"
                        action [Hide("messenger_reply"), Function(contact.selected_reply, reply)]


screen phone_image(img=None):
    modal True
    zorder 200
    
    python:
        if os.path.splitext(img)[0][-3:] != "big":
            bigImage = os.path.splitext(img)[0] + "big" + os.path.splitext(img)[1]

    add "images/darker.webp"
    if renpy.loadable(bigImage):
        add bigImage at truecenter
    else:
        add img at truecenter

    imagebutton:
        idle "images/bigbutton.webp"
        action Hide("phone_image")
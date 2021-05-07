init python:
    class Contact:
        def __init__(self, name, profilePicture, locked=True):
            self.name = name
            self.profilePicture = profilePicture
            self.locked = locked
            self.newMessages = False
            self.sentMessages = []
            self.pendingMessages = []
            contacts.append(self)

        def newMessage(self, message, queue=True):
            message = Message(self, message)

            try: contacts.insert(0, contacts.pop(contacts.index(self))) # Moves contact to the top when recieving a new message
            except Exception: pass

            # Add message to queue
            if queue:
                self.pendingMessages.append(message)
            else:
                self.pendingMessages = []
                self.sentMessages.append(message)

            self.unlock()
            self.newMessages = True
            return message

        def newImgMessage(self, img, queue=True):
            message = ImageMessage(self, img)

            try: contacts.insert(0, contacts.pop(contacts.index(self))) # Moves contact to the top when recieving a new message
            except Exception: pass

            # Add message to queue
            if queue:
                self.pendingMessages.append(message)
            else:
                self.pendingMessages = []
                self.sentMessages.append(message)

            self.unlock()
            self.newMessages = True
            return message

        def addReply(self, message, func):
            reply = Reply(message, func)

            # Append reply to last sent message
            try:
                if self.pendingMessages:
                    self.pendingMessages[-1].replies.append(reply)
                else:
                    self.sentMessages[-1].replies.append(reply)
            except Exception:
                message = self.newMessage("", queue=False)
                message.replies.append(reply)

            self.unlock()

        def addImgReply(self, image, var=None, value=0):
            reply = ImgReply(image, label)

            # Append reply to last sent message
            try:
                if self.pendingMessages:
                    self.pendingMessages[-1].replies.append(reply)
                else:
                    self.sentMessages[-1].replies.append(reply)
            except Exception:
                self.newMessage("", queue=False)
                self.pendingMessages[-1].replies.append(reply)

            self.unlock()

        def seenMessage(self):
            if not any([contact.newMessages for contact in contacts]):
                msgApp.seenNotification()

        def selectedReply(self, reply):
            self.sentMessages.append(reply)
            self.sentMessages[-1].reply = reply
            self.sentMessages[-1].replies = []

            reply.func()

            # Send next queued message
            try:
                self.sentMessages.append(self.pendingMessages[0])
            except IndexError: pass

        def unlock(self):
            if self not in contacts:
                contacts.append(self)
            self.locked = False

        def getReplies(self):
            try:
                return self.sentMessages[-1].replies
            except Exception: return False

    class Message:
        def __init__(self, contact, msg):
            self.contact = contact
            self.msg = msg
            self.replies = []
            self.reply = None

    class ImageMessage:
        def __init__(self, contact, image):
            self.contact = contact
            self.image = image

    class Reply:
        def __init__(self, message, func):
            self.message = message
            self.func = func

    class ImgReply:
        def __init__(self, image, func):
            self.image = image
            self.func = func

init offset = -1
default contacts = []

screen contactsscreen():
    tag phoneTag

    use phoneTemplate:

        add "images/contactsscreen.webp" at truecenter ## Contact Screen Background

        fixed:
            xysize(375, 78)
            pos(772, 168)

            text "Messages" align(0.1, 0.5) style "phonetext"

        vpgrid:
            cols 1
            mousewheel True
            draggable True
            scrollbars "vertical"
            xysize(375, 663)
            pos(772, 247)

            for contact in contacts:
                if not contact.locked:
                    fixed:
                        xysize(375, 74)

                        add contact.profilePicture yalign 0.5 xpos 20
                        text contact.name style "nametext" yalign 0.5 xpos 100

                        if contact.sentMessages and contact.sentMessages[-1].replies:
                            add "images/contactmsgnot.webp" yalign 0.5 xpos 275

                        imagebutton:
                            idle "images/contactbutton.webp" align(0.5, 0.5)
                            action [Function(renpy.retain_after_load), Show("messager", contact=contact)]


screen messager(contact=None):
    tag phoneTag

    python:
        yadj.value = yadjValue
        contact.seenMessage()

    use phoneTemplate:

        add "images/msg.webp" at truecenter ## Messenger Screen Background

        fixed:
            xysize(375, 112)
            xalign 0.5
            ypos 168

            imagebutton:
                idle "images/msgarrow.webp"
                action [Show("contactsscreen"), Hide("messager"), Hide("reply")]
                yalign 0.5

            vbox:
                align (0.5, 0.5)

                add contact.profilePicture xalign 0.5
                text contact.name style "nametext"

        viewport:
            yadjustment yadj
            mousewheel True
            xysize(374, 556)
            pos(773, 282)

            vbox:
                for message in contact.sentMessages:
                    if isinstance(message, Message) and message.msg.strip():
                        textbutton message.msg style "msgleft"
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

        if contact.sentMessages and contact.sentMessages[-1].replies:
                hbox:
                    xalign 0.5
                    ypos 855

                    textbutton "Reply":
                        style "replybox"
                        action Show("reply", contact=contact)

    if kiwii:
        timer 0.1 action Show ("popup19")


screen reply(contact=None):

    vbox xpos 1200 yalign 0.84 spacing 15:

        for reply in contact.sentMessages[-1].replies:
            if isinstance(reply, Reply):
                textbutton reply.message:
                    style "replies_style"
                    if reply.func:
                        action [Hide("reply"), Function(contact.selectedReply, reply), Function(reply.func)]
                    else:
                        action [Hide("reply"), Function(contact.selectedReply, reply)]
            elif isinstance(reply, ImgReply):
                imagebutton:
                    idle Transform(reply.image, zoom=0.15)
                    style "replies_style"
                    if reply.func:
                        action [Hide("reply"), Function(contact.selectedReply, reply), Function(reply.func)]
                    else:
                        action [Hide("reply"), Function(contact.selectedReply, reply)]


screen phone_image(img=None):
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
init python:
    class Contact:
        def __init__(self, name, profilePicture, newMessages=False, locked=True):
            self.name = name
            self.profilePicture = profilePicture
            self.newMessages = newMessages
            self.locked = locked
            self.messages = []
            self.replies = []
            contacts.append(self)

        def newMessage(self, message):
            message = Message(self, message)
            self.newMessages = True
            contacts.insert(0, contacts.pop(contacts.index(self))) # Moves contact to the top when recieving a new message
            if message not in self.messages:
                self.messages.append(message)

        def newImgMessage(self, img):
            message = ImageMessage(self, img)
            self.newMessages = True
            contacts.insert(0, contacts.pop(contacts.index(self))) # Moves contact to the top when recieving a new message
            if message not in self.messages:
                self.messages.append(message)

        def addReply(self, message, label=None):
            reply = Reply(message, label)
            self.replies.append(reply)
            self.newMessages = True

        def addImgReply(self, image, label=None):
            reply = ImgReply(image, label)
            self.replies.append(reply)
            self.newMessages = True

        def seenMessage(self):
            self.newMessages = False
            if not any([contact.newMessages for contact in contacts]):
                msgApp.seenNotification()

        def selectedReply(self, reply):
            self.messages.append(reply)
            self.messages[-1].reply = reply
            self.replies = []

        def unlock(self):
            self.locked = False

    class Message:
        def __init__(self, contact, msg):
            self.contact = contact
            self.msg = msg
            self.reply = None

    class ImageMessage:
        def __init__(self, contact, image):
            self.contact = contact
            self.image = image

    class Reply:
        def __init__(self, message, label=None):
            self.message = message
            self.label = label

    class ImgReply:
        def __init__(self, image, label=None):
            self.image = image
            self.label = label

init offset = -1
default contacts = []

screen contactsscreen():
    tag phoneTag

    use phoneTemplate:

        add "images/contactsscreen.png" at truecenter ## Contact Screen Background

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

                        if contact.newMessages or (contact.messages and contact.messages[-1].replies):
                            add "images/contactmsgnot.png" yalign 0.5 xpos 275

                        imagebutton:
                            idle "images/contactbutton.png" align(0.5, 0.5)
                            action [Function(renpy.retain_after_load), Show("messager", contact=contact)]


screen messager(contact=None):
    tag phoneTag

    python:
        yadj.value = yadjValue
        contact.seenMessage()

    use phoneTemplate:

        add "images/msg.png" at truecenter ## Messenger Screen Background

        fixed:
            xysize(375, 112)
            xalign 0.5
            ypos 168

            imagebutton:
                idle "images/msgarrow.png"
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
                for message in contact.messages:
                    if isinstance(message, Message):
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

        if contact.replies:
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

        for reply in contact.replies:
            if isinstance(reply, Reply):
                textbutton reply.message:
                    style "replies_style"
                    if reply.label:
                        action [Hide("reply"), Hide("messager"), Function(contact.selectedReply, reply), Call(reply.label)]
                    else:
                        action [Function(contact.selectedReply, reply), Hide("reply")]
            elif isinstance(reply, ImgReply):
                imagebutton:
                    idle Transform(reply.image, zoom=0.15)
                    style "replies_style"
                    if reply.label:
                        action [Hide("reply"), Hide("messager"), Function(contact.selectedReply, reply), Call(reply.label)]
                    else:
                        action [Function(contact.selectedReply, reply), Hide("reply")]


screen phone_image(img=None):
    python:
        if os.path.splitext(img)[0][-3:] != "big":
            bigImage = os.path.splitext(img)[0] + "big" + os.path.splitext(img)[1]

    add "images/darker.png"
    if renpy.loadable(bigImage):
        add bigImage at truecenter
    else:
        add img at truecenter

    imagebutton:
        idle "images/bigbutton.png"
        action Hide("phone_image")
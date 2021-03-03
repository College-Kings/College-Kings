init python:
    class Contact:
        def __init__(self, name, profilePicture, newMessages=False, locked=True):
            self.name = name
            self.profilePicture = profilePicture
            self.newMessages = newMessages
            self.locked = locked
            self.messages = []
            contacts.append(self)

        def newMessage(self, message):
            self.newMessages = True
            msgApp.newNotification()
            contacts.insert(0, contacts.pop(contacts.index(self)))
            if message not in self.messages:
                self.messages.append(message)

        def seenMessage(self):
            self.newMessages = False
            if not any([contact.newMessages for contact in contacts]):
                msgApp.seenNotification()

        def unlock(self):
            self.locked = False

    class Message:
        def __init__(self, contact, msg):
            self.contact = contact
            self.msg = msg
            self.replies = []
            self.reply = False
            tempMessages.append(self)

        def addReply(self, reply, label):
            reply = [reply, label]
            if reply not in self.replies and not self.reply:
                self.replies.append(reply)

        def selectedReply(self, reply):
            self.reply = reply[0]
            self.replies = []

    class ImageMessage(Message):
        def __init__(self, contact, image):
            self.contact = contact
            self.image = image
            self.replies = []
            self.reply = False
            tempMessages.append(self)

init offset = -1
default contacts = []
default tempMessages = []

screen contactsscreen():
    tag phoneTag

    use phoneTemplate:

        add "images/contactsscreen.png" at truecenter

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
                        # text "{}".format(contact.newMessages) style "nametext" yalign 0.5 xpos 275
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

        add "images/msg.png" at truecenter

        fixed:
            xysize(374, 112)
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
                    if isinstance(message, ImageMessage):
                        imagebutton:
                            idle message.image
                            style "msgleft"
                            action Show("phone_image", img=message.image)
                    elif message.msg: # <---
                        textbutton message.msg style "msgleft"
                    if message.reply:
                        textbutton message.reply style "msgright"

        if contact.messages:
            if contact.messages[-1].replies:
                hbox:
                    xalign 0.5
                    ypos 855

                    textbutton "Reply":
                        style "replybox"
                        action Show("reply", message=contact.messages[-1])

    if kiwii == True:
        timer 0.1 action Show ("popup19")




screen reply(message=None):

    python:
        yadj.value = yadjValue

    vbox xpos 1200 yalign 0.84 spacing 15:

        for reply in message.replies:
            textbutton reply[0]:
                style "replies_style"
                action [Hide("reply"), Hide("messager"), Function(message.selectedReply, reply), Jump(reply[1])]


screen phone_image(img=None):
    python:
        if os.path.splitext(img)[0][-3:] != "big":
            bigImage = os.path.splitext(img)[0] + "big" + os.path.splitext(img)[1]

    add "images/darker.png"
    add bigImage at truecenter

    imagebutton:
        idle "images/bigbutton.png"
        action Hide("phone_image")

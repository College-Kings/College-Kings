init python:
    class SimplrContact(Contact):
            def __init__(self, name, profilePicture, profilePictureLarge, condition=True):
                self.name = name
                self.profilePicture = "images/phone/simplr/contacts/{}".format(profilePicture)
                self.profilePictureLarge = "images/phone/simplr/contacts/{}".format(profilePictureLarge)
                self.condition = condition

                self.sentMessages = []
                self.pendingMessages = []

                simplr_pendingContacts.append(self)

            def removeContact(self):
                simplr_pendingContacts.pop(0)

            def likedContact(self):
                self.removeContact()

                if self.condition:
                    simplr_contacts.append(self)
                
            def newMessage(self, message, queue=True):
                message = Message(self, message)

                # Moves contact to the top when recieving a new message
                if self in simplr_contacts:
                    simplr_contacts.insert(0, simplr_contacts.pop(simplr_contacts.index(self)))

                # Add message to queue
                if queue:
                    self.pendingMessages.append(message)
                else:
                    self.pendingMessages = []
                    self.sentMessages.append(message)

                if self in simplr_contacts: simplrApp.newNotification()
                
                return message

            def newImgMessage(self, img, queue=True):
                message = ImageMessage(self, img)

                # Moves contact to the top when recieving a new message
                if self in simplr_contacts:
                    simplr_contacts.insert(0, simplr_contacts.pop(simplr_contacts.index(self)))

                # Add message to queue
                if queue:
                    self.pendingMessages.append(message)
                else:
                    self.pendingMessages = []
                    self.sentMessages.append(message)

                if self in simplr_contacts: simplrApp.newNotification()

                return message

            def addReply(self, message, func=None):
                reply = Reply(message, func)

                # Append reply to last sent message
                try:
                    if self.pendingMessages:
                        self.pendingMessages[-1].replies.append(reply)
                    else:
                        self.sentMessages[-1].replies.append(reply)
                except IndexError:
                    message = self.newMessage("", queue=False)
                    message.replies.append(reply)

            def addImgReply(self, image, func):
                reply = ImgReply(image, func)

                # Append reply to last sent message
                try:
                    if self.pendingMessages:
                        self.pendingMessages[-1].replies.append(reply)
                    else:
                        self.sentMessages[-1].replies.append(reply)
                except Exception:
                    self.newMessage("", queue=False)
                    self.pendingMessages[-1].replies.append(reply)

            def seenMessage(self):
                if not any([contact.replies for contact in simplr_contacts]):
                    simplrApp.seenNotification()

            def getMessage(self, message):
                for msg in self.sentMessages:
                    try:
                        if message == msg.message:
                            return msg
                    except AttributeError:
                        if message == msg.image:
                            return msg
                return False

init -1:
    default simplr_pendingContacts = []
    default simplr_contacts = []

screen simplr_app():
    tag phoneTag
    python:
        try: simplr_contact = simplr_pendingContacts[0]
        except IndexError: simplr_contact = None

    use phoneTemplate:
        fixed:
            pos (770, 168)
            xysize (375, 740)

            add "images/phone/simplr/appAssets/background.webp"
            
            # Top UI
            hbox:
                xalign 0.5
                yoffset 10
                spacing 100

                imagebutton:
                    yalign 0.5
                    idle "images/phone/simplr/appAssets/profileIcon.webp"
                    hover "images/phone/simplr/appAssets/profileIconHover.webp"
                    action NullAction()

                add "images/phone/simplr/appAssets/simplrLogo.webp" yalign 0.5

                imagebutton:
                    yalign 0.5
                    idle "images/phone/simplr/appAssets/messageIcon.webp"
                    hover "images/phone/simplr/appAssets/messageIconHover.webp"
                    action Show("simplr_contacts")

            # Profile Picture
            if simplr_contact:
                add Transform(simplr_contact.profilePictureLarge, size=(362, 585)) align (0.5, 0.5)

            # Bottom UI
            hbox:
                xalign 0.5
                yoffset 678
                spacing 20

                imagebutton:
                    yalign 0.5
                    idle "images/phone/simplr/appAssets/yesButton.webp"
                    hover "images/phone/simplr/appAssets/yesButtonHover.webp"
                    if simplr_contact:
                        action Function(simplr_contact.likedContact)

                imagebutton:
                    yalign 0.5
                    idle "images/phone/simplr/appAssets/noButton.webp"
                    hover "images/phone/simplr/appAssets/noButtonHover.webp"
                    if simplr_contact:
                        action Function(simplr_contact.removeContact)


screen simplr_contacts():
    tag phoneTag

    use phoneTemplate:

        add "images/contactsscreen.webp" at truecenter # Contact Screen Background

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

            for contact in simplr_contacts:
                fixed:
                    xysize(375, 74)

                    add Transform(contact.profilePicture, size=(55, 55)) yalign 0.5 xpos 20
                    text contact.name style "nametext" yalign 0.5 xpos 100

                    if contact.replies:
                        add "images/contactmsgnot.webp" yalign 0.5 xpos 275

                    imagebutton:
                        idle "images/contactbutton.webp" align(0.5, 0.5)
                        action [Function(renpy.retain_after_load), Function(contact.seenMessage), Show("simplr_messenger", contact=contact)]


screen simplr_messenger(contact=None):
    tag phoneTag

    use phoneTemplate:

        add "images/msg.webp" at truecenter # Messenger Screen Background

        fixed:
            xysize(375, 112)
            xalign 0.5
            ypos 460

            imagebutton:
                idle "images/msgarrow.webp"
                action [Show("simplr_app"), Hide("simplr_messenger"), Hide("simplr_reply")]
                yalign 0.5

            vbox:
                align (0.5, 0.5)

                add Transform(contact.profilePicture, size=(55, 55)) xalign 0.5
                text contact.name style "nametext"

        viewport:
            yinitial 1.0
            mousewheel True
            xysize(374, 556)
            pos(773, 282)

            vbox:
                spacing 5
                
                for message in contact.sentMessages:
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
                            action Show("simplr_image", img=message.image)

        if contact.replies:
                hbox:
                    xalign 0.5
                    ypos 855

                    textbutton "Reply":
                        style "replybox"
                        action Show("simplr_reply", contact=contact)


screen simplr_reply(contact=None):

    vbox:
        xpos 1200
        yalign 0.84
        spacing 15

        for reply in contact.replies:
            if isinstance(reply, Reply):
                textbutton reply.message:
                    style "replies_style"
                    action [Hide("reply"), Function(contact.selectedReply, reply)]

            elif isinstance(reply, ImgReply):
                imagebutton:
                    idle Transform(reply.image, zoom=0.15)
                    style "replies_style"
                    action [Hide("reply"), Function(contact.selectedReply, reply)]


screen simplr_image(img=None):
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
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

            for (dirpath, dirname, filenames) in os.walk(os.path.join(contacts_file_path, name.lower(), "large_profile_pictures")):
                self.large_profile_pictures = ["images/nonplayable_characters/{}/large_profile_pictures/{}".format(name.lower(), filename) for filename in filenames]

            self.sent_messages = []
            self.pending_messages = []

        @property
        def profile_picture(self):
            return "images/nonplayable_characters/{0}/{0}_profile_picture.webp".format(self.name.lower())

        def removeContact(self):
            simplr_pendingContacts.pop(0)

        def likedContact(self):
            self.removeContact()

            if self.condition:
                simplr_contacts.append(self)
            
        def newMessage(self, message, force_send=False):
            message = Message(self, message)

            # Moves contact to the top when recieving a new message
            if self in simplr_contacts:
                simplr_contacts.insert(0, simplr_contacts.pop(simplr_contacts.index(self)))

            # Add message to queue
            if not force_send:
                self.pending_messages.append(message)
            else:
                self.pending_messages = []
                self.sent_messages.append(message)

            if self in simplr_contacts: simplr_app.notification = True
            
            return message

        def newImgMessage(self, img, force_send=False):
            message = ImageMessage(self, img)

            # Moves contact to the top when recieving a new message
            if self in simplr_contacts:
                simplr_contacts.insert(0, simplr_contacts.pop(simplr_contacts.index(self)))

            # Add message to queue
            if not force_send:
                self.pending_messages.append(message)
            else:
                self.pending_messages = []
                self.sent_messages.append(message)

            if self in simplr_contacts: simplr_app.notification = True

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

        def seenMessage(self):
            if not any(contact.replies for contact in simplr_contacts):
                simplr_app.notification = False

        def getMessage(self, message):
            for msg in self.sent_messages:
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
    tag phone_tag
    python:
        try: simplr_contact = simplr_pendingContacts[0]
        except IndexError: simplr_contact = None

    use base_phone:

        default image_path = "images/phone/simplr/appAssets/"

        fixed:
            pos (770, 168)
            xysize (375, 740)

            add Transform(image_path + "simplr_main_bg.webp", zoom=0.25) at truecenter xoffset 4 yoffset 1
            
            # Top UI
            hbox:
                xalign 0.5
                yoffset 10
                spacing 100

                imagebutton:
                    yalign 0.5
                    idle Transform("images/phone/simplr/appAssets/profileIcon.webp", zoom=0.20)
                    hover Transform("images/phone/simplr/appAssets/profileIconHover.webp", zoom=0.20)
                    action NullAction()

                add Transform("images/phone/simplr/appAssets/simplrLogo.webp", zoom=0.20) yalign 0.5

                imagebutton:
                    yalign 0.5
                    idle Transform("images/phone/simplr/appAssets/messageIcon.webp", zoom=0.20)
                    hover Transform("images/phone/simplr/appAssets/messageIconHover.webp", zoom=0.20)
                    action Show("simplr_contacts")

            # Profile Picture
            if simplr_contact is not None:
                add Transform(simplr_contact.large_profile_pictures[0], size=(362, 585)) align (0.5, 0.5)

            # Bottom UI
            if simplr_contact is not None:
                hbox:
                    xalign 0.5
                    yoffset 500
                    spacing 10

                    imagebutton:
                        yalign 0.5
                        idle Transform("images/phone/simplr/appAssets/yesButton.webp", zoom=0.25)
                        hover Transform("images/phone/simplr/appAssets/yesButtonHover.webp", zoom=0.25)
                        if simplr_contact is not None:
                            action Function(simplr_contact.likedContact)

                    imagebutton:
                        yalign 0.5
                        idle Transform("images/phone/simplr/appAssets/noButton.webp", zoom=0.25)
                        hover Transform("images/phone/simplr/appAssets/noButtonHover.webp", zoom=0.25)
                        if simplr_contact is not None:
                            action Function(simplr_contact.removeContact)
            else:
                hbox:
                    align (0.5, 0.5)
                    spacing 10
                    xmaximum 340

                    text "No new profiles to show...\nYou can however still chat with your matches!\n\nBe sure to check back soon!":
                        xalign 0.5
                        style "simplr_no_more_profiles"
                    


screen simplr_contacts():
    tag phone_tag

    use base_phone:

        default image_path = "images/phone/simplr/appAssets/"

        add Transform(image_path + "simplr_contacts_bg.webp", zoom=0.25) at truecenter xoffset 2

        vpgrid:
            cols 1
            mousewheel True
            draggable True
            xysize(375, 663)
            pos(772, 247)

            for contact in simplr_contacts:
                fixed:
                    xysize(375, 74)

                    if hasattr(contact, "profile_picture"):
                        add Transform(contact.profile_picture, size=(55, 55)) yalign 0.5 xpos 20
                    else:
                        add Transform(contact.profilePicture, size=(55, 55)) yalign 0.5 xpos 20

                    text contact.name style "nametext" yalign 0.5 xpos 100

                    if contact.replies:
                        add "images/contactmsgnot.webp" yalign 0.5 xpos 275

                    imagebutton:
                        idle "images/contactbutton.webp" align(0.5, 0.5)
                        action [Function(renpy.retain_after_load), Function(contact.seenMessage), Show("simplr_messenger", contact=contact)]


screen simplr_messenger(contact=None):
    tag phone_tag

    use base_phone:

        default image_path = "images/phone/simplr/appAssets/"

        add Transform(image_path + "simplr_msg_bg.webp", zoom=0.25) at truecenter xoffset 2

        fixed:
            xysize(375, 112)
            xalign 0.5
            ypos 168

            hbox:
                yalign 0.5

                imagebutton:
                    idle Transform("images/phone/messages/appAssets/back_button.webp", size=(25, 25))
                    action [Show("simplr_app"), Hide("simplr_messenger"), Hide("simplr_reply")]
                    yalign 0.5
                    xoffset 15

                if hasattr(contact, "profile_picture"):
                    add Transform(contact.profile_picture, size=(64, 64)) yalign 0.5 xoffset 30
                else:
                    add Transform(contact.profilePicture, size=(64, 64)) yalign 0.5 xoffset 30

                text contact.name style "nametext" yalign 0.5 xoffset 50

        viewport:
            yadjustment inf_adj
            mousewheel True
            pos(773, 282)
            xysize(374, 556)

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
                    action [Hide("simplr_reply"), Function(contact.selected_reply, reply)]

            elif isinstance(reply, ImgReply):
                imagebutton:
                    idle Transform(reply.image, zoom=0.15)
                    style "replies_style"
                    action [Hide("simplr_reply"), Function(contact.selected_reply, reply)]


screen simplr_image(img=None):
    python:
        if os.path.splitext(img)[0][-3:] != "big":
            bigImage = os.path.splitext(img)[0] + "big" + os.path.splitext(img)[1]

    add "darker_80"
    if renpy.loadable(bigImage):
        add bigImage at truecenter
    else:
        add img at truecenter

    button:
        action Hide("simplr_image")
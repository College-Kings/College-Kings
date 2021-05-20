init -1 python:
    import os

    if renpy.loadable("bugTesting_Overwrite.rpy.rpy"):
        os.remove(os.path.join(config.basedir, "game", "bugTesting", "bugTesting_Overwrite.rpy.rpy"))
    if renpy.loadable("bugTesting_Overwrite.rpy.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "bugTesting", "bugTesting_Overwrite.rpy.rpyc"))

    if renpy.loadable("phonescript.rpy"):
        os.remove(os.path.join(config.basedir, "game", "phone", "phonescript.rpy"))
    if renpy.loadable("phonescript.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "phone", "phonescript.rpyc"))
    
    if renpy.loadable("scriptv06.rpy"):
        os.remove(os.path.join(config.basedir, "game", "scriptv06.rpy"))
    if renpy.loadable("scriptv06.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "scriptv06.rpyc"))

    if renpy.loadable("scriptv07.rpy"):
        os.remove(os.path.join(config.basedir, "game", "scriptv07.rpy"))
    if renpy.loadable("scriptv07.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "scriptv07.rpyc"))

label after_load:
    python:
        # Applications
        msgApp.img = "images/phone/messages/appAssets/messagesIcon.webp"
        statsApp.img = "images/phone/stats/appAssets/statsIcon.webp"
        achApp.img = "images/phone/achievements/appAssets/achievementsIcon.webp"
        kiwiiApp.img = "images/phone/kiwii/appAssets/kiwiiIcon.webp"

        for app in applications:
            try: app.homeScreen = app.screen
            except AttributeError: pass

        # Kiwii Users
        for user in kiwiiUsers:
            kiwiiUsers[user]["profilePicture"] = os.path.splitext(kiwiiUsers[user]["profilePicture"])[0].replace("Profile Pictures", "profilePictures") + ".webp"

        # Kiwii Posts
        for kiwiiPost in kiwiiPosts:
            try: kiwiiPost.img = kiwiiPost.image
            except AttributeError: pass

            kiwiiPost.img = os.path.splitext(kiwiiPost.img)[0] + ".webp"

            for i in range(7, 10):
                if renpy.loadable("images/phone/kiwii/posts/v{}/{}".format(i, kiwiiPost.img.split("/")[-1])):
                    kiwiiPost.img = "images/phone/kiwii/posts/v{}/{}".format(i, kiwiiPost.img.split("/")[-1])
                    break

            try: kiwiiPost.message = kiwiiPost.caption
            except AttributeError: pass

            if kiwiiPost.message[0] == "[" and kiwiiPost.message[1] != "[":
                kiwiiPost.message = "[" + kiwiiPost.message

            try: kiwiiPost.sentComments = kiwiiPost.comments
            except AttributeError: pass

            kiwiiPost.profilePicture = kiwiiPost.getProfilePicture()

            # Kiwii Comments
            for comment in kiwiiPost.sentComments:
                try: comment.message = comment.text
                except AttributeError: pass

                comment.profilePicture = comment.getProfilePicture()
                
            # Kiwii Replies
            try:
                for reply in kiwiiPost.replies:
                    kiwiiPost.replies.remove(reply)
                    kiwiiPost.addReply(reply.reply, numberLikes=reply.numberLikes, mentions=reply.mentions)
            except AttributeError: pass

        # Contacts
        contact_Lindsey.profilePicture = "lindseyprofilepic"

        if contact_Lindsey not in contacts:
            contacts.append(contact_Lindsey)

        for contact in contacts:
            try: contact.pendingMessages
            except AttributeError: contact.pendingMessages = []

            try: contact.sentMessages
            except AttributeError: contact.sentMessages = []
            
            # Messages
            try:
                for message in contact.messages:
                    try: message.image = os.path.splitext(message.image)[0] + ".webp"
                    except AttributeError: pass

                    try: message.message = message.msg
                    except AttributeError: pass

                    try: message.replies
                    except AttributeError: message.replies = []

                    contact.sentMessages.append(message)

                    # Replies
                    for reply in message.replies:
                        try: reply.func
                        except AttributeError: reply.func = None
            except AttributeError: pass

        # Variables 
        try:
            if chlorers: chloers = True
        except NameError: pass
        try: kiwiiPost1
        except NameError: kiwii_firstTime = False

    show screen phoneIcon
    return
init -1 python:
    import os

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

        # Kiwii
        for kiwiiPost in kiwiiPosts:
            try: kiwiiPost.message = kiwiiPost.caption
            except AttributeError: pass

            try: kiwiiPost.img = kiwiiPost.image
            except AttributeError: pass

            for i in range(7, 10):
                if renpy.loadable("images/phone/kiwii/posts/v{}/{}".format(i, kiwiiPost.img.split("/")[-1])):
                    kiwiiPost.img = "images/phone/kiwii/posts/v{}/{}".format(i, kiwiiPost.img.split("/")[-1])
                    break

            kiwiiPost.img = os.path.splitext(kiwiiPost.img)[0] + ".webp"

            try: kiwiiPost.sentComments = kiwiiPost.comments
            except AttributeError: pass

            try: kiwiiPost.message = kiwiiPost.caption
            except AttributeError: pass

        # Contact/Messages/Replies
        for contact in contacts:
            try: contact.pendingMessages
            except AttributeError: contact.pendingMessages = []

            try: contact.sentMessages
            except AttributeError: contact.sentMessages = []
            
            try:
                for message in contact.messages:
                    try: message.image = os.path.splitext(message.image)[0] + ".webp"
                    except AttributeError: pass

                    try: message.message = message.msg
                    except AttributeError: pass

                    contact.sentMessages.append(message)

                    for reply in message.replies:
                        try: reply.func
                        except AttributeError: reply.func = None
            except AttributeError: pass

        contact_Lindsey.profilePicture = "lindseyprofilepic"

        # Variables 
        try:
            if chlorers: chloers = True
        except NameError: pass
        try: kiwiiPost1
        except: kiwii_firstTime = False

    show screen phoneIcon
    return
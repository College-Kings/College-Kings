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
        for app in applications:
            app.image = os.path.splitext(app.image)[0] + ".webp"

        for kiwiiPost in kiwiiPosts:
            kiwiiPost.image = os.path.splitext(kiwiiPost.image)[0] + ".webp"
            if kiwiiPost.caption[0] == "[" and kiwiiPost.caption[1] != "[":
                kiwiiPost.caption = "[" + kiwiiPost.caption

        for contact in contacts:
            try:
                for message in contact.messages:
                    try: message.image = os.path.splitext(message.image)[0] + ".webp"
                    except AttributeError: pass

                    try: message.message = message.msg
                    except AttributeError: pass

                    contact.seenMessages.append(message)
            except Exception: pass
                
        try:
            if chlorers: chloers = True
        except NameError: pass

        contact_Lindsey.profilePicture = "lindseyprofilepic"

    return
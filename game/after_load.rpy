init python:
    import os

label after_load:
    python:
        kiwiiUsers = {
            "Adam": {
                "username": "A.D.A.M.",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/adpp.png"
            },
            "Imre": {
                "username": "BadBoyImre",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/impp.png"
            },
            "Mason": {
                "username": "Mason_Mas",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/masonpp.png"
            },
            "Ryan": {
                "username": "Ryanator",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/rypp.png"
            },
            "Cameron": {
                "username": "Cameroon",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/capp.png"
            },
            "Chris": {
                "username": "Chriscuit",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/chpp.png"
            },
            "Elijah": {
                "username": "Elijah_Woods",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/elpp.png"
            },
            "Grayson": {
                "username": "G-rayson",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/grpp.png"
            },
            "Josh": {
                "username": "Josh80085",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/jopp.png"
            },
            "Aubrey": {
                "username": "Aubs123",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/aupp.png"
            },
            "Amber": {
                "username": "Amber_xx",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/ampp.png"
            },
            "Kim": {
                "username": "KimPlausible",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/kimpp.png"
            },
            "Nora": {
                "username": "Nora_12",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/nopp.png"
            },
            "Penelope": {
                "username": "Penelopeeps",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/pepp.png"
            },
            "Lauren": {
                "username": "LoLoLauren",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/lapp.png"
            },
            "Autumn": {
                "username": "Its_Fall",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/autpp.png"
            },
            "Riley": {
                "username": "RileyReads",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/ripp.png"
            },
            "Emily": {
                "username": "emilyyyy",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/empp.png"
            },
            "Chloe": {
                "username": "Chloe101",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/clpp.png"
            },
            "MC": {
                "username": "MC",
                "profilePicture": profilePictures[0]
            },
            "Caleb": {
                "username": "Aleb",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/calebpp.png"
            },
            "Parker": {
                "username": "Parker",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/parkerpp.webp"
            },
            "Sebastian": {
                "username": "Big Seb",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/sebastianpp.webp"
            },
            "Kai": {
                "username": "Kai",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/kaipp.webp"
            }
        }

        for app in applications:
            app.image = os.path.splitext(app.image)[0] + ".webp"

        for kiwiiPost in kiwiiPosts:
            kiwiiPost.image = os.path.splitext(kiwiiPost.image)[0] + ".webp"
            if kiwiiPost.caption[0] == "[" and kiwiiPost.caption[1] != "[":
                kiwiiPost.caption = "[" + kiwiiPost.caption


        for contact in contacts:
            if contact.messages: contact.unlock()
            for message in contact.messages:
                try:
                    message.image = os.path.splitext(message.image)[0] + ".webp"
                except AttributeError: continue
                
        try:
            if chlorers: chloers = True
        except NameError: pass

        if contact_Lindsey not in contacts:
            contacts.append(contact_Lindsey)

        contact_Lindsey.profilePicture = "lindseyprofilepic"
    return
init python:
    import os

label after_load:
    python:
        kiwiiUsers = {
            "Adam": {
                "username": "A.D.A.M.",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/adpp.webp"
            },
            "Imre": {
                "username": "BadBoyImre",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/impp.webp"
            },
            "Mason": {
                "username": "Mason_Mas",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/masonpp.webp"
            },
            "Ryan": {
                "username": "Ryanator",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/rypp.webp"
            },
            "Cameron": {
                "username": "Cameroon",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/capp.webp"
            },
            "Chris": {
                "username": "Chriscuit",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/chpp.webp"
            },
            "Elijah": {
                "username": "Elijah_Woods",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/elpp.webp"
            },
            "Grayson": {
                "username": "G-rayson",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/grpp.webp"
            },
            "Josh": {
                "username": "Josh80085",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/jopp.webp"
            },
            "Aubrey": {
                "username": "Aubs123",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/aupp.webp"
            },
            "Amber": {
                "username": "Amber_xx",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/ampp.webp"
            },
            "Kim": {
                "username": "KimPlausible",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/kimpp.webp"
            },
            "Nora": {
                "username": "Nora_12",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/nopp.webp"
            },
            "Penelope": {
                "username": "Penelopeeps",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/pepp.webp"
            },
            "Lauren": {
                "username": "LoLoLauren",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/lapp.webp"
            },
            "Autumn": {
                "username": "Its_Fall",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/autpp.webp"
            },
            "Riley": {
                "username": "RileyReads",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/ripp.webp"
            },
            "Emily": {
                "username": "emilyyyy",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/empp.webp"
            },
            "Chloe": {
                "username": "Chloe101",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/clpp.webp"
            },
            "MC": {
                "username": "MC",
                "profilePicture": profilePictures[0]
            },
            "Caleb": {
                "username": "Aleb",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/calebpp.webp"
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

        for contact in contacts:
            for message in contact.messages:
                try:
                    message.image = os.path.splitext(message.image)[0] + ".webp"
                    print(message.image)
                except AttributeError: continue
                
        try:
            if chlorers:
                chloers = True
        except NameError: pass

        contact_Lindsey.unlock()
        contact_Penelope.unlock()

        if contact_Lindsey not in contacts:
            contacts.append(contact_Lindsey)

        contact_Lindsey.profilePicture = "lindseyprofilepic"
    return
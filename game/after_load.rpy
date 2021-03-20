label after_load:
    python:
        persistent.ep = 8
        
        before_contacts = contacts.copy()
        contacts = []
        contact_Emily = Contact("Emily", "emilyprofilepic", locked=False)
        contact_Lauren = Contact("Lauren", "laurenprofilepic", locked=False)
        contact_Julia = Contact("Julia", "juliaprofilepic", locked=False)
        contact_Ryan = Contact("Ryan", "ryanprofilepic", locked=False)
        contact_Josh = Contact("Josh", "joshprofilepic", locked=False)
        contact_Aubrey = Contact("Aubrey", "aubreyprofilepic", locked=False)
        contact_Chloe = Contact("Chloe", "chloeprofilepic", locked=False)
        contact_Evelyn = Contact("Evelyn", "evelynprofilepic", locked=False)
        contact_Amber = Contact("Amber", "amberprofilepic", locked=False)
        contact_Penelope = Contact("Penelope", "penelopeprofilepic", locked=False)
        contact_Riley = Contact("Riley", "rileyprofilepic", locked=False)
        contact_Autumn = Contact("Autumn", "autumnprofilepic", locked=False)
        contact_Imre = Contact("Imre", "imreprofilepic", locked=False)

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
                "profilePicture": "https://cdn.discordapp.com/attachments/778214108369387530/822528644525719572/parkerpp.png"
            }
        }

        try:
            for before_contact in before_contacts:
                for contact in contacts:
                    if before_contact.name == contact.name:
                        for message in before_contact.messages:
                            contact.newMessage(message.msg)
                        break
        except Exception: pass

return
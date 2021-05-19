screen v6_fr3garden():
    tag v6_freeroam
    
    if not kimpuke:
        add "images/fr3garden.webp" # location picture

        # Josh button
        imagebutton:
            pos (1195, 430)
            idle "images/fr3gardenjoshblank.webp"
            hover "images/fr3gardenjosh.webp"

            if not fr3josh:
                action Jump("v6_fr3josh1")

            elif relics >= 5 and upstairs == "nobody" and not askedkim: # Asking people for upstairs
                action Jump("v6_fr3josh3")
            else:
                action Jump("v6_fr3josh2")

    else:
        add "images/fr3garden2.webp"

    # Go inside
    imagebutton:
        pos (485, 190)
        idle "images/fr3gardendoorblank.webp"
        hover "images/fr3gardendoor.webp"
        action Show("v6_fr3downstairs")


screen v6_fr3downstairs():
    tag v6_freeroam

    add "images/fr3downstairs.webp" # location picture

    imagebutton: #Go outside
        pos (440, 900)
        idle "images/fr3downstairsbackblank.webp"
        hover "images/fr3downstairsback.webp"
        action Show("v6_fr3garden")

    imagebutton: #Go upstairs
        xpos 940
        idle "images/fr3downstairsstairsblank.webp"
        hover "images/fr3downstairsstairs.webp"
        action Show("v6_fr3upstairs")

    imagebutton: #Go living room
        pos (360, 70)
        idle "images/fr3downstairsdoorblank.webp"
        hover "images/fr3downstairsdoor.webp"
        action Show("v6_fr3livingroom")

    imagebutton: #Go kitchen
        pos (1486, 368)
        idle "images/fr3downstairsrightblank.webp"
        hover "images/fr3downstairsright.webp"
        action Show("v6_fr3kitchen")


screen v6_fr3livingroom():
    tag v6_freeroam

    add "images/fr3livingroom.webp" # location picture

    # Guy1 button
    imagebutton: 
        pos (760, 392)
        idle "images/fr3livingroomsofablank.webp"
        hover "images/fr3livingroomsofa.webp"

        if not fr3guy:
            action Jump("v6_fr3guy1")
        else:
            action Jump("v6_fr3guy2")

    # Aubrey button
    imagebutton:
        pos (804, 254)
        idle "images/fr3livingroomaubreyblank.webp"
        hover "images/fr3livingroomaubrey.webp"

        if not fr3aubrey:
            action Jump("v6_fr3aubrey1")
        elif relics >= 5 and upstairs == "nobody": # Asking people for upstairs
            action Jump("v6_fr3aubrey3")
        else:
            action Jump("v6_fr3aubrey2")

    # Go back
    imagebutton:
        ypos 915
        xpos 432
        idle "images/fr3livingroombackblank.webp"
        hover "images/fr3livingroomback.webp"
        action Show("v6_fr3downstairs")

    # Go kitchen
    imagebutton:
        ypos 106
        xpos 1700
        idle "images/fr3livingroomdoorblank.webp"
        hover "images/fr3livingroomdoor.webp"
        action Show("v6_fr3kitchen")


screen v6_fr3kitchen():
    tag v6_freeroam

    add "images/fr3kitchen.webp" # location picture

    imagebutton: #chris button
        pos (1147, 60)
        idle "images/fr3kitchenchrisblank.webp"
        hover "images/fr3kitchenchrisn.webp"

        if not fr3chris:
            action Jump("v6_fr3chris1")
        else:
            action Show("endFreeRoamConfirm", continueLabel="v6_fr3chris3")

    imagebutton: #Matt button
        pos (1048, 139)
        idle "images/fr3kitchenmattblank.webp"
        hover "images/fr3kitchenmatt.webp"

        if not fr3matt:
            action Jump("v6_fr3matt1")
        else:
            action Jump("v6_fr3matt2")

    imagebutton: # Go Kitchen 2
        ypos 99
        idle "images/fr3kitchenleftblank.webp"
        hover "images/fr3kitchenleft.webp"
        action Show("v6_fr3kitchen2")

    imagebutton: # Go Living room
        ypos 100
        idle "images/fr3kitchenlivingdoorblank.webp"
        hover "images/fr3kitchenlivingdoor.webp"
        action Show("v6_fr3livingroom")

    imagebutton: #Riley button
        pos (328, 270)
        idle "images/fr3kitchenrileyblank.webp"
        hover "images/fr3kitchenriley.webp"

        if not fr3riley:
            action Jump("v6_fr3riley1")
        elif relics >= 5 and upstairs == "nobody" and not askedriley: # Asking people for upstairs
            action Jump("v6_fr3riley3")
        else:
            action Jump("v6_fr3riley2")


screen v6_fr3kitchen2():
    tag v6_freeroam

    add "images/fr3kitchen2.webp" # location picture

    imagebutton: # Go Ktichen
        pos (358, 836)
        idle "images/fr3kitchen2backblank.webp"
        hover "images/fr3kitchen2back.webp"
        action Show("v6_fr3kitchen")

    imagebutton: # Go Middleroom
        ypos 65
        xpos 0
        idle "images/fr3kitchen2doorblank.webp"
        hover "images/fr3kitchen2door.webp"
        action Show("v6_fr3middleroom")

    imagebutton: # Go downstairs hallway
        ypos 245
        xpos 1364
        idle "images/fr3kitchen2rightblank.webp"
        hover "images/fr3kitchen2right.webp"
        action Show("v6_fr3downstairs")


screen v6_fr3middleroom():
    tag v6_freeroam

    add "images/fr3middleroom.webp" # location picture

    imagebutton: # Go Kitchen2
        xpos 50
        idle "images/fr3middleroomleftblank.webp"
        hover "images/fr3middleroomleft.webp"
        action Show("v6_fr3kitchen2")

    imagebutton: # Downstairs bathroom
        ypos 106
        xpos 700
        idle "images/fr3middleroommiddleblank.webp"
        hover "images/fr3middleroommiddle.webp"
        action Jump("v6_fr3dsbathroom")

    imagebutton: # Go garage
        xpos 1210
        idle "images/fr3middleroomrightblank.webp"
        hover "images/fr3middleroomright.webp"
        action Show("v6_fr3garage")


screen v6_fr3garage():
    tag v6_freeroam

    if not kimpuke:
        add "images/fr3garage.webp" # location picture

        imagebutton: #Amber button
            pos (345, 235)
            idle "images/fr3garageamberblank.webp"
            hover "images/fr3garageamber.webp"

            if not fr3amber:
                action Jump("v6_fr3amber1")

            elif relics >= 5 and upstairs == "nobody" and not askedamber: #Asking people for upstairs
                action Jump("v6_fr3amber3")
            else:
                action Jump("v6_fr3amber2")

    else:
        add "images/fr3garage2.webp"

    imagebutton: #sebastian button
        ypos 168
        xpos 1338
        idle "images/fr3garagefightblank.webp"
        hover "images/fr3garagefight.webp"

        if not fr3sebastian:
            action Jump("v6_fr3sebastian1")
        else:
            action Jump("v6_fr3sebastian2")

    imagebutton: # Go back to middleroom
        ypos 877
        xpos 473
        idle "images/fr3garagebackblank.webp"
        hover "images/fr3garageback.webp"
        action Show("v6_fr3middleroom")


screen v6_fr3upstairs():
    tag v6_freeroam

    add "images/fr3upstairs.webp" # location picture

    imagebutton: # Go backdownstairs
        align (0.5, 1.0)
        idle "images/fr3upstairsbackblank.webp"
        hover "images/fr3upstairsback.webp"
        action Show("v6_fr3downstairs")

    imagebutton: # go office
        pos (1125, 140)
        idle "images/fr3upstairsrightblank.webp"
        hover "images/fr3upstairsright.webp"
        action Jump("v6_fr3office")

    imagebutton: # Go roofroom
        pos (922, 115)
        idle "images/fr3upstairsmiddleblank.webp"
        hover "images/fr3upstairsmiddle.webp"
        action Show("v6_fr3roofroom")

    imagebutton: #chloe button
        ypos 25
        xpos 490
        idle "images/fr3upstairsleftblank.webp"
        hover "images/fr3upstairsleft.webp"

        if not fr3chloe:
            action Jump("v6_fr3chloe1")
        else:
            action Jump("v6_fr3chloe2")


screen v6_fr3office():
    tag v6_freeroam

    add "images/fr3office.webp" # location picture

    imagebutton: # Go back out of office
        pos (440, 847)
        idle "images/fr3officebackblank.webp"
        hover "images/fr3officeback.webp"
        action Show("v6_fr3upstairs")

    imagebutton: # picture
        pos (100, 115)
        idle "images/fr3officephotoblank.webp"
        hover "images/fr3officephoto.webp"
        action Jump("v6_fr3picture")

    imagebutton: # certificate
        pos (1240, 212)
        idle "images/fr3officecertificateblank.webp"
        hover "images/fr3officecertificate.webp"
        action Jump("v6_fr3certificate")

    imagebutton: # books
        pos (1382, 593)
        idle "images/fr3officebooksblank.webp"
        hover "images/fr3officebooks.webp"
        action Jump("v6_fr3books")

    imagebutton: # trophies
        xpos 1480
        yalign 1.0
        idle "images/fr3officetrophyblank.webp"
        hover "images/fr3officetrophy.webp"
        action Jump("v6_fr3trophies")


screen v6_fr3roofroom():
    tag v6_freeroam

    add "images/fr3roofroom.webp" # location picture

    imagebutton: # Go back
        xpos 500
        yalign 1.0
        idle "images/fr3roofroombackblank.webp"
        hover "images/fr3roofroomback.webp"
        action Show("v6_fr3upstairs")

    imagebutton: #Window (Nora) button
        pos (327, 50)
        idle "images/fr3roofroomwindowblank.webp"
        hover "images/fr3roofroomwindow.webp"

        if not fr3nora:
            action Jump ("v6_fr3nora1")
        else:
            action Jump ("v6_fr3nora2")
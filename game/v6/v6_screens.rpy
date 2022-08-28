screen v6_fr3garden():
    tag free_roam
    
    if not upstairs == "amber":
        add "images/v6/fr3garden.webp" # location picture

        # Josh button
        imagebutton:
            pos (1195, 430)
            idle "images/v6/fr3gardenjoshblank.webp"
            hover "images/v6/fr3gardenjosh.webp"

            if not "josh" in freeroam3:
                action Jump("v6_fr3josh1")

            elif relics >= 5 and upstairs == "nobody" and not "kim" in freeroam3asked: # Asking people for upstairs
                action Jump("v6_fr3josh3")
            else:
                action Jump("v6_fr3josh2")

    else:
        add "images/v6/fr3garden2.webp"

    # Go inside
    imagebutton:
        pos (485, 190)
        idle "images/v6/fr3gardendoorblank.webp"
        hover "images/v6/fr3gardendoor.webp"
        action Show("v6_fr3downstairs")

    if config_debug:
        python:
            actions = []

            if not "josh" in freeroam3:
                actions.append(Jump("v6_fr3josh1"))
            elif relics >= 5 and upstairs == "nobody" and not "kim" in freeroam3asked: # Asking people for upstairs
                actions.append(Jump("v6_fr3josh3"))

            actions.append(Show("v6_fr3downstairs"))

        timer 0.1 action renpy.random.choice(actions)


screen v6_fr3downstairs():
    tag free_roam

    add "images/v6/fr3downstairs.webp" # location picture

    imagebutton: #Go outside
        pos (440, 900)
        idle "images/v6/fr3downstairsbackblank.webp"
        hover "images/v6/fr3downstairsback.webp"
        action Show("v6_fr3garden")

    imagebutton: #Go upstairs
        xpos 940
        idle "images/v6/fr3downstairsstairsblank.webp"
        hover "images/v6/fr3downstairsstairs.webp"
        action Show("v6_fr3upstairs")

    imagebutton: #Go living room
        pos (360, 70)
        idle "images/v6/fr3downstairsdoorblank.webp"
        hover "images/v6/fr3downstairsdoor.webp"
        action Show("v6_fr3livingroom")

    imagebutton: #Go kitchen
        pos (1486, 368)
        idle "images/v6/fr3downstairsrightblank.webp"
        hover "images/v6/fr3downstairsright.webp"
        action Show("v6_fr3kitchen")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v6_fr3garden", "v6_fr3upstairs", "v6_fr3livingroom", "v6_fr3kitchen")))


screen v6_fr3livingroom():
    tag free_roam

    add "images/v6/fr3livingroom.webp" # location picture

    # Guy1 button
    imagebutton: 
        pos (760, 392)
        idle "images/v6/fr3livingroomsofablank.webp"
        hover "images/v6/fr3livingroomsofa.webp"

        if not "peter" in freeroam3:
            action Jump("v6_fr3guy1")
        else:
            action Jump("v6_fr3guy2")

    # Aubrey button
    imagebutton:
        pos (804, 254)
        idle "images/v6/fr3livingroomaubreyblank.webp"
        hover "images/v6/fr3livingroomaubrey.webp"

        if not "aubrey" in freeroam3:
            action Jump("v6_fr3aubrey1")
        elif relics >= 5 and upstairs == "nobody": # Asking people for upstairs
            action Jump("v6_fr3aubrey3")
        else:
            action Jump("v6_fr3aubrey2")

    # Go back
    imagebutton:
        ypos 915
        xpos 432
        idle "images/v6/fr3livingroombackblank.webp"
        hover "images/v6/fr3livingroomback.webp"
        action Show("v6_fr3downstairs")

    # Go kitchen
    imagebutton:
        ypos 106
        xpos 1700
        idle "images/v6/fr3livingroomdoorblank.webp"
        hover "images/v6/fr3livingroomdoor.webp"
        action Show("v6_fr3kitchen")

    if config_debug:
        python:
            actions = []

            if not "peter" in freeroam3:
                actions.append(Jump("v6_fr3guy1"))

            if not "aubrey" in freeroam3:
                actions.append(Jump("v6_fr3aubrey1"))
            elif relics >= 5 and upstairs == "nobody": # Asking people for upstairs
                actions.append(Jump("v6_fr3aubrey3"))

            actions.append(Show("v6_fr3downstairs"))

            actions.append(Show("v6_fr3kitchen"))

        timer 0.1 action renpy.random.choice(actions)


screen v6_fr3kitchen():
    tag free_roam

    add "images/v6/fr3kitchen.webp" # location picture

    imagebutton: #chris button
        pos (1147, 60)
        idle "images/v6/fr3kitchenchrisblank.webp"
        hover "images/v6/fr3kitchenchrisn.webp"

        if not "chris" in freeroam3:
            action Jump("v6_fr3chris1")
        else:
            action Show("confirm", message=_("Are you sure you want to end the free roam?"), yes_action=[Hide("confirm"), Jump("v6_fr3chris3")])

    imagebutton: #Matt button
        pos (1048, 139)
        idle "images/v6/fr3kitchenmattblank.webp"
        hover "images/v6/fr3kitchenmatt.webp"

        if not "matt" in freeroam3:
            action Jump("v6_fr3matt1")
        else:
            action Jump("v6_fr3matt2")

    imagebutton: # Go Kitchen 2
        ypos 99
        idle "images/v6/fr3kitchenleftblank.webp"
        hover "images/v6/fr3kitchenleft.webp"
        action Show("v6_fr3kitchen2")

    imagebutton: # Go Living room
        ypos 100
        idle "images/v6/fr3kitchenlivingdoorblank.webp"
        hover "images/v6/fr3kitchenlivingdoor.webp"
        action Show("v6_fr3livingroom")

    imagebutton: #Riley button
        pos (328, 270)
        idle "images/v6/fr3kitchenrileyblank.webp"
        hover "images/v6/fr3kitchenriley.webp"

        if not "riley" in freeroam3:
            action Jump("v6_fr3riley1")
        elif relics >= 5 and upstairs == "nobody" and not "riley" in freeroam3asked: # Asking people for upstairs
            action Jump("v6_fr3riley3")
        else:
            action Jump("v6_fr3riley2")

    if config_debug:
        python:
            actions = []

            if not "chris" in freeroam3:
                actions.append(Jump("v6_fr3chris1"))
            else:
                actions.append(Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v6_fr3chris3")]))

            if not "matt" in freeroam3:
                actions.append(Jump("v6_fr3matt1"))

            actions.append(Show("v6_fr3kitchen2"))

            actions.append(Show("v6_fr3livingroom"))

            if not "riley" in freeroam3:
                actions.append(Jump("v6_fr3riley1"))
            elif relics >= 5 and upstairs == "nobody" and not "riley" in freeroam3asked: # Asking people for upstairs
                actions.append(Jump("v6_fr3riley3"))

        timer 0.1 action renpy.random.choice(actions)


screen v6_fr3kitchen2():
    tag free_roam

    add "images/v6/fr3kitchen2.webp" # location picture

    imagebutton: # Go Ktichen
        pos (358, 836)
        idle "images/v6/fr3kitchen2backblank.webp"
        hover "images/v6/fr3kitchen2back.webp"
        action Show("v6_fr3kitchen")

    imagebutton: # Go Middleroom
        ypos 65
        xpos 0
        idle "images/v6/fr3kitchen2doorblank.webp"
        hover "images/v6/fr3kitchen2door.webp"
        action Show("v6_fr3middleroom")

    imagebutton: # Go downstairs hallway
        ypos 245
        xpos 1364
        idle "images/v6/fr3kitchen2rightblank.webp"
        hover "images/v6/fr3kitchen2right.webp"
        action Show("v6_fr3downstairs")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v6_fr3kitchen", "v6_fr3middleroom", "v6_fr3downstairs")))


screen v6_fr3middleroom():
    tag free_roam

    add "images/v6/fr3middleroom.webp" # location picture

    imagebutton: # Go Kitchen2
        xpos 50
        idle "images/v6/fr3middleroomleftblank.webp"
        hover "images/v6/fr3middleroomleft.webp"
        action Show("v6_fr3kitchen2")

    imagebutton: # Downstairs bathroom
        ypos 106
        xpos 700
        idle "images/v6/fr3middleroommiddleblank.webp"
        hover "images/v6/fr3middleroommiddle.webp"
        action Jump("v6_fr3dsbathroom")

    imagebutton: # Go garage
        xpos 1210
        idle "images/v6/fr3middleroomrightblank.webp"
        hover "images/v6/fr3middleroomright.webp"
        action Show("v6_fr3garage")

    if config_debug:
        $ actions = (Show("v6_fr3kitchen2"), Jump("v6_fr3dsbathroom"), Show("v6_fr3garage"))

        timer 0.1 action renpy.random.choice(actions)


screen v6_fr3garage():
    tag free_roam

    if not upstairs == "amber":
        add "images/v6/fr3garage.webp" # location picture

        imagebutton: #Amber button
            pos (345, 235)
            idle "images/v6/fr3garageamberblank.webp"
            hover "images/v6/fr3garageamber.webp"

            if not "amber" in freeroam3:
                action Jump("v6_fr3amber1")

            elif relics >= 5 and upstairs == "nobody" and not "amber" in freeroam3asked: #Asking people for upstairs
                action Jump("v6_fr3amber3")
            else:
                action Jump("v6_fr3amber2")

    else:
        add "images/v6/fr3garage2.webp"

    imagebutton: #sebastian button
        ypos 168
        xpos 1338
        idle "images/v6/fr3garagefightblank.webp"
        hover "images/v6/fr3garagefight.webp"

        if not "sebastian" in freeroam3:
            action Jump("v6_fr3sebastian1")
        else:
            action Jump("v6_fr3sebastian2")

    imagebutton: # Go back to middleroom
        ypos 877
        xpos 473
        idle "images/v6/fr3garagebackblank.webp"
        hover "images/v6/fr3garageback.webp"
        action Show("v6_fr3middleroom")

    if config_debug:
        python:
            actions = []

            if not upstairs == "amber":
                if not "amber" in freeroam3:
                    actions.append(Jump("v6_fr3amber1"))

                elif relics >= 5 and upstairs == "nobody" and not "amber" in freeroam3asked: #Asking people for upstairs
                    actions.append(Jump("v6_fr3amber3"))


            if not "sebastian" in freeroam3:
                actions.append(Jump("v6_fr3sebastian1"))

            actions.append(Show("v6_fr3middleroom"))

        timer 0.1 action renpy.random.choice(actions)


screen v6_fr3upstairs():
    tag free_roam

    add "images/v6/fr3upstairs.webp" # location picture

    imagebutton: # Go backdownstairs
        align (0.5, 1.0)
        idle "images/v6/fr3upstairsbackblank.webp"
        hover "images/v6/fr3upstairsback.webp"
        action Show("v6_fr3downstairs")

    imagebutton: # go office
        pos (1125, 140)
        idle "images/v6/fr3upstairsrightblank.webp"
        hover "images/v6/fr3upstairsright.webp"
        action Jump("v6_fr3office")

    imagebutton: # Go roofroom
        pos (922, 115)
        idle "images/v6/fr3upstairsmiddleblank.webp"
        hover "images/v6/fr3upstairsmiddle.webp"
        action Show("v6_fr3roofroom")

    imagebutton: #chloe button
        ypos 25
        xpos 490
        idle "images/v6/fr3upstairsleftblank.webp"
        hover "images/v6/fr3upstairsleft.webp"

        if not "chloe" in freeroam3:
            action Jump("v6_fr3chloe1")
        else:
            action Jump("v6_fr3chloe2")

    if config_debug:
        python:
            actions = []

            actions.append(Show("v6_fr3downstairs"))
            actions.append(Jump("v6_fr3office"))
            actions.append(Show("v6_fr3roofroom"))

            if not "chloe" in freeroam3:
                actions.append(Jump("v6_fr3chloe1"))

        timer 0.1 action renpy.random.choice(actions)


screen v6_fr3office():
    tag free_roam

    add "images/v6/fr3office.webp" # location picture

    imagebutton: # Go back out of office
        pos (440, 847)
        idle "images/v6/fr3officebackblank.webp"
        hover "images/v6/fr3officeback.webp"
        action Show("v6_fr3upstairs")

    imagebutton: # picture
        pos (100, 115)
        idle "images/v6/fr3officephotoblank.webp"
        hover "images/v6/fr3officephoto.webp"
        action Jump("v6_fr3picture")

    imagebutton: # certificate
        pos (1240, 212)
        idle "images/v6/fr3officecertificateblank.webp"
        hover "images/v6/fr3officecertificate.webp"
        action Jump("v6_fr3certificate")

    imagebutton: # books
        pos (1382, 593)
        idle "images/v6/fr3officebooksblank.webp"
        hover "images/v6/fr3officebooks.webp"
        action Jump("v6_fr3books")

    imagebutton: # trophies
        xpos 1480
        yalign 1.0
        idle "images/v6/fr3officetrophyblank.webp"
        hover "images/v6/fr3officetrophy.webp"
        action Jump("v6_fr3trophies")

    if config_debug:
        python:
            actions = []

            actions.append(Show("v6_fr3downstairs"))
            actions.append(Jump("v6_fr3office"))
            actions.append(Show("v6_fr3roofroom"))

            if not "chloe" in freeroam3:
                actions.append(Jump("v6_fr3chloe1"))

        timer 0.1 action renpy.random.choice(actions)


screen v6_fr3roofroom():
    tag free_roam

    add "images/v6/fr3roofroom.webp" # location picture

    imagebutton: # Go back
        xpos 500
        yalign 1.0
        idle "images/v6/fr3roofroombackblank.webp"
        hover "images/v6/fr3roofroomback.webp"
        action Show("v6_fr3upstairs")

    imagebutton: #Window (Nora) button
        pos (327, 50)
        idle "images/v6/fr3roofroomwindowblank.webp"
        hover "images/v6/fr3roofroomwindow.webp"

        if not "nora" in freeroam3:
            action Jump ("v6_fr3nora1")
        else:
            action Jump ("v6_fr3nora2")

    if config_debug:
        python:
            actions = []

            actions.append(Show("v6_fr3upstairs"))

            if not "nora" in freeroam3:
                actions.append(Jump("v6_fr3nora1"))

        timer 0.1 action renpy.random.choice(actions)


screen emilysexoverlay():

    default overlay = True

    if overlay:
        textbutton "hide overlay":
            xpos 250
            action SetScreenVariable("overlay", False)
    else:
        textbutton "show overlay":
            xpos 10
            action SetScreenVariable("overlay", True)

    if overlay:
        vpgrid:
            cols 1
            pos (10, 10)
            mousewheel True
            draggable True

            imagebutton:
                idle "images/v6/emhead.webp"
                action Jump("emhead")

            imagebutton:
                idle "images/v6/emfacefuck.webp"
                action Jump("emfacefuck")

            imagebutton:
                idle "images/v6/embehind.webp"
                action Jump("embehind")

            imagebutton:
                idle "images/v6/embutterfly.webp"
                action Jump("embutterfly")

            imagebutton:
                idle "images/v6/emclimax.webp"
                action Jump("emclimax")


screen aubreysexoverlay():

    default overlay = True

    if overlay:
        textbutton "hide overlay":
            xpos 250
            action SetScreenVariable("overlay", False)
    else:
        textbutton "show overlay":
            xpos 10
            action SetScreenVariable("overlay", True)

    if overlay:
        vpgrid:
            cols 1
            pos (10, 10)
            
            mousewheel True
            draggable True

            imagebutton:
                idle "images/v6/naubblowjob.webp"
                action Jump ("naubblowjob")

            imagebutton:
                idle "images/v6/naub69.webp"
                action Jump ("naub69")

            imagebutton:
                idle "images/v6/naubfingering.webp"
                action Jump ("naubfingering")

            imagebutton:
                idle "images/v6/naubmissionary.webp"
                action Jump ("naubmissionary")

            imagebutton:
                idle "images/v6/naubbehind.webp"
                action Jump ("naubbehind")

            imagebutton:
                idle "images/v6/naubclimax.webp"
                action Jump ("naubclimax")

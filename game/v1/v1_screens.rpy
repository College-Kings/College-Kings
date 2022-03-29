screen v1_freeRoam1_1():
    tag free_roam

    add "images/v1/s50.webp"

    # Riley character
    imagebutton:
        align (0.86, 0.12)
        idle "images/v1/fr1riley.webp"
        hover "images/v1/fr1rileyhover.webp"

        if not "riley" in freeroam1:
            action [Hide("tutorial"), Jump("v1_freeRoam1_riley")]
        else:
            action Jump("v1_freeRoam1_riley2")

    # Elijah character
    imagebutton:
        align (0.335, 0.195)
        idle "images/v1/fr1elijah.webp"
        hover "images/v1/fr1elijahoverh.webp"

        if not "elijah" in freeroam1:
            action [Hide("tutorial"), Jump("v1_freeRoam1_elijah")]
        else:
            action Jump("v1_freeRoam1_elijah2")

    # Next room
    imagebutton:
        yalign 0.07
        xalign 0.65
        idle "images/v1/fr1b.webp"
        hover "images/v1/fr1bhover.webp"
        action [Hide("tutorial"), Show("v1_freeRoam1_2")]


screen v1_freeRoam1_2():
    tag free_roam

    if not "chris" in freeroam1:
        add "images/v1/s55.webp"

        # Chris + Nora characters
        imagebutton:
            align (0.685, 0.5)
            idle "images/v1/fr1chris.webp"
            hover "images/v1/fr1chrishover.webp"
            action Jump("v1_freeRoam1_chris")

    else:
        add "images/v1/s56.webp"

        # Nora character
        imagebutton:
            yalign 0.53
            xalign 0.74
            idle "images/v1/fr1nora.webp"
            hover "images/v1/fr1norahover.webp"
            if not "nora" in freeroam1:
                action Jump("v1_freeRoam1_nora")
            else:
                action Jump("v1_freeRoam1_nora2")

    # Next room
    imagebutton:
        yalign 0.38
        xalign 0.21
        idle "images/v1/fr1c.webp"
        hover "images/v1/fr1chover.webp"
        action Show("v1_freeRoam1_3")

    # Back
    imagebutton:
        yalign 1.0
        xalign 0.23
        idle "images/v1/backchris.webp"
        hover "images/v1/backchrishover.webp"
        action Show("v1_freeRoam1_1")


screen v1_freeRoam1_3():
    tag free_roam

    add "images/v1/s58.webp"

    # Left Dorm
    imagebutton:
        yalign 0.025
        xalign 0.26
        idle "images/v1/fr1dorm.webp"
        hover "images/v1/fr1dormhover.webp"
        if not "aubrey" in freeroam1:
            action Jump("v1_freeRoam1_aubrey")
        else:
            action Jump("v1_freeRoam1_aubrey2")

    # MC Dorm
    imagebutton:
        yalign 0.05
        xalign 0.82
        idle "images/v1/fr1yours.webp"
        hover "images/v1/fr1yourshover.webp"
        action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("efra")])

    # Back
    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/v1/dormback.webp"
        hover "images/v1/dormbackhover.webp"
        action Show("v1_freeRoam1_2")


screen v1_freeRoam2_1(): # outside
    tag free_roam

    if not "sam" in freeroam2:
        add "images/v1/s100.webp"
    else:
        add "images/v1/s100a.webp"

    # Sam + Karen characters
    imagebutton:
        align (0.43, 1.0)
        idle "images/v1/fr2sam.webp"
        hover "images/v1/fr2samh.webp"
        if not "sam" in freeroam2:
            action Jump("v1_freeRoam2_sam")
        else:
            action Jump("v1_freeRoam2_sam2")

    # Front door
    imagebutton:
        yalign 0
        xalign 0.482
        idle "images/v1/fr2door.webp" #inside
        hover "images/v1/fr2doorh.webp"
        if not "door" in freeroam2:
            action Jump("v1_freeRoam2_door")
        else:
            action Show("v1_freeRoam2_2")


screen v1_freeRoam2_2():
    tag free_roam

    add "images/v1/s102.webp"

    # Josh + Aubrey
    imagebutton:
        align (0.515, 1.0)
        idle "images/v1/fr2josh.webp"
        hover "images/v1/fr2joshh.webp"
        if not "josh" in freeroam2:
            action Jump("v1_freeRoam2_josh")
        else:
            action Jump("v1_freeRoam2_josh2")

    # Pool room
    imagebutton:
        align (1.0, 1.0)
        idle "images/v1/fr2pool.webp"
        hover "images/v1/fr2poolh.webp"
        action Jump("v1_freeRoam2_pool")

    # Back outside
    imagebutton:
        align (0.5, 1.0)
        idle "images/v1/fr2outside.webp" 
        hover "images/v1/fr2outsideh.webp"
        action Show("v1_freeRoam2_1")

    # Courtney character
    imagebutton:
        align (0.242, 0.4)
        idle "images/v1/fr2courtney.webp"
        hover "images/v1/fr2courtneyh.webp"
        if not "courtney" in freeroam2:
            action Jump("v1_freeRoam2_courtney")
        else:
            action Jump("v1_freeRoam2_courtney2")

    # Left room
    imagebutton:
        align (0, 1.0)
        idle "images/v1/fr2camp.webp"
        hover "images/v1/fr2camph.webp"
        action Jump("v1_freeRoam2_camp")

    # Stairs
    imagebutton:
        align (0.42, 0)
        idle "images/v1/fr2stairs.webp"
        hover "images/v1/fr2stairsh.webp"
        action Jump("v1_freeRoam2_stairs")


screen v1_freeRoam2_3():
    tag free_roam

    add "images/v1/s104.webp"

    # Mason character
    imagebutton:
        align (1.0, 1.0)
        idle "images/v1/fr2mason.webp"
        hover "images/v1/fr2masonh.webp"
        if not "mason" in freeroam2:
            action Jump("v1_freeRoam2_mason")
        else:
            action Jump("v1_freeRoam2_mason2")

    # Katy character
    imagebutton:
        align (0.52, 0.38)
        idle "images/v1/fr2katy.webp"
        hover "images/v1/fr2katyh.webp"
        if not "katy" in freeroam2:
            action Jump("v1_freeRoam2_katy")
        else:
            action Jump("v1_freeRoam2_katy2")

    # Back - Hallway
    imagebutton:
        align (0.5, 1.0)
        idle "images/v1/backpool.webp"
        hover "images/v1/backpoolh.webp"
        action Show("v1_freeRoam2_2")

screen v1_freeRoam2_4():
    tag free_roam

    add "images/v1/s106.webp"

    # Chloe character
    imagebutton:
        yalign 1.0
        xalign 0.21
        idle "images/v1/fr2chloe.webp"
        hover "images/v1/fr2chloeh.webp"
        action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v1_freeRoam2_end")])

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/v1/fr2campback.webp"
        hover "images/v1/fr2campbackh.webp"
        action Show("v1_freeRoam2_2")

screen v1_freeRoam2_5():
    tag free_roam

    add "images/v1/s105.webp"

    # Grayson room
    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/v1/fr2grayson.webp"
        hover "images/v1/fr2graysonh.webp"
        if not "grayson" in freeroam2:
            action Jump("v1_freeRoam2_grayson")
        else:
            action Jump("v1_freeRoam2_grayson2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/v1/fr2down.webp"
        hover "images/v1/fr2downh.webp"
        action Show("v1_freeRoam2_2")

screen nsfw_Toggle():
    

    add "gui/frame.webp":
        align (0.5,0.5)
        ysize 350

    vbox:
        xsize 700
        align (0.5, 0.5)
        spacing 20
        text "Explicit Sex Scenes":
            #color "#FFD166"
            size 40
            text_align 0.5
            xalign 0.5

        text "This game contains fully explicit sex scenes. These are not suitable for Twitch or Youtube. Please select if you'd like to enable explicit sex scenes.":
            font "fonts/OpenSans.ttf"
            size 25
            text_align 0.5
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            textbutton "Enable":
                text_size 40
                selected False
                action [SetVariable("config_censored", False), Return()]
            textbutton "Disable":
                text_size 40
                selected False
                action [SetVariable("config_censored", True), Return()]
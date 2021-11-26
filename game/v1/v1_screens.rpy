screen v1_freeRoam1_1():
    tag v1_freeRoam1

    add "images/s50.webp"

    # Riley character
    imagebutton:
        align (0.86, 0.12)
        idle "images/fr1riley.webp"
        hover "images/fr1rileyhover.webp"

        if not v1_freeRoam1_riley:
            action [Hide("freeRoamTutorial"), Jump("v1_freeRoam1_riley")]
        else:
            action Jump("v1_freeRoam1_riley2")

    # Elijah character
    imagebutton:
        align (0.335, 0.195)
        idle "images/fr1elijah.webp"
        hover "images/fr1elijahoverh.webp"

        if not v1_freeRoam1_elijah:
            action [Hide("freeRoamTutorial"), Jump("v1_freeRoam1_elijah")]
        else:
            action Jump("v1_freeRoam1_elijah2")

    # Next room
    imagebutton:
        yalign 0.07
        xalign 0.65
        idle "images/fr1b.webp"
        hover "images/fr1bhover.webp"
        action [Hide("freeRoamTutorial"), Show("v1_freeRoam1_2")]


screen v1_freeRoam1_2():
    tag v1_freeRoam1

    if not v1_freeRoam1_chrisGone:
        add "images/s55.webp"

        # Chris + Nora characters
        imagebutton:
            align (0.685, 0.5)
            idle "images/fr1chris.webp"
            hover "images/fr1chrishover.webp"
            action Jump("v1_freeRoam1_chris")

    else:
        add "images/s56.webp"

        # Nora character
        imagebutton:
            yalign 0.53
            xalign 0.74
            idle "images/fr1nora.webp"
            hover "images/fr1norahover.webp"
            if not v1_freeRoam1_nora:
                action Jump("v1_freeRoam1_nora")
            else:
                action Jump("v1_freeRoam1_nora2")

    # Next room
    imagebutton:
        yalign 0.38
        xalign 0.21
        idle "images/fr1c.webp"
        hover "images/fr1chover.webp"
        action Show("v1_freeRoam1_3")

    # Back
    imagebutton:
        yalign 1.0
        xalign 0.23
        idle "images/backchris.webp"
        hover "images/backchrishover.webp"
        action Show("v1_freeRoam1_1")


screen v1_freeRoam1_3():
    tag v1_freeRoam1

    add "images/s58.webp"

    # Left Dorm
    imagebutton:
        yalign 0.025
        xalign 0.26
        idle "images/fr1dorm.webp"
        hover "images/fr1dormhover.webp"
        if not v1_freeRoam1_aubrey:
            action Jump("v1_freeRoam1_aubrey")
        else:
            action Jump("v1_freeRoam1_aubrey2")

    # MC Dorm
    imagebutton:
        yalign 0.05
        xalign 0.82
        idle "images/fr1yours.webp"
        hover "images/fr1yourshover.webp"
        action Show("endFreeRoamConfirm", continueLabel="efra")

    # Back
    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/dormback.webp"
        hover "images/dormbackhover.webp"
        action Show("v1_freeRoam1_2")


screen v1_freeRoam2_1(): # outside
    tag free_roam

    if not v1_samTalk:
        add "images/s100.webp"
    else:
        add "images/s100a.webp"

    # Sam + Karen characters
    imagebutton:
        align (0.43, 1.0)
        idle "images/fr2sam.webp"
        hover "images/fr2samh.webp"
        if not v1_samTalk:
            action Jump("v1_freeRoam2_sam")
        else:
            action Jump("v1_freeRoam2_sam2")

    # Front door
    imagebutton:
        yalign 0
        xalign 0.482
        idle "images/fr2door.webp" #inside
        hover "images/fr2doorh.webp"
        if not v1_fr2door:
            action Jump("v1_freeRoam2_door")
        else:
            action Show("v1_freeRoam2_2")


screen v1_freeRoam2_2():
    tag free_roam

    add "images/s102.webp"

    # Josh + Aubrey
    imagebutton:
        align (0.515, 1.0)
        idle "images/fr2josh.webp"
        hover "images/fr2joshh.webp"
        if not v1_joshTalk:
            action Jump("v1_freeRoam2_josh")
        else:
            action Jump("v1_freeRoam2_josh2")

    # Pool room
    imagebutton:
        align (1.0, 1.0)
        idle "images/fr2pool.webp"
        hover "images/fr2poolh.webp"
        action Jump("v1_freeRoam2_pool")

    # Back outside
    imagebutton:
        align (0.5, 1.0)
        idle "images/fr2outside.webp" 
        hover "images/fr2outsideh.webp"
        action Show("v1_freeRoam2_1")

    # Courtney character
    imagebutton:
        align (0.242, 0.4)
        idle "images/fr2courtney.webp"
        hover "images/fr2courtneyh.webp"
        if not v1_courtneyTalk:
            action Jump("v1_freeRoam2_courtney")
        else:
            action Jump("v1_freeRoam2_courtney2")

    # Left room
    imagebutton:
        align (0, 1.0)
        idle "images/fr2camp.webp"
        hover "images/fr2camph.webp"
        action Jump("v1_freeRoam2_camp")

    # Stairs
    imagebutton:
        align (0.42, 0)
        idle "images/fr2stairs.webp"
        hover "images/fr2stairsh.webp"
        action Jump("v1_freeRoam2_stairs")


screen v1_freeRoam2_3():
    tag free_roam

    add "images/s104.webp"

    # Mason character
    imagebutton:
        align (1.0, 1.0)
        idle "images/fr2mason.webp"
        hover "images/fr2masonh.webp"
        if not v1_masonTalk:
            action Jump("v1_freeRoam2_mason")
        else:
            action Jump("v1_freeRoam2_mason2")

    # Katy character
    imagebutton:
        align (0.52, 0.38)
        idle "images/fr2katy.webp"
        hover "images/fr2katyh.webp"
        if not v1_katyTalk:
            action Jump("v1_freeRoam2_katy")
        else:
            action Jump("v1_freeRoam2_katy2")

    # Back - Hallway
    imagebutton:
        align (0.5, 1.0)
        idle "images/backpool.webp"
        hover "images/backpoolh.webp"
        action Show("v1_freeRoam2_2")

screen v1_freeRoam2_4():
    tag free_roam

    add "images/s106.webp"

    # Chloe character
    imagebutton:
        yalign 1.0
        xalign 0.21
        idle "images/fr2chloe.webp"
        hover "images/fr2chloeh.webp"
        action Show("endFreeRoamConfirm", continueLabel="v1_freeRoam2_end")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr2campback.webp"
        hover "images/fr2campbackh.webp"
        action Show("v1_freeRoam2_2")

screen v1_freeRoam2_5():
    tag free_roam

    add "images/s105.webp"

    # Grayson room
    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr2grayson.webp"
        hover "images/fr2graysonh.webp"
        if not v1_graysonTalk:
            action Jump("v1_freeRoam2_grayson")
        else:
            action Jump("v1_freeRoam2_grayson2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr2down.webp"
        hover "images/fr2downh.webp"
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
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
    tag v1_freeRoam2

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
            action Jump("fr2courtney2")

    imagebutton:
        yalign 1.0
        xalign 0
        idle "images/fr2camp.webp"
        hover "images/fr2camph.webp"
        action Jump ("fr2camp")

    imagebutton:
        yalign 0
        xalign 0.42
        idle "images/fr2stairs.webp"
        hover "images/fr2stairsh.webp"
        action Jump ("fr2stairs")


screen v1_freeRoam2_3():

    add "images/s104.webp"

    imagebutton:
        yalign 1.0
        xalign 1.0
        idle "images/fr2mason.webp"
        hover "images/fr2masonh.webp"
        if masontalk == 1:
            action Jump ("fr2mason2")
        else:
            action Jump ("fr2mason")

    imagebutton:
        yalign 0.38
        xalign 0.52
        idle "images/fr2katy.webp"
        hover "images/fr2katyh.webp"
        if katytalk == 1:
            action Jump ("fr2katy2")
        else:
            action Jump ("fr2katy")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/backpool.webp"
        hover "images/backpoolh.webp"
        action Jump ("fr2poolback")

screen freeroam2d(): ###camp room

    add "images/s106.webp"

    imagebutton:
        yalign 1.0
        xalign 0.21
        idle "images/fr2chloe.webp"
        hover "images/fr2chloeh.webp"
        action Jump ("fr2chloe")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr2campback.webp"
        hover "images/fr2campbackh.webp"
        action Jump ("fr2campback")

screen freeroam2e(): ###stairs

    add "images/s105.webp"

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr2grayson.webp"
        hover "images/fr2graysonh.webp"
        if graysontalk == 1:
            action Jump ("fr2grayson2")
        else:
            action Jump ("fr2grayson")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr2down.webp"
        hover "images/fr2downh.webp"
        action Jump ("fr2down")

screen endfreeroam2():
    add "images/endfr.webp"
    text "Are you sure you want to end free roam?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("fr2end")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("fr2dontend")
        text_align 0.5
        xalign 0.43
        yalign 0.58
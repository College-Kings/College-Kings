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
        action Jump("fr1b2")
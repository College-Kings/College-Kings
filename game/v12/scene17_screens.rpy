screen v12s17_lindsey_sex_overlay():

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
                idle "images/v12/Scene 17/overlay_buttons/handjob.webp"
                action Jump("v12s17_lindsey_handjob")

            imagebutton:
                idle "images/v12/Scene 17/overlay_buttons/blowjob.webp"
                action Jump("v12s17_lindsey_blowjob")

            imagebutton:
                idle "images/v12/Scene 17/overlay_buttons/sixty_nine.webp"
                action Jump("v12s17_lindsey_sixty_nine")
screen v12s29_lauren_sex_overlay():

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
                idle "images/v12/Scene 29/overlay_buttons/fingering.webp"
                action Jump("v12s29_lauren_fingering")

            imagebutton:
                idle "images/v12/Scene 29/overlay_buttons/blowjob.webp"
                action Jump("v12s29_lauren_blowjob")

            imagebutton:
                idle "images/v12/Scene 29/overlay_buttons/legs_up.webp"
                action Jump("v12s29_lauren_legs_up")

            imagebutton:
                idle "images/v12/Scene 29/overlay_buttons/cowgirl.webp"
                action Jump("v12s29_lauren_cowgirl")
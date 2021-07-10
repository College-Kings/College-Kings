screen v9s16_emilySexOverlay():

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
                idle "images/v9/Scene 16/Overlay Buttons/blowjob.webp"
                action Jump("v9s16_emilyBlowjob")

            imagebutton:
                idle "images/v9/Scene 16/Overlay Buttons/missionary.webp"
                action Jump("v9s16_emilyMissionary")

            imagebutton:
                idle "images/v9/Scene 16/Overlay Buttons/cowgirl.webp"
                action Jump("v9s16_emilyCowgirl")

            imagebutton:
                idle "images/v9/Scene 16/Overlay Buttons/doggy.webp"
                action Jump("v9s16_emilyDoggy")
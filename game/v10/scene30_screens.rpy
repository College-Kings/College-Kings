screen v10s30_chloeSexOverlay():

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
                idle "images/v10/Scene 30/Overlay Buttons/licking.webp"
                action Jump("v10s30_chloeLicking")

            imagebutton:
                idle "images/v10/Scene 30/Overlay Buttons/blowjob.webp"
                action Jump("v10s30_chloeBlowjob")
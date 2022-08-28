screen v8s30_amberSexOverlay():

    default overlay = True

    if overlay:
        textbutton _("hide overlay"):
            xpos 250
            action SetScreenVariable("overlay", False)
    else:
        textbutton _("show overlay"):
            xpos 10
            action SetScreenVariable("overlay", True)

    if overlay:
        vpgrid:
            cols 1
            pos (10, 10)
            mousewheel True
            draggable True

            imagebutton:
                idle "images/v8/Scene 30/Overlay Buttons/blowjob.webp"
                action Jump("v8s30_amberBlowjob")

            imagebutton:
                idle "images/v8/Scene 30/Overlay Buttons/cowgirl.webp"
                action Jump("v8s30_amberCowgirl")

            imagebutton:
                idle "images/v8/Scene 30/Overlay Buttons/anal.webp"
                action Jump("v8s30_amberAnal")
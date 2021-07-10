screen v8s5_amberSexOverlay():

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
                idle "images/v8/Scene 5/Overlay Buttons/blowjob.webp"
                action Jump("v8s5_amberBlowjob")

            imagebutton:
                idle "images/v8/Scene 5/Overlay Buttons/missionary.webp"
                action Jump("v8s5_amberMissonary")

            imagebutton:
                idle "images/v8/Scene 5/Overlay Buttons/facefuck.webp"
                action Jump("v8s5_amberFacefuck")
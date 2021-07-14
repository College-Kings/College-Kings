screen v10s40_rileySexOverlay():

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
                idle "images/v9/Scene 34/Overlay Buttons/reverse.webp"
                action Jump("v10s40_rileyReverse")

            imagebutton:
                idle "images/v9/Scene 34/Overlay Buttons/cowgirl.webp"
                action Jump("v10s40_rileyCowgirl")
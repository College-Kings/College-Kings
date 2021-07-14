screen v10s17_aubreySexOverlay():

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
                idle "images/v10/Scene 17/Overlay Buttons/blowjob.webp"
                action Jump("v10s17_aubreyBlowjob")

            imagebutton:
                idle "images/v10/Scene 17/Overlay Buttons/cowgirl.webp"
                action Jump("v10s17_aubreyCowgirl")

            imagebutton:
                idle "images/v10/Scene 17/Overlay Buttons/standing.webp"
                action Jump("v10s17_aubreyStanding")
screen v9s34_rileySexOverlay():

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
                idle "images/v9/Scene 34/Overlay Buttons/blowjob.webp"
                action Jump("v9s34_rileyBlowjob")

            imagebutton:
                idle "images/v9/Scene 34/Overlay Buttons/licking.webp"
                action Jump("v9s34_rileyLicking")

            imagebutton:
                idle "images/v9/Scene 34/Overlay Buttons/missionary.webp"
                action Jump("v9s34_rileyMissionary")

            imagebutton:
                idle "images/v9/Scene 34/Overlay Buttons/cowgirl.webp"
                action Jump("v9s34_rileyCowgirl")
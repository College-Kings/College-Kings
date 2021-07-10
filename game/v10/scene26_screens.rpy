screen v10s26_amberSexOverlay():

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
                idle "images/v10/Scene 26/Overlay Buttons/blowjob.webp"
                action Jump("v10s26_amberBlowjob")

            imagebutton:
                idle "images/v10/Scene 26/Overlay Buttons/lying.webp"
                action Jump("v10s26_amberLying")

            imagebutton:
                idle "images/v10/Scene 26/Overlay Buttons/doggy.webp"
                action Jump("v10s26_amberDoggy")

            imagebutton:
                idle "images/v10/Scene 26/Overlay Buttons/cowgirl.webp"
                action Jump("v10s26_amberCowgirl")
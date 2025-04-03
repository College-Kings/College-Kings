screen v8s3_rileySexOverlay():

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
                idle "images/v8/Scene 3/Overlay Buttons/cowgirl.webp"
                action Jump("v8s3_rileyCowgirl")

            imagebutton:
                idle "images/v8/Scene 3/Overlay Buttons/liftdoggy.webp"
                action Jump("v8s3_rileyLiftDoggy")

            imagebutton:
                idle "images/v8/Scene 3/Overlay Buttons/doggy.webp"
                action Jump("v8s3_rileyDoggy")
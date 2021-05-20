screen realmode():
    modal True
    
    add "images/REALLIFEMODE.webp"

    imagebutton:
        pos (417, 683)
        idle "images/rlmt.webp"
        hover "images/enable.webp"
        action [SetVariable("realmode", True), SetVariable("config.rollback_enabled", False), SetVariable("showkct", False), Show("phoneIcon"), Jump("v1start")]

    imagebutton:
        pos (1016, 683)
        idle "images/rlmt.webp"
        hover "images/disable.webp"
        action [SetVariable("realmode", False), SetVariable("config.rollback_enabled", True), SetVariable("showkct", True), Show("phoneIcon"), Jump("v1start")]


screen fantasyOverlay():
    add "images/fantasyoverlay.webp"


screen endFreeRoamConfirm(continueLabel):
    modal True
    
    add "images/endfr.webp"

    text "Are you sure you want to end free roam?" style "endfree"

    textbutton "Yes":
        style "endfr"
        action [Hide("endFreeRoamConfirm"), SetVariable("freeRoam", False), Jump(continueLabel)]
        text_align 0.5
        align (0.43, 0.58)

    textbutton "No":
        style "endfr"
        action Hide("endFreeRoamConfirm")
        text_align 0.5
        align (0.57, 0.58)


screen kiwiiPopup():
    modal True

    add "images/endfr.webp"

    text "You've just unlocked the social media app Kiwii! Open it now from the homescreen." style "endfree"

    textbutton "OK":
        style "endfr"
        action [SetVariable("kiwii_firstTime", False), Hide("kiwiiPopup")]
        text_align 0.5
        align (0.5, 0.58)


screen fightPopup(fightMove):
    modal True
    add "images/endfr.webp"

    text "Congratulations! You have learned a new fighting move: {b}[fightMove]{/b}." style "endfree"

    textbutton "OK" style "endfr":
        action Return()
        text_align 0.5
        align (0.5, 0.58)


screen kctPopup():
    modal True

    add "images/endfr.webp"

    text "Congratulations! Your Key Character Trait {b}[kct]{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK":
        style "endfr"
        action Return()
        text_align 0.5
        align (0.5, 0.58)
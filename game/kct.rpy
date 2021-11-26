init python:
    from enum import Enum


    class KCT(Enum):
        BRO = "bro"
        BOYFRIEND = "boyfriend"
        TROUBLEMAKER = "troublemaker"


    def add_point(var, value=1):
        # Don't update kct if kct is locked
        if locked_kct:
            return

        # Update the KCT variables
        setattr(store, var.value, getattr(store, var.value) + value)
        
        old_kct = kct

        # Sort KCT values
        kctDict = {"popular": bro * troublemaker / boyfriend, "confident": boyfriend * troublemaker / bro, "loyal": bro * boyfriend / troublemaker}
        setattr(store, "sortedKCT", [k for k, v in sorted(kctDict.items(), key=lambda item: item[1], reverse=True)])
        
        # Update KCT
        setattr(store, "kct", sortedKCT[0])

        # Notify user on KCT change
        if sortedKCT[0] != old_kct:
            renpy.notify("Your KCT has changed to " + kct)


# KCT Screens
screen kct_choice():
    fixed:
        xysize (298, 76)
        xalign 1.0

        add "gui/kct.webp"
        text kct:
            align (0.5, 0.5)
            font "fonts/Freshman.ttf"
            size 40
            if kct == "popular":
                color "#53d769"
            if kct == "loyal":
                color "#fecb2e"
            if kct == "confident":
                color "#fc3d39"


screen kct_popup(required_kct=None):
    modal True
    zorder 300

    use endfrTemplate:

        if required_kct is None or required_kct == kct:
            text "Congratulations! Your Key Character Trait {b}[kct!c]{/b} has just changed the outcome of a decision someone was making.":
                style "endfree"
                xalign 0.5
        else:
            text "Unfortunately, your Key Character Trait {b}[kct!c]{/b} did not change the outcome of this decision.":
                style "endfree"
                xalign 0.5

        textbutton "OK":
            align (0.5, 1.0)
            action Return()
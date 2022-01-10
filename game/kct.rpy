init python:
    class KCT(Enum):
        BRO = "bro"
        BOYFRIEND = "boyfriend"
        TROUBLEMAKER = "troublemaker"


    def add_point(var, value=1):
        # Don't update kct if kct is locked
        if locked_kct or _in_replay:
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
screen kct_choice_hint():
    style_prefix "kct_choice"

    window:
        xalign 1.0
        xoffset -50
        background "kct_choice_hint_background"

        hbox:
            null width 10

            add "gui/kct/logo.png" align (0.5, 0.5)

            text kct.upper() align (0.5, 0.5)

            null width 30


style kct_choice_text is druk_wide_bold_22


screen kct_popup(required_kct=None):
    modal True
    zorder 300

    if required_kct is None or required_kct == kct:
        $ message = "Congratulations! Your Key Character Trait {{b}}{}{{/b}} has just changed the outcome of a decision someone was making.".format(kct)
    else:
        $ message = "Unfortunately, your Key Character Trait {{b}}{}{{/b}} did not change the outcome of this decision.".format(kct)

    use alert_template(message):
        textbutton "OK":
            align (0.5, 1.0)
            action Return()
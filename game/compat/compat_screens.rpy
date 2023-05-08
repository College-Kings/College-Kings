screen compat_frat_is_none():
    zorder 200
    modal True
    style_prefix "alert"

    frame:
        align (0.5, 0.5)
        minimum (758, 363)
        background "alert_background"

        vbox:
            align (0.5, 0.5)
            spacing 45

            text _("Your frat data has been corrupted please confirm which frat your character is:") xalign 0.5 xsize 650

            hbox:
                xalign 0.5
                spacing 50

                textbutton "Wolves":
                    action [SetField(mc, "frat", Frat.WOLVES), Return()]

                textbutton "Apes":
                    action [SetField(mc, "frat", Frat.APES), Return()]
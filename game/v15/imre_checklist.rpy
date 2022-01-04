screen v15_imre_checklist_icon():
    zorder 100

    imagebutton:
        idle "images/v15/Scene 18/imre_checklist/icon.webp"
        action ToggleScreen("v15_imre_checklist")


screen v15_imre_checklist():
    tag checklist
    modal True

    add "images/v15/Scene 18/imre_checklist/background.webp" align (0.5, 0.5)

    button:
        action Hide("v15_imre_checklist")

    vbox:
        pos (600, 325)
        xysize (491, 390)

        for item in checklist:
            hbox:
                spacing 20

                if item.complete:
                    add "images/v15/Scene 18/imre_checklist/check.webp" 
                else:
                    add "images/v15/Scene 18/imre_checklist/uncheck.webp"

                text item.name yalign 0.5 style "v15_imre_checklist_text"


style v15_imre_checklist_text is text:
    font "fonts/RockSalt-Regular.ttf"
    size 20
    color "#343434"
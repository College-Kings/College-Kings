screen v15_imre_checklist_icon():
    tag checklist

    imagebutton:
        idle "images/v15/Scene 18/imre_checklist/icon.png"
        action Show("v15_imre_checklist")


screen v15_imre_checklist():
    tag checklist
    zorder 100
    modal True

    add "images/v15/Scene 18/imre_checklist/background.png"

    button:
        action Show("v15_imre_checklist_icon")

    vbox:
        pos (600, 325)
        xysize (491, 390)

        for item in checklist:
            hbox:
                spacing 20

                if item.complete:
                    add "images/v15/Scene 18/imre_checklist/check.png" 
                else:
                    add "images/v15/Scene 18/imre_checklist/uncheck.png"

                text item.name yalign 0.5 style "v15_imre_checklist_text"


style v15_imre_checklist_text is text:
    font "fonts/RockSalt-Regular.ttf"
    size 20
    color "#343434"
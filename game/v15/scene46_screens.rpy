screen v15s46_chooselocation():
    zorder -1

    modal True

    add "darker_80"

    vbox:
        align (0.5, 0.5)
        spacing 50

        text "Where is Nora?" size 100
        
        hbox:
            spacing 20

            button:
                action Jump("v15s46_choosedad")
                xysize (550, 131)
                idle_background "gui/choice/button_idle.png"
                hover_background "gui/choice/button_hover.png"
                text "Dad's house" align (0.5, 0.5)

            button:
                action Jump("v15s46_choosemsrose")
                xysize (550, 131)
                idle_background "gui/choice/button_idle.png"
                hover_background "gui/choice/button_hover.png"
                text "Ms. Rose's house" align (0.5, 0.5)

            if len(v15_nora_locations) > 4:
                button:
                    action Jump("v15s46_choosecabin")
                    xysize (550, 131)
                    idle_background "gui/choice/button_idle.png"
                    hover_background "gui/choice/button_hover.png"
                    text "Dad's cabin" align (0.5, 0.5)

        hbox:
            spacing 20
            
            if len(v15_nora_locations) <= 4:
                button:
                    action Jump("v15s46_choosecabin")
                    xysize (550, 131)
                    idle_background "gui/choice/button_idle.png"
                    hover_background "gui/choice/button_hover.png"
                    text "Dad's cabin" align (0.5, 0.5)

            button:
                action Jump("v15s46_chooseaunt")
                xysize (550, 131)
                idle_background "gui/choice/button_idle.png"
                hover_background "gui/choice/button_hover.png"
                text "Aunt's apartment" align (0.5, 0.5)

            if v15_nora_clue_camping:
                button:
                    action Jump("v15s46_choosecamping")
                    xysize (550, 131)
                    idle_background "gui/choice/button_idle.png"
                    hover_background "gui/choice/button_hover.png"
                    text "Camping by herself" align (0.5, 0.5)

            if v15_nora_clue_ex:
                button:
                    action Jump("v15s46_chooseex")
                    xysize (550, 131)
                    idle_background "gui/choice/button_idle.png"
                    hover_background "gui/choice/button_hover.png"
                    text "Ex's boyfriend's place" align (0.5, 0.5)
screen v15s46_chooselocation():
    zorder -1

    modal True

    vbox:
        align (0.5, 0.5)
        spacing 50
        
        hbox:
            spacing 20

            button:
                action Jump("v15s46_choosedad")

                fixed:
                    xysize (289, 74)
                    add "gui/common/button_gray_larger.webp"
                    text "Dad's house" align (0.5, 0.5)

            button:
                action Jump("v15s46_choosemsrose")

                fixed:
                    xysize (289, 74)
                    add "gui/common/button_gray_larger.webp"
                    text "Ms. Rose's house" align (0.5, 0.5)

            if len(v15_nora_locations) > 4:
                button:
                    action Jump("v15s46_choosecabin")

                    fixed:
                        xysize (289, 74)
                        add "gui/common/button_gray_larger.webp"
                        text "Dad's cabin" align (0.5, 0.5)

        hbox:
            spacing 20
            
            if len(v15_nora_locations) <= 4:
                button:
                    action Jump("v15s46_choosecabin")

                    fixed:
                        xysize (289, 74)
                        add "gui/common/button_gray_larger.webp"
                        text "Dad's cabin" align (0.5, 0.5)

            button:
                action Jump("v15s46_chooseaunt")

                fixed:
                    xysize (289, 74)
                    add "gui/common/button_gray_larger.webp"
                    text "Aunt's apartment" align (0.5, 0.5)

            if v15_nora_clue_camping:
                button:
                    action Jump("v15s46_choosecamping")

                    fixed:
                        xysize (289, 74)
                        add "gui/common/button_gray_larger.webp"
                        text "Camping" align (0.5, 0.5)

            if v15_nora_clue_ex:
                button:
                    action Jump("v15s46_chooseex")

                    fixed:
                        xysize (289, 74)
                        add "gui/common/button_gray_larger.webp"
                        text "Ex's house" align (0.5, 0.5)
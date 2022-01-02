screen v13s40_chloe():
    add Transform("images/v13/Scene 40/v13s40_12.webp", blur=10)

    vbox:
        align (0.5, 1.0)
        yoffset -50

        hbox:
            align (0.5, 0.5)
            spacing 25

            if mc.has_item(honey):# or True:
                button:
                    action Jump("v13s40_honey")

                    fixed:
                        xysize (269, 74)
                        add "images/button_gray.webp"
                        text honey.name align (0.5, 0.5)

            if mc.has_item(spankers):# or True:
                button:
                    action Jump("v13s40_spanker")

                    fixed:
                        xysize (269, 74)
                        add "images/button_gray.webp"
                        text spankers.name align (0.5, 0.5)

            if mc.has_item(feather):# or True:
                button:
                    action Jump("v13s40_feather")

                    fixed:
                        xysize (269, 74)
                        add "images/button_gray.webp"
                        text feather.name align (0.5, 0.5)

        hbox:
            align (0.5, 0.5)
            spacing 25

            button:
                action Jump("v13s40_neck")

                fixed:
                    xysize (269, 74)
                    add "images/button_gray.webp"
                    text "Neck" align (0.5, 0.5)

            button:
                action Jump("v13s40_chest")

                fixed:
                    xysize (269, 74)
                    add "images/button_gray.webp"
                    text "Chest" align (0.5, 0.5)

            button:
                action Jump("v13s40_back")

                fixed:
                    xysize (269, 74)
                    add "images/button_gray.webp"
                    text "Back" align (0.5, 0.5)

            button:
                action Jump("v13s40_shoulder")

                fixed:
                    xysize (269, 74)
                    add "images/button_gray.webp"
                    text "Shoulders" align (0.5, 0.5)

        button:
            action Show("confirm", message="Are you sure you want to end free roam?", yes_action=[Hide("confirm"), Jump("v13s40_end_free_roam")])
            align (0.5, 0.5)

            fixed:
                xysize (269, 74)
                add "images/button_gray.webp"
                text "Continue" align (0.5, 0.5)
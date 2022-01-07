screen sex_overlay(options=sex_overlay_options, continue_label):
    vbox:
        align (0.5, 1.0)
        yoffset -100
        spacing 10

        for row in options:
            hbox:
                align (0.5, 0.5)
                spacing 25

                for cell in row:
                    button:
                        action Jump(cell[1])
                        background "gui/common/button_gray.webp"
                        xysize (269, 74)

                        text cell[0] align (0.5, 0.5)

        button:
            background "gui/common/button_gray.webp"
            action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump(continue_label)])
            xalign 0.5
            xysize (269, 74)

            text "Continue" align (0.5, 0.5)

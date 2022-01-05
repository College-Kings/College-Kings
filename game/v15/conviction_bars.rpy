screen generic_conviction_bar(new_value, max_value, title, foreground, additional_info=""):
    tag animated_value_bar
    style_prefix "conviction_bar"

    $ title = title.upper()
    $ additional_info = additional_info.upper()

    frame:
        xalign 0.5
        xysize (1297, 266)

        fixed:
            xysize (820, 95)
            xalign 0.5
            ypos 83

            use animated_value_bar(None, new_value, max_value, "blue_bar", "ruby_bar", offset=(13, 0), size=(820, 95))
            text "$ {}".format(new_value) align (0.5, 0.5)

        add foreground

        fixed:
            xalign 0.5
            ypos 52
            xysize (262, 30)

            text title align (0.5, 0.5)

        fixed:
            xalign 0.5
            ypos 181
            xysize (222, 30)

            text additional_info align (0.5, 0.5)


screen teacher_conviction_bar(new_value, teacher_name):
    tag animated_value_bar
    style_prefix "conviction_bar"

    $ teacher_name = teacher_name.upper()

    default foregrounds = {
        "MR LEE": "images/v15/conviction_bars/mr_lee_background.png",
        "MS. ROSE": "images/v15/conviction_bars/ms_rose_background.png",
        "DEAN": "images/v15/conviction_bars/dean_background.png"
    }

    frame:
        xalign 0.5
        ypos -20
        xysize (1136, 238)

        use animated_value_bar(None, new_value, 100, "blue_bar", "ruby_bar", offset=(0, 30), size=(803, 92))

        add foregrounds[teacher_name]

        fixed:
            xalign 0.5
            ypos 65
            xysize (262, 35)

            text "CONVINCE TEACHER" align (0.5, 0.5)

        text teacher_name pos (220, 141)


style conviction_bar_text is text:
    font "fonts/Olympus Mount.ttf"
    size 19
    yoffset -5
screen teacher_conviction_bar(percentage, title, teacher_name, background):
    tag conviction_bar

    default old_value = animated_value_percent

    fixed:
        pos (624, 125)
        maximum (744, 32)

        bar:
            # at presidency_bar
            value AnimatedValue(percentage, 100, 2, old_value)
            left_bar Frame("gui/bar/blue.webp", 10, 0)
            right_bar Frame("gui/bar/ruby.webp", 10, 0)

        text teacher_name xpos 20 yalign 0.5 yoffset 5 style "conviction_bar_header"

    add background:
        # at presidency_bar
        xalign 0.5

    fixed:
        pos (860, 62)
        maximum (265, 32)

        text title align (0.5, 0.5) yoffset 5 style "conviction_bar_header"

    timer 4 action [SetVariable("animated_value_percent", percentage), Hide("conviction_bar")]


style conviction_bar_header is text:
    font "fonts/Olympus Mount.ttf"
    size 19

style conviction_bar_body is text:
    font "fonts/ABeeZee-Regular.ttf"
    size 24

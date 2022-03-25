init python:
    def set_presidency_percent(amount):
        old_value = getattr(store, "v14_lindsey_popularity")
        setattr(store, "v14_lindsey_popularity", amount)
        new_value = getattr(store, "v14_lindsey_popularity")

        renpy.show_screen("chicks_presidency_bar", old_value, new_value)


screen chicks_presidency_bar(old_value, new_value):
    tag animated_value_bar

    frame:
        background "#0000"
        foreground "/images/v14/chicks_presidency_race/presidency_bar/background.webp"
        xysize (1138, 238)
        xalign 0.5

        bar:
            value AnimatedValue(new_value, 100, 2, old_value)
            left_bar "blue_bar"
            right_bar "yellow_bar"
            xysize (820, 95)
            xalign 0.5
            ypos 96

        button action Hide("chicks_presidency_bar")

    # timer 4 action Hide("chicks_presidency_bar")

transform presidency_bar:
    yoffset -200
    linear 0.5 yoffset 0
    3.0
    linear 0.5 yoffset -200

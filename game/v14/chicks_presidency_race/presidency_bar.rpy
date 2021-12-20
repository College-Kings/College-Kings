init python:
    def set_presidency_percent(amount):
        old_var = getattr(store, "v14_lindsey_popularity")
        setattr(store, "v14_lindsey_popularity", amount)
        new_var = getattr(store, "v14_lindsey_popularity")

        renpy.show_screen("chicks_presidency_bar", old_var, new_var)


screen chicks_presidency_bar(old_var, new_var):
    bar:
        # at presidency_bar
        value AnimatedValue(new_var, 100, 2, old_var)
        left_bar Frame("images/v14/chicks_presidency_race/presidency_bar/left_bar.webp", 10, 0)
        right_bar Frame("images/v14/chicks_presidency_race/presidency_bar/right_bar.webp", 10, 0)
        maximum (758, 32)
        align (0.5, 0.11)

    add "images/v14/chicks_presidency_race/presidency_bar/background.webp":
        # at presidency_bar
        xalign 0.5

    timer 4 action Hide("chicks_presidency_bar")


transform presidency_bar:
    yoffset -200
    linear 0.5 yoffset 0
    3.0
    linear 0.5 yoffset -200

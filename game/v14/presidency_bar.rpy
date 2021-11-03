init python:
    def set_presidency_percent(amount):
        old_var = getattr(store, "v14_lindsey_popularity")
        setattr(store, "v14_lindsey_popularity", amount)
        new_var = getattr(store, "v14_lindsey_popularity")

        print(old_var)
        print(new_var)

        renpy.show_screen("chicks_presidency_bar", old_var, new_var)


screen chicks_presidency_bar(old_var, new_var):
    fixed:
        at presidency_bar

        bar:
            value AnimatedValue(new_var, 100, 5, old_var)
            left_bar Frame("gui/bar/left.webp", 10, 0)
            right_bar Frame("gui/bar/right.webp", 10, 0)
            maximum (758, 32)
            align (0.5, 0.11)
            
        add "images/presidency_bar/example.png" xalign 0.5

    timer 6 action Hide("lindsey_vs_chloe")


transform presidency_bar:
    ypos -200
    linear 0.5 xpos 0 ypos 0
    5.0
    linear 0.5 xpos 0 ypos -200
    
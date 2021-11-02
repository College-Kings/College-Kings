init python:
    def add_votes(person, amount):
        old_var = float(chloe.votes) / (lindsey.votes + chloe.votes) * 100
        setattr(person, "votes", getattr(person, "votes") + amount)      
        new_var = float(chloe.votes) / (lindsey.votes + chloe.votes) * 100

        renpy.show_screen("lindsey_vs_chloe", old_var, new_var)


screen lindsey_vs_chloe(old_var, new_var):
    fixed:
        at presidency_bar

        bar:
            value AnimatedValue(old_var, 100, 1.0, new_var)
            left_bar Frame("gui/bar/left.webp", 10, 0)
            right_bar Frame("gui/bar/right.webp", 10, 0)
            maximum (758, 32)
            align (0.5, 0.11)

        hbox:
            spacing 450
            align (0.5, 0.11)
            
            text "{} VOTES".format(lindsey.votes)
            text "{} VOTES".format(chloe.votes)

        add "images/presidency_bar/example.png" xalign 0.5


transform presidency_bar:
    ypos -200
    linear 0.5 xpos 0 ypos 0
    5.0
    linear 0.5 xpos 0 ypos -200
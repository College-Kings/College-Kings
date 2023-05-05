screen girls():
    modal True

    # character, label
    default girl_labels = (
        (chloe, "juchloe"),
        (aubrey, "juaubrey"),
        (lauren, "julauren"),
        (riley, "juriley"),
        (emily, "juemily"),
        (penelope, "jupenelope"),
    )

    add "images/v4/jc_background.webp"

    vpgrid:
        cols 3
        rows 2
        spacing 60
        xalign 0.5
        ypos 450

        for girl_obj, l in girl_labels:
            button:
                background "girl_button_idle"
                hover_background "girl_button_hover"
                xysize (307, 112)
                action Jump(l)

                add Transform(girl_obj.profile_picture, xysize=(100, 100)) xpos 6 yalign 0.5
 
                vbox:
                    xpos 120
                    yalign 0.5
                    spacing -2

                    text girl_obj.name:
                        size 30
                        color "#FFF"
    
    if config_debug:
        timer 0.1 action Jump(renpy.random.choice(list(i[1] for i in girl_labels)))
        
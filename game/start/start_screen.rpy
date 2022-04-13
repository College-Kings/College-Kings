screen start_screen():
    tag start_screens
    modal True

    default button_ui_path = "images/recap/ui/"

    add "images/start/start_screen_bg.webp"

    # Recap
    frame:
        xysize (558, 520)
        pos (306, 271)

        text "Jump into the action (and bed) right away with a pre-generated and summarized story, but with the chance to make major game choices.":
            style "effra_regular_23"
            text_align 0.5
            xsize 373
            align (0.5, 0.5)

        button:
            idle_background "blue_filled_button_idle"
            hover_background "blue_filled_button_hover"
            xysize (420, 144)
            xalign 0.5
            yalign 1.0
            yoffset -35
            action [Function(setup), Hide("start_screen", transition=dissolve), Jump("recap_start")]

            text "Start" style "bebas_neue_30" align (0.5, 0.5)

    # Path builder
    frame:
        xysize (558, 520)
        pos (970, 271)

        text "Played the game before, or want to choose your own path? Pick where you start in the story, your major character trait and romantic history.":
            style "effra_regular_23"
            text_align 0.5
            xsize (373, 140)
            align (0.5, 0.5)

        button:
            idle_background "pink_button_idle"
            hover_background "pink_button_hover"
            xysize (420, 144)
            xalign 0.5
            yalign 1.0
            yoffset -35
            action [Function(setup), Show("path_builder", from_main_menu=False)]

            text "Start" style "bebas_neue_30" align (0.5, 0.5)

    on "show" action Hide("phone_icon")
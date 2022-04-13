screen start_screen():
    tag start_screens
    modal True

    default button_ui_path = "images/recap/ui/"

    add "images/start/start_screen_bg.webp"

    # Recap/ CK1 First Day of College 
    frame:
        xysize (558, 520)
        pos (301, 271)

        text "Students come to San Vallejo College for dynamic student life. . . though the zero tolerance for drinking, drugs and violence is often overlooked. The full College Kings experience from the first day of college on.":
            style "effra_regular_23"
            text_align 0.5
            xsize (373,140)
            align (0.5, 0.5)

        button:
            idle_background "blue_filled_button_idle"
            hover_background "blue_filled_button_hover"
            xysize (420, 144)
            xalign 0.5
            yalign 1.0
            yoffset -35
            action [Function(setup), Hide("start_screen", transition=dissolve), Jump("v1start")]

            text "Start" style "bebas_neue_30" align (0.5, 0.5)

    # Path builder/ CK1 EuroTrip
    frame:
        xysize (558, 520)
        pos (975, 271)

        text "The students of San Vallejo College gear up for an educational trip to Europe, although not the education the chaperones are hoping for. Jump right into the action for the best College Kings has to offer with a recap of the early game.":
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
            action [Function(setup), Hide("start_screen", transition=dissolve), Jump("recap_start")]

            text "Start" style "bebas_neue_30" align (0.5, 0.5)

    on "show" action Hide("phone_icon")
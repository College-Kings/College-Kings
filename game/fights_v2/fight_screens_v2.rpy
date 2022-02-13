screen fight_player_turn():

    zorder 50

    style_prefix "fight_turn"

    if opponent_guard == 2: # opponent guard image
        add "fight_prototype/images/opp_full_guard.webp"
    elif opponent_guard == 1:
        add "fight_prototype/images/opp_semi_guard.webp"
    else:
        add "fight_prototype/images/opp_no_guard.webp"

    # key r:
    #     action Jump ("tomkick1")
    # key w:
    #     action Jump ("tomkick2")
    # key q:
    #     action Jump ("tomkick3")

    vbox:
        spacing 10
        align (0.5, 0.93)
        hbox:
            spacing 5
            for x in range(1, 7):
                imagebutton:
                    idle "gui/fight_prototype/fight_circle_dark_idle.png"
        hbox:

            button:
                xysize (100, 100)
                idle_background "#a8a8a8"
                hover_background "#ffd000"
                selected_background "#ffd000"
                action ToggleScreen ("action")

                hbox:
                    align (0, 1.0)
                    spacing 10
                    text "4" text_align 0.5 font "fonts/Montserrat-Bold.ttf" # action cost
                    text "Hook" text_align 0.5 # action name
                text "Q" align (0, 0) text_align 0.5 font "fonts/Montserrat-Bold.ttf" # keybind

    

        


screen action():

    style_prefix "fight_turn"

    zorder 100

    frame:
        xalign (0.5)
        ypos 670
        xysize (800, 200)
        background "#fff"

        vbox:
            align (0.5, 0.5)
            spacing 30
            vbox:
                xalign 0.5
                spacing 10
                button:
                    xalign 0.5
                    idle_background "#a8a8a8"
                    hover_background "#ffd000"
                    action [Hide ("action"), Jump("player_hook_v2")]
                    text ">> Hook <<" size 40 font "fonts/Montserrat-Bold.ttf" align (0.5, 0.5)
                text "Attack the opponent with a hook to the face. Small chance to break guard." xalign 0.5

            hbox:
                xalign 0.5
                spacing 560
                text "50% Hit" font "fonts/Montserrat-Bold.ttf" xalign 0.5
                text "25% Crit" font "fonts/Montserrat-Bold.ttf" xalign 0.5


    

style fight_turn_text is text:
    size 20
    color "#000"
    font "fonts/Montserrat-Regular.ttf"



    
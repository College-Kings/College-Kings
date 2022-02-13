screen fight_player_turn():

    zorder 50

    style_prefix "fight_turn"

    if opponent_stance == 2: # opponent guard image
        add "fight_prototype/images/opp_full_guard.webp"
    elif opponent_stance == 1:
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
            for x in range(0, actionpoints):
                imagebutton:
                    idle "gui/fight_prototype/fight_circle_dark_idle.png"
        hbox:

            spacing 30

            button:
                xysize (100, 100)
                idle_background "#fff"
                hover_background "#ffd000"
                selected_background "#ffd000"
                insensitive_background "#a7a7a7"
                if actionpoints >= 4:
                    action ToggleScreen ("action", action_cost = 4, action_name = "Hook", action_label = "player_hook_v2", action_description = "Hit the opponent with a devastating hook to the face.", stance = 0, action_damage = 10)

                hbox:
                    align (0, 1.0)
                    spacing 10
                    text "4" text_align 0.5 font "fonts/Montserrat-Bold.ttf" # action cost
                    text "Hook" text_align 0.5 # action name
                text "Q" align (0, 0) text_align 0.5 font "fonts/Montserrat-Bold.ttf" # keybind

            button:
                xysize (100, 100)
                idle_background "#fff"
                hover_background "#ffd000"
                selected_background "#ffd000"
                insensitive_background "#a7a7a7"
                if actionpoints >= 2:
                    action ToggleScreen ("action", action_cost = 2, action_name = "Jab", action_label = "player_jab_v2", action_description = "Hit the opponent with a jab to the face.", stance = 1)

                hbox:
                    align (0, 1.0)
                    spacing 10
                    text "2" text_align 0.5 font "fonts/Montserrat-Bold.ttf" # action cost
                    text "Jab" text_align 0.5 # action name
                text "W" align (0, 0) text_align 0.5 font "fonts/Montserrat-Bold.ttf" # keybind

            button:
                xysize (100, 100)
                idle_background "#fff"
                hover_background "#ffd000"
                selected_background "#ffd000"
                insensitive_background "#a7a7a7"
                if actionpoints >= 2:
                    action ToggleScreen ("action", action_cost = 0, action_name = "Trash Talk", action_label = "opponent_attack_v2", action_description = "Trash Talk Description", stance = 1)

                hbox:
                    align (0, 1.0)
                    spacing 10
                    text "0" text_align 0.5 font "fonts/Montserrat-Bold.ttf" # action cost
                    text "Trash Talk" text_align 0.5 # action name
                text "R" align (0, 0) text_align 0.5 font "fonts/Montserrat-Bold.ttf" # keybind


            button:
                xysize (100, 100)
                idle_background "#fff"
                hover_background "#ffd000"
                selected_background "#ffd000"
                insensitive_background "#a7a7a7"
                if actionpoints >= 2:
                    action ToggleScreen ("action", action_cost = 4, action_name = "Guard Up", action_label = "opponent_attack_v2", action_description = "Go into a defensive stance.\nEnds Turn.", stance = 2)

                hbox:
                    align (0, 1.0)
                    spacing 10
                    text "4" text_align 0.5 font "fonts/Montserrat-Bold.ttf" # action cost
                    text "Guard Up" text_align 0.5 # action name
                text "E" align (0, 0) text_align 0.5 font "fonts/Montserrat-Bold.ttf" # keybind

    vbox:
        align (0.1,0.9)
        text "Player Stance: [player_stance]"
        text "Player Mindset: [player_mindset]"
        text "Opponent Stance: [opponent_stance]"
        text "Opponent Mindset: [opponent_mindset]"
        text "Opponent Health: [opponent_health]"
        text "Player Health: [player_health]"


screen action(action_cost, action_name, action_label, action_description, stance, action_damage = 0):

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
                    action [SetVariable ("actionpoints", actionpoints-action_cost), SetVariable("player_stance", stance),SetVariable("opponent_health", opponent_health-action_damage), Hide ("action"), Jump(action_label)]
                    text ">>[action_name] <<" size 40 font "fonts/Montserrat-Bold.ttf" align (0.5, 0.5)
                text "[action_description]" xalign 0.5

            hbox:
                xalign 0.5
                spacing 560
                text "50% Hit" font "fonts/Montserrat-Bold.ttf" xalign 0.5
                text "25% Crit" font "fonts/Montserrat-Bold.ttf" xalign 0.5


    

style fight_turn_text is text:
    size 20
    color "#000"
    font "fonts/Montserrat-Regular.ttf"



    
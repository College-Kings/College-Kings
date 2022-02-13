screen fight_player_turn():

    zorder 50

    style_prefix "fight_turn"

    if opponent_stance == 2: # opponent guard image
        add "fight_prototype/images/opp_full_guard.webp"
    elif opponent_stance == 1:
        add "fight_prototype/images/opp_semi_guard.webp"
    else:
        add "fight_prototype/images/opp_no_guard.webp"

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

            for move in Move2:

                button:
                    xysize (100, 100)
                    idle_background "#fff"
                    hover_background "#ffd000"
                    selected_background "#ffd000"
                    insensitive_background "#a7a7a7"
                    if actionpoints >= 4:
                        action ToggleScreen ("action")

                    hbox:
                        align (0, 1.0)
                        spacing 10
                        text move.stamina_cost text_align 0.5 font "fonts/Montserrat-Bold.ttf" # action cost
                        text move.name text_align 0.5 # action name

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



    
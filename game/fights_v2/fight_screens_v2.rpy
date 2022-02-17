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

            for move in FightMove.moves:
                button:
                    xysize (100, 100)
                    idle_background "#fff"
                    hover_background "#ffd000"
                    selected_background "#ffd000"
                    insensitive_background "#a7a7a7"
                    if actionpoints >= move.stamina_cost:
                        action ToggleScreen("action", None, move.name, move.description, move.damage, move.accuracy, move.stamina_cost, move.stance, move.effect, move.jump_to)

                    text str (move.stamina_cost) align (1.0, 0) font "fonts/Montserrat-Bold.ttf" # action cost
                    text move.name align (0.5, 0.5) text_align 0.5 # action name

    frame:
        align (0.1,0.9)
        background "#fff"
        vbox:
            text "Player Stance: [player_stance]" 
            text "Player Mindset: [player_mindset]"
            text "Opponent Stance: [opponent_stance]"
            text "Opponent Mindset: [opponent_mindset]"
            text "Opponent Health: [opponent_health]"
            text "Player Health: [player_health]"
        


screen action(name, description, damage, accuracy, stamina_cost, stance, effect, jump_to):
    zorder 100
    style_prefix "fight_turn"

    frame:
        xalign (0.5)
        ypos 670
        xysize (900, 200)
        background "#fff"
        padding (10,10)

        hbox:
            align (0.5, 0.5)
            spacing 50

            if accuracy > 0:

                hbox:
                    xsize 240

                    vbox:
                        spacing 5
                        xsize 200
                        text "Hit" font "fonts/Montserrat-Bold.ttf"
                        null height 15
                        text "Base Accuracy"
                        if opponent_stance == 2 or opponent_stance == 0:
                            text "Opponent Stance"
                        if player_mindset == 2:
                            text "Shaken"
                        elif player_mindset == 0:
                            text "Confident"

                    vbox:
                        spacing 5
                        xsize 40
                        text "X%" font "fonts/Montserrat-Bold.ttf"
                        null height 15
                        text "+[accuracy]"
                        if opponent_stance == 2:
                            text "+10%"
                        elif opponent_stance == 0: 
                            text "-10%"
                        if player_mindset == 2:
                            text "-10%"
                        elif player_mindset == 0:
                            text "+10%"

            vbox:
                xsize 300
                spacing 20
                xalign 0.5

                button:
                    xalign 0.5
                    idle_background "#a8a8a8"
                    hover_background "#ffd000"
                    if stamina_cost == 0:
                        action [SetVariable("opponent_health", opponent_health - damage),
                            Hide("action"),
                            Jump(jump_to)] # Jumps will be changed to a single label with dynamic expressions
                    else:
                        action [SetVariable("actionpoints", actionpoints - stamina_cost),
                            SetVariable("player_stance", stance), 
                            SetVariable("opponent_health", opponent_health - damage),
                            Hide("action"),
                            Jump(jump_to)] # Jumps will be changed to a single label with dynamic expressions

                    text ">> {} <<".format(name) size 30 font "fonts/Montserrat-Bold.ttf" align (0.5, 0.5)

                text description xalign 0.5 text_align 0.5

                text effect xalign 0.5 font "fonts/Montserrat-Bold.ttf"

            if damage > 0:

                hbox:
                    xsize 240

                    vbox:
                        spacing 5
                        xsize 200
                        text "Damage" font "fonts/Montserrat-Bold.ttf"
                        null height 15
                        text "Base Damage"
                        if player_stance == 2:
                            text "Aggressive Stance"
                        elif player_stance == 0: 
                            text "Defensive Stance"

                    vbox:
                        spacing 5
                        xsize 40
                        text "X" font "fonts/Montserrat-Bold.ttf"
                        null height 15
                        text "+[damage]"
                        if player_stance == 2:
                            text "+5"
                        elif player_stance == 0: 
                            text "-5"
                    



    

style fight_turn_text is text:
    size 20
    color "#000"
    font "fonts/Montserrat-Regular.ttf"



    
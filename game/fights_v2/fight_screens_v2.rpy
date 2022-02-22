screen fight_player_turn(player, opponent):
    style_prefix "fight_turn"

    default selected_move = None

    add opponent.stance_image

    vbox:
        xalign 0.5
        yalign 1.0
        yoffset -50
        spacing 20

        hbox:
            spacing 30
            xalign 0.5

            for move in player.base_attacks:
                button:
                    xysize (100, 100)
                    idle_background "#fff"
                    hover_background "#ffd000"
                    selected_background "#ffd000"
                    insensitive_background "#a7a7a7"
                    selected (selected_move == move)
                    if selected_move == move:
                        action [SetScreenVariable("selected_move", None), Hide("action_info")]
                    else:
                        action [SetScreenVariable("selected_move", move), Show("action_info", None, move, player, opponent)]

                    text str(move.stamina_cost) xalign 1.0 font "fonts/Montserrat-Bold.ttf"
                    text move.name align (0.5, 0.5) text_align 0.5

        hbox:
            spacing 30
            xalign 0.5

            for move in player.turn_moves:
                button:
                    xysize (200, 50)
                    idle_background "#fff"
                    hover_background "#ffd000"
                    selected_background "#ffd000"
                    insensitive_background "#a7a7a7"
                    selected (selected_move == move)
                    if selected_move == move:
                        action [SetScreenVariable("selected_move", None), Hide("action_info")]
                    else:
                        action [SetScreenVariable("selected_move", move), Show("action_info", None, move, player, opponent)]

                    text str(move.stamina_cost) xalign 1.0 font "fonts/Montserrat-Bold.ttf"
                    text move.name align (0.5, 0.5) text_align 0.5

    frame:
        xpos 35
        yalign 1.0
        yoffset -35
        background "#fff"
        padding (50, 5)
        
        text "Current Stance: {{color=#6a0dad}}{}".format(player.stance.name) align (0.5, 0.5)


screen action_info(move, player, opponent):
    zorder 100
    style_prefix "fight_turn"

    frame:
        xalign 0.5
        ypos 650
        xysize (900, 200)
        background "#fff"
        padding (10, 10)

        vbox:
            spacing 20

            hbox:
                spacing 20

                button:
                    xalign 0.5
                    idle_background "#a8a8a8"
                    hover_background "#ffd000"
                    if player.stamina >= move.stamina_cost:
                        action [Hide("action_info"), Call("player_attack_turn", move, player, opponent)]
                    
                    text ">>> {} <<<".format(move.name) size 30 font "fonts/Montserrat-Bold.ttf" align (0.5, 0.5)

                vbox:
                    if hasattr(move, "accuracy") and move.accuracy is not None:
                        text "{{font=fonts/Montserrat-Bold.ttf}}Accuracy:{{/font}} {}%".format(get_accuracy(move, opponent))
                    if hasattr(move, "damage") and move.damage is not None:
                        text "{{font=fonts/Montserrat-Bold.ttf}}Damage:{{/font}} {}".format(get_total_damage(move, player))

            text move.description
            text "{{font=fonts/Montserrat-Bold.ttf}}Ideal Stance Effect:{{/font}} {}".format(move.effect)

        vbox:
            align (1.0, 0.5)

            if move.ideal_stance is not None:
                text "Ideal Stance:" font "fonts/Montserrat-Bold.ttf"
                text move.ideal_stance.name

            null height 10

            if move.end_stance is not None:
                text "End Stance:" font "fonts/Montserrat-Bold.ttf"
                text move.end_stance.name


screen fight_debug(player, opponent):
    zorder 1000
    style_prefix "fight_turn"

    frame:
        pos (50, 100)
        background "#fff"
        
        vbox:
            text "Player Health: {}".format(player.health) 
            text "Player Stance: {}".format(player.stance)
            text "Player Stamina: {}".format(player.stamina)

            null height 10

            text "Opponent Health: {}".format(opponent.health) 
            text "Opponent Stance: {}".format(opponent.stance) 
            text "Opponent Stamina: {}".format(opponent.stamina)


style fight_turn_text is text:
    size 20
    color "#000"
    font "fonts/Montserrat-Regular.ttf"



    
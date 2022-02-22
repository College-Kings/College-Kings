screen fight_player_turn(player, opponent):
    style_prefix "fight_turn"

    default selected_move = None

    add opponent.stance_image

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

            for move in player.base_attacks + player.turn_moves:
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

                    text str (move.stamina_cost) align (1.0, 0) font "fonts/Montserrat-Bold.ttf" # action cost
                    text move.name align (0.5, 0.5) text_align 0.5 # action name
        


screen action_info(move, player, opponent):
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

            # Accuracy Breakdown
            if hasattr(move, "accuracy") and move.accuracy is not None:
                hbox:
                    xsize 240

                    vbox:
                        spacing 5
                        xsize 200

                        text "Hit" font "fonts/Montserrat-Bold.ttf"
                        null height 15
                        text "Base Accuracy"
                        text "Opponent Stance"
                        # if player_mindset == 2:
                        #     text "Shaken"
                        # elif player_mindset == 0:
                        #     text "Confident"

                    vbox:
                        spacing 5
                        xsize 40

                        text "{}%".format(get_accuracy(move, opponent)) font "fonts/Montserrat-Bold.ttf"
                        null height 15
                        text "{:+}%".format(move.accuracy)
                        text "{:+}%".format(FightMove.ACCURACY_DICT[opponent.stance])

            vbox:
                xsize 300
                spacing 20
                xalign 0.5

                button:
                    xalign 0.5
                    idle_background "#a8a8a8"
                    hover_background "#ffd000"
                    if player.stamina >= move.stamina_cost:
                        action [Hide("action_info"), Call("player_attack_turn", move, player, opponent)]
                    
                    text ">> {} <<".format(move.name) size 30 font "fonts/Montserrat-Bold.ttf" align (0.5, 0.5)

                text move.description xalign 0.5 text_align 0.5

                text move.effect xalign 0.5 font "fonts/Montserrat-Bold.ttf"

            # Damage Breakdown
            if hasattr(move, "damage") and move.damage is not None:
                hbox:
                    xsize 240

                    vbox:
                        spacing 5
                        xsize 200

                        text "Damage" font "fonts/Montserrat-Bold.ttf"
                        null height 15
                        text "Base Damage"
                        text "Player Stance"

                    vbox:
                        spacing 5
                        xsize 40

                        text str(get_total_damage(move, player)) font "fonts/Montserrat-Bold.ttf"
                        null height 15
                        text "{:+}".format(move.damage)
                        text "{:+}".format(FightMove.DAMAGE_DICT[player.stance])


screen fight_debug(player, opponent):
    zorder 1000
    style_prefix "fight_turn"

    frame:
        xpos 50
        yalign 0.9
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



    
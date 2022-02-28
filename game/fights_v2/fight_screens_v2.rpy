screen fight_player_turn(player, opponent):
    style_prefix "fight_turn"

    default selected_move = None
    default opponent_bar_segment_width = 50

    add opponent.stance_image

    use health_bars(player, opponent)

    if isinstance(selected_move, FightMove):
        # add Transform("fight_guard_animation", size=(min(opponent_bar_segment_width * opponent.guard, opponent_bar_segment_width * selected_move.damage), 20)):
        #     xalign 1.0
        #     xoffset (-760 - (opponent_bar_segment_width * (BasePlayer.MAX_GUARD - opponent.guard)))
        #     ypos 50

        # add Transform("fight_health_animation", size=(min(opponent_bar_segment_width * opponent.health, opponent_bar_segment_width * (selected_move.damage - opponent.guard)), 20)):
        #     xalign 1.0
        #     xoffset (-560 - (opponent_bar_segment_width * (opponent.max_health - opponent.health)))
        #     ypos 70

        vbox:
            xalign 0.5
            ypos 50
            spacing 5

            # Opponent Guard
            hbox:
                xalign 0.5
                spacing 2
                ysize 20

                for i in range(opponent.guard - selected_move.damage):
                    null width 50

                for i in range(min(opponent.guard, selected_move.damage)):
                    add Transform("fight_guard_animation", size=(50, 20))

                for i in range(BasePlayer.MAX_GUARD - opponent.guard):
                    null width 50

            # Opponent Health
            hbox:
                xalign 0.5
                spacing 2

                for i in range(opponent.max_health - min(opponent.health, (selected_move.damage - opponent.guard)) - (opponent.max_health - opponent.health)):
                    null width 50

                for i in range(min(opponent.health, (selected_move.damage - opponent.guard))):
                    add Transform("fight_health_animation", size=(50, 20))

                for i in range(opponent.max_health - opponent.health):
                    null width 50




    vbox:
        xalign 0.5
        yalign 1.0
        yoffset -50
        spacing 20

        hbox:
            spacing 5
            xalign 0.5

            for i in range(1, player.max_stamina + 1):
                if i > player.stamina:
                    add "gui/fight_prototype/fight_circle_idle.png" yalign 0.5
                elif selected_move is None or i <= (player.stamina - selected_move.stamina_cost):
                    add "gui/fight_prototype/fight_circle_hover.png" yalign 0.5
                else:
                    add "gui/fight_prototype/fight_circle_gold_hover.png" yalign 0.5
                
        hbox:
            spacing 30
            xalign 0.5

            for move in player.base_attacks + player.turn_moves:
                button:
                    xysize (100, 100)
                    if move.ideal_stance == player.stance:
                        idle_background "#7cf87c"
                    else:
                        idle_background "#fff"
                    hover_background "#ffd000"
                    selected_background "#ffd000"
                    insensitive_background "#a7a7a7"
                    sensitive (player.stamina >= move.stamina_cost)
                    selected (selected_move == move)
                    if selected_move == move:
                        action [SetScreenVariable("selected_move", None), Hide("action_info")]
                    else:
                        action [SetScreenVariable("selected_move", move), Show("action_info", None, move, player, opponent)]

                    text str(move.stamina_cost) xalign 1.0 font "fonts/Montserrat-Bold.ttf"
                    text move.name align (0.5, 0.5) text_align 0.5

    vbox:
        xpos 35
        yalign 1.0
        yoffset -35
        spacing 5

        for stance in FightStance:
            frame:
                background "#fff"
                xysize (250, 50)

                text stance.name align (0.5, 0.5)

                if player.stance == stance:
                    add "#ffd000" xysize (35, 50)

                if selected_move is not None and selected_move.ideal_stance == stance:
                    add "#7cf87c" xysize (35, 50)

                if (selected_move is not None) and ((selected_move.end_stance is None and player.stance == stance) or (selected_move.end_stance == stance)):
                    add "#ffd000" xysize (35, 50) xalign 1.0


screen fight_opponent_turn():
    add "images/3 hits.webp"


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
                    action [Hide("action_info"), Call("player_attack_turn", move, player, opponent)]
                    
                    text ">>> {} <<<".format(move.name) size 30 font "fonts/Montserrat-Bold.ttf" align (0.5, 0.5)

                vbox:
                    if hasattr(move, "damage") and move.damage is not None:
                        text "{{font=fonts/Montserrat-Bold.ttf}}Damage:{{/font}} {}".format(move.damage)

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


screen health_bars(player, opponent):
    vbox:
        xalign 0.5
        ypos 50
        spacing 5

        # Opponent Guard
        hbox:
            xalign 0.5
            spacing 2

            for i in range(1, BasePlayer.MAX_GUARD + 1):
                if i > opponent.guard:
                    add Transform("#404040", size=(50, 20))
                else:
                    add Transform("#00f", size=(50, 20))

        # Opponent Health
        hbox:
            xalign 0.5
            spacing 2

            for i in range(1, opponent.max_health + 1):
                if i > opponent.health:
                    add Transform("#404040", size=(50, 20))
                else:
                    add Transform("#f00", size=(50, 20))

    fixed:
        pos (15, 700)
        xysize (400, 95)

        use animated_value_bar(None, player.health, player.max_health, "ruby_bar", "transparent_bar", offset=(13, 0), size=(400, 95), delay=1) # Player Health Bar
        use animated_value_bar(None, player.guard, player.stance.value, "blue_bar", "transparent_bar", offset=(13, 0), size=(400, 95), delay=1) # Player Guard Bar


screen fight_debug(player, opponent):
    zorder 1000
    style_prefix "fight_turn"

    frame:
        pos (50, 100)
        background "#fff"
        
        vbox:
            text "Player Guard: {}".format(player.guard)
            text "Player Health: {}".format(player.health)
            text "Player Stance: {}".format(player.stance)
            text "Player Stamina: {}".format(player.stamina)

            null height 10

            text "Opponent Guard: {}".format(opponent.guard)
            text "Opponent Health: {}".format(opponent.health) 
            text "Opponent Stance: {}".format(opponent.stance) 
            text "Opponent Stamina: {}".format(opponent.stamina)


style fight_turn_text is text:
    size 20
    color "#000"
    font "fonts/Montserrat-Regular.ttf"



    
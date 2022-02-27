screen fight_player_turn(player, opponent):
    style_prefix "fight_turn"

    default selected_move = None
    default opponent_guard_bar_segment_width = 400 / 30 # Bar Width / Max Guard
    default opponent_health_bar_segment_width = 800 / opponent.max_health # Bar Width / Max Health

    add opponent.stance_image

    use health_bars(player, opponent)

    if selected_move is not None:
        add Transform("fight_health_animation", size=(opponent_health_bar_segment_width * selected_move.damage, 20)):
            xalign 1.0
            xoffset (-560 + (opponent_health_bar_segment_width * (opponent.max_health - opponent.health)))
            ypos 70

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
        spacing 25

        frame:
            background "#fff"
            padding (50, 5)
            
            text "Current Stance: {{color=#6a0dad}}{}".format(player.stance.name) align (0.5, 0.5)


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

        # Opponent Guard
        bar:
            value AnimatedValue(opponent.guard, 30, delay=1)
            left_bar "#00f"
            right_bar "#404040"
            xysize (400, 20)
            xalign 0.5

        # Opponent Health
        bar:
            value AnimatedValue(opponent.health, opponent.max_health, delay=1)
            left_bar "#f00"
            right_bar "#000"
            xysize (800, 20)

    fixed:
        pos (15, 925)
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



    
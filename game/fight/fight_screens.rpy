screen fight_overview_info(competitor, profile_picture, is_player=False):
    default image_path = "images/fight/overview/"
    default special_attacks = [
        Headbutt({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }),
        OverhandPunch({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }),
        Uppercut({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }),
    ]

    frame:
        add "images/fight/overview/frame-background.png" pos (-54, -50)

        fixed:
            xysize (170, 30)
            pos (568, -40)

            text "COMPETITOR" size 16 align (0.5, 0.5)

        hbox:
            pos (20, -55)
            spacing 10

            add Transform(profile_picture, xysize=(100, 100)) yalign 0.5

            vbox:
                spacing 20

                text competitor.name size 34
                text "VICTORIES: {}".format(competitor.wins) size 19

        hbox:
            xalign 0.5
            ypos 55
            spacing 2

            for i in range(int(competitor.max_health)):
                add Transform("#f00", size=((750/competitor.max_health) - 2, 20))

        vbox:
            align (0.5, 0.5)
            spacing 10

            hbox:
                spacing 50

                text "BASIC ATTACKS" yalign 0.5

                grid 2 2:
                    spacing 10

                    for attack in competitor.base_attacks:
                        button:
                            idle_background image_path + "attack-idle.png"
                            hover_background image_path + "attack-idle.png"
                            tooltip attack.description
                            action NullAction()
                            xysize (206, 58)
                            padding (5, 5)

                            text attack.name align (0.5, 0.5)

            hbox:
                spacing 35

                text "SPECIAL ATTACK" yalign 0.5

                vpgrid:
                    cols 2
                    spacing 10

                    for attack in special_attacks:
                        button:
                            idle_background image_path + "attack-idle2.png"
                            selected_background image_path + "attack-hover.png"
                            selected (competitor.special_attack is not None and competitor.special_attack.name == attack.name)
                            tooltip attack.description
                            xysize (206, 58)
                            padding (5, 5)
                            if is_player:
                                hover_background image_path + "attack-hover.png"
                                action SetField(competitor, "special_attack", attack)
                            else:
                                hover_background image_path + "attack-idle2.png"
                                action NullAction()

                            text attack.name align (0.5, 0.5)
                 
            hbox:
                spacing 25

                text "QUIRK" yalign 0.5

                vpgrid:
                    cols 3
                    spacing 10

                    for quirk in FightQuirk.quirks:
                        button:
                            idle_background image_path + "attack-idle2.png"
                            selected_background image_path + "attack-hover.png"
                            selected (competitor.quirk is not None and competitor.quirk.name == quirk.name)
                            # tooltip attack.description
                            xysize (206, 58)
                            padding (5, 5)
                            if is_player:
                                hover_background image_path + "attack-hover.png"
                                action SetField(competitor, "quirk", quirk)
                            else:
                                hover_background image_path + "attack-idle2.png"
                                action NullAction()

                            text quirk.name align (0.5, 0.5)

        $ tooltip = GetTooltip()

        fixed:
            align (0.5, 1.0)
            ysize 125

            if tooltip:
                text "[tooltip]" align (0.5, 0.5)


screen fight_overview(fight, title):
    modal True
    style_prefix "fight_overview"

    default image_path = "images/fight/overview/"
    default difficulties = ["Easy", "Normal", "Hard", "Oscar"]
    default difficulty_index = 1

    python:
        player = fight.player.fighter
        opponent = fight.opponent.fighter

    add image_path + "background.png"

    text title style "fight_overview_title" xalign 0.5 ypos 50

    # Player info
    fixed:
        xysize (790, 662)
        xpos 100
        yalign 0.5

        use fight_overview_info(player, fight.player.profile_picture, is_player=True)

    # Opponent info
    fixed:
        xysize (790, 662)
        align (1.0, 0.5)
        xoffset -100

        use fight_overview_info(opponent, fight.player.profile_picture, is_player=False)

    hbox:
        xpos 100
        yalign 1.0
        yoffset -100
        spacing 20

        text "DIFFICULTY:"

        imagebutton:
            idle Transform("gui/common/left-arrow.png", xysize=(10, 15))
            if difficulty_index > 0:
                action [SetScreenVariable("difficulty_index", difficulty_index - 1),
                    SetField(opponent, "max_health", opponent.max_health * 1/1.25),
                    SetField(opponent, "attack_multiplier", opponent.attack_multiplier - 0.5),
                    SetField(opponent, "max_stamina", opponent.max_stamina * 1/1.25)]
            yalign 0.5

        frame:
            xsize 100
            yalign 0.5

            text difficulties[difficulty_index] xalign 0.5

        imagebutton:
            idle Transform("gui/common/right-arrow.png", xysize=(10, 15))
            if difficulty_index < len(difficulties) - 1:
                action [SetScreenVariable("difficulty_index", difficulty_index + 1),
                    SetField(opponent, "max_health", opponent.max_health * 1.25),
                    SetField(opponent, "attack_multiplier", opponent.attack_multiplier + 0.5),
                    SetField(opponent, "max_stamina", opponent.max_stamina * 1.25)]
            yalign 0.5

    hbox:
        align (0.5, 1.0)
        yoffset -25
        spacing 20

        imagebutton:
            idle image_path + "play-fight-idle.png"
            hover image_path + "play-fight-hover.png"
            action [SetField(opponent, "max_health", int(opponent.max_health)),
                SetField(opponent, "max_stamina", int(opponent.max_stamina)),
                Call("fight_start_turn", fight, opponent, player)]
            yalign 0.5

        imagebutton:
            idle image_path + "skip-fight-idle.png"
            hover image_path + "skip-fight-hover.png"
            action [SetField(opponent, "max_health", int(opponent.max_health)),
                SetField(opponent, "max_stamina", int(opponent.max_stamina)),
                Jump(fight.end_label)]
            yalign 0.5


screen fight_player_turn(fight, player, opponent):
    style_prefix "fight_turn"

    default selected_move = None
    default max_stamina = player.stamina

    add opponent.stance_image

    use health_bars(fight.player, fight.opponent, selected_move)

    vbox:
        xalign 0.5
        yalign 1.0
        yoffset -50
        spacing 20

        hbox:
            spacing 5
            xalign 0.5

            for i in range(1, max_stamina + 1):
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
                        action [SetScreenVariable("selected_move", move), Show("action_info", None, fight, player, opponent, move)]

                    text str(move.stamina_cost) xalign 1.0 font "fonts/Montserrat-Bold.ttf"
                    text move.name align (0.5, 0.5) text_align 0.5

            if player.special_attack is not None:
                button:
                    xysize (100, 100)
                    if player.special_attack.ideal_stance == player.stance:
                        idle_background "#7cf87c"
                    else:
                        idle_background "#fff"
                    hover_background "#ffd000"
                    selected_background "#ffd000"
                    insensitive_background "#a7a7a7"
                    sensitive player.special_attack.is_sensitive(fight, opponent, player)
                    selected (selected_move == player.special_attack)
                    if selected_move == player.special_attack:
                        action [SetScreenVariable("selected_move", None), Hide("action_info")]
                    else:
                        action [SetScreenVariable("selected_move", player.special_attack), Show("action_info", None, fight, player, opponent, player.special_attack)]

                    text str(player.special_attack.stamina_cost) xalign 1.0 font "fonts/Montserrat-Bold.ttf"
                    text player.special_attack.name align (0.5, 0.5) text_align 0.5

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


screen health_bars(player, opponent, move=None):
    default bar_size = 550.0
    default guard_segment_size = (bar_size - BasePlayer.MAX_GUARD) / BasePlayer.MAX_GUARD
    default opponent_health_segment_size = (bar_size - opponent.fighter.max_health) / opponent.fighter.max_health
    default player_health_segment_size = (bar_size - player.fighter.max_health) / player.fighter.max_health

    hbox:
        xalign 1.0
        xoffset -20
        ypos 50
        spacing 10

        vbox:
            yalign 0.5
            spacing 5

            # Opponent Guard
            hbox:
                xalign 0.5
                spacing 1

                if hasattr(move, "damage"):
                    for i in range(opponent.fighter.guard - move.damage):
                        add Transform("#00f", size=(guard_segment_size, 25))

                    for i in range(min(opponent.fighter.guard, move.damage)):
                        add Transform("fight_guard_animation", size=(guard_segment_size, 25))

                    for i in range(BasePlayer.MAX_GUARD - opponent.fighter.guard):
                        add Transform("#404040", size=(guard_segment_size, 25))

                else:
                    for i in range(1, BasePlayer.MAX_GUARD + 1):
                        if i > opponent.fighter.guard:
                            add Transform("#404040", size=(guard_segment_size, 25))
                        else:
                            add Transform("#00f", size=(guard_segment_size, 25))

            # Opponent Health
            hbox:
                xalign 0.5
                spacing 1

                if hasattr(move, "damage"):
                    for i in range(opponent.fighter.max_health - min(opponent.fighter.health, (move.damage - opponent.fighter.guard)) - (opponent.fighter.max_health - opponent.fighter.health)):
                        add Transform("#f00", size=(opponent_health_segment_size, 35))

                    for i in range(min(opponent.fighter.health, (move.damage - opponent.fighter.guard))):
                        add Transform("fight_health_animation", size=(opponent_health_segment_size, 35))

                    for i in range(opponent.fighter.max_health - opponent.fighter.health):
                        add Transform("#404040", size=(opponent_health_segment_size, 35))

                else:
                    for i in range(1, opponent.fighter.max_health + 1):
                        if i > opponent.fighter.health:
                            add Transform("#404040", size=(opponent_health_segment_size, 35))
                        else:
                            add Transform("#f00", size=(opponent_health_segment_size, 35))

        add Transform(opponent.profile_picture, xysize=(65, 65))

    hbox:
        pos (20, 50)
        spacing 10

        add Transform(player.profile_picture, xysize=(65, 65))

        vbox:
            yalign 0.5
            spacing 5

            # Player Guard
            hbox:
                xalign 0.5
                spacing 1

                for i in range(1, BasePlayer.MAX_GUARD + 1):
                    if i > player.fighter.guard:
                        add Transform("#404040", size=(guard_segment_size, 25))
                    else:
                        add Transform("#00f", size=(guard_segment_size, 25))

            # Player Health
            hbox:
                xalign 0.5
                spacing 1

                for i in range(1, player.fighter.max_health + 1):
                    if i > player.fighter.health:
                        add Transform("#404040", size=(player_health_segment_size, 35))
                    else:
                        add Transform("#f00", size=(player_health_segment_size, 35))


screen action_info(fight, player, opponent, move):
    zorder 100
    style_prefix "fight_turn"

    frame:
        xalign 0.5
        ypos 700
        background Frame("#fff")
        padding (10, 10)

        vbox:
            spacing 20

            hbox:
                spacing 20

                button:
                    xalign 0.5
                    idle_background "#a8a8a8"
                    hover_background "#ffd000"
                    action [Hide("action_info"), Function(player.set_stance_bonus, move), Call("fight_attack_turn", fight, opponent, player, move)]
                    
                    text ">>> {} <<<".format(move.name) size 30 font "fonts/Montserrat-Bold.ttf" align (0.5, 0.5)

                if hasattr(move, "damage") and move.damage is not None:
                    text "{{font=fonts/Montserrat-Bold.ttf}}Damage:{{/font}} {}".format(move.damage) xalign 0.5

            text move.description
            text "{{font=fonts/Montserrat-Bold.ttf}}Stance Bonus:{{/font}} {}".format(move.effect)


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

style fight_overview_title is montserrat_extra_bold_64:
    color "#fff"

style fight_overview_text is text:
    font "fonts/Montserrat-ExtraBold.ttf"
    color "#fff"
    size 20
    text_align 0.5
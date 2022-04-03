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
        add "images/fight/overview/frame-background.webp" pos (-54, -50)

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
            spacing 25

            hbox:
                spacing 50

                text "BASIC ATTACKS" yalign 0.5

                grid 2 2:
                    spacing 10

                    for attack in competitor.base_attacks:
                        button:
                            idle_background image_path + "attack-idle.webp"
                            hover_background image_path + "attack-idle.webp"
                            if is_player:
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
                            idle_background image_path + "attack-idle2.webp"
                            selected_background image_path + "attack-hover.webp"
                            selected (competitor.special_attack is not None and competitor.special_attack.name == attack.name)                               
                            xysize (206, 58)
                            padding (5, 5)
                            if is_player:
                                tooltip attack.description
                                hover_background image_path + "attack-hover.webp"
                                # action SetField(competitor, "special_attack", attack) # Disabled for v3.0
                                action NullAction()
                            else:
                                hover_background image_path + "attack-idle2.webp"
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
                            idle_background image_path + "attack-idle2.webp"
                            selected_background image_path + "attack-hover.webp"
                            selected (competitor.quirk is not None and competitor.quirk.name == quirk.name)
                            xysize (206, 58)
                            padding (5, 5)
                            if is_player:
                                # tooltip attack.description
                                hover_background image_path + "attack-hover.webp"
                                # action SetField(competitor, "quirk", quirk)
                                action NullAction() # Disabled for v3.0
                            else:
                                hover_background image_path + "attack-idle2.webp"
                                action NullAction()

                            text quirk.name align (0.5, 0.5)

        $ tooltip = GetTooltip()

        fixed:
            align (0.5, 1.0)
            xysize (700, 100)

            if tooltip and is_player:
                text "[tooltip]" align (0.5, 0.5)
            else:
                text "Special Attacks and Quirks are {b}disabled{/b} to keep the fight simple and get accurate feedback on player experience" align (0.5, 0.5)


screen fight_overview(fight, title):
    modal True
    style_prefix "fight_overview"

    default image_path = "images/fight/overview/"
    default difficulties = ["Easy", "Normal", "Hard", "Oscar"]
    default difficulty_index = 1

    python:
        player = fight.player.fighter
        opponent = fight.opponent.fighter

    add image_path + "background.webp"

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

        use fight_overview_info(opponent, fight.opponent.profile_picture, is_player=False)

    hbox:
        xpos 100
        yalign 1.0
        yoffset -100
        spacing 20

        text "DIFFICULTY:"

        imagebutton:
            idle Transform("gui/common/left-arrow.webp", xysize=(10, 15))
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
            idle Transform("gui/common/right-arrow.webp", xysize=(10, 15))
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
            idle image_path + "play-fight-idle.webp"
            hover image_path + "play-fight-hover.webp"
            action [SetField(opponent, "max_health", int(opponent.max_health)),
                SetField(opponent, "max_stamina", int(opponent.max_stamina)),
                Call("fight_start_turn", fight, opponent, player)]
            yalign 0.5

        imagebutton:
            idle image_path + "skip-fight-idle.webp"
            hover image_path + "skip-fight-hover.webp"
            action [SetField(opponent, "max_health", int(opponent.max_health)),
                SetField(opponent, "max_stamina", int(opponent.max_stamina)),
                Jump(fight.end_label)]
            yalign 0.5

    if config_debug:
        timer 0.1 action [SetField(opponent, "max_health", int(opponent.max_health)),
                SetField(opponent, "max_stamina", int(opponent.max_stamina)),
                Call("fight_start_turn", fight, opponent, player)]


screen fight_player_turn(fight, player, opponent):
    tag fight_screen
    style_prefix "fight_turn"

    default image_path = "images/fight/player-turn/"
    default selected_move = None
    default max_stamina = player.stamina

    add opponent.stance_image

    use health_bars(fight.player, fight.opponent, selected_move)

    frame:
        background image_path + "stance1.webp"
        xalign 0.5
        ypos 50
        xysize (568, 63)
        style_prefix "fight_turn_stance"

        hbox:
            align (0.5, 0.5)

            for i in FightStance:
                frame:
                    align (0.5, 0.5)

                    if i == player.stance:
                        xysize (164, 81)

                        add image_path + "stance-current.webp"

                        vbox:
                            align (0.5, 0.5)

                            text "CURRENT STANCE" size 14 xalign 0.5
                            text i.name xalign 0.5

                    elif selected_move is not None and i == selected_move.ideal_stance:
                        xysize (135, 63)

                        add image_path + "stance-ideal.webp"

                        vbox:
                            align (0.5, 0.5)

                            text "IDEAL STANCE" size 14 xalign 0.5
                            text i.name xalign 0.5
 
                    elif selected_move is not None and i == selected_move.end_stance:
                        xysize (135, 63)

                        add image_path + "stance-end.webp"

                        vbox:
                            align (0.5, 0.5)

                            text "END STANCE" size 14 xalign 0.5
                            text i.name xalign 0.5

                    else:
                        xysize (135, 63)

                        text i.name align (0.5, 0.5)

    hbox:
        xalign 0.5
        yalign 1.0
        yoffset -50
        spacing -17

        for move in player.base_attacks + player.turn_moves:
            button:
                if move.ideal_stance == player.stance:
                    idle_background image_path + "actions-ideal-idle.webp"
                    hover_background image_path + "actions-ideal-hover.webp"
                    selected_background image_path + "actions-ideal-hover.webp"
                else:
                    idle_background image_path + "actions-idle.webp"
                    hover_background image_path + "actions-hover.webp"
                    selected_background image_path + "actions-hover.webp"
                insensitive_background image_path + "actions-insensitive.webp"
                sensitive (player.stamina >= move.stamina_cost)
                selected (selected_move == move)
                if selected_move == move:
                    action [SetScreenVariable("selected_move", None), Hide("action_info")]
                else:
                    action [SetScreenVariable("selected_move", move), Show("action_info", None, fight, player, opponent, move)]
                xysize (234, 172)
                padding (45, 45)

                vbox:
                    align (0.5, 0.5)
                    spacing 5

                    text move.name xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 5

                        for i in range(1, player.max_stamina + 1):
                            if i > move.stamina_cost:
                                add image_path + "action-stamina-empty.webp"
                            else:
                                add image_path + "action-stamina-filled.webp"

        if player.special_attack is not None or False: # INFO: Disabled for act 1 (missing images)
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
        xpos 50
        yalign 1.0
        yoffset -35
        spacing 5

        text "STAMINA" size 15

        hbox:
            spacing 5

            for i in range(1, player.max_stamina + 1):
                if i > player.stamina:
                    add image_path + "stamina-empty.webp"
                else:
                    add image_path + "stamina-filled.webp"

    if config_debug:
        timer 0.1 action [Function(player.set_stance_bonus, renpy.random.choice(player.base_attacks + player.turn_moves)), Call("fight_attack_turn", fight, opponent, player, move)]


style fight_turn_text is text:
    size 26
    color "#fff"
    font "fonts/Montserrat-Regular.ttf"
    text_align 0.5

style fight_turn_stance_text is text:
    size 24
    color "#fff"
    font "fonts/BebasNeue-Regular.ttf"
    text_align 0.5


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
    style_prefix "fight_turn"

    default image_path = "images/fight/player-turn/"
    default player_max_stamina = player.stamina

    vbox:
        align (0.5, 1.0)
        yoffset -250
        spacing 35

        if move.ideal_stance == player.stance or move.ideal_stance is None:
            frame:
                xysize (428, 132)
                background image_path + "action-stance-info.webp"
                padding (12, 48, 12, 12)

                text move.effect align (0.5, 0.5) text_align 0.5 size 13

        frame:
            xysize (428, 142)
            background image_path + "action-info.webp"
            padding (15, 15)

            vbox:
                xalign 0.5
                spacing 15

                frame:
                    ysize 30

                    if hasattr(move, "damage") and move.damage is not None:
                        text "Damage: {}".format(move.damage) size 15 yalign 0.5

                    text move.name size 30 align (0.5, 0.5)

                    hbox:
                        align (1.0, 0.5)
                        spacing 2

                        for i in range(1, player_max_stamina + 1):
                            if i > move.stamina_cost:
                                add Transform(image_path + "stamina-empty.webp", zoom=0.4)
                            else:
                                add Transform(image_path + "stamina-filled.webp", zoom=0.4)

                text move.description size 13 text_align 0.5 xalign 0.5

            button:
                align (0.5, 1.0)
                yoffset 60
                idle_background image_path + "action-use-idle.webp"
                hover_background image_path + "action-use-hover.webp"
                action [Hide("action_info"), Function(player.set_stance_bonus, move), Call("fight_attack_turn", fight, opponent, player, move)]
                xysize (160, 96)
                padding (32, 32)

                text "USE" align (0.5, 0.5)


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


style fight_overview_title is montserrat_extra_bold_64:
    color "#fff"

style fight_overview_text is text:
    font "fonts/Montserrat-ExtraBold.ttf"
    color "#fff"
    size 20
    text_align 0.5
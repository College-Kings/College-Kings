screen base_fight_stats(character):
    tag fight_screens
    modal True
    style_prefix "fight_stats"

    default fighter = opponent
    default next_rank_win_requirement = FightRank.next_rank(fighter.wins)

    text str(character.name) size 50 xalign 0.0

    text "Victories: {} | Rank: {} | Fighting Style: {}".format(fighter.wins, fighter.rank.name, fighter.fighting_style.name.replace('_', ' ')):
        size 16
        font "fonts/Montserrat-Regular.ttf"
        xalign 0.0

    bar:
        value fighter.wins
        range next_rank_win_requirement
        left_bar "gui/fight_prototype/rank_bar_fill.png"
        right_bar "gui/fight_prototype/rank_bar_background.png"
        xysize (476, 10)

    text "{} win(s) to next rank.".format(next_rank_win_requirement - fighter.wins):
        font "fonts/Montserrat-Regular.ttf"
        size 16
        xalign 0.0

    null height 25

    transclude # Attacks

    null height 25

    vbox:
        spacing 10

        text "Defenses" xalign 0.0

        # hbox:
        #     spacing 20

            # for guard in Guard:
            #     button:
            #         xysize (58, 58)
            #         idle_background "gui/fight_prototype/fight_slot_hover.png"
            #         hover_background "gui/fight_prototype/fight_slot_hover.png"
            #         action NullAction()

            #         text guard.name.replace('_', ' ') align (0.5, 0.9) size 15


screen player_fight_stats(player_attacks=None, player=player, extra_points=0):
    tag fight_screens
    modal True
    style_prefix "fight_stats"

    $ selected_attrs = list(attr.value for attr in player.attributes)
    default locked_attribute_values = selected_attrs
    default available_points = player.rank.value["bonus_attribute_points"] + extra_points

    frame:
        background Transform("gui/fight_prototype/fight_background.png", size=(700, 900))
        xysize (700, 900)
        padding (50, 50)
        xpos 50
        yalign 0.5

        has vbox
    
        use base_fight_stats(mc):
            vbox:
                spacing 10

                text "Attacks"

                hbox:
                    spacing 100

                    vbox:
                        spacing 5

                        text "Light Attack" size 15
                        hbox:
                            spacing 20

                            for attack in filter(lambda attack: attack.move_type == AttackType.LIGHT, player_attacks):
                                button:
                                    xysize (58, 58)
                                    idle_background "gui/fight_prototype/fight_slot_idle.png"
                                    hover_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected player.attacks[AttackType.LIGHT] == attack
                                    action SetDict(player.attacks, AttackType.LIGHT, attack)

                                    text attack.name.name.replace('_', ' ') align (0.5, 0.9) size 15

                    vbox:
                        spacing 5

                        text "Heavy Attack" size 15
                        hbox:
                            spacing 20

                            for attack in filter(lambda attack: attack.move_type == AttackType.HEAVY, player_attacks):
                                button:
                                    xysize (58, 58)
                                    idle_background "gui/fight_prototype/fight_slot_idle.png"
                                    hover_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected player.attacks[AttackType.HEAVY] == attack
                                    action SetDict(player.attacks, AttackType.HEAVY, attack)

                                    text attack.name.name.replace('_', ' ') align (0.5, 0.9) size 15

        null height 25

        vbox:
            spacing 10

            hbox:
                spacing 10
                
                text "Attributes"
                text "+" + str(available_points) color "#44D7B6"
                
                null width 50

                textbutton "Confirm" action [SetScreenVariable("locked_attribute_values", selected_attrs), Function(player.set_specials)]

            hbox:
                spacing 10

                vbox:
                    spacing 10

                    for attr in player.attributes:
                        text attr.name xalign 1.0 size 15

                vbox:
                    spacing 10

                    for i, attr in enumerate(player.attributes):
                        hbox:
                            spacing 10

                            for x in range(1, 11):
                                imagebutton:
                                    if (x == 5 or x == 10) and x <= locked_attribute_values[i]:
                                        idle "gui/fight_prototype/fight_circle_gold_hover.png"
                                        insensitive "gui/fight_prototype/fight_circle_gold_hover.png"
                                    elif x <= locked_attribute_values[i]:
                                        idle "gui/fight_prototype/fight_circle_dark_idle.png"
                                        insensitive "gui/fight_prototype/fight_circle_dark_idle.png"
                                    elif x == 5 or x == 10:
                                        idle "gui/fight_prototype/fight_circle_gold_idle.png"
                                        hover "gui/fight_prototype/fight_circle_gold_hover.png"
                                        selected_idle "gui/fight_prototype/fight_circle_gold_hover.png"
                                    else:
                                        idle "gui/fight_prototype/fight_circle_idle.png"
                                        hover "gui/fight_prototype/fight_circle_hover.png"
                                        selected_idle "gui/fight_prototype/fight_circle_hover.png"
                                    insensitive "gui/fight_prototype/fight_circle_insensitive.png"
                                    sensitive ( available_points - x + attr.value ) >= 0
                                    selected x <= attr.value
                                    if x > locked_attribute_values[i]:
                                        action [
                                            ToggleField(attr, "value", x, locked_attribute_values[i]),
                                            ToggleScreenVariable("available_points", available_points + selected_attrs[i] - x, available_points + selected_attrs[i] - locked_attribute_values[i])
                                            ]

                            if attr.value == 10:
                                text "Active Unlocked" color "#44D7B6" size 16 yalign 0.5
                            elif attr.value >= 5:
                                text "Passive Unlocked" color "#44D7B6" size 16 yalign 0.5

            null height 30

            hbox:
                xsize 650
                xoffset -25

                vbox:
                    spacing 5

                    text "Attribute Passives" size 15
                    hbox:
                        spacing 20

                        for ability in player.passive_abilities:
                            button:
                                xysize (58, 58)
                                idle_background "gui/fight_prototype/fight_slot_idle.png"
                                hover_background "gui/fight_prototype/fight_slot_hover.png"
                                selected_background "gui/fight_prototype/fight_slot_hover.png"
                                selected ability in player.passive_abilities
                                action NullAction()

                                text ability.name.replace('_', ' ') align (0.5, 0.9) size 15

                vbox:
                    spacing 5
                    xalign 1.0
                    xsize 292

                    text "Attribute Actives" size 15
                    hbox:
                        spacing 20

                        for ability in player.special_abilities:
                            button:
                                xysize (58, 58)
                                idle_background "gui/fight_prototype/fight_slot_idle.png"
                                hover_background "gui/fight_prototype/fight_slot_hover.png"
                                selected_background "gui/fight_prototype/fight_slot_hover.png"
                                selected player.special_ability == ability
                                action ToggleField(player, "special_ability", ability, None)

                                text ability.name.replace('_', ' ') align (0.5, 0.9) size 15

# IMPROVEMENT: Improve slider experience on attributes


screen opponent_fight_stats(opponent):
    tag fight_screens
    modal True
    style_prefix "fight_stats"

    frame:
        background Transform("gui/fight_prototype/fight_background.png", size=(700, 900))
        xysize (700, 900)
        padding (50, 50)
        xalign 1.0
        xoffset -50
        yalign 0.5

        has vbox
    
        use base_fight_stats(adam):
            vbox:
                spacing 10

                text "Attacks"

                hbox:
                    spacing 100

                    vbox:
                        spacing 5

                        text "Light Attack" size 15
                        hbox:
                            spacing 20

                            button:
                                xysize (58, 58)
                                idle_background "gui/fight_prototype/fight_slot_idle.png"
                                hover_background "gui/fight_prototype/fight_slot_hover.png"
                                selected_background "gui/fight_prototype/fight_slot_hover.png"
                                selected True
                                action NullAction()

                                text opponent.attacks[AttackType.LIGHT].name.name.replace('_', ' ') align (0.5, 0.9) size 15

                    vbox:
                        spacing 5

                        text "Heavy Attack" size 15
                        hbox:
                            spacing 20

                            button:
                                xysize (58, 58)
                                idle_background "gui/fight_prototype/fight_slot_idle.png"
                                hover_background "gui/fight_prototype/fight_slot_hover.png"
                                selected_background "gui/fight_prototype/fight_slot_hover.png"
                                selected True
                                action NullAction()

                                text opponent.attacks[AttackType.HEAVY].name.name.replace('_', ' ') align (0.5, 0.9) size 15
        null height 25

        vbox:
            spacing 10
                
            text "Attributes"

            hbox:
                spacing 10

                vbox:
                    spacing 10

                    for attr in AttributeType:
                        text attr.name.replace('_', ' ') xalign 1.0 size 15

                vbox:
                    spacing 10

                    for attr in opponent.attributes:
                        hbox:
                            spacing 10

                            for x in range(1, 11):
                                if (x == 5 or x == 10) and x <= attr.value:
                                    add "gui/fight_prototype/fight_circle_gold_hover.png"
                                elif x <= attr.value:
                                    add "gui/fight_prototype/fight_circle_dark_idle.png"
                                else:
                                    add "gui/fight_prototype/fight_circle_insensitive.png"

            null height 30

            hbox:
                xsize 650
                xoffset -25

                vbox:
                    spacing 5

                    text "Attribute Passives" size 15
                    hbox:
                        spacing 20

                        for ability in opponent.passive_abilities:
                            button:
                                xysize (58, 58)
                                idle_background "gui/fight_prototype/fight_slot_idle.png"
                                selected_background "gui/fight_prototype/fight_slot_hover.png"
                                selected True
                                action NullAction()

                                text ability.name.replace('_', ' ') align (0.5, 0.9) size 15

                vbox:
                    spacing 5
                    xalign 1.0
                    xsize 292

                    text "Attribute Actives" size 15
                    hbox:
                        spacing 20

                        for ability in opponent.special_abilities:
                            button:
                                xysize (58, 58)
                                idle_background "gui/fight_prototype/fight_slot_idle.png"
                                selected_background "gui/fight_prototype/fight_slot_hover.png"
                                selected True
                                action NullAction()

                                text ability.name.replace('_', ' ') align (0.5, 0.9) size 15


screen fight_menu(player_attacks, rivalry_status, player=player, opponent=opponent, extra_points=0):
    tag fight_screens
    modal True
    style_prefix "fight_stats"

    default difficulties = (
        ("Easy", 1.5),
        ("Medium", 1),
        ("Hard", 0.75),
        ("Impossible", 0.5)
    )
    default difficulty_index = 0

    use player_fight_stats(player_attacks, player, extra_points)
    
    vbox:
        xalign 0.5
        ypos 100

        text "Rivalry Status" color "#fff" xalign 0.5
        text str(rivalry_status) color "#fff" xalign 0.5

    textbutton "Difficulty: {}".format(difficulties[difficulty_index][0]):
        xalign 0.5
        ypos 950
        text_color "#fff"
        if difficulty_index < len(difficulties) - 1:
            action [SetScreenVariable("difficulty_index", difficulty_index + 1), SetVariable("fight_reaction_time", difficulties[difficulty_index][1])]
        else:
            action [SetScreenVariable("difficulty_index", 0), SetVariable("fight_reaction_time", 1.5)]

    use opponent_fight_stats(opponent)

    hbox:
        xalign 0.5
        ypos 1015
        spacing 100

        textbutton "Skip Fight (Auto-win)":
            action Jump(fight_end_label)
            text_color "#fff"

        textbutton "Play Fight":
            action Return()
            text_color "#fff"

    on "show" action [SetVariable("quick_menu", False), Hide("phone_icon")]
    on "hide" action [SetVariable("quick_menu", True), Show("phone_icon")]
    on "replace" action [SetVariable("quick_menu", False), Hide("phone_icon")]
    on "replaced" action [SetVariable("quick_menu", True), Show("phone_icon")]

style fight_stats_text is text:
    color "#000"
    font "fonts/Montserrat-Bold.ttf"

style fight_stats_button_text is button_text:
    idle_color "#fff"
    hover_color "#44D7B6"
    font "fonts/Montserrat-Bold.ttf"
    size 25
    outlines [ (absolute(0), "#000", absolute(0), absolute(0)) ]


screen fight_attack(player=player, opponent=opponent):
    tag fight_screens
    modal True

    default timing_var = 0 ## TODO: Remove debugging

    add opponent.images["neutral"]

    use animated_value_bar(None, timing_var, 100, "blue_bar", "ruby_bar", offset=(13, 0), size=(800, 95), delay=0.025)

    for k, move in player.moves.items():
        key k:
            action Call("player_attack_turn", move, player, opponent)

    timer 0.025:
        repeat True
        if timing_var == 100:
            action [SetField(player, "stamina", player.stamina + 5), SetField(opponent, "stamina", opponent.stamina + 5), Call("opponent_attack_turn", player, opponent)]
        else:
            action SetScreenVariable("timing_var", timing_var + 1)


screen fight_defense(opponent_attack, player=player, opponent=opponent):
    tag fight_screens
    modal True

    default timing_var = 0 ## TODO: Remove debugging

    add opponent_attack.images["start_image"]

    use animated_value_bar(None, timing_var, 100, "blue_bar", "ruby_bar", offset=(13, 0), size=(800, 95), delay=0.01)

    for k, move in player.moves.items():
        key k:
            action Call("player_defence_turn", timing_var, move, player, opponent_attack, opponent)

    timer 0.01:
        repeat True
        if timing_var == 100:
            action Call("player_defence_turn", timing_var, None, player, opponent_attack, opponent)
        else:
            action SetScreenVariable("timing_var", timing_var + 1)


screen fight_popup(message):
    text message:
        size 100

    timer 2 action Hide("fight_popup", transition=dissolve)


screen new_fight_overlay(player, opponent):
    zorder 100

    vbox:
        pos (50, 900)
        spacing -25

        hbox:
            text "Health bar:" yalign 0.5
            use animated_value_bar(None, player.health, player.max_health, "blue_bar", "ruby_bar", offset=(13, 0), size=(400, 95), delay=1) # Player Health Bar
        hbox:
            text "Stamina bar:" yalign 0.5
            use animated_value_bar(None, player.stamina, player.max_stamina, "blue_bar", "ruby_bar", offset=(13, 0), size=(400, 95), delay=1) # Player Stamina Bar

    vbox:
        xalign 0.5
        ypos 50

        use animated_value_bar(None, opponent.health, opponent.max_health, "blue_bar", "ruby_bar", offset=(13, 0), size=(1000, 95), delay=1) # Opponent Health Bar


screen test_health():
    zorder 100

    text str(fight_game_state.name) xalign 0.5

    vbox:
        align (0.1, 0.1)

        text "Player" size 50
        # text "Guard: {}".format(player.guard):
        #     size 50
        #     color "#494ce6"
        text "Stamina: {}".format(player.stamina):
            size 50
            color "#ffa600"

        null height 100

        text "Opponent" size 50
        # text "Guard: {}".format(opponent.guard):
        #     size 50
        #     color "#494ce6"
        text "Stamina: {}".format(opponent.stamina):
            size 50
            color "#ffa600"


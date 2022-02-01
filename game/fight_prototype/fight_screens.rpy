screen fight_menu(player_attacks=None, player=player):
    tag fight_screens
    modal True
    style_prefix "fight_menu_style"

    $ selected_attrs = list(attr.value for attr in player.attributes)
    default locked_attribute_values = selected_attrs
    default available_points = player.fight_rank.value

    frame:
        background Transform("gui/fight_prototype/fight_background.png", size=(700, 900))
        xysize (700, 900)
        padding (50, 50)
        align (0.5, 0.5)

        vbox:
            spacing 30

            vbox:
                text name size 50 
                hbox: 
                    spacing 100
                    text "Brawler" size 25 # TODO: Fighting style

                    hbox:
                        spacing 5
                        text "Rivalry:" size 25
                        text "First Fight" size 25 # TODO: Rivalry style

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

            vbox:
                spacing 10

                text "Defense"
                hbox:
                    spacing 20

                    for guard in Guard:
                        button:
                            xysize (58, 58)
                            idle_background "gui/fight_prototype/fight_slot_hover.png"
                            hover_background "gui/fight_prototype/fight_slot_hover.png"
                            action NullAction()

                            text guard.name.replace('_', ' ') align (0.5, 0.9) size 15

            # Attributes
            vbox:
                spacing 10

                # $ available_points = max_points - sum(selected_attrs)

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

        # Confirm Button
        textbutton "Continue":
            action Return()
            sensitive (locked_attribute_values == selected_attrs)
            align (1.0, 1.0)

# IMPROVEMENT: Improve slider experience on attributes

style fight_menu_style_text is text:
    color "#000"
    font "fonts/Montserrat-Bold.ttf"
    text_align 0.5

style fight_menu_style_button_text is button_text:
    color "#000"
    font "fonts/Montserrat-Bold.ttf"
    size 25
    outlines [(0, "#000", 0, 0)]
    hover_outlines [(0, "#44D7B6", 0, 0)]
    hover_color "#44D7B6"


screen fight_attack(player=player, opponent=opponent):
    tag fight_screens
    modal True

    add opponent.guard_image

    for k, move in player.moves.items():
        key k:
            action Call("player_attack_turn", move, player, opponent) 

    timer fight_reaction_time action Call("opponent_attack_turn", player, opponent)


screen fight_defense(opponent_attack, player=player, opponent=opponent):
    tag fight_screens
    modal True

    add opponent_attack.images["start_image"]

    for k, move in player.moves.items():
        key k:
            action Call("player_defence_turn", move, player, opponent_attack, opponent)

    timer fight_reaction_time action Call("player_defence_turn", None, player, opponent_attack, opponent)


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
            use animated_value_bar(None, player.health, player.max_health, "blue_bar", "ruby_bar", offset=(13, 0), size=(400, 95)) # Player Health Bar
        hbox:
            text "Stamina bar:" yalign 0.5
            use animated_value_bar(None, player.stamina, player.max_stamina, "blue_bar", "ruby_bar", offset=(13, 0), size=(400, 95), delay=1) # Player Stamina Bar

    vbox:
        xalign 0.5
        ypos 50

        use animated_value_bar(None, opponent.health, opponent.max_health, "blue_bar", "ruby_bar", offset=(13, 0), size=(1000, 95)) # Opponent Health Bar


screen test_health():
    zorder 100

    vbox:
        align (0.1, 0.1)

        text "Player" size 50
        text "Guard: {}".format(player.guard):
            size 50
            color "#494ce6"

        null height 100

        text "Opponent" size 50
        text "Guard: {}".format(opponent.guard):
            size 50
            color "#494ce6"
        text "Stamina: {}".format(opponent.stamina):
            size 50
            color "#ffa600"


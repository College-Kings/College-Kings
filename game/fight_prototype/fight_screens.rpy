screen fight_menu(attacks=None, player=player, max_points=18):
    modal True
    style_prefix "fight_menu_style"

    default locked_attribute_values = list(attr.value for attr in player.attributes)

    frame:
        background Transform("gui/fight_prototype/fight_background.png", size=(700, 900))
        xysize (700, 900)
        padding (50, 50)
        align (0.5, 0.5)

        vbox:
            spacing 30

            vbox:
                text name size 50 
                text "Brawler" size 25 # TODO: Fighting style

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

                            for attack in filter(lambda attack: attack.move_type == AttackType.LIGHT, attacks):
                                button:
                                    xysize (58, 58)
                                    idle_background "gui/fight_prototype/fight_slot_idle.png"
                                    hover_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected player.attacks[AttackType.LIGHT] == attack
                                    action SetDict(player.attacks, AttackType.LIGHT, attack)

                                    text attack.name align (0.5, 0.9) size 15

                    vbox:
                        spacing 5

                        text "Heavy Attack" size 15
                        hbox:
                            spacing 20

                            for attack in filter(lambda attack: attack.move_type == AttackType.HEAVY, attacks):
                                button:
                                    xysize (58, 58)
                                    idle_background "gui/fight_prototype/fight_slot_idle.png"
                                    hover_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected player.attacks[AttackType.HEAVY] == attack
                                    action SetDict(player.attacks, AttackType.HEAVY, attack)

                                    text attack.name align (0.5, 0.9) size 15

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

                $ available_points = max_points - sum(attr.value for attr in player.attributes)

                hbox:
                    spacing 10
                    text "Attributes"
                    text "+" + str(available_points) color "#44D7B6"
                    textbutton "Confirm" action [SetScreenVariable("locked_attribute_values", list(attr.value for attr in player.attributes)), Function(player.set_specials)]

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
                                            action ToggleField(attr, "value", x, locked_attribute_values[i])

                                if attr.value == 10:
                                    text "Active Unlocked" color "#44D7B6" size 16 yalign 0.5
                                elif attr.value >= 5:
                                    text "Passive Unlocked" color "#44D7B6" size 16 yalign 0.5

                hbox:
                    spacing 100

                    vbox:
                        spacing 5

                        text "Attribute Passives" size 15
                        hbox:
                            spacing 20

                            for attack in filter(lambda attack: attack.move_type == AttackType.LIGHT, attacks): #TODO: show attribute passives
                                button:
                                    xysize (58, 58)
                                    idle_background "gui/fight_prototype/fight_slot_idle.png"
                                    hover_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected player.attacks[AttackType.LIGHT] == attack 
                                    action SetDict(player.attacks, AttackType.HEAVY, attack) #TODO: no effect, unlocked based on attributes

                                    text attack.name align (0.5, 0.9) size 15

                    vbox:
                        spacing 5

                        text "Attribute Actives" size 15
                        hbox:
                            spacing 20

                            for attack in filter(lambda attack: attack.move_type == AttackType.HEAVY, attacks): #TODO: show attribute actives
                                button:
                                    xysize (58, 58)
                                    idle_background "gui/fight_prototype/fight_slot_idle.png"
                                    hover_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected_background "gui/fight_prototype/fight_slot_hover.png"
                                    selected player.attacks[AttackType.HEAVY] == attack
                                    action SetDict(player.attacks, AttackType.HEAVY, attack) #TODO: no effect, unlocked based on attributes

                                    text attack.name align (0.5, 0.9) size 15

# TODO: Improve slider experience on attributes

style fight_menu_style_text is text:
    color "#000"
    font "fonts/Montserrat-Bold.ttf"


screen fight_attack(player=player, opponent=opponent):
    tag fight
    modal True

    add opponent.guard_image

    for k, move in player.moves.items():
        key k:
            action Call("player_attack_turn", move, player, opponent) 

    timer fight_reaction_time action Call("opponent_attack_turn", player, opponent)


screen fight_defense(opponent_attack, player=player, opponent=opponent):
    tag fight
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


screen health_bar(current_health, new_health, max_health=100):
    tag health_bar
    zorder 100

    fixed:
        xysize (820, 95)
        xalign 0.5
        ypos 83
        use animated_value_bar(current_health, new_health, max_health, "blue_bar", "ruby_bar", offset=(13, 0), size=(820, 95))


screen test_health():
    zorder 100

    vbox:
        align (0.1, 0.1)
        text "[opponent.health]":
            size 50
            color "#eb5858"  
        text "[opponent.guard]":
            size 50
            color "#494ce6"
        text str(opponent.stamina):
            size 50
            color "#ffa600"

    vbox:
        align (0.1, 0.9)
        text "[player.health]":
            size 50
            color "#eb5858"
        text "[player.guard]":
            size 50
            color "#494ce6"
        text str(player.stamina):
            size 50
            color "#ffa600"


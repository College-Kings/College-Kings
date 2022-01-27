screen fight_menu(attacks=None, player=player):
    modal True
    style_prefix "fight_menu_style"

    default temp_attribute_health = 0
    default temp_attribute_stamina = 0
    default temp_attribute_light_attack_damage = 0
    default temp_attribute_heavy_attack_damage = 0

    default temp_max_available_attributes = 18
    
    python:
        temp_available_attributes = temp_max_available_attributes - sum((temp_attribute_health, temp_attribute_stamina, temp_attribute_light_attack_damage, temp_attribute_heavy_attack_damage))

        attributes = [
            ("Health", "temp_attribute_health"),
            ("Stamina", "temp_attribute_stamina"),
            ("Light Attack Damage", "temp_attribute_light_attack_damage"),
            ("Heavy Attack Damage", "temp_attribute_heavy_attack_damage")
        ]

    frame:
        background Transform("gui/fight_prototype/fight_background.png", size=(700, 900))
        xysize (700, 900)
        padding (50, 50)
        align (0.5, 0.5)

        vbox:
            spacing 50

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
                                    action Function(player.set_attack, AttackType.LIGHT, attack)

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
                                    action Function(player.set_attack, AttackType.HEAVY, attack)

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

            vbox:
                spacing 10

                hbox:
                    spacing 10
                    text "Attributes"
                    text "+" + str(temp_available_attributes) color "#44D7B6"

                hbox:
                    spacing 10

                    vbox:
                        spacing 10

                        for attr in attributes:
                            text attr[0] xalign 1.0 size 15 # Name

                    vbox:
                        spacing 10

                        for attr in attributes:
                            $ attribute_var = renpy.current_screen().scope[attr[1]]

                            hbox:
                                spacing 10

                                for i in range(1, 11):
                                    imagebutton:
                                        if i == 5 or i == 10:
                                            idle "gui/fight_prototype/fight_circle_gold_idle.png"
                                            hover "gui/fight_prototype/fight_circle_gold_hover.png"
                                            selected_idle "gui/fight_prototype/fight_circle_gold_hover.png"
                                        else:
                                            idle "gui/fight_prototype/fight_circle_idle.png"
                                            hover "gui/fight_prototype/fight_circle_hover.png"
                                            selected_idle "gui/fight_prototype/fight_circle_hover.png"
                                        insensitive "gui/fight_prototype/fight_circle_insensitive.png"
                                        sensitive ( temp_available_attributes - i + attribute_var ) >= 0
                                        selected i <= attribute_var
                                        action ToggleScreenVariable(attr[1], i, 0)

                                if attribute_var == 10:
                                    text "Active Unlocked" color "#0f0" size 16 yalign 0.5
                                elif attribute_var >= 5:
                                    text "Passive Unlocked" color "#0f0" size 16 yalign 0.5

# TODO: Improve slider experiance on attributes

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


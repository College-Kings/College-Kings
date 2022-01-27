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

screen fight_style_selection():

    add "images/v15/detective_board/archetype_background.webp"

    text "You've watched enough crime shows to know what questions need to be asked. You've got the mind of a true detective.":
        pos (190,700)
        xsize 400
        text_align 0.5
        font "fonts/Effra-Regular.ttf"
        size 23

    text "Why do people do the things they do? What are the obvious signs of a liar? You're perceptive, mindful, and thorough.":
        pos (787,700)
        xsize 400
        text_align 0.5
        font "fonts/Effra-Regular.ttf"
        size 23

    text "The bad cop approach. It doesn't always make sense, but you're angry, and that can be useful... sometimes.":
        pos (1345,700)
        xsize 400
        text_align 0.5
        font "fonts/Effra-Regular.ttf"
        size 23


    imagebutton:
        pos (176, 850)
        idle "images/v15/detective_board/archetype_blue_button.webp"
        hover "images/v15/detective_board/archetype_blue_button_hover.webp"
        action [SetField(mc, "detective", Detective.PROFESSIONAL), Return()]

    imagebutton:
        pos (755, 850)
        idle "images/v15/detective_board/archetype_yellow_button.webp"
        hover "images/v15/detective_board/archetype_yellow_button_hover.webp"
        action [SetField(mc, "detective", Detective.PSYCHOLOGIST), Return()]
    
    imagebutton:
        pos (1334, 850)
        idle "images/v15/detective_board/archetype_pink_button.webp"
        hover "images/v15/detective_board/archetype_pink_button_hover.webp"
        action [SetField(mc, "detective", Detective.LOOSE_CANNON), Return()]

screen fight_menu():

    hbox:
        align (0.5,0.5)
        spacing 100
        fixed:
            xysize (700,900)
            add Transform("gui/alert/background.webp", size=(700, 900))

            vbox:
                spacing 10
                align (0.5,0.5)

                text name:
                    size 50

                text "Health: [player.health]":
                    size 50
                    color "#eb5858"

                text "Stamina: [player.stamina]":
                    size 50
                    color "#ffa600"

                text "Fame: Unknown Brawler"

                text "Fight Style: [player_fight_style]"

                text "Heavy Attack Damage: [player_heavy_attack.damage]"

                text "Light Attack Damage: [player_light_attack.damage]"

                fixed:
                    xysize (137, 61)

                    imagebutton:
                        idle "blue_button_idle"
                        hover "blue_button_hover"
                        selected_idle "blue_button_hover"
                        action ToggleVariable("player_attack_1", "Hook", "Jab")
                    text player_attack_1 align (0.5, 0.5)

                fixed:
                    xysize (137, 61)

                    imagebutton:
                        idle "blue_button_idle"
                        hover "blue_button_hover"
                        selected_idle "blue_button_hover"
                        action ToggleVariable("player_attack_1", "Hook", "Jab")
                    text player_attack_1 align (0.5, 0.5)

                fixed:
                    xysize (137, 61)

                    imagebutton:
                        idle "blue_button_idle"
                        hover "blue_button_hover"
                        selected_idle "blue_button_hover"
                        action ToggleVariable("player_attack_1", "Hook", "Jab")
                    text player_attack_1 align (0.5, 0.5)

                fixed:
                    xysize (137, 61)

                    imagebutton:
                        idle "blue_button_idle"
                        hover "blue_button_hover"
                        selected_idle "blue_button_hover"
                        action ToggleVariable("player_attack_1", "Hook", "Jab")
                    text player_attack_1 align (0.5, 0.5)

                textbutton "Start":
                    action Jump ("fight_start")

        fixed:
            xysize (700,900)
            add Transform("gui/alert/background.webp", size=(700, 900))

            vbox:
                spacing 10
                align (0.5,0.5)

                text name:
                    size 50

                text "Health: [opponent.health]":
                    size 50
                    color "#eb5858"

                text "Stamina: [opponent.stamina]":
                    size 50
                    color "#ffa600"

                text "Fame: Unknown Brawler"

                text "Fight Style: [player_fight_style]"

                text "Heavy Attack Damage: {}".format(opponent.attacks[AttackType.HEAVY].damage)

                text "Light Attack Damage: {}".format(opponent.attacks[AttackType.LIGHT].damage)

                fixed:
                    xysize (137, 61)

                    imagebutton:
                        idle "blue_button_idle"
                        hover "blue_button_hover"
                        selected_idle "blue_button_hover"
                        action ToggleVariable("player_attack_1", "Hook", "Jab")
                    text player_attack_1 align (0.5, 0.5)

                fixed:
                    xysize (137, 61)

                    imagebutton:
                        idle "blue_button_idle"
                        hover "blue_button_hover"
                        selected_idle "blue_button_hover"
                        action ToggleVariable("player_attack_1", "Hook", "Jab")
                    text player_attack_1 align (0.5, 0.5)

                fixed:
                    xysize (137, 61)

                    imagebutton:
                        idle "blue_button_idle"
                        hover "blue_button_hover"
                        selected_idle "blue_button_hover"
                        action ToggleVariable("player_attack_1", "Hook", "Jab")
                    text player_attack_1 align (0.5, 0.5)

                fixed:
                    xysize (137, 61)

                    imagebutton:
                        idle "blue_button_idle"
                        hover "blue_button_hover"
                        selected_idle "blue_button_hover"
                        action ToggleVariable("player_attack_1", "Hook", "Jab")
                    text player_attack_1 align (0.5, 0.5)

                textbutton "Start":
                    action Jump ("fight_start")


screen fight_menu(attacks=None, player=player):
    modal True
    style_prefix "fight_menu_style"

    python:
        attacks = (
            Attack(AttackType.LIGHT, "Jab", 5, 2, Guard.SEMI_GUARD, {
                "start_image": "images/v2/jab2start.webp",
                "hit_image": "images/v2/jab2pic.webp",
                "block_image": "images/v2/jab1pic.webp"
            }),
            Attack(AttackType.LIGHT, "Jab", 5, 2, Guard.SEMI_GUARD, {
                "start_image": "images/v2/jab2start.webp",
                "hit_image": "images/v2/jab2pic.webp",
                "block_image": "images/v2/jab1pic.webp"
            }),
            Attack(AttackType.LIGHT, "Jab", 5, 2, Guard.SEMI_GUARD, {
                "start_image": "images/v2/jab2start.webp",
                "hit_image": "images/v2/jab2pic.webp",
                "block_image": "images/v2/jab1pic.webp"
            }),
            Attack(AttackType.HEAVY, "Jab", 5, 2, Guard.SEMI_GUARD, {
                "start_image": "images/v2/jab2start.webp",
                "hit_image": "images/v2/jab2pic.webp",
                "block_image": "images/v2/jab1pic.webp"
            }),
            Attack(AttackType.HEAVY, "Jab", 5, 2, Guard.SEMI_GUARD, {
                "start_image": "images/v2/jab2start.webp",
                "hit_image": "images/v2/jab2pic.webp",
                "block_image": "images/v2/jab1pic.webp"
            }),
            Attack(AttackType.HEAVY, "Jab", 5, 2, Guard.SEMI_GUARD, {
                "start_image": "images/v2/jab2start.webp",
                "hit_image": "images/v2/jab2pic.webp",
                "block_image": "images/v2/jab1pic.webp"
            })
        )

    default temp_attribute_1 = 5

    hbox:
        align (0.5, 0.5)
        spacing 100

        frame:
            background Transform("gui/fight_prototype/fight_background.png", size=(700, 900))
            xysize (700, 900)
            padding (50, 50)

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
                        spacing 100
                        vbox:
                            spacing 5
                            hbox:
                                spacing 20
                                button:
                                    xysize (58,58)
                                    idle_background "gui/fight_prototype/fight_slot_idle.png"
                                    action NullAction()
                                    text "Low Guard" align (0.5, 0.9) size 15
                                button:
                                    xysize (58,58)
                                    idle_background "gui/fight_prototype/fight_slot_idle.png"
                                    action NullAction()
                                    text "Semi Guard" align (0.5, 0.9) size 15
                                button:
                                    xysize (58,58)
                                    idle_background "gui/fight_prototype/fight_slot_idle.png"
                                    action NullAction()
                                    text "Full Guard" align (0.5, 0.9) size 15

                vbox:
                    spacing 10

                    text "Attributes"
                    vbox:
                        spacing 5

                        hbox:
                            spacing 20
                            
                            for i in range(10):
                                imagebutton:
                                    idle "gui/fight_prototype/fight_circle_idle.png"
                                    hover "gui/fight_prototype/fight_circle_hover.png"
                                    selected_idle "gui/fight_prototype/fight_circle_hover.png"
                                    selected i <= temp_attribute_1
                                    action SetScreenVariable("temp_attribute_1", i)


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

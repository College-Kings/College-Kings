screen fight_attack(player=player, opponent=opponent):
    tag fight
    modal True

    add opponent.guard_image

    for k, move in player.moves.items():
        key k:
            action Call("player_attack_turn", move, player, opponent) 

    # timer fight_reaction_time action Jump("opponent_attacks")


screen fight_defense(opponent_attack, player=player, opponent=opponent):
    tag fight
    modal True

    add opponent_attack.images["start_image"]

    for k, move in player.moves.items():
        key k:
            action Call("player_defence_turn", move, player, opponent_attack, opponent)

    # timer fight_reaction_time: 
    #     if attack == opponent.attacks[AttackType.LIGHT]: #tom light and time ran out ## NEEDS FIX
    #         if player.guard == Guard.LOW_GUARD: # player no guard
    #             action Jump ("opponent_light_hit")
    #         else: # player full or semi guard
    #             action Jump ("opponent_light_block")
    #     else: # tom heavy and time ran out
    #         if player.guard == Guard.FULL_GUARD: # player full guard
    #             action Jump ("opponent_heavy_block")
    #         else: # player no or semi guard
    #             action Jump ("opponent_heavy_hit")


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

screen fight_template():
    if opponent.guard == Guard.FULL_GUARD: #opp full guard
        add "images/v2/tomstancekick.webp"
    elif opponent.guard == Guard.LOW_GUARD: #opp light guard
        add "images/v2/tomstancehook.webp"
    else:  #opp no guard
        add "images/v2/tomstancejab.webp"
    
screen fight_neutral():
    use fight_template

    key q: #light attack
        action Jump ("player_light")
    key w: #heavy attack
        action Jump ("player_heavy")
    key e: # semi guard
        action Jump ("player_semi_guard")
    key r: #full guard
        action Jump ("player_full_guard")

    timer 1 action Jump ("opponent_attacks")

screen fight_defense(attack="light"):
    add opponent.attacks[attack].image

    for k in player.moves.keys():
        key k:
            action Function(player.turn)


    timer 1:
        if opponent_attack == 0: #tom light and time ran out
            if player_guard == 0: # player no guard
                action Jump ("opponent_light_hit")
            else: # player full or semi guard
                action Jump ("opponent_light_block")
        else: # tom heavy and time ran out
            if player_guard == 2: # player full guard
                action Jump ("opponent_heavy_block")
            else: # player no or semi guard
                action Jump ("opponent_heavy_hit")

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
            size 100
            color "#eb5858"  
        text "[opponent_guard]":
            size 100
            color "#494ce6"  

    vbox:
        align (0.1, 0.9)
        text "[player_health]":
            size 100
            color "#eb5858"
        text "[player_guard]":
            size 100
            color "#494ce6"  

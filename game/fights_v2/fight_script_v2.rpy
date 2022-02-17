label fight_v2:
    call screen fight_player_turn

label player_hook_v2:
    scene player_start_hook
    
    pause 0.5

    scene player_hit_hook
    with vpunch

    pause 1.0

    if actionpoints == 0:
        jump opponent_attack_v2
    else:
        call screen fight_player_turn

label player_jab_v2:
    scene player_start_jab
    
    pause 0.5

    scene player_hit_jab
    with vpunch

    pause 1.0

    if actionpoints == 0:
        jump opponent_attack_v2
    else:
        call screen fight_player_turn

label player_trash_talk_v2:
    scene player_start_jab # call screen trash_talk
    
    pause 0.5

    scene player_hit_jab
    with vpunch

    pause 1.0

    if actionpoints == 0:
        jump opponent_attack_v2
    else:
        call screen fight_player_turn

label player_guard_up_v2:

    if opponent_stance == 2: # opponent guard image
        scene opp_full_guard
    elif opponent_stance == 1:
        scene opp_semi_guard
    else:
        scene opp_no_guard

    show screen fight_popup("Guard Up")

    pause 1.0

    jump opponent_attack_v2

label opponent_attack_v2:

    if opponent_stance == 2: # opponent guard image
        scene opp_full_guard
    elif opponent_stance == 1:
        scene opp_semi_guard
    else:
        scene opp_no_guard

    show screen fight_popup("Opponent Turn")

    pause 1.0

    $ actionpoints = 8 # reset player action points

    

    scene opponent_start_jab
    
    pause 0.5

    scene opponent_jab_blocked
    with vpunch

    pause 1.0

    call screen fight_player_turn
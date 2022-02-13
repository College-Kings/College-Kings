label fight_v2:
    call screen fight_player_turn

label player_hook_v2:
    scene player_start_hook
    
    pause 0.5

    scene player_hit_hook
    with vpunch

    pause 1.0

    call screen fight_player_turn
label fight_test:

    call screen player_attack

label fight_test_insult:

    if opponent_guard == 2:
        scene tomstancekick
    elif opponent_guard == 1:
        scene tomstancehook
    else: 
        scene tomstancejab

    u "You suck{w=1.0}{nw}"

    show screen fight_popup("MENTAL HIT")

    $ opponent_guard -= 1

    if opponent_guard == 2:
        scene tomstancekick
    elif opponent_guard == 1:
        scene tomstancehook
    else: 
        scene tomstancejab

    pause 1

    call screen player_attack

label fight_test_hook:

    if opponent_guard == 2:
        scene tomstancekick
    elif opponent_guard == 1:
        scene tomstancehook
    else: 
        scene tomstancejab

    scene hook2start

    pause 0.5

    $ fight_hit = renpy.random.choice([0, 1, 2]) #chance to hit
    
    if fight_hit == 0: # player hits opp

        scene hook2pic
        with vpunch

        show screen fight_popup("PHYSICAL HIT")

        pause 1

        call screen player_attack
    
    elif fight_hit == 1: # opp blocks

        scene hook1pic
        with vpunch

        show screen fight_popup("BLOCKED")

        pause 1

        call screen player_attack

    else: # opp attacks

        scene hook1pic
        with vpunch

        show screen fight_popup("COUNTERED")

        pause 1

        $ opponent_attack = renpy.random.choice([0, 1]) #opponent attack choice

        call screen opponent_attack with dissolve

label opponent_attacks:

        if opponent_guard == 2:
            scene tomstancekick
            with dissolve
        elif opponent_guard == 1:
            scene tomstancehook
            with dissolve
        else: 
            scene tomstancejab
            with dissolve

        pause 0.5

        $ opponent_attack = renpy.random.choice([0, 1]) #opponent attack choice

        call screen opponent_attack


label fight_test_blocked_jab:

    scene tomjabblock
    with vpunch

    show screen fight_popup("BLOCKED")

    pause 1

    jump opponent_attacks

label fight_test_blocked_kick:

    scene tomkickblock
    with vpunch

    show screen fight_popup("BLOCKED")

    pause 1

    jump opponent_attacks

label fight_test_countered_jab:

    scene tomjabblock
    with vpunch

    show screen fight_popup("COUNTERED")

    pause 1

    call screen player_attack

label fight_test_countered_kick:

    scene tomkickblock
    with vpunch

    show screen fight_popup("COUNTERED")

    pause 1

    call screen player_attack

label fight_test_jab_hit:

    scene tomjabhit
    with vpunch

    show screen fight_popup("PHYSICAL HIT")

    pause 1

    jump opponent_attacks

label fight_test_kick_hit:

    scene tomkickhit
    with vpunch

    show screen fight_popup("PHYSICAL HIT")

    pause 1

    jump opponent_attacks



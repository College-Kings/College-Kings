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

    if opponent_guard > 0:
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
    
    if opponent_guard == 0 or opponent_guard == 1: # guard down or semi, player hits

        scene hook2pic
        with vpunch

        show screen fight_popup("PHYSICAL HIT")

        pause 1

        jump opponent_attacks
    
    else: # guard up, opp blocks

        scene hook1pic
        with vpunch

        show screen fight_popup("BLOCKED")

        pause 1

        jump opponent_attacks

label fight_test_jab:

    if opponent_guard == 2:
        scene tomstancekick
    elif opponent_guard == 1:
        scene tomstancehook
    else: 
        scene tomstancejab

    scene jab2start

    pause 0.5
    
    if opponent_guard == 0: #guard down

        $ counter_chance = renpy.random.choice([light_attack_fury]) #chance to counter

        if counter_chance == 0: # opponent counters

            scene jab1pic
            with vpunch

            show screen fight_popup("COUNTERED")

            pause 1

            $ light_attack_fury = 3

            jump opponent_counter

        else: # player hits

            scene jab2pic
            with vpunch

            show screen fight_popup("PHYSICAL HIT")

            pause 1

            $ light_attack_fury -= 1

            call screen player_attack
    
    else: #guard semi or up opp blocks

        scene jab1pic
        with vpunch

        show screen fight_popup("BLOCKED")

        pause 1

        call screen player_attack

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

        pause 0.7

        label opponent_counter:

        $ opponent_attack = renpy.random.choice([0, 1]) #opponent attack choice

        call screen opponent_attack


label fight_test_blocked_jab:

    scene tomjabblock
    with vpunch

    show screen fight_popup("BLOCKED")

    pause 1

    if opponent_guard > 0:
        $ opponent_guard -= 1

    jump opponent_attacks

label fight_test_blocked_kick:

    scene tomkickblock
    with vpunch

    show screen fight_popup("BLOCKED")

    pause 1

    if opponent_guard < 2:
        $ opponent_guard += 1

    call screen player_attack

label fight_test_countered_jab:

    scene tomjabblock
    with vpunch

    show screen fight_popup("COUNTERED")

    pause 1

    call screen player_attack

label fight_test_jab_hit:

    scene tomjabhit
    with vpunch

    show screen fight_popup("PHYSICAL HIT")

    pause 1

    if opponent_guard < 2:
        $ opponent_guard += 1

    jump opponent_attacks

label fight_test_kick_hit:

    scene tomkickhit
    with vpunch

    show screen fight_popup("PHYSICAL HIT")

    pause 1

    $ opponent_guard = 2

    call screen player_attack




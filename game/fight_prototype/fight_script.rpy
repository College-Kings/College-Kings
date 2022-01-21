init python:
    def change_opponent_health(value):
        current_health = getattr(store, "opp_health")
        renpy.show_screen("opponent_health_bar", current_health, current_health + value)
        setattr(store, "opp_health", value)

label fight_test:
    show screen test_health
    show screen opponent_health_bar(100, 100)
    $ opp_health = 100
    $ player_health = 100

    call screen player_attack

label player_hook:

    if opponent_guard == 2:
        scene tomstancekick
    elif opponent_guard == 1:
        scene tomstancehook
    else: 
        scene tomstancejab

    scene hook2start

    pause 0.5
    
    if opponent_guard == 0: # guard down, player hits

        label hook_hit:

        scene hook2pic
        with vpunch

        $ opp_health -= 10
        #show screen opponent_health_bar(opp_health, opp_health-10)

        show screen fight_popup("PHYSICAL HIT")

        pause 1

        $ opponent_guard = 1

        jump opponent_attacks

    elif opponent_guard == 1:

        $ heavy_hit_chance = renpy.random.choice([0, 1, 2])

        if heavy_hit_chance == 0:
            jump hook_blocked

        elif heavy_hit_chance == 1:
            jump hook_hit

        else:
            $ opponent_attack = 0
            jump opp_light_counter

    else: # guard up, opp blocks

        label hook_blocked:

        scene hook1pic
        with vpunch

        $ opp_health -= 2

        show screen fight_popup("BLOCKED")

        pause 1

        $ opponent_guard = 0

        jump opponent_attacks

label player_jab:

    if opponent_guard == 2:
        scene tomstancekick
    elif opponent_guard == 1:
        scene tomstancehook
    else: 
        scene tomstancejab

    scene jab2start

    pause 0.5
    
    if opponent_guard == 0: #guard down

        if reset_chance == 1:
            $ reset = renpy.random.choice([0,1,2,3,4,5]) #chance to reset = 2/6
        elif reset_chance == 2:
            $ reset = renpy.random.choice([0,1,2,3]) #chance to reset, 3/6
        else:
            $ reset = renpy.random.choice([0,1,2]) #chance to reset 4/6

        if reset == 0 or reset == 1: # opponent resets

            scene jab1pic # Opp blocks
            with vpunch

            show screen fight_popup("RESET")

            pause 1
            $ reset_chance = 1
            $ opponent_guard = 2

            call screen player_attack

        else:

            scene jab2pic # Player hits
            with vpunch

            $ opp_health -= 5

            show screen fight_popup("Light Hit")

            pause 1

            $ reset_chance += 1

            call screen player_attack
    
    elif opponent_guard == 1: # opp light guard

        if break_chance == 1:
            $ breaking = renpy.random.choice([0,1,2,3,4,5]) #chance to reset = 2/6
        elif break_chance == 2:
            $ breaking = renpy.random.choice([0,1,2,3]) #chance to reset, 3/6
        else:
            $ breaking = renpy.random.choice([0,1,2]) #chance to reset 4/6

        if breaking == 0 or breaking == 1: # guard breaks

            scene jab1pic # opp blocks
            with vpunch

            show screen fight_popup("GUARD BROKEN")

            pause 1
            $ break_chance = 1
            $ opponent_guard = 0

            call screen player_attack

        else: # guard doesn't break

            scene jab1pic # opp blocks
            with vpunch

            show screen fight_popup("BLOCKED")

            pause 1

            $ break_chance += 1

            call screen player_attack


    else: # opponent_guard = 2, opp blocks

            scene jab1pic
            with vpunch

            show screen fight_popup("BLOCKED")

            pause 1

            call screen player_attack

label opponent_attacks:

        call screen opponent_ready

        label opponent_counters:

        $ opponent_attack = renpy.random.choice([0, 1]) #opponent attack choice

        label opp_light_counter:

        call screen opponent_attack


label player_blocks_jab:

    scene tomjabblock
    with vpunch

    show screen fight_popup("BLOCKED")

    pause 1

    jump opponent_attacks

label player_blocks_kick:

    scene tomkickblock
    with vpunch

    $ player_health -= 2

    show screen fight_popup("BLOCKED")

    pause 1

    call screen player_attack

label opp_jab:

    scene tomjabhit
    with vpunch

    $ player_health -= 5

    show screen fight_popup("LIGHT HIT")

    pause 1

    jump opponent_attacks

label opp_kick:

    scene tomkickhit
    with vpunch

    $ player_health -= 10

    show screen fight_popup("HEAVY HIT")

    pause 1

    call screen player_attack




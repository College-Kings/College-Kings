screen player_attack():

    if opponent_guard == 2: #full guard opponent
        add "images/v2/tomstancekick.webp"
    elif opponent_guard == 1: #semi guard
        add "images/v2/tomstancehook.webp"
    else:  # no guard
        add "images/v2/tomstancejab.webp"

    key q: #jab attack
        action Jump ("fight_test_jab")
    key w: #heavy attack
        action Jump ("fight_test_hook")
    key e: #verbal attack
        action Jump ("fight_test_insult")

    timer 1 action Jump ("opponent_counter")

screen opponent_attack():

    if opponent_attack == 0: # tom jabs, light attack
        add "images/v2/tomjab.webp"
    else: # tom kicks, heavy attack
        add "images/v2/tomkick.webp"

    key q: # block
        if opponent_attack == 0: # tom jabbed
            action Jump ("fight_test_blocked_jab")
        else: # tom kicked
            action Jump ("fight_test_blocked_kick")
    key w: # counter
        if opponent_attack == 0: # tom jabbed
            action Jump ("fight_test_countered_jab")
        else: # tom kicked
            action Jump ("fight_test_kick_hit")


    if opponent_attack == 0: #tom jabbed and time ran out
        timer 1 action Jump ("fight_test_jab_hit")
    else: # tom kicked and time ran out
        timer 1 action Jump ("fight_test_kick_hit")

screen fight_popup(message):
    text message:
        size 100

    timer 2 action Hide("fight_popup", transition=dissolve)
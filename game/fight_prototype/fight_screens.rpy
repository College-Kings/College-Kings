screen player_attack():

    if opponent_guard == 2: #opp heavy guard
        add "images/v2/tomstancekick.webp"
    elif opponent_guard == 1: #opp light guard
        add "images/v2/tomstancehook.webp"
    else:  #opp no guard
        add "images/v2/tomstancejab.webp"

    text "OFFENSE":
        size 100
        xalign 0.9

    key q: #light jab attack
        action Jump ("player_jab")
    key w: #heavy hook attack
        action Jump ("player_hook")
    key e: # light guard
        action Jump ("opponent_counters")
    key r: #heavy guard
        action Jump ("opponent_counters")

    timer 1 action Jump ("opponent_counters")

screen opponent_ready():

    if opponent_guard == 2: #opp heavy guard
        add "images/v2/tomstancekick.webp"
    elif opponent_guard == 1: #opp light guard
        add "images/v2/tomstancehook.webp"
    else:  #opp no guard
        add "images/v2/tomstancejab.webp"

    text "NEUTRAL":
        size 100
        xalign 0.9

    key q: #light jab attack
        if player_guard < 2:
            action Jump ("player_jab")
        else:
            action Jump ("player_jab")
    key w: #heavy hook attack
        action Jump ("opponent_counters")
    key e: # light guard
        action Jump ("opponent_counters")
    key r: #heavy guard
        action Jump ("opponent_counters")

    timer 0.5 action Jump ("opponent_counters")

screen opponent_attack():
    if opponent_attack == 0: # tom jabs, light attack
        add "images/v2/tomjab.webp"
    else: # tom kicks, heavy attack
        add "images/v2/tomkick.webp"

    text "DEFENSE":
        size 100
        xalign 0.9

    key q: #light jab attack
        if opponent_attack == 0: # tom light
            action Jump ("opp_jab")
        else: # tom heavy
            action Jump ("player_jab")
    key w: #heavy hook attack
        if opponent_attack == 0: # tom light
            action Jump ("opp_jab")
        else: # tom heavy
            action Jump ("opp_kick")
    key e: # light guard
        if opponent_attack == 0: # tom light
            action [SetVariable("player_guard", 1), Jump ("player_blocks_jab")]
        else: # tom heavy
            action [SetVariable("player_guard", 1), Jump ("opp_kick")]
    key r: #heavy guard
        if opponent_attack == 0: # tom light
            action [SetVariable("player_guard", 2), Jump ("player_blocks_jab")]
        else: # tom heavy
            action [SetVariable("player_guard", 2), Jump ("player_blocks_kick")]


    if opponent_attack == 0: #tom light and time ran out
        timer 0.5 action Jump ("opp_jab")
    else: # tom heavy and time ran out
        timer 1 action Jump ("opp_kick")

screen fight_popup(message):
    text message:
        size 100

    timer 2 action Hide("fight_popup", transition=dissolve)

screen opponent_health_bar(current_health, new_health, max_health=100):
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
        text "[opp_health]":
            size 100
            color "#eb5858"  

    vbox:
        align (0.1, 0.9)
        text "[player_health]":
            size 100
            color "#eb5858"

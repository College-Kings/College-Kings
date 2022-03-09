# SCENE 29: Transition Mc goes home
# Locations: Street
# Characters: MC (Outfit: 9), RANDOM GIRL (Outfit: Gym clothes)
# Time: Afternoon

label v16s29:
    scene v16s29_1 # TPP. Show MC walking on the street, slight smile, mouth closed
    with fade

    pause 0.75

    scene v16s29_2 # TPP. Show MC walking down the street (different place), have some hot girl running past him, winking at MC and giving a sexy smile
    with dissolve

    pause 0.75

    if joinwolves:
        jump v16s30

    else:
        jump v16s31
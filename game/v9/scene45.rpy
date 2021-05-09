# SCENE 45: Cliffhanger
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7), Cameron (Outfit 3), Sebastian (Outfit 1)
# Time: Saturday Night

label v9_ending:
    scene v9end1 # TPP. Show MC walking near the exit of the warehouse.
    with fade

    play music "music/v09/Scene 45/Track Scene 45.mp3" fadein 2

    pause 1

    scene v9end2 # FPP. Show Sebastian and Cameron running out through the Warehouse doors.
    with dissolve

    u "(What the fuck is going on!?)"

    scene v9end3 # TPP. Show MC running to the exit of the Warehouse, worried expression.
    with dissolve

    pause 1

    scene v9end4 # TPP. Show MC emerging from the exit of the warehouse and looking to his side, worried expression.
    with dissolve

    pause 1

    stop music fadeout 5

    scene v9end5 # TPP. Close up of MC's face, MC looking to the side, MC's face grows even more worried.
    with dissolve

    u "(Awww shit!)"

    scene black
    with fade

    pause 2

    jump ending9

label ending9:
    if persistent.ep == 9:
        jump end9
    else:
        jump v10start

label end9:
    scene savenow
    with Fade (1,0,1)
    " "
    if persistent.ep == 9:
        jump end_credits
    else:
        jump v10start

# <3 ~Lew
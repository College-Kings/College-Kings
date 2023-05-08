# SCENE 54: MC goes to bed (his bed)
# Locations: Hotel Corridor, Hotel Room
# Characters: MC (Outfit: 5)
# Time: Night

label v13s54:
    #scene v13s54_1 # TPP. MC walking in corridor, neutral expression, mouth closed ###ERROR wrong outfit
    scene v12pht11
    with dissolve

    u "(What will be in store for me tomorrow?)"

    play music music.v13_Track_Scene_52 fadein 2

    #scene v13s54_2 # TPP. MC walking into his room, neutral expression, mouth closed ###ERROR wrong outfit
    scene v13s5_8
    with dissolve

    pause 0.5

    #scene v13s54_3 # TPP. Show MC removing his shirt, only in his boxers, neutral expression, mouth closed ###ERROR wrong outfit
    scene v13s43_9
    with dissolve

    u "*Sighs*"

    #scene v13s54_4 # TPP. Show MC turning off the lights ###ERROR wrong outfit
    scene v13s43_8
    with dissolve

    pause 0.75
    
    scene v13s54_5 # TPP. Show MC getting into bed, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v13s54_6 # TPP. Show MC laying in bed, looking at the roof, mouth closed, neutral expression
    with dissolve

    u "(Guess we'll find out soon.)"

    scene v13s54_7 # TPP. Show MC sleeping
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s54a
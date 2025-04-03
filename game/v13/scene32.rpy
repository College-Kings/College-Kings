# SCENE 32: MC Back in his room to sleep
# Locations: Hotel Room
# Characters: AMBER (Outfit: 1), LAUREN (Outfit: 3, MC (Outfit: 9)
# Time: Night

label v13s32:
    play music music.v13_Track_Scene_32 fadein 2

    if not v13_lauren_smoke:
        scene v13s32_1 # TPP. Show MC, Lauren and Amber walking into the room, all slightly smiling, mouths closed
        with dissolve

        pause 0.75

        scene v13s32_2 # FPP. MC, Amber and Lauren standing in the room, MC looking at Amber, Amber looking at Lauren's direction (Lauren out of shot), Amber slight smile, mouth open
        with dissolve

        am "Lauren, do you want me to tuck you in? I heard babies like that."

        scene v13s32_3 # FPP. Same positioning as v13s32_2, MC looking at Lauren, Lauren looking at Amber's direction (only Lauren in shot), Lauren slight smile, mouth closed
        with dissolve

        la "I'm not here for your games Amber, but I am going to bed. *Chuckles*"

        if CharacterService.is_girlfriend(lauren):
            play sound sound.kiss
            scene v13s32_4 # TPP. Show Lauren kissing MC
            with dissolve

            pause

            scene v13s32_3a # FPP. Same as v13s32_3, Lauren looking at MC, slight smile, mouth open
            with dissolve

            la "Goodnight, babe."

            scene v13s32_3b # FPP. Same as v13s32_3a, Lauren slight smile, mouth closed
            with dissolve

            u "Goodnight."

        else:
            scene v13s32_2
            with dissolve

            am "Goodnight goody two-shoes."

            scene v13s32_3
            with dissolve

            la "*Chuckles*"

        scene v13s32_5 # TPP. Show MC and Amber still in same position, Lauren walking towards bathroom, all slightly smiling, mouths closed
        with dissolve

        pause 0.75

        scene v13s32_2a # FPP. Same as v13s32_2, Amber looking at MC, Amber slight smile, mouth open
        with dissolve

        am "You know, I may give her a lot of shit, but I'm glad she doesn't cave to peer pressure."

        scene v13s32_2b # FPP. Same as v13s32_2a, Amber slight smile, mouth closed
        with dissolve

        u "She's set on her ways. *Chuckles*"

        scene v13s32_2a
        with dissolve

        am "Very true... Goodnight, [name]. Thanks for hanging today."

        scene v13s32_2b
        with dissolve

        u "Of course, I had fun. Night."

        scene v13s32_6 # TPP. Show MC walking out of the room, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v13s32_7 # TPP. Show MC walking in the hotel room corridor, slight smile, mouth closed
        with dissolve

        pause 0.75
    
    scene v13s32_8 # TPP. Show MC sneaking into his room, slight smile, mouth closed, room is dark
    with fade

    u "(I keep coming back late.)"

    scene v13s32_9 # TPP. Show MC looking over at his roommate's bed (don't show roommate), MC slight smile, mouth slightly open
    with dissolve

    u "*Whispers* Roomie, Roomie...?"

    u "As expected."

    scene v13s32_10 # TPP. Show MC removing his shirt, pants already off, using boxers, slight smile, mouth closed
    with dissolve

    u "(Guess I'm just gonna clock out. *Chuckles*)"

    scene v13s32_11 # TPP. Show MC getting into bed, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s32_12 # TPP. Show MC sleeping
    with fade

    pause 0.75

    scene v13s32_12a # TPP. Same as v13s32_10, MC different pose
    with fade

    pause 0.75

    stop music fadeout 3

    jump v13s33
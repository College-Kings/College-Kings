# SCENE 33: MC Wakes Up
# Locations: Hotel Room, Hotel Corridor, Hotel Lobby
# Characters: MC (Outfit: 5), RILEY (Outfit: 3)
# Time: Morning

label v13s33:
    play music music.v13_Track_Scene_33 fadein 2

    if not v11_riley_roomate:
        scene black
        with vpunch

        play sound sound.knock

        pause

        scene v13s33_1 # FPP. MC laying in his bed, looking at the closed door, MC is in his boxers
        with dissolve

        u "Come in!"

        scene v13s33_1a # FPP. Same as v13s33_1, door open, Riley walking in to the room, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v13s33_1b # FPP. Same as v13s33_1a, Riley walking over to MC's bed
        with dissolve

        pause 0.75

    scene v13s33_2 # FPP. Riley standing next to MC's bed, looking at MC, MC laying down, Riley slight smile, mouth open
    with dissolve

    ri "C'mon, get up! I wanna go to the treasure hunt place."

    scene v13s33_2a # FPP. Same as v13s33_2, Riley slight smile, mouth closed
    with dissolve

    u "Why are you waking me up to do this?"

    scene v13s33_2
    with dissolve

    ri "Because I'm ready to go! And based on where it is, I'm not trying to go during any other part of the day."

    scene v13s33_2a
    with dissolve

    u "*Sighs* Where is it?"

    scene v13s33_2b # FPP. Same as v13s33_2, different pose
    with dissolve

    ri "An old dungeon..."

    scene v13s33_2c # FPP. Same as v13s33_2b, Riley slight smile, mouth closed
    with dissolve

    u "How do you know this time?"

    scene v13s33_2b
    with dissolve

    ri "Same way I knew the last few times, these clues are way too easy. *Chuckles*"

    scene v13s33_2c
    with dissolve

    u "What was the clue?"

    scene v13s33_2
    with dissolve

    ri "Not important, now get up!"

    scene v13s33_2a
    with dissolve

    u "*Sighs*"

    scene v13s33_3 # TPP. Show MC getting up, slightly annoyed, mouth closed
    with dissolve

    pause 0.75
    
    scene v13s33_4 # TPP. Show MC putting on his shirt, pants already on, slightly annoyed, mouth closed
    with dissolve

    pause 0.75

    scene v13s33_5 # FPP. Riley standing next to MC, MC looking at Riley, slight smile, mouth closed
    with dissolve

    u "Lead the way."

    scene v13s33_6 # TPP. MC and Riley walking out of the hotel room, slightly smiling, mouths closed
    with dissolve

    pause 0.75
    
    scene v13s33_7 # TPP. MC and Riley walking in hotel corridor, slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v13s33_8 # TPP. MC and Riley walking in hotel lobby towards the exit, slight smiles, mouths closed
    with fade

    pause 0.75

    scene v13s33_9 # TPP. MC and Rileyu walking out of hotel lobby, slight smiles, mouths closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s34
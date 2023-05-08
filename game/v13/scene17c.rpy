# SCENE 17c: MC Wakes Up (His Bed)
# Locations: Hotel Room, Hotel Corridor
# Characters: MC (Outfit: 9)
# Time: Morning

label v13s17c:
    scene v13s17c_1 # TPP. Show MC sleeping in his bed, alone, it's morning, in his boxers
    with Fade(1,1,1)

    pause 0.75

    play music music.v13_Track_Scene_17 fadein 2

    scene v13s17c_1a # TPP. Same as v13s17c_1, show MC slightly startled, looking down at his stomach, mouth closed
    with vpunch

    u "*Stomach growls*"

    u "(Oh, I'm hungry as fuck... Luuk better have some food this morning.)"

    scene v13s17c_2 # TPP. Show MC getting out of his bed, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s17c_3 # TPP. Show MC putting on his shirt, pants already on, slight smile, mouth closed
    with fade

    pause 0.75

    scene v13s17c_4 # TPP. Show MC walking out of the room, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s17c_5 # TPP. Show MC walking in the hotel room corridor, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s18
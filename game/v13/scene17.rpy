# SCENE 17: MC Wakes Up (Chloe's Bed)
# Locations: Hotel Room, Hotel Corridor
# Characters: MC (Outfit: 9), CHLOE (Outfit: 6)
# Time: Morning

label v13s17:
    scene v13s17_1 # TPP. Show MC and Chloe sleeping together in her bed, it's morning, MC in his boxers
    with Fade(1,1,1)

    pause 0.75

    play music music.v13_Track_Scene_17 fadein 2

    scene v13s17_1a # TPP. Same as v13s17_1, show MC waking up, slight smile, mouth closed, Chloe still sleeping
    with dissolve

    pause 0.75

    scene v13s17_2 # FPP. MC laying in bed, looking at Chloe, she's asleep
    with dissolve

    u "(Maybe I can get up without waking her.)"

    scene v13s17_3 # TPP. Show MC getting out of bed, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s17_4 # TPP. Show MC standing next to the bed, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s17_5 # FPP. MC same position as v13s17_4, looking at Chloe, Chloe slight smile, mouth open
    with dissolve

    cl "[name]? What time is it?"

    scene v13s17_5a # FPP. Same as v13s17_5, Chloe slight smile, mouth closed
    with dissolve

    u "Still pretty early... Just grabbing some breakfast."

    scene v13s17_5
    with dissolve

    cl "Mmm... Time for more sleep then."

    scene v13s17_5a
    with dissolve

    u "Haha, enjoy."

    scene v13s17_6 # TPP. Show MC putting on his shirt, pants already on, slight smile, mouth closed
    with fade

    pause 0.75

    scene v13s17_7 # TPP. Show MC walking out of the room, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s17_8 # TPP. Show MC walking in the hotel room corridor, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s18
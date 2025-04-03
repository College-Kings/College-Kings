# SCENE 2: Heading To Amsterdam
# Locations: Hotel Lobby, Hotel Room, Hotel Room Corridor
# Characters: MS. ROSE (Outfit: 1), MC (Outfit: 1), PENELOPE (Outfit: 2)
# Time: Morning

label v13s2:
    scene v13s2_1 # TPP. Show MC walking in the hotel corridor, slight smile, mouth closed
    with dissolve

    pause 0.75

    play music music.ck1.v13.Track_Scene_2_1 fadein 2

    scene v13s2_2 # TPP. Show MC walking into his hotel room, slight smile, mouth closed
    with dissolve

    pause 1

    scene v13s2_3 # TPP. Show MC grabbing his luggage, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s2_4 # TPP. Show MC leaving his hotel room with his luggage, slight smile, mouth closed
    with dissolve

    pause 1

    scene v13s2_5 # TPP. Show MC walking in the hotel lobbt with his luggage, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music music.ck1.v13.Track_Scene_2_2 fadein 2

    if v11_pen_goes_europe:
        scene v13s2_6 # FPP. MC looking at Ms. Rose, Ms. Rose looking at MC, Ms. Rose slight smile, mouth open, Penelope standing next to Ms. Rose, looking at her, Penelope slight smile, mouth closed, Penelope carrying some luggage from other students
        with dissolve

        ro "Seven hours of uninterrupted sleep... This is something I'm definitely looking forward to."

        scene v13s2_6a # FPP. Same as v13s2_6, Ms. Rose mouth closed, slight smile, Penelope slight smile, mouth closed
        with dissolve

        u "(She must be having a hard time sleeping for some reason.)"
    
    else:
        scene v13s2_6b # FPP. Same as v13s2, but no Penelope
        with dissolve

        ro "Seven hours of uninterrupted sleep... This is something I'm definitely looking forward to."

        scene v13s2_6c # FPP. Same as v13s2_6a, but no Penelope
        with dissolve

        u "(She must be having a hard time sleeping for some reason.)"
        
    scene v13s2_7 # TPP. Show MC leaving the hotel, Ms. Rose in front of him, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s3
# SCENE 58: Walking to Canoeing With Aubrey
# Locations: Hotel Lobby, Canoeing location.
# Characters: MC (Outfit: 3), AUBREY (Outfit: 2)
# Time: Afternoon

label v13s58:
    scene v13s58_1 # TPP. Show MC sitting in one of the chairs in the hotel lobby, Arms crossed, slight smile, mouth closed.
    with dissolve

    u "(There goes all my money.)"

    play music music.v13_Track_Scene_58 fadein 2

    scene v13s58_1a # TPP. Same as v13s58_1, slight smile, mouth open.
    with dissolve

    u "*Sighs*"

    scene v13s58_1
    with dissolve

    pause 0.75

    scene v13s58_1b # TPP. Same as v13s58_1, MC different pose, slight smile, mouth closed.
    with fade

    pause 0.75

    scene v13s58_2 # FPP. Show Aubrey walking up to MC, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s58_2a # FPP. Same as v13s58_2, Aubrey looking at MC sitting down, MC looking at Aubrey, Aubrey slight smile, mouth open.
    with dissolve

    au "Ready for our little outing?"

    scene v13s58_2b # FPP. Same as v13s58_2a, Aubrey slight smile, mouth closed.
    with dissolve

    u "Say less... I had a feeling you'd come down here looking for me soon."

    scene v13s58_2a
    with dissolve

    au "You feel like you know me that well, huh?"

    scene v13s58_2b
    with dissolve

    u "Yes, ma'am."

    scene v13s58_2a
    with dissolve

    au "*Chuckles* Okay mister, whatever you say..."

    scene v13s58_2b
    with dissolve

    pause 0.75

    scene v13s58_3 # TPP. Show MC standing in the hotel lobby next to Aubrey, both slight smile, mouth closed.
    with dissolve

    if v13s48_canoeing_as_date: 
        pause 0.75

        scene v13s58_3a # TPP. Same as v13s58_3, MC holding his hand out for Aubrey, both slight smile, mouth closed. 
        with dissolve

        pause 0.75

        scene v13s58_3b # TPP. Same as v13s58_3a, Aubrey holding MC's hand, Aubrey full smile, mouth open, MC slight smile, mouth closed.
        with dissolve

        au "*Chuckles*"

        scene v13s58_4 # TPP. Show Aubrey and MC walking towards the hotel door while holding hands, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v13s58_4a # TPP. Same as v13s58_4, Show MC and Aubrey leaving the hotel.
        with dissolve

        pause 0.75

        scene v13s58_5 # TPP. Show Aubrey and MC at the canoeing location holding hands, both slight smile, mouths closed.
        with fade

        pause 0.75
    else: 
        pause 0.75

        scene v13s58_4b # TPP. Same as v13s58_4b, Show Aubrey and MC holding hands, both slight smile, mouths closed.
        with dissolve

        pause 0.75

        scene v13s58_4c # TPP. Same as v13s58_4b, Show MC and Aubrey not holding hands leaving the hotel, both slight smile, mouths cloed
        with dissolve

        pause 0.75

        scene v13s58_5b # TPP. Show Aubrey and MC at the canoeing location not holding hand, both slight smile, mouths closed.
        with fade

        pause 0.75

    stop music fadeout 3
    
    jump v13s59
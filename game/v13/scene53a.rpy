# SCENE 53a: MC wakes up (Riley's Bed)
# Locations: Hotel Room, Hotel Corridor, Hotel Lobby
# Characters: MC (Outfit: 3), RILEY (Outfit: 5)
# Time: Morning

label v13s53a:
    scene v13s53a_1 # TPP. Show Riley sleeping, MC waking up next to her, Riley with her mouth open (as if she were snoring)
    with Fade(1,0.75,1)

    pause 0.75

    play music music.v13_Track_Scene_52a fadein 2

    scene v13s53a_1a # TPP. Same as v13s53a_1, MC looking at Riley, MC laughing, Riley same
    with dissolve

    u "*Laughs*"

    scene v13s53a_2 # FPP. Same positioning as v13s53a_1, MC looking at Riley, Riley waking up, slightly annoyed, mouth open, looking at MC
    with dissolve

    ri "*Yawn* What?"

    scene v13s53a_2a # FPP. Same as v13s53a_2, Riley mouth closed, awake
    with dissolve

    u "You had your mouth wide open."

    scene v13s53a_2b # FPP. Same as v13s53a_2a, Riley mouth open
    with dissolve

    ri "Oh my god... I'm going back to sleep."

    scene v13s53a_2c # FPP. Same as v13s53a_2, Riley rolling over to sleep
    with dissolve

    u "Haha, well I'm getting up."

    scene v13s53a_3 # TPP. Show MC getting out of bed, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s53a_4 # TPP. Show MC putting his shirt on, pants already on, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s53a_5 # TPP. Show MC walking out of room, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s53a_6 # TPP. Show MC walking in hotel corridor, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s53a_7 # TPP. Show MC arriving at the hotel lobby, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s55
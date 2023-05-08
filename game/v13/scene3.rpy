# SCENE 3: Bus Trip To Amsterdam
# Locations: Bus
# Characters: MC (Outfit: 1)
# Time: Morning/Evening/Night

label v13s3:
    scene v13s3_1 # TPP. Show MC getting on the bus, slight smile, mouth closed
    with dissolve

    pause 0.75

    play music music.ck1.v13.Track_Scene_3 fadein 2

    scene v13s3_2 # TPP. Show MC sitting down in his seat, no one next to him, MC slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s3_3 # TPP. Show MC sleeping on the bus
    with dissolve

    pause 0.75

    scene v13s3_3a # TPP. Same as v13s3_3, MC different pose
    with dissolve

    pause 0.75

    scene v13s3_3b # TPP. Same as v13s3_3a, MC different pose, now evening
    with Fade(0.5, 1.75, 0.5)

    pause 0.75

    scene v13s3_3c # TPP. Same as v13s3_3b, different pose, now night
    with Fade(0.5, 1.75, 0.5)

    pause 0.75

    scene v13s3_3d # TPP. Same as v13s3_3c, MC now awake, slight smile, mouth closed, bus in front of the hotel in Amsterdam
    with fade

    pause 0.75

    stop music fadeout 3

    jump v13s4
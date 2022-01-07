# SCENE 45: Lauren and MC picking up the bikes
# Locations: Bike pick up/drop off spot.
# Characters: LAUREN (Outfit: 3), MC (Outfit: 1)
# Time: Morning

label v13s45:
    scene v13s45_1 # TPP. Lauren and MC standing at the bike spot, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 45.mp3" fadein 2

    scene v13s45_2 # FPP. MC looking at Lauren, Lauren looking at MC, Slight smile, mouth open.
    with dissolve

    la "Luuk said these are free to use."

    scene v13s45_2a # FPP. Same as v13s45_2, Lauren slight smile, mouth closed.
    with dissolve

    u "Perfect!"

    scene v13s45_3 # TPP. Show MC and Lauren choosing their bikes, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s45_4 # TPP. Show MC and Lauren somewhere down the way on the bike, both slight smile, mouth closed.
    with fade

    pause 0.75

    stop music fadeout 3

    jump v13s46
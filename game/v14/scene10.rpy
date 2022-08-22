# SCENE 10: Flight to San Vallejo
# Locations: Airplane
# Characters: MC (Outfit: 5), RILEY (Outfit: 2), LAUREN (Outfit: 3), AMBER (Outfit: 1), MS. ROSE (Outfit: 1), MR. LEE (Outfit: 1)
# Time: Afternoon

label v14s10:
    play music "music/v11/Track Scene 13_1.mp3" fadein 2

    scene v14s10_1 # TPP. Show the plane taking off
    with fade

    pause 0.75

    scene v14s10_2 # TPP. Show MC and Riley sitting next to each other, Riley asleep on MC's shoulder, MC smiling, both mouths closed
    with dissolve

    pause 1.5

    scene v14s10_3 # TPP. Show Lauren and Amber sitting next to each other, both laughing
    with dissolve

    pause 1.5

    scene v14s10_4 # TPP. Show Ms. Rose sitting next to Mr. Lee, both slight smiles, Mr. Lee mouth open, Ms. Rose mouth closed
    with dissolve

    pause 1.5

    scene v14s10_5 # TPP. Show the plane landing
    with Fade(1,0.5,1)

    pause 1.5

    stop music fadeout 3

    jump game_end
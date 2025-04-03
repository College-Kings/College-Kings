# SCENE 41a: MC and Lindsey Walk Back to The Hotel
# Locations: Hotel lobby, sidewalk
# Characters: LINDSEY (Outfit: 1), MC (Outfit: 5)
# Time: night

label v13s41a:
    scene v13s41a_1 # TPP.MC and lindsey on the sidewalk
    with fade

    pause 0.75

    play music music.ck1.v13.Track_Scene_41a fadein 2

    scene v13s41a_2 # TPP. MC and lindsey arriving in the hotel lobby
    with dissolve

    pause 0.75

    scene v13s41a_3 # FPP. Now in the hote lobby, lindsey smiling, mouth opened
    with dissolve

    li "Thank you for tonight [name]."

    scene v13s41a_4 # TPP. Lindsey gives mc a hug, both smiling
    with dissolve

    pause 0.75

    scene v13s41a_3 
    with dissolve

    li "Have a good night, okay?"

    scene v13s41a_3a # FPP. Same as 3, mouth closed
    with dissolve

    u "You too."

    scene v13s41a_3b # FPP. Lindsey leaves the hotel lobby, back to the camera
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s42 

# -Lindsey goes off-
# -Transition to Scene 42-
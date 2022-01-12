# SCENE 53b: CAMERON INTERROGATION
# Locations: Apes Frat House
# Characters: MC (Outfit: 1)
# Time: Night

label v14s53b:
    play music "music/v12/Track Scene 23_1.mp3" fadein 2
    scene v14s53b_1 # TPP. Show MC going to the door to leave the Apes Dream Room, tired, mouth closed
    with fade

    if not v14_SamanthaDrugs:
        u "(I think I deserve a good night's sleep.)"

    else:
        u "*Sighs* (I'm so ready for bed.)"

    play sound "music/v14/Track Scene 53b_2 SFX Bag Over Head.mp3"
    scene v14s53b_2 # TPP. Show a bag coming over MC's head as he passes thought the door (don't show who is putting the bag on his head), show MC's shocked face as the bag comes on his head
    with vpunch

    pause

    stop music fadeout 3

    jump end14

label end14:
    if not renpy.loadable("v15/scene1.rpy"):
        scene savenow #nothing needed
        with Fade (1,0,1)
        " "

    if renpy.loadable("v15/scene1.rpy"):
        jump v15_start
    else:
        call screen end_screen
        
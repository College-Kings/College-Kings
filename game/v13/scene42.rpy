# SCENE 42: MC goes to bed
# Locations: Hotel room, hotel lobby and hotel corridor
# Characters: MC (Outfit: 5)
# Time: night

label v13s42:
    scene v13s42_1 # TPP. MC leaves the hotel lobby, smiling
    with dissolve

    pause 0.75

    play music music.v13_Track_Scene_42 fadein 2

    scene v13s42_2 # TPP. MC walking in the hotel corridor heading to his room still smiling
    with dissolve

    pause 0.75

    scene v13s42_3 # TPP. MC arriving in his room (dont show roomate)
    with dissolve

    pause 0.75

    scene v13s42_4 # TPP. MC plops on his bed, arms behind his head
    with dissolve

    u "(Another night, and soon a new day.)"

    scene v13s42_5 # TPP. Images of MC sleeping
    with dissolve
    
    pause 0.75

    scene v13s42_6 # TPP. Images of MC sleeping
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s43

# -Transition to Scene 43-
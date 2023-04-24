# SCENE 5: MC goes to bed (rooming with Chloe) some random change
# Locations: Hotel corridor, Hotel Room
# Characters: MC (Outfit: 1), CHLOE (Outfit: 3)
# Time: Night

label v13s5:
    play music "music/v13/Track Scene 5.mp3" fadein 2
    if not CharacterService.is_girlfriend(chloe):
        scene v13s5_1 # TPP. Show MC and Chloe walking in the hotel corridor, carrying their luggage, Chloe frowning, tired, mouth closed, MC slight smile, mouth closed
        with dissolve

        pause 1

    scene v13s5_2 # TPP. Show MC and Chloe walking into the hotel room, carrying their luggage, Chloe frowning, tired, mouth closed, MC slight smile, mouth closed
    with dissolve

    pause 1

    scene v13s5_3 # TPP. Show MC placing down his luggage, slight smile, mouth closed
    with dissolve

    pause 1

    scene v13s5_4 # FPP. MC looking at Chloe, she is sleeping on her bed
    with dissolve

    u "Chloe?"

    scene v13s5_5 # FPP. MC now standing in front of Chloe, Chloe sleeping, MC looking at her
    with dissolve

    u "Chloe?"

    u "(That didn't last long. *Chuckles*)"

    if CharacterService.is_girlfriend(chloe, Relationship.GIRLFRIEND):
        scene v13s5_6 # TPP. Show MC tucking Chloe in to sleep
        with dissolve

        pause 1.25

        play sound "sounds/kiss.mp3"

        scene v13s5_7 # TPP. Show MC kissing Chloe on the forehead
        with dissolve

        pause 1.75

    scene v13s5_8 # TPP. Show MC turning the lights off, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s5_9 # TPP. Show MC removing his shirt, room dark, slight smile, mouth closed
    with dissolve

    pause 1

    scene v13s5_10 # TPP. Show MC getting in his bed, he's in his boxers, slight smile, mouth closed
    with dissolve

    pause 1

    scene v13s5_11 # TPP. Show MC sleeping
    with fade

    pause 1

    scene v13s5_11a # TPP. Same as v13s5_11, different pose
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s06
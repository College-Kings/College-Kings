# SCENE 41: Apes Pre-Fight
# Locations: MC Apes Room
# Characters: MC (Outfit 3/Outfit 7), Grayson (Outfit 3), Ryan (Outfit 2), Caleb (Outfit 2), Cameron (Outfit 3), Sam (Outfit 2)
# Time: Saturday Night

label v9_apes_pre_fight:
    scene v9apf1 # TPP. Show MC on his bed in his Apes room.
    with fade
    
    if lindsey.relationship >= Relationship.KISSED:
        u "(What a day!)"

        scene v9apf1a # TPP. Same camera as v9apf1a, MC smile.
        with dissolve

        u "(I can still taste the caramel.)"

        scene v9apf1
        with dissolve

    else:
        u "(I hope Lindsey's not mad at me. She's a nice girl. And she's really hot! I don't wanna blow it.)"

    u "(I suppose I should get ready for the Brawl.)"

    scene v9apf2 # TPP. Show MC stood in the middle of his room now wearing outfit 7.
    with fade

    pause 2

    play music "music/v9/Track Scene 14.mp3" fadein 2

    scene v9apf3 # TPP. Show Grayson barging through the door of MC's room.
    with dissolve

    pause 1

    scene v9apf4 # FPP. Show Grayson, looking angry (Not super angry, but Grayson amount of angry), mouth open.
    with dissolve

    gr "Time to go! Downstairs."

    scene v9apf5 # TPP. Show Grayson leaving MC's room, MC stood watching him leave looking a little dumfounded.
    with dissolve

    pause 2

    scene v9apf6 # TPP. Show Ryan and Caleb stood against a wall next to eachother, Grayson, Cameron and Sam stood opposite, MC walking over to Ryan and Caleb.
    with fade

    pause 1

    scene v9apf7 # TPP. Show Grayson, Cameron and Sam, Grayson same expression as v9apf4, Cameron agitated, Sam neutral, Cameron mouth open.
    with dissolve
    
    ca "Bout damn time!"

    scene v9apf8 # TPP. Show Ryan, Caleb and MC in a line, show Cameron placing a blindfold on Ryan.
    with dissolve

    pause 2

    scene v9apf8a # TPP. Same camera as v9apf8, Ryan now blindfolded, show Cameron now placing a blindfold on Caleb.
    with dissolve

    pause 2

    scene v9apf9 # FPP. Show Cameron now stood infront of MC, Sebastian mouth open.
    with dissolve

    ca "Lights out."

    scene v9apf9a # FPP. Same camera as v9apf9, show Cameron stepping towards the camera holding out a blindfold as if he's a bout to place the blindfold on MC. (Blindfold should be the main focus).
    with dissolve

    pause 1

    scene black
    with dissolve

    ca "Let's go."

    stop music fadeout 3

    jump v9_at_warehouse
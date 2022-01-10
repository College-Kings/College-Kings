# SCENE 40: Wolves Pre-Fight
# Locations: MC Wolves Room
# Characters: MC (Outfit 3/Outfit 7), Chris (Outfit 2), Imre (Outfit 4), Perry (Outfit 3), Sebastian (Outfit 1), Marcus (Outfit 2)
# Time: Saturday Night

label v9_wolves_pre_fight:
    scene v9wpf1 # TPP. Show MC sat on his bed in his Wolves room.
    with fade

    if lindsey.relationship >= Relationship.KISS:
        u "(What a day!)"

        scene v9wpf1a # TPP. Same camera as v9wpf1, MC smiling.
        with dissolve

        u "(I can still taste the caramel.)"

        scene v9wpf1
        with dissolve

    else:
        u "(I hope Lindsey's not mad at me. She's a nice girl. And she's really hot! I don't wanna blow it.)"

    u "(I suppose I should get ready for the Brawl.)"

    scene v9wpf2 # TPP. Show MC stood in his room now wearing outfit 2.
    with fade

    pause 1

    scene v9wpf3 # TPP. Show MC's door.
    with dissolve

    play sound "sounds/knock.mp3"

    "*Knock* *knock*"

    u "Come in!"

    scene v9wpf4 # TPP. Show Chris entering MC's Wolves room.
    with dissolve

    pause 1

    scene v9wpf5 # FPP. Show Chris, smile, mouth open.
    with dissolve

    ch "It's about that time, ready to do this?"

    scene v9wpf5a # FPP. Same camera as v9wpf5, smile, mouth closed.
    with dissolve

    u "More than ready!"

    play music "music/v9/Track Scene 14.mp3" fadein 2

    scene v9wpf5b # FPP. Same camera as v9wpf5, neutral expression, mouth open.
    with dissolve

    ch "A lot of people are going to be paying close attention tonight. Girls, frat brothers, enemies, friends and foes, everyone."
    ch "But when you're in the ring don't think about anything except your opponent. No distractions, got it?"

    scene v9wpf5c # FPP. Same camera as v9wpf5, neutral expression, mouth closed.
    with dissolve

    u "No distractions."

    scene v9wpf5
    with dissolve

    ch "Great, time to go! Downstairs."

    scene v9wpf6 # TPP. Show Chris and MC leaving MC's room, MC walking behind Chris.
    with dissolve

    pause 1

    scene v9wpf7 # FPP. Show Sebastian, Chris and Marcus, Sebastian stood in the middle, Sebastian mouth open.
    with fade

    se "Alright guys, let's get this show on the road!"

    scene v9wpf8 # TPP. Show Imre, Perry and MC stood in a line, Sebastian goes up to Imre and places a blindfold on him.
    with dissolve

    pause 2

    scene v9wpf8a # TPP. Same camera as v9wpf8, Imre now blindfolded, Sebastian now putting the blindfold on Perry.
    with dissolve

    pause 2

    scene v9wpf9 # FPP. Show Sebastian now stood infront of MC, Sebastian mouth open.
    with dissolve

    se "Lights out."

    scene v9wpf9a # FPP. Same camera as v9wpf9, show Sebastain stepping towards the camera holding out a blindfold as if he's about to place the blindfold on MC. (Blindfold should be the main focus).
    with dissolve

    pause 1

    scene black
    with dissolve

    se "Let's go!"

    stop music fadeout 3

    jump v9_at_warehouse
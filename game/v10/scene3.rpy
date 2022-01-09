# SCENE 3: First Matchup - Imre vs Caleb (Apes)
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7), Grayson (Outfit 3), Josh (Outfit 2), 
# Time: Saturday Night

label v10_imre_vs_caleb:
    scene v10ivc1 # TPP. Show MC walking towards the ring, Josh in ring in tux, mouths closed, nerutal expressions-
    with fade
    play music "music/v10/Track Scene 2.mp3" fadein 2

    pause 0.75

    scene v10ivc2 # FPP. Show Josh in the ring, mouth closed, slight smile
    with dissolve

    u "(Let's see who's up first)"

    scene v10ivc2a # FPP. Same Camera as v10ivc2, Show josh with his left hand held up pointing to Imre, neutral expression, josh mouth open
    with dissolve

    jo "Ladies and Gentlemen, the time has arrived for our first matchup to begin. In the Wolves corner, we have Imre!"

    scene v10ivc2b # FPP. Same Camera as v10ivc2, Show josh with his left hand held up pointing to Imre, neutral expression, josh mouth closed
    with dissolve

    u "Boooo!"

    scene v10ivc2c # FPP. Same Camera as v10ivc2, Show josh with his right other hand held up pointing to Caleb, neutral expression, josh mouth open
    with dissolve

    jo "And for the Apes, we have Caleb!"

    scene v10ivc2d # FPP. Same Camera as v10ivc2, Show josh with his right other hand held up pointing to Caleb, neutral expression, josh mouth closed
    with dissolve

    u "Woooo!"

    scene v10ivc3 # FPP. Show Caleb, hand over his mouth looking like he's going to be sick, mouth closed
    with dissolve
    # -MC turns to Caleb to cheer him on and sees Caleb clutching his stomach-

    u "Oh no! What's wrong?"

    scene v10ivc3a # FPP. Same Camera as v10ivc3, Show Caleb, hand now slightly lowered looking like he's going to be sick, mouth open
    with dissolve

    cal "I don't think I can do this. I feel... sick."

    scene v10ivc4 # FPP. Show Grayson, pointing at caleb, slight angry face, caleb hand over mouth, Grayson mouh open
    with dissolve

    gr "Aww fuck, man. None of that shit! Suck it up and get in that ring!"

    scene v10ivc5 # FPP. Show Caleb running for the door to go puke
    with dissolve

    pause 0.75

    scene v10ivc2e # FPP. Same Camera as v10ivc2,Show Josh in the ring, mouth open, slight smile
    with dissolve

    jo "Well, now..."
    
    stop music fadeout 3

    jump v10_imre_vs_caleb_fight

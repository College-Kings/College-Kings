# SCENE 40a: MC wakes up (Sebastian Talk)
# Locations: Wolves house
# Characters: MC (Outfit: 1), SEBASTIAN (Outfit: 1) # No Sebastian outfits in the document
# Time: Morning

label v14s40a:
    scene v14s40a_1
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 18.mp3" fadein 2

    scene v14s40a_2 # TPP. Show MC standing in his room putting on pants 
    with dissolve
    
    pause

    scene v14s40a_2a # TPP. Same as v14s40a_2, MC fully dressed for the day, slight smile, mouth closed.
    with dissolve

    pause 

    scene v14s40a_3 # TPP. MC walking down the stairs in the Wolves house, slight smile, mouth closed.
    with dissolve

    u "(Let's start the day, shall we?)"

    scene v14s40a_4 # TPP. MC walking up to Sebastian who is in the living room of the Wolves house.
    with dissolve

    pause 

    scene v14s40a_5 # FPP. MC looking at Sebastian, Sebastian looking at MC, Sebastian slight smile, mouth open.
    with dissolve

    se "Morning sunshine! I thought you were planning on sleeping all day. *Laughs*"

    scene v14s40a_5a # FPP. Same as v14s40a_5, Sebastian slight smile, mouth closed.
    with dissolve

    u "Sunshine?"

    scene v14s40a_5
    with dissolve

    se "Ah, sorry. Heard it in a show and can't stop saying it."

    menu:
        "I don't hate it":
            $ add_point(KCT.BOYFRIEND)
            scene v14s40a_5a
            with dissolve

            u "I... don't hate it, actually. *Laughs*"

            scene v14s40a_5
            with dissolve

            se "Good to know, sunshine."

            scene v14s40a_5a
            with dissolve

            u "Okay, maybe-"

            scene v14s40a_5
            with dissolve

            se "Too much?"

            scene v14s40a_5a
            with dissolve

            u "A little."

            scene v14s40a_5
            with dissolve

        "Don't do it again":
            $ add_point(KCT.BRO)
            scene v14s40a_5a
            with dissolve

            u "*Chuckles* What the fuck? Just don't use it on me."

            scene v14s40a_5
            with dissolve

            se "Your loss."

    se "Anyway... Just a little heads up. There may be a drug test coming up soon so make sure you're clean. Are you clean?"

    menu:
        "I'm clean":
            $ add_point(KCT.BOYFRIEND)
            scene v14s40a_5a
            with dissolve

            u "I am, yeah."

        "I'm not clean":
            $ add_point(KCT.BRO)
            $ add_point(KCT.TROUBLEMAKER)
            scene v14s40a_5a
            with dissolve
    
            u "Not right now, no."

    scene v14s40a_5
    with dissolve

    se "Clean or not clean, just make sure that test comes back negative, got it?"

    scene v14s40a_5a
    with dissolve

    u "When is it?"

    scene v14s40a_5
    with dissolve

    se "I don't know, soon. You have class today so go ahead, I'll catch you later."

    scene v14s40a_5b # FPP. Show Sebastian walking off.
    with dissolve

    u "(This man is calling me sunshine and he knows my class schedule? Is this what it's like to have a father...? *Laughs*)"

    scene v14s40a_6 # TPP. Show MC entering the class hallways, slight smile, mouth closed.
    with fade

    pause 0.75

    stop music fadeout 3

    jump v14s43
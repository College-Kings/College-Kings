# SCENE 38: Walking home with Jenny
# Locations: Sidewalk
# Characters: MC (Outfit: 2), JENNY (Outfit: Sexy bikini top from v14s36 and denim shorts) (Wed)
# Time: Night

label v14s38:
    scene v14s38_1 # TPP. Camera slightly behind and over MC's shoulder showing MC (walking) and Jenny (her back) just a few feet in front of him, walking.
    with dissolve

    pause 0.75

    play music "music/v12/Track Scene 33_5.mp3" fadein 2

    scene v14s38_2 # FPP. Jenny, walking down the side walk, her back to MC.
    with dissolve

    u "Jenny!"

    scene v14s38_2a # FPP. Jenny, smiling, mouth open, turing around and looking at MC.
    with dissolve

    jen "Oh, hey again. *Chuckles*"

    scene v14s38_2b # FPP. same as v14s38_2a, but Jenny mouth closed.
    with dissolve

    u "I hung back for a quick phone call, I thought you'd be gone by now."

    scene v14s38_3 # FPP. Jenny's body facing forward, her head turned toward MC (camera), smiling, mouth open, background 1 behind Jenny.
    with dissolve

    jen "Oh, I'm honestly taking my sweet time tonight."

    scene v14s38_3a # FPP. Same as v14s38_3, but Jenny's mouth closed
    with dissolve

    u "It doesn't bother you to walk around alone at night?"

    scene v14s38_3 # FPP. Same as v14s38_3, but Jenny's head has a subtle tilt and background 2 behind Jenny (so it looks like they are walking).
    with dissolve

    jen "Not really, I used to do it all the time growing up. Nothing's happened so far, haha."

    scene v14s38_3a # FPP. Same as v14s38_3a, but background 2 behind Jenny.
    with dissolve

    u "Okay, well don't say it like that. *Laughs* Hopefully nothing ever happens."

    scene v14s38_4 # FPP. Same as v14s38_4, but Jenny's head has a subtle tilt different than v14s38_4 and background 3 behind Jenny.
    with dissolve

    jen "If you keep stalking me I won't even have to worry."

    menu:
        "Apologize":
            $ add_point(KCT.BOYFRIEND)

            scene v14s38_4a # FPP. Same as v14s38_4a, but background 3 behind Jenny.
            with dissolve

            u "I wasn't trying to-"

            scene v14s38_4
            with dissolve

            jen "Relax, I'm kidding."

            scene v14s38_4a
            with dissolve

            u "*Laughs* Cool, I don't want you thinking I'm some creep."

            scene v14s38_4
            with dissolve

            jen "Trust me, if I did, I would've said something by now."

            scene v14s38_4a
            with dissolve

            u "So, since you haven't said anything by now..."

            scene v14s38_4
            with dissolve

            jen "I want to be stalked by you, yes."

        "Compliment her":
            $ add_point(KCT.BRO)

            scene v14s38_4a
            with dissolve
           
            u "Well maybe if you weren't so cute I wouldn't have to pretend to run into you all the time, haha."

            scene v14s38_4
            with dissolve

            jen "Awww, haha. Fine you can keep stalking me."


    scene v14s38_4a
    with dissolve

    u "*Chuckles*"

    scene v14s38_4 # # FPP. Same as v14s38_4, but Jenny laughing, but use the same background from v14s38_4. 
    with dissolve

    jen "*Laughs*"

    scene v14s38_6 # TPP. MC and Jenny reach fork in the path and Jenny is heading in the opposite direction than MC. Both looking at each other, smiling, mouths closed.
    with dissolve

    pause 0.75

    scene v14s38_7 # FPP. Jenny completlly facing MC, smiling, mouth closed.
    with dissolve
    
    u "Oh, guess this is where our paths change for the night."

    scene v14s38_7a # FPP. same as v14s38_7, but Jenny's mouth open.
    with dissolve

    jen "Yep, haha. See you soon?"

    scene v14s38_7
    with dissolve

    u "You better."

    scene v14s38_6a # TPP. same as v14s38_6, but MC and and Jenny each walking in opposite directions, neutral expression, mouths closed.
    with dissolve

    pause 0.75

    stop music fadeout 3

    if joinwolves:
        jump v14s40
    
    else:
        jump v14s41
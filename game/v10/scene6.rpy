# SCENE 6: MC vs Ryan (Wolves)
# Locations: Warehouse
# Characters: 
# Time: Saturday Night

label v10_mc_vs_ryan_fight:
    scene v10mvr1 # FPP. Show imre and chris near ring, imre excited look, mouth open chris mouth closed
    with dissolve

    imre "Holy shit man, did you see that shit!? I was planning on doing that one-two thing Sebastian showed me but I guess the one was enough!"

    scene v10mvr1a # FPP. Same camera as v10mvr1, Show imre and chris near ring, imre excited look, mouth closed chris mouth closed
    with dissolve

    u "*Laughs* Yeah man, that fucking sick!"

    scene v10mvr1
    with dissolve
    # -Imre starts dancing-
    imre "*Sings* I'm getting me some pussy after that! I'm getting me some pussy! I'm getting me some pussy!"

    scene v10mvr1b # FPP. Same camera as v10mvr1, Show imre and chris near ring, excited look, imre mouth closed Chris mouth open
    with dissolve

    ch "Imre did good out there, but don't let his win distract you."

    scene v10mvr2 # FPP. Show Jost leant against the edge of the ring, slight smile, mouth open
    with dissolve

    jo "*Loud whisper* Hey, I got some plans tonight. How much longer is..."

    scene v10mvr1b
    with dissolve

    ch "We're ready Josh! *Laughs*"

    scene v10mvr1
    with dissolve

    imre "Go take him apart!"

    scene v10mvr1a
    with dissolve

    u "You got it man."

    scene v10mvr3 # TPP. Show Josh in the ring, mc walking towards him from behind mc. 
    with dissolve
    
    pause 0.5

    scene v10mvr4 # TPP. Show josh in the centre of the ring and ryan and MC in opposite corners, Josh mouth open, mc and ryan mouth closed
    with dissolve
    jo "Looks like our fighters are ready!"

    scene v10mvr5 # TPP. Show josh in the centre of the ring and ryan next to josh either side, Josh mouth closed, mc mouth closed, ryan mouth open
    with dissolve

    ry "You ready to do this?"

    menu:
        "Fight Ryan":

            scene v10mvr6a # FPP. Show Ryan infront of camera in ring, mouth open, hands raised ready to fight.
            with dissolve
            u "Question is, are you ready?"

            jo "Same rules as before, just get it guys!"

            # -Manual Fight-

            jump v10_fight_result

        "Don't Fight":
            $ v10_ryan_fight = True
            scene v10mvr6a 
            with dissolve

            u "I don't think I can do this. Sorry guys."

            scene v10mvr7 # FPP. Show Close up from ring of Chris and imre stood watching, Imre mouth open, chris mouth closed
            with dissolve
            imre "Dude, you better not quit right now!"

            scene v10mvr7a # FPP. Show Close up from ring of Chris and imre stood watching, Imre mouth closed, chris mouth open
            with dissolve

            ch "Come on, man. You got this!"

            scene v10mvr6  #Ryan mouth open
            with dissolve

            ry "Man, what are you doing?! We have to do this."

            scene v10mvr6a
            with dissolve

            u "I can't, I just can't."

            jump v10_avoid_fight


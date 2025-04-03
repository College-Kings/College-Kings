# SCENE 1: Outside Scuffle
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7),Imre (Outfit 4), Sebastian (Outfit 1), Cameron (Outfit 3), Ryan (Outfit 2)
# Time: Saturday Night
 
label v10start:
    scene v10sta1 # FPP. Show Imre and ryan on the floor fighting, imre on bottom, ryan on top, angry faces, mouths closed
    with dissolve
    u "What are you guys doing!?"

    play music music.ck1.v10.Track_Scene_1 fadein 2

    scene v10sta2 # FPP. Show MC trying to pull Ryan and imre apart, imre/ryan angry, mc worried look, mouths closed
    with dissolve

    pause 0.75

    if mc.frat == Frat.WOLVES:
        scene v10sta2 # FPP. Show Imre and ryan now standing in fighting stances both with fists raised, angry look on imre/ryan, ryan mouth closed, imre mouth open
        with dissolve

        imre "Stay the fuck out [name]! This is my fight."

        scene v10sta2       
        with dissolve

        ry "You're gonna wish you hadn't called off your back up."

    else:
        scene v10sta2
        with dissolve
  
        ry "No! This is my fight! Don't fucking interfere!"
 
        scene v10sta3
        with dissolve

        imre "I'll bash your fucking head in right now."

        scene v10sta3a # FPP. Same camera as v10sta3, angry look on imre/ryan, ryan mouth open, imre mouth closed

        with dissolve

        ry "You couldn't bash someone's head in if they gave you a fucking head bashing machine!"

        scene v10sta3b # FPP. Same camera as v10sta3, Imre and ryan grappling each other, sebastian pulling away imre, cameron pulling away ryan, angry faces, imre/ryan/cameron closed mouths, Sebastian mouth open.
        with dissolve
 
        se "Alright guys, better stop here before it gets embarrassing."
 
        scene v10sta3c
        with dissolve
 
        ca "Why the fuck would you wrestle him?! Go for a fucking punch if you mean it!"

    stop music fadeout 3

    if mc.frat == Frat.WOLVES:
        scene v10sta4a # FPP. Same Camera as v10sta4, imre now left scene, Show Sebastian near the warehouse doors facing camera, neutral look, mouth open
        with dissolve
 
        se "Why the fuck would you wrestle him?! Go for a fucking punch if you mean it!"

        jump v10_ryan_v_perry

    else:
        scene v10sta5 # FPP. Show Cameron Facing Camera, neutral look, mouth open
        with dissolve

        ca "Don't you have a fight to get ready for?"

        scene v10sta5a # FPP. Same camera as v10sta5,Show Cameron Facing Camera, neutral look, mouth closed
        with dissolve

        u "(This ought to be a fucking show.)"

        scene v10sta6 # TPP. Show MC back to camera heading towards warehouse
        with dissolve

        jump v10_imre_vs_caleb
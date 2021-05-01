# SCENE 1: Outside Scuffle
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7),Imre (Outfit 4), Sebastian (Outfit 1), Cameron (Outfit 3), Ryan (Outfit 2)
# Time: Saturday Night

label v10start:
    scene v10sta1 # FPP. Show Imre and ryan on the floor fighting, imre on bottom, ryan on top, angry faces, mouths closed
    with dissolve
    u "What are you doing!?"

    scene v10sta2 # FPP. Show MC trying to pull Ryan and imre apart, imre/ryan angry, mc worried look, mouths closed
    with dissolve

    pause 1

    if joinwolves:

        scene v10sta3 # FPP. Show Imre and ryan now standing in fighting stances both with fists raised, angry look on imre/ryan, ryan mouth closed, imre mouth open
        with dissolve

        imre "Not this time, stay the fuck out of this! This is my fight!"

        scene v10sta3a # FPP. Same camera as v10sta3, angry look on imre/ryan, ryan mouth open, imre mouth closed
        with dissolve

        ry "You're gonna wish you hadn't called off your back up."

    else:
        scene v10sta3b # FPP. Same camera as v10sta3, Imre and ryan grappling each other, sebastian pulling away imre, cameron pulling away ryan, angry faces, imre/ryan/cameron closed mouths, Sebastian mouth open.
        with dissolve 
    
        Ryan "No! This is my fight! Don't fucking interfere!"

        scene v10sta3c # FPP. Same camera as v10sta3, Show Cameron smacks Ryan on the back of the head, cameron angry face, ryan slight angry face, cameron mouth open, ryan mouth closed
        with dissolve

        se "Glad you're in fighting spirits, now let's use all that energy on something useful."

        scene v10sta4 # FPP. Show Sebastian pulling Imre towards the warehouse, backs to camera
        with dissolve

        pause 1

        scene v10sta3c
        with dissolve

        ca "Fucking idiot! Fights are getting ready to be annouced, get inside."

    if joinwolves:
        scene v10sta4a # FPP. Same Camera as v10sta4, imre now left scene, Show Sebastian near the warehouse doors facing camera, neutral look, mouth open
        with dissolve

        se "They're going to announce soon. Get inside [name]."

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



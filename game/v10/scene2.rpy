# SCENE 2: Ryan vs Perry
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7), Chris (Outfit ), Perry (Outfit ), Josh (Outfit 2), 
# Time: Saturday Night

label v10_ryan_v_perry:
    play music music.ck1.v10.Track_Scene_2 fadein 2
    scene v10rvp1 # FPP. Show Josh in the ring walking around, taking the announcer role in his stride. Mouth open.
    with dissolve

    jo "Ladies and Gentlemen, the time has arrived for our first matchup to begin. In the Wolves corner, we have Perry!"

    scene v10rvp2 # FPP. Show Perry stood next to Chris just outside the ring, perry looks super worried, Chris smile, Perry mouth open.
    with dissolve

    guyd "I can't do this. I'm gonna be sick."

    scene v10rvp2a # FPP. Same as rvp2, Chris and Perry both looking at eachother, Chris smile, Perry worried, Chris mouth open.
    with dissolve

    ch "Of course you can. You're a wolf. You got this! You'll feel better once you get in there."

    scene v10rvp2b # FPP. Same as rvp2, Chris no longer has his hand on perry, Chris looks slightly concerned, perry with his hand on his stomach as if he's about to puke, Perry mouth open.
    with dissolve

    guyd "I'm gonna..."

    scene v10rvp3 # TPP. Show Josh now looking in the direction of Perry, josh looks a little confused.
    with dissolve

    pause 1

    stop music fadeout 3

    jump v9_ryan_v_perry_fight

# Walking back w Grayson
# Location: Apes House
# Outfits: MC Outfit 2, Grayson Outfit 2
# Time: Tuesday Night

label walk_home_w_gray:
    scene v8swbg1 # TPP. Show MC and Grayson walking down the path outside of the front of the Apes house, towards the entrance.
    with Fade(0.75, 0.25, 0.75)

    pause 0.5

    scene v8swbg2 # FPP. Show Grayson turning to his side to look at MC (Camera) Grayson slight smile, mouth open.
    with dissolve

    gr "Aw man it's gonna be epic. You ready?"

    scene v8swbg2a # FPP. Same camera as v8swbg2, Grayson looking back forward, mouth closed.
    with dissolve

    u "(Still not sure what I signed up for. He was so intense in those woods)"

    u "Yeah... what exactly do I need to be ready for?"

    scene v8swbg2b # FPP. Same camera as v8swbg2, Grayson looking back at the camera, grin, mouth open.
    with dissolve

    if not hesitantwgrayson:
        gr "Aw, man, I almost don't wanna tell you."

        scene v8swbg2a
        with dissolve

        u "Dude! You took me to some creepy ass woods and we pounded our chests! I deserve to know."

        scene v8swbg2b
        with dissolve

        gr "Yeah, you're right..."

        scene v8swbg2a
        with dissolve

        u "Well?"

        scene v8swbg2c # FPP. Same camera as v8swbg2, Grayson looking at camera, laugh, mouth open.
        with dissolve

        gr "Nah! I can't. It's too much fun to torture you!"

        scene v8swbg2a
        with dissolve

        u "Dick!"

        scene v8swbg2c
        with dissolve

        gr "Hey! It's Big Dick to you!"

        scene v8swbg2c
        with dissolve

        u "If you say so..."

        scene v8swbg2b
        with dissolve

        gr "Not just me."

    else:
        gr "That's the best part!"

        scene v8swbg2b
        with dissolve

        u "How so?"

        scene v8swbg2c
        with dissolve

        gr "It's a surprise!"

        scene v8swbg2a
        with dissolve

        u "What?"

        scene v8swbg2b
        with dissolve

        gr "Yeah... I think I'll keep it to myself... for now."

        scene v8swbg2a
        with dissolve

        u "Aw, you ass! At least give me a hint."

    scene v8swbg3 # TPP. Show Grayson and MC entering the apes house.
    with dissolve

    pause 0.5

    scene v8swbg4 # FPP. Close up Grayson who is now stood at the bottom of the Apes stairs, Grayson neutral expression, mouth open.
    with dissolve

    gr "Let's just say we're gonna be seeing a lot of each other from now on."

    scene v8swbg4a # FPP. Same camera as v8swbg4, Grayson mouth closed.
    with dissolve

    u "(Not ominous at all, dude)"

    scene v8swbg5 # FPP. Show Grayson beginning to walk up the Apes stairs, he turns around and waves, Grayson smile, mouth open.
    with dissolve

    gr "Later, you Great Ape, you!"

    scene v8swbg5a # FPP. Same camera as v8swbg5, Grayson turns back forward and continues walking up the stairs.
    with dissolve

    u "Just don't get me expelled."

    scene v8swbg6 # TPP. Show MC walking up the stairs behind Grayson, Grayson turns around again to look at MC with a grin, Grayson mouth open.
    with dissolve

    gr "No promises."

    stop music fadeout 3

    scene v8swbg7 # TPP. Show Grayson entering a room, MC walking to his Apes room.
    with dissolve

    pause 0.5

    jump tue_night_in_room

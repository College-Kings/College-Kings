# SCENE 62: Threesome Cliffhanger
# Locations: Hotel Room
# Characters: AUBREY (Outfit: 6), MC (Outfit: 3), RILEY (Outfit: 6)
# Time: Night

label v13s62:
    scene v13s62_1 # FPP. MC looking at the door, lying on his bed, Aubrey and Riley walking in, both worried, mouths closed
    with dissolve

    pause 1.5

    play music "music/v13/Track Scene 62.mp3" fadein 2

    scene v13s62_2 # FPP. Show Aubrey and Rilet sitting on the bed next to MC, both slightly worried, looking at MC, Aubrey mouth open, RIley mouth closed
    with dissolve

    au "How are you feeling?"

    scene v13s62_2a # FPP. Same as v13s62_2, mouths closed
    with dissolve

    u "I'm doing better, thanks."

    scene v13s62_2b # FPP. Same as v13s62_2, both slight smiles
    with dissolve

    au "I felt so terrible for what happened to you so, me and Riley thought we'd come by and try to cheer you up. *Chuckles*"

    scene v13s62_2c # FPP. Same as v13s62_2a, both slight smiles
    with dissolve

    u "Seeing both of you here is definitely cheering me up already."

    scene v13s62_2d # FPP. Same as v13s62_2c, but Riley mouth open
    with dissolve

    ri "*Chuckles*"

    scene v13s62_2b
    with dissolve

    au "Is that so?"

    scene v13s62_2e # FPP. Same as v13s62_2b, Aubrey and Riley looking at each other
    with dissolve

    au "You hear that Riley? He likes both of us..."

    scene v13s62_2f # FPP. Same as v13s62_2e, Riley mouth open, Aubrey mouth closed
    with dissolve

    ri "Yeah, I'm pretty sure I heard that too... *Chuckles*"

    scene v13s62_2e
    with dissolve

    au "Since both of us have been a little mean to him recently, we should probably make him feel better, right?"

    scene v13s62_2f
    with dissolve

    ri "I think I'd have to agree with that. *Chuckles* What'd you have in mind?"

    scene v13s62_3 # TPP. Show Aubrey placing her hand on MC's pants (where his dick is), Aubrey slight smile, mouth closed, Riley slight smile, mouth closed
    with dissolve

    u "Oh, wow..."

    scene v13s62_2g # FPP. Same as v13s62_2e, Aubrey has her hand on MC's pants (where his dick is)
    with dissolve

    au "I was thinking we should give him a little massage to begin."

    scene v13s62_3a # TPP. Same as v13s62_3, Riley's hand also on his pants where his dick is
    with dissolve

    pause

    scene v13s62_2h # FPP. Same as v13s62_2f, Aubrey and Riley's hand on MC's pants (where his dick is)
    with dissolve

    ri "I like that idea."

    scene v13s62_2i # FPP. Riley and Aubrey start making out with their hands still on MC's dick
    with dissolve

    u "(Is this happening?!)"

    stop music fadeout 3

label end13:
    if not renpy.loadable("v14/scene1.rpy"):
        call screen savenow()
        with Fade (1,0,1)
        " "

    if renpy.loadable("v14/scene1.rpy"):
        jump v14_start
    elif config.enable_steam:
        call screen end_screen(support_link="https://store.steampowered.com/dlc/1463120/College_Kings__Act_I/")
    else:
        call screen end_screen
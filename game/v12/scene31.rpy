# SCENE 31: Mc woken up by Aubrey
# Locations: Hotel Room
# Characters: AUBREY (Outfit: 3), MC (Outfit: 2), CHLOE (Outfit: 5)
# Time: Morning
# Phone Images: NONE

label v12_aubrey_wake_up:
    scene black
    with vpunch

    au "Hey, wake up!"

    play music "music/v12/Track Scene 31.mp3" fadein 2

    scene v12auw1 # FPP. MC lying in his bed, Aubrey standing next to him, MC and Aubrey looking at each other, Aubrey slight smile, mouth closed
    with dissolve

    u "Huh? Wait... What? How'd you get in here?"

    scene v12auw1a # FPP. Same as v12auw1, Aubrey slight smile, mouth open
    with dissolve

    au "Chloe let me in. I know I forgot to tell you, but I need you to hurry up and come on! My sister's shoot is in thirty minutes."

    scene v12auw1
    with dissolve

    u "What shoot?!"

    scene v12auw1a
    with dissolve

    au "The shoot at Lew's I told you about, now hurry up."

    scene v12auw2 # TPP. Show MC getting out of his bed, slightly annoyed, mouth closed
    with dissolve

    u "*Sighs*"

    scene v12auw3 # TPP. Show MC walking over to the dresser, MC slightly annoyed, mouth closed
    with dissolve

    pause 0.75

    scene v12auw4 # FPP. MC in front of the dresser, Aubrey and Chloe sitting on Chloe's bed. MC looking at Chloe, Chloe looking at Aubrey, Chloe slight smile, mouth open (Only Chloe in shot)
    with dissolve

    cl "Sorry, he's a little slow."

    scene v12auw5 # FPP. Same positioning as v12auw4, MC looking at Aubrey, Aubrey looking at Chloe, Aubrey slight smile, mouth open (Only Aubrey in shot)
    with dissolve

    au "Don't worry, I've noticed. *Chuckles*"

    scene v12auw4a # FPP. Same as v12auw4, Chloe looking at MC, Chloe slight smile, mouth closed
    with dissolve

    u "Is it \"gang up on [name]\" day?"

    scene v12auw4b # FPP. Same as v12auw4a, Chloe slight smile, mouth open
    with dissolve

    if CharacterService.is_girlfriend(chloe, Relationship.GIRLFRIEND):
        cl "You know I'm just messing around, I wouldn't make fun of my boyfriend. Even if he is slow... *Chuckles*"

        scene v12auw4a
        with dissolve

        u "*Chuckles* Good to know."

        scene v12auw5a # FPP. Same as v12auw5, Aubrey confused, mouth open
        with dissolve

        au "\"Boyfriend\"?"

        scene v12auw4
        with dissolve

        cl "Oh yeah, we're dating."

        scene v12auw5b # FPP. Same as v12auw5, Aubrey looking at MC, Aubrey confused, mouth closed
        with dissolve

        u "Surprise!"

        scene v12auw5a
        with dissolve

        au "Since when? Why hadn't either of you told me?"

        scene v12auw4
        with dissolve

        cl "Since London! I honestly hadn't thought to go around telling everyone."

        scene v12auw5b
        with dissolve

        u "We'll have time for all the stories later, gotta hurry, remember? C'mon."

    else:
        scene v12auw4b
        #with dissolve
        
        cl "Chicks always ride together."

        scene v12auw5c # FPP. Same as v12auw5b, Aubrey slight smile, mouth open
        with dissolve

        au "Sorry, it's the truth."

        scene v12auw5d # FPP. Same as v12auw5c, Aubrey slight smile, mouth closed
        with dissolve

        u "*Sighs* C'mon, we're in a hurry, right?"

    scene v12auw5
    with dissolve

    au "Bye Chloe."

    scene v12auw4
    with dissolve

    cl "Bye guys, have fun."

    scene v12auw6 # TPP. Show Aubrey and MC leaving the hotel room, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v12s32 #scene 32
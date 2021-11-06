# SCENE 29: Imre calls MC
# Locations: Campus Sidewalk, Imre's wolves house room.
# Characters: MC (Outfit: 2), IMRE (Outfit: 1)
# Time: Afternoon

label v14s29:
    scene v14s29_1 # TPP. Show MC walking down the Sidewalk campus, slight smile, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/call.mp3"

    scene v14s29_2 # TPP. Close up of MC looking at his phone while standing on the sidewalk, slight smile, mouth open.
    with vpunch

    u "(And I know when my hotline bling!) *Chuckles*"

    stop sound
    play sound "sounds/answercall.mp3"

    scene v14s29_2a # TPP. Same as v14s29_2, Show MC holding the phone to his ear, slight smile, mouth open.
    with dissolve

    u "Hello?"

    scene v14s29_3 # TPP. Show Imre in his room at the Wolve's house on the phone, Imre slight smile, mouth open.
    with dissolve

    imre "Aye, let's hit the gym! I need to blow off some steam."

    scene v14s29_3a # TPP. Same as v14s29_3, Imre on the phone, Imre slight smile, mouth closed.
    with dissolve

    if v14_talk_to_chris:
        u "Sorry man, I'm doing the Wolves photoshoot with Chris. You aren't?"

        scene v14s29_3
        with dissolve

        imre "Oh fuck, I forgot about that. Shit, guess I'll meet you there."

        scene v14s29_3a
        with dissolve

        u "Haha, see you soon."

        play sound "sounds/rejectcall.mp3"

        scene v14s29_2
        with dissolve

        u "(That guy!) *Chuckles*"

        scene v14s29_4 # TPP. Show MC walking down the sidewalk towards the wolves house
        with dissolve

        if v14_realwolf:
            pause 0.75
            jump v14s30a

        else:
            pause 0.75
            jump v14s30

    elif not v14_help_chloe:
        u "Just like that, huh?"

        scene v14s29_3
        with dissolve

        imre "Just like that! Hurry up, I'm headed there now."

        scene v14s29_3a
        with dissolve

        u "I'm on my way."

        scene v14s29_6 # TPP. Show MC starting to walk towards the gym, slight smile, mouth closed.
        with dissolve

        pause 0.75

        jump v14s32
        
    #elif not v14_talk_to_chris: #Placeholder for helping Chloe but didn't talk to Chris.
    else:
        u "Okay sure."

        scene v14s29_3
        with dissolve

        imre "Ahh shit... Sorry, I just remembered something I gotta do."

        scene v14s29_3a
        with dissolve

        u "*Chuckles* Okay."

        play sound "sounds/rejectcall.mp3"
        
        scene v14s29_2
        with dissolve

        u "(This dude's weird.) *Chuckles*"

        scene v14s29_5 # TPP. Show MC standing on the sidewalk, slight smile, mouth closed.
        with dissolve

        pause 0.75

        jump v14s31
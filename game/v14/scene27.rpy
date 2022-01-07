# SCENE 27: Emily passes you on campus
# Locations: Campus
# Characters: EMILY (Outfit: 1), MC (Outfit: 2)
# Time: Morning

label v14s27:
    scene v14s27_1 # TPP. MC and Emily walking towards each other on the sidewalk on Campus, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 23.mp3" fadein 2

    scene v14s27_1a # TPP. Same as v14s27_1, Getting closer as they walk towards each other, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s27_2 # FPP. MC looking at Emily, Emily looking at MC, Emily nervous smile, mouth open.
    with dissolve

    em "Hey, [name]."

    if "v13_emily" in sceneList:
        scene v14s27_2a # FPP. Same as v14s27_2, Emily nervous smile, mouth closed.
        with dissolve

        u "What's up, Emily?"
        
        scene v14s27_2
        with dissolve

    else:
        scene v14s27_2a
        with dissolve

        u "Emily."

        scene v14s27_2
        with dissolve

        em "Ha, okay..."
    
    em "It's actually good that I ran into you."

    scene v14s27_2a
    with dissolve

    u "Why's that?"

    scene v14s27_2
    with dissolve

    em "I have some pretty major news to share with you."

    scene v14s27_2a
    with dissolve

    u "Oh. What is it?"

    scene v14s27_2
    with dissolve

    em "Can we speak somewhere a little more... private?"

    scene v14s27_2a
    with dissolve

    menu:

        "Of course":
            $ add_point(KCT.BOYFRIEND)
            u "Of course. Where do you wanna go?"

        "Can't we speak here?":
            $ add_point(KCT.TROUBLEMAKER)
            u "Is it that serious that you can't say it here?"

            scene v14s27_2b # FPP. Same as v14s27_2, Emily slightly upset, mouth open.
            with dissolve

            em "Oh my god, [name]. What the fuck?"

            em "Can you give me a single ounce of decency? All I asked was to speak to you in private, okay?"

            scene v14s27_2a
            with dissolve

            u "*Sighs* Okay, let's talk."

    scene v14s27_2
    with dissolve

    em "I need to get some of my stuff out of the locker room, we can talk there."

    scene v14s27_2a
    with dissolve

    u "Lead the way."

    scene v14s27_3 #TPP. Show MC and Emily walking down the side walk together, both nervous smile, mouth closed.
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s28
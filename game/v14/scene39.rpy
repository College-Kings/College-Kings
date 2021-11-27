# SCENE 39: Walking home with Penelope
# Locations: Sidewalk on the way back from the Restaurant
# Characters: PENELOPE (Outfit: Date Dress), MC (Outfit: Date Outfit)
# Time: Night

label v14s39:
    scene v14s39_1a # FPP. Same as v14s39_1, Penelope neutral face, mouth closed.
    with dissolve

    u "Some people would just rather not deal with the confrontation."

    play music "music/v12/Track Scene 33_5.mp3" fadein 2

    scene v14s39_1
    with dissolve

    pe "Even he knew she was out of her mind."

    scene v14s39_1a
    with dissolve

    u "Did you consider that it may be something else keeping him around? Something outside of just her?"

    scene v14s39_1
    with dissolve

    pe "Like what? I can't think of anything that's worth putting up with her."

    scene v14s39_1a
    with dissolve

    u "Kids maybe? She also said he lost his job, so I assume she's the breadwinner right now."

    scene v14s39_1
    with dissolve

    pe "*Sighs* I didn't even think about that. He was probably just trying to stay quiet for as long as he could."

    scene v14s39_1a
    with dissolve

    u "Yeah, that's what I was thinking at least."

    scene v14s39_1
    with dissolve

    pe "Promise me that we'll never be those people."

    scene v14s39_1a
    with dissolve

    u "Hey, you're the lady! You need to be the one promising me. *Laughs* I don't think I can be as nice and tame as he was."

    scene v14s39_1
    with dissolve

    pe "Haha, you'd snap back at me in front of everyone?"

    menu:
        "I'd wait":
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.TROUBLEMAKER)
            $ v14s39_id_wait = True
            scene v14s39_1a
            with dissolve

            u "I'd probably wait until we got home, and then we'd discuss what happened in private."

            scene v14s39_1
            with dissolve

            pe "Oh my gosh, [name]!"

            scene v14s39_1a
            with dissolve

            u "What'd I say?"

            scene v14s39_1
            with dissolve

            pe "\"We'll discuss what happened... in private.\""

            scene v14s39_1a
            with dissolve

            u "Haha! I did not say it like that, I just meant..."

            scene v14s39_2 # FPP. MC and Penelope further up the sidewalk, change the background scenery to make it look like they are moving as they talk, Penelope slight smile, mouth closed.
            with dissolve

            pe "Oh, haha, sorry. I thought you meant- Well, you know what I thought."

            pe "Discussing it at home sounds perfect."

            scene v14s39_2a # FPP. Same as v14s39_2, Penelope slight smile, mouth closed.
            with dissolve

            u "*Laughs* Good. Discussing, spanking, same thing."

            scene v14s39_2
            with dissolve

            pe "[name]!"

            scene v14s39_2a
            with dissolve

            u "*Laughs*"

            scene v14s39_2
            with dissolve

            pe "You're naughty..."

        "Hell yeah!":
            $ add_point(KCT.BRO)
            scene v14s39_1a
            with dissolve
        
            u "Hell yeah, I would. I don't care what the reason is. I wouldn't just let you talk to me like that in front of everyone."

            scene v14s39_2
            with dissolve

            pe "Well, I don't plan to ever push you that far... Ha."

            scene v14s39_2a
            with dissolve

            u "Yeah, of course. I know that."

            scene v14s39_2
            with dissolve

            pe "Let's hope I never do. Ha."

            scene v14s39_2a
            with dissolve

            u "I can't even imagine you being angry besides with what just happened..."

            scene v14s39_2
            with dissolve

            pe "Haha, it's not pretty."

            scene v14s39_2a
            with dissolve

            u "Now I'm curious..."

            scene v14s39_2
            with dissolve

            pe "Oh my god... *Chuckles*"

    scene v14s39_3 # TPP. Show MC and Penelope stopping at a cross in the road.
    with dissolve

    pause 0.75

    scene v14s39_4 # FPP. MC and Penelope at the Cross in the road, MC looking at Penelope, Penelope looking at MC, Penelope slight smile, mouth open.
    with dissolve

    pe "I'm headed this way."

    scene v14s39_4a # FPP. Same as v14s39_4, Penlope slight smile, mouth closed.
    with dissolve

    u "Okay, I'm this way."

    if v14s37_focus_on_us or kct == "confident":
        if not v14s37_focus_on_us:
            call screen kct_popup

        scene v14s39_4b # FPP. Same as v14s39_4, Penelope nervous smile, mouth open.
        with dissolve

        pe "I..."

        pe "...was kinda hoping..."

        scene v14s39_4c # FPP. Same as v14s39_4b, Penelope nervous smile, mouth closed.
        with dissolve

        u "What do you want, Penelope? Just say the words."

        scene v14s39_4b
        with dissolve

        pe "Maybe our night doesn't have to end here?"

        scene v14s39_5 # TPP. Show MC holding Penelope's hands romantically.
        with dissolve

        pause 0.75

        scene v14s39_4d # FPP. Same as v14s39_4c, Penelope's arms extended out holding MC's, Penelope slight smile, mouth closed.
        with dissolve

        u "Okay, sure. What do you wanna do?"

        scene v14s39_4e # FPP. Same as v14s39_4c, Still holding hands, Penelope slight smile, mouth open.
        with dissolve

        pe "Would you, umm..."

        pe "Would you want to come over? And like, stay over? Or..."

        scene v14s39_4d
        with dissolve

        u "Stay over?"

        scene v14s39_4e
        with dissolve

        pe "Like, stay the night?"

        scene v14s39_4d
        with dissolve

        u "*Chuckles*"

        scene v14s39_4e
        with dissolve

        pe "You probably think that's stupid, I'm probably rushing things... This was our first \"date\" date and here I am trying to-"

        scene v14s39_4f # FPP. Same as v14s39_4e, MC grabbing Penelope's face with both hands gently, Penelope slight smile, mouth closed.
        with dissolve

        u "I would love to stay the night with you."

        scene v14s39_4g # FPP. Same as v14s39_4f, MC still grabbing her face gently, Penelope full smile, mouth open.
        with dissolve

        pe "Really?!"

        scene v14s39_4f
        with dissolve

        u "Are you kidding? I can't wait, haha."

        play sound "sounds/kiss.mp3"

        scene v14s39_6 # TPP. Show Penelope and MC kissing.
        with dissolve

        pause 0.75

        scene v14s39_4e
        with dissolve

        pe "Let's go."

        scene v14s39_7 # TPP. Show MC and Penelope holding hands and walking down the sidewalk towards Penelope's dorm, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v14s42

    else:
        scene v14s39_4
        with dissolve

        pe "Well, thanks for tonight. I'll see you around?"

        scene v14s39_4h # FPP. Same as v14s39_4, Penelope puts up a fist for a fist bump, slight smile, mouth closed.
        with dissolve

        u "*Chuckles*"

        scene v14s39_4i # FPP. Same as v14s39_4h, MC giving Penelope a fist bump, Penelope slight smile, mouth open
        with dissolve

        pe "I'm sorry, that was weird..."

        scene v14s39_4a
        with dissolve

        u "It's fine, I'm sorry if tonight was... also weird."

        scene v14s39_4
        with dissolve

        pe "It's okay. At least you kept your promise, haha. I'm gonna go."

        scene v14s39_4a
        with dissolve

        u "Okay, be safe."

        if v14s39_id_wait:
            scene v14s39_4
            with dissolve

            pe "I mean..."

            pe "Maybe we can try this again? Maybe with a little more planning or something?"

            scene v14s39_4a
            with dissolve

            u "Yeah, that sounds great. Thank you."

            scene v14s39_4
            with dissolve

            pe "Perfect."

        else:
            scene v14s39_4
            with dissolve
    
            pe "You too."
        
        scene v14s39_8 # FPP. Show Penelope walking her way down the side walk.
        with dissolve

        pause 0.75

        scene v14s39_9 # TPP. MC walking down the side walk to his room, slight smile, mouth closed.
        with dissolve

        u "(*Sighs* That was a rocky night.)"

        pause 0.75

        stop music fadeout 3

        if joinwolves:
            jump v14s40
        else:
            jump v14s41
# SCENE 42a: Waking up with Penelope
# Locations: Penelope Dorm, Dorm corridor
# Characters: MC (Outfit: Boxers / 1), PENELOPE (Outfit: Lingerie / 1)
# Time: Morning

label v14s42a:
    scene v14s42a_1 # TPP. Show MC sleeping on Penelope's bed, Penelope awake laying next to him, caressing his cheek, Penelope smiling, mouth closed
    with fade

    pause 0.75

    play music "music/v12/Track Scene 26b.mp3" fadein 2

    scene v14s42a_2 # FPP. MC now awake, looking at Penelope who is laying next to him, Penelope smiling, mouth closed
    with dissolve

    u "*Yawns* Morning sunshine. Did you sleep well?"

    scene v14s42a_2a # FPP. Same as v14s42a_2, Penelope mouth open, smiling
    with dissolve

    pe "Best sleep I've had in a long time."

    scene v14s42a_2
    with dissolve

    u "Why's that?"

    scene v14s42a_2a
    with dissolve

    pe "I had a pretty good pillow."

    scene v14s42a_2
    with dissolve

    u "Haha, glad I could be of service."

    scene v14s42a_2a
    with dissolve

    pe "I wanted to mention that, I'm sorry for last night."

    scene v14s42a_2b # FPP. Same as v14s42a_2, Penelope slightly sad, mouth closed
    with dissolve

    u "Huh? Sorry for what?"

    scene v14s42a_2c # FPP. Same as v14s42a_2b, Penelope slightly sad, mouth open
    with dissolve

    pe "For getting you all dressed up and making you take me out on a date."

    scene v14s42a_2b
    with dissolve

    u "Penelope..."

    scene v14s42a_2c
    with dissolve

    pe "And then bringing you home and not doing anything..."

    pe "I'm sure you were looking forward to something special."

    scene v14s42a_2b
    with dissolve

    u "Well-"

    scene v14s42a_2c
    with dissolve

    pe "I mean, I was looking forward to our night together as well, but I got so tired and comfy while we were cuddling. I must have fallen asleep."

    scene v14s42a_2b
    with dissolve

    menu:
        "I wouldn't have changed a thing":
            $ add_point(KCT.BOYFRIEND)
            $ penelope.relationship = Relationship.LOYAL

            scene v14s42a_2
            with dissolve

            u "There's nothing to apologize for, I wouldn't change a thing about last night."

            scene v14s42a_2a
            with dissolve

            pe "Really?"

            scene v14s42a_2d # FPP. Same as v14s42a_2, Penelope different pose
            with dissolve

            u "Really."

            scene v14s42a_2e # FPP. Same as v14s42a_2d, Penelope smiling, mouth open
            with dissolve

            pe "Our next night together will be a night to remember."

            scene v14s42a_2d
            with dissolve

            u "Is that a promise?"

            scene v14s42a_2e
            with dissolve

            pe "Yes. Yes it is."

        "Sex would've been nice":
            $ add_point(KCT.BRO)
            scene v14s42a_2f # FPP. Same as v14s42a_2, Penelope slightly uncomfortable, mouth closed
            with dissolve

            u "Well, yeah, I can't lie. When you came out looking like that... *Chuckles* I kinda thought something was gonna end up happening."

            scene v14s42a_2g # FPP. Same as v14s42a_2f, Penelope slightly uncomfortable, mouth open
            with dissolve

            pe "Yeah, my bad. Haha, sorry."

            scene v14s42a_2f
            with dissolve

            u "It's no problem, I had a nice night and slept great as well."

            scene v14s42a_2g
            with dissolve

            pe "Good."

    scene v14s42a_2
    with dissolve

    u "So... Are you ready to leave for class?"

    scene v14s42a_2a
    with dissolve

    pe "Class?"

    scene v14s42a_2
    with dissolve

    u "Yeah, Mr. Lee's?"

    scene v14s42a_2e
    with dissolve

    pe "Oh my god! I got distracted and completely forgot. Are we late?"

    scene v14s42a_2d
    with dissolve

    u "Haha, nah. We have enough time to get ready and walk there."

    scene v14s42a_3 # TPP. Show Penelope jumping out of bed, smiling, mouth open, MC still laying down, looking at Penelope, MC slight smile, mouth closed
    with dissolve

    pe "Good, because I don't wanna be late."

    scene v14s42a_4 # TPP. Show MC getting out of bed, slight smile, mouth closed, Penelope looking through her closet (has her back turned to camera, make sure to show her ass)
    with dissolve

    pause

    scene v14s42a_5 # TPP. Show MC putting on his shirt (pants on), Penelope still looking in her closet (she has pants on now)
    with fade

    pause 0.75

    scene v14s42a_6 # FPP. Penelope standing in front of her closet, MC standing next to her, Penelope looking at MC, smiling, mouth closed (she only has her pants and bra on)
    with dissolve

    u "C'mon, slow poke!"

    scene v14s42a_6a # FPP. Same as v14s42a_6, Penelope smiling, mouth open
    with dissolve

    pe "Sorry that I actually attempt to look presentable."

    scene v14s42a_6
    with dissolve

    u "Hey! What's that supposed to mean? *Chuckles*"

    scene v14s42a_6a
    with dissolve

    pe "*Laughs*"

    scene v14s42a_7 # TPP. Show Penelope putting her shirt on, slight smile, mouth closed
    with fade

    pause
    
    scene v14s42a_8 # TPP. Show Penelope walking out of the room, pulling MC by the arm, smiling, mouth open, MC smiling, mouth closed
    with dissolve

    pe "C'mon, slow poke!"

    scene v14s42a_9 # TPP. Show Penelope and MC running in the corridor, close to her room door, both laughing
    with dissolve

    u "*Laughs*"

    stop music fadeout 3

    jump v14s43a
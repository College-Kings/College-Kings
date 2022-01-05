# SCENE 5: If Ms. Rose Rs, Drug Testing Announcement
# Locations: Campus/Classroom
# Characters: MC (Outfit: 5), Ms. Rose (Outfit: 1)
# Time: Morning

label v15s5:
    # -MC is walking outside on campus, near the library-
    scene v15s5_1 # TPP. Show MC walking outside of campus near the library, MC slight smile, mouth closed.
    with fade

    pause 0.75

    scene v15s5_1a # TPP. Same as v15s5_1, Show MC walking he was just positioned walking, looking ahead of him, slight smile, mouth closed.
    with dissolve

    u "(Oh boy...)"

    scene v15s5_2 # TPP. Close up of just Ms. Rose walking in the oppisite direction towards MC, looking at MC, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s5_2a # TPP. Same as v15s5_2, Ms. Rose standing in place a little bit up from where she was walking, pointing at a nearby classroom subtly, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s5_2b # TPP. Same as v15s5_2a, Ms, Rose signing at MC with her finger to follow her to the classroom, slight smile, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/doorclose.mp3"

    scene v15s5_3 # TPP. Show Ms. Rose leaning against the deck inside the classroom, MC standing near her by the desk, both slight smile, mouth closed.
    with fade

    pause 0.75

    scene v15s5_4 # FPP. MC looking at Ms. Rose leaning against the desk, Ms. Rose looking at MC, Ms. Rose worried smile, mouth open.
    with dissolve

    ro "Hi, [name], how are you?"

    scene v15s5_4a # FPP. Same as v15s5_4, Ms. Rose worried smile, mouth closed.
    with dissolve

    u "Um, I'm good. How are you? *Chuckles*"

    scene v15s5_4
    with dissolve

    ro "I'm pleased to see that you're in a good mood. It might be easier to get through this conversation..."

    scene v15s5_4a
    with dissolve

    u "What conversation?"

    scene v15s5_4
    with dissolve

    ro "I heard that there's going to be a drug test for all students participating in the tournament coming up."

    scene v15s5_4a
    with dissolve

    u "Oh, yeah. I already heard something about that..."

    u "Do you know exactly when they're testing us?"

    scene v15s5_4
    with dissolve

    ro "I don't. I just know that it's sometime soon."

    if "v14_amber" in sceneList or v14s31b_smoke_weed_with_aubrey or v13_smoke_weed or v15_autumn_smoke:
        scene v15s5_4a
        with dissolve

        u "Are they testing for weed?"

        scene v15s5_4
        with dissolve

        ro "They will be testing for everything."

        ro "So, I just wanted to apologize in advance in case they find you positive for the drug I put in your drink while we were in Paris."

    else:
        scene v15s5_4a
        with dissolve

        u "I should be fine... I'm not worried."

        scene v15s5_4
        with dissolve

        ro "Well, I hope there's nothing to worry about."

        ro "I just wanted to apologize in advance in case they find you positive for the drug I put in your drink while we were in Paris."

    ro "I'm not sure how long it can stay in your system but... They might detect traces of it since these tests are very sophisticated."

    ro "A little bit of weed is one thing, [name]. But that was a serious drug I slipped you."

    menu:
        "Be calm":
            $ add_point(KCT.BRO)
            
            u "*Sighs*"

            u "I'm sure it'll be okay."

            scene v15s5_4b # FPP. Same as v15s5_4a, Ms. Rose looking at MC with a super embarassed and sorry look, mouth closed.
            with dissolve

            u "I'll just drink loads of water or something to make sure it's all flushed out of my system. *Chuckles*"

            scene v15s5_4c # FPP. Same as v15s5_4b, Ms. Rose starting to have cheered up a little, slight smile, mouth open.
            with dissolve

            ro "*Chuckles* That's my boy..."

            ro "Thank you for not being angry with me."

            scene v15s5_4d # FPP. Same as v15s5_4c, Ms. Rose slight smile, mouth closed.
            with dissolve

            u "Yeah, of course. It was worth it, I think..."

            scene v15s5_4c
            with dissolve

            ro "I thought so too."

            scene v15s5_4d
            with dissolve

            u "I- uh, I better go before your class starts showing up."

            scene v15s5_4c
            with dissolve

            ro "If they ever do... *Laughs*"

            scene v15s5_4d
            with dissolve

            u "*Laughs*"

            scene v15s5_4c
            with dissolve

            ro "I'll see you around, [name]."

            scene v15s5_4e # FPP. Ms. Rose giving MC a flirtatious look and winking at him, mouth closed.
            with dissolve

            pause 0.75

            play sound "sounds/dooropen.mp3"

            scene v15s5_5 # TPP. Show MC walking out of the classroom, Ms. Rose in the background leaning against the desk looking at him leave, both slight smile, mouth closed.
            with dissolve
            play sound "sounds/doorclose.mp3"
            pause 0.75

            scene v15s5_6 # TPP. Shot of the classroom door closed.
            with dissolve
            
            pause 0.75
        
        "Get angry":
            $ add_point(KCT.BOYFRIEND)
            $ v15_mad_at_ms_rose = True
            
            scene v15s5_4b
            with dissolve
            
            u "Fuck, Lorraine..."

            scene v15s5_4f # FPP. Same as v15s5_4b, Ms. Rose embarrassed and sorry look, mouth open.
            with dissolve

            ro "I'm sorry, [name]. I never thought that you'd be getting drug tested."

            scene v15s5_4b
            with dissolve

            u "Yeah, neither did I. Now look."

            scene v15s5_4f
            with dissolve

            ro "I'm sorry."

            scene v15s5_4b
            with dissolve

            u "What can they do to me? Throw me out of the tournament? Can they throw me out of college?!"

            scene v15s5_4f
            with dissolve

            ro "I don't know about college, but they will ban you from participating in the tournament."

            scene v15s5_4b
            with dissolve

            u "Fuck! That's so messed up!"

            u "You literally drugged me, without my permission. And now-"

            scene v15s5_4f
            with dissolve

            ro "I know you're angry, [name], but... I don't regret it."

            ro "The sex we had was one of the best experiences of my entire life."

            menu:
                "Agree":
                    $ add_point(KCT.TROUBLEMAKER)
                    
                    scene v15s5_4b
                    with dissolve
        
                    u "Yeah, it was amazing. You're not wrong."

                "Disagree":
                    $ add_point(KCT.BOYFRIEND)
                    
                    scene v15s5_4b
                    with dissolve

                    u "Well, not for me. It might have been fun but..."

            u "It's not worth losing everything I've worked for."

            scene v15s5_4f
            with dissolve

            ro "[name], please. Let me make it up to you."

            scene v15s5_4b
            with dissolve

            u "How can you make it up to me? Are you going to take the drug test for me? *Scoffs* I don't think that'll work."

            scene v15s5_4g
            with dissolve

            ro "I'll think of something to take your mind off it..."
            
            scene v15s5_5a # TPP. Same as v15s5_5a, MC walking out of the classroom, MC looking angry, mouth open, Ms. Rose in the back watching MC leave with a flirtatious look as she bites her lip, mouth closed.
            with dissolve

            u "I need to go. This is... so fucked up."

            play sound "sounds/doorclose.mp3"

            scene v15s5_6
            with hpunch
            
            pause 0.75

    jump v15s6
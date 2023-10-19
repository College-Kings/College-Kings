# SCENE 11: Amber Tease/Penelope Kiss
# Location: Airport, boarding area
# Characters: MC (Outfit 1), Amber (Outfit X), Penelope (Outfit X)
# Time: Saturday morning

label v11_Amber_Penelope:
    scene v11amp1 # FPP In airport boarding area, show Amber, neutral expression, mouth closed
    with dissolve
    play music music.ck1.v11.Track_Scene_11 fadein 2
    menu:
        "Tease her":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ v11_tease_amber += 1
            scene v11amp1
            with dissolve

            u "Amber, is that you? I didn't recognize you outside your work uniform."

            scene v11amp1b # FPP Same angle as v11amp1, Amber with pained expression, mouth open
            with dissolve

            am "This is exactly what I wanted to talk about..."

            scene v11amp1
            with dissolve
            
            pause 0.5

        "Don't tease her":
            scene v11amp1
            with dissolve

            u "(I'll leave her alone.)"

            scene v11amp1
            with dissolve

            u "What's up?"

    scene v11amp1b # FPP Same angle as v11amp1, Amber with concerned expression, mouth open
    with dissolve

    am "Listen, the real reason I don't want anyone knowing that I work at Lew's is because it's kind of... embarrassing. It's not really my ideal job, but it pays really well."
    am "So, can we please just pretend you never saw me there?"

    menu:
        "Tease her":
            $ v11_tease_amber += 1

            scene v11amp1c # FPP Same angle and expression as v11amp1a, Amber mouth closed
            with dissolve

            u "*Chuckles* Maybeee."

            scene v11amp1d # FPP Same angle as v11amp1, Amber looks nervous, mouth open
            with dissolve

            am "[name]... please."

            scene v11amp1e # FPP Same angle and expression as v11amp1d, Amber mouth closed
            with dissolve

            u "This'll be fun."

        "Don't tease her":
            scene v11amp1
            with dissolve

            u "No worries, it's already forgotten."

            scene v11amp1f # FPP Same angle as v11amp1, Amber looks relieved, mouth open
            with dissolve

            am "For real? Thanks, [name]."

            scene v11amp1g # FPP Same angle and expression as v11amp1f, Amber mouth closed
            with dissolve

            u "No problem."

    scene v11amp1
    with dissolve

    u "So why were you asking if we could do whatever we want? Sounds oddly suspicious."

    scene v11amp1h # FPP Same angle as v11amp1, Amber smiling and raising an eyebrow, mouth open
    with dissolve

    am "So that I can do whatever I want, duh. *Chuckles*"

    scene v11amp1
    with dissolve

    u "Well, what are you wanting to do?"

    scene v11amp1i # FPP Same angle and expression as v11amp1, Amber mouth open
    with dissolve

    am "Kim told me in Amsterdam there's some canals and if you get high at night while looking into the water it looks like snakes in the moonlight."

    scene v11amp1
    with dissolve

    u "That sounds... romantic?"

    scene v11amp1i
    with dissolve

    am "I just want an excuse to get high and it'd be cool to see if it actually looks like snakes. You can come with if you'd like."

    menu:
        "Of course":
            $ v11_smoke_amber_amsterdam = True
            
            scene v11amp1
            with dissolve

            u "Of course, anything to have a good time."

            scene v11amp1j # FPP Same angle as v11amp1, Amber smiling, mouth open
            with dissolve

            am "Cool."

        "No":
            scene v11amp1
            with dissolve

            u "Haha, I'll pass."

            scene v11amp1i
            with dissolve

            am "Your loss."

    if not v11_pen_goes_europe: # -If Penelope isn't there-
        scene v11amp2 # FPP Show Ms. Rose with mouth open, speaking loudly
        with dissolve

        ro "Alright everyone, time to board!"

        scene v11amp1j
        with dissolve

        am "Later, loser."

        # Non-dialogue images of MC getting on the plane
        scene v11amp3 # TPP Show MC grabbing his bag and heading toward the boarding gate
        with dissolve

        pause 0.75

        scene v11amp4 # TPP Show MC boarding the plane
        with dissolve

        pause 0.75   

    else: # Penelope is there
        scene v11amp5 # FPP Show Penelope, neutral expression, mouth open
        with dissolve

        pe "Hey Amber, [name], it's time to get on the plane."

        scene v11amp1j
        with dissolve

        am "Later, loser."

        scene v11amp6 # FPP Show Amber walking away, towards boarding the plane
        with dissolve

        pause 0.75

        scene v11amp5a # FPP Same angle and expression as v11amp5, Penelope mouth closed
        with dissolve

        u "They working you hard?"

        scene v11amp5
        with dissolve

        pe "It's better than paying $15,000. Ms. Rose is taking it easy on me, but Mr. Lee won't let up. He's making me do anything he can think of."
        pe "He already had me carry all the bags with the baggage handlers. Speaking of, I need to drop these off."

        scene v11amp5a
        with dissolve

        u "Here, let me help."

        scene v11amp7 # TPP Show MC and Penelope carrying a few bags
        with dissolve

        pause 0.75

        scene v11amp8 # TPP Show MC and Penelope setting down bags with other baggage
        with dissolve

        pause 0.75

        scene v11amp5d
        with dissolve

        u "I'm just glad this is as bad as it gets."

        scene v11amp5b
        with dissolve

        pe "I'm sure Mr. Lee will get more creative than this."

        scene v11amp5d
        with dissolve

        u "It'll be over in no time."

        scene v11amp5b
        with dissolve

        pe "Thanks. It still doesn't feel real how this all ended up going."

        scene v11amp5d
        with dissolve

        u "Told you I was a good lawyer. *Chuckles*"

        scene v11amp5b # FPP Same angle as v11amp5, Penelope smiling, mouth open
        with dissolve

        pe "Haha, yeah... you really were..."

        scene v11amp9 # TPP Show Penelope kissing MC on the cheek
        with dissolve

        play sound sound.kiss

        pause 0.75

        scene v11amp5c # FPP Same angle as v11amp5, Penelope with hand on her ear, looking down
        with dissolve

        menu:
            "Kiss her":
                $ CharacterService.set_relationship(penelope, Relationship.DATING)
                $ reputation.add_point(RepComponent.BOYFRIEND)

                play sound sound.kiss

                scene v11amp9a # TPP Same angle as v11amp9, MC with his hand on Penelope's cheek, kissing her on the lips
                with dissolve
                
                grant Achievement("cross_your_heart", "Kiss Penelope at the airport")

                pause 1.75
                
                scene v11amp9b # TPP Same angle as v11amp9, MC still has hand on Penelope's cheek, pulling back after kiss, Penelope smiling
                with dissolve

                pause 0.75

            "Don't kiss her":
                scene v11amp5d # FPP Same angle and expression as v11amp5b, Penelope mouth closed
                with dissolve

                u "*Smirks*"

        scene v11amp5b
        with dissolve

        pe "Let's get on the plane before they leave us. *Chuckles*"

        scene v11amp5d
        with dissolve

        u "Haha, okay."

        # Same non-dialoge images of MC getting on the plane
        scene v11amp3
        with dissolve

        pause 0.75

        scene v11amp4
        with dissolve

        pause 0.75
    stop music fadeout 3
# Transition to Scene 12
jump v11_sit_ryan_convo
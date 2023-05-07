# SCENE 34: Amber talk after spa
# Locations: Spa, Sauna, Hotel Lobby
# Characters: MC (Outfit: Naked in towel/2), AMBER (Outfit: Naked in towel), IMRE (Outfit: Naked in towel), AUBREY (Outfit: Naked in towel)
# Time: Evening
# Phone Images: None

label v12_amber_after_spa:
    scene v12ams1 # TPP. Show MC, Amber, Aubrey and Imre hanging out outside the sauna in their towels, all smiling mouths closed
    with dissolve

    pause 1.25

    play music "music/v12/Track Scene 34_1.mp3" fadein 2

    scene v12ams2 # FPP. MC, Amber, Aubrey and Imre talking to each other, MC looking at Amber, Amber looking at MC, smiling, mouth closed (make sure Lew's logo on towel is visible)
    with dissolve

    menu:
        "Tease Amber":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ v11_tease_amber += 1

            scene v12ams2a # FPP. Same as v12ams2, Amber slightly annoyed, mouth closed
            with dissolve

            u "Damn Amber, is that employee merch? *Chuckles*"

        "Nice towel":
            scene v12ams2b # FPP. Same as v12ams2, Amber neutral expression, mouth closed
            with dissolve

            u "Wow Amber, that's a really nice towel."

            stop music fadeout 3
            play music "music/v12/Track Scene 34_2.mp3" fadein 2

            scene v12ams2
            with dissolve

            am "Haha thanks."
 
            scene v12ams6 # TPP. Show MC leaving the sauna, slight smile, mouth closed
            with dissolve

            pause 1

            scene v12ams7 # TPP. Show MC getting dressed, slight smile, mouth closed
            with dissolve

            pause 1

            scene v12ams8 # TPP. Show MC walking out of spa, slight smile, mouth closed, fully dressed
            with dissolve

            pause 1

            scene v12ams9 # TPP. Show MC walking in hotel lobby, fully dressed, mouth closed, slight smile
            with dissolve

            pause 1

            stop music fadeout 3

            jump v12_chris_nora_room
                
    if v11_tease_amber <= 2 or reputation() == Reputations.POPULAR:
        $ v11_amber_sauna_convo = True
        if not (v11_tease_amber <= 2):
            call screen reputation_popup

        scene v12ams2a
        with dissolve

        am "You know what?"

        stop music fadeout 3
        play music "music/v12/Track Scene 34_2.mp3" fadein 2

        scene v12ams3 # FPP. MC looking as Amber pullsd him into the sauna, Amber mouth open, neutral expression
        with dissolve

        am "You sure do like teasing me, don't you?"

        scene v12ams4 # FPP. MC and Amber inside sauna looking at each other, Amber slight smile, mouth closed
        with dissolve

        u "*Chuckles* Come on... Just having a little fun, Amber."

        scene v12ams4a # FPP. Same as v12ams4, Amber slight smile, mouth open
        with dissolve

        am "Then how about I have some fun, huh?"

        scene v12ams5 # TPP. Show Amber kissing MC
        with dissolve

        menu:
            "Pull away":
                $ reputation.add_point(RepComponent.BRO)
                scene v12ams4
                with dissolve

                u "Woah, what are you doing?"

                scene v12ams4a
                with dissolve

                am "Well, I was just gonna tease you... Until you killed the fun."

                scene v12ams4
                with dissolve

                u "Haha, my bad. Just got a little surprised."

                scene v12ams4a
                with dissolve

                am "Oh well, let's go."

                scene v12ams6 # TPP. Show MC leaving the sauna, slight smile, mouth closed
                with dissolve

                pause 0.75

                scene v12ams7 # TPP. Show MC getting dressed, slight smile, mouth closed
                with dissolve

                pause 0.75

                scene v12ams8 # TPP. Show MC walking out of spa, slight smile, mouth closed, fully dressed
                with dissolve

                pause 0.75

                scene v12ams9 # TPP. Show MC walking in hotel lobby, fully dressed, mouth closed, slight smile
                with dissolve

                pause 0.75

                stop music fadeout 3

                jump v12_chris_nora_room

            "Don't pull away":
                scene v12ams5a # TPP. Same as v12ams5, MC placing his hand on Amber's butt
                with dissolve

                pause 1

                scene v12ams5b # TPP. Same as v12ams5, Amber pulling away from the kiss, MC slightly surprised, Amber slight smile, both mouths closed
                with dissolve

                pause 0.75

                scene v12ams4a
                with dissolve

                am "Teasing sucks, doesn't it?"

                scene v12ams4
                with dissolve

                u "(Oh she's good.)"

                scene v12ams4b # FPP. Same as v12ams4, Amber walking away from MC
                with dissolve

                pause 1.25

                scene v12ams6
                with fade

                pause 0.75

                scene v12ams7
                with dissolve

                pause 0.75

                scene v12ams8
                with dissolve

                pause 0.75

                scene v12ams9
                with dissolve

                pause 0.75

                stop music fadeout 3
                jump v12_chris_nora_room

    else:
        $ ambermad = True

        scene v12ams2c # FPP. Same as v12ams2, Amber very angry, mouth open
        with dissolve

        stop music fadeout 3
        play music "music/v12/Track Scene 34_2.mp3" fadein 2

        am "You just can't mind your own fucking business?"

        scene v12ams10 # TPP. Same positioning as v12ams2, Show Amber smacking MC on the side of the head, Amber very angry, MC startled, both mouths closed
        with vpunch
        play sound sound.slap

        pause 1.25

        scene v12ams11 # TPP. Same positioning as v12ams2, Show Imre and Aubrey looking shocked at MC's direction, only Imre and Aubrey in shot, mouths closed
        with dissolve

        pause 0.75

        scene v12ams2c
        with dissolve

        am "I told you to leave my job shit alone, and yet you keep going on and on about it. Maybe now you'll know what I mean when I say knock it the fuck off."

        scene v12ams2d # FPP. Same as v12ams2c, show Amber storming off, very angry, mouth closed
        with dissolve

        pause 0.75

        scene v12ams12 # FPP. Same positioning as v12ams2, Amber no longer in conversation, MC looking at Imre, Imre looking at MC, Imre smiling, mouth open
        with dissolve

        imre "Damn bro, she just rocked your shit! *Laughs*"

        scene v12ams12a # FPP. Same as v12ams12, Imre smiling, mouth closed
        with dissolve

        u "Imre, shut the fuck up."

        scene v12ams13 # FPP. Same positioning as v12ams12, MC looking at Aubrey, Aubrey looking at MC, Aubrey smiling, mouth open
        with dissolve

        au "Good thing I didn't keep teasing her. *Chuckles* It's better that you get fucked up than me."

        scene v12ams13a # FPP. Same as v12ams13, Aubrey smiling, mouth closed
        with dissolve

        u "Shit, she hit me harder than any of the guys ever have..."

        scene v12ams12
        with dissolve

        imre "Yeah, we saw. *Laughs*"

        scene v12ams12a
        with dissolve

        u "Fuck... I'm gonna head up to my room."

        scene v12ams13
        with dissolve

        au "Probably a good idea. *Chuckles* Get some rest, soy boy!"

        scene v12ams13a
        with dissolve

        u "(Shit!)"

        scene v12ams6a # TPP. Same as v12ams6, MC slightly annoyed, mouth closed
        with dissolve

        pause 0.75

        scene v12ams7a # TPP. Same as v12ams7, MC slightly annoyed, mouth closed
        with dissolve

        pause 0.75

        scene v12ams8a # TPP. Same as v12ams8, MC slightly annoyed, mouth closed
        with dissolve

        pause 0.75

        scene v12ams9a # TPP. Same as v12ams9, MC slightly annoyed, mouth closed
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v12_chris_nora_room
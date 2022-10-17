# SCENE 25: Date with Emmy
# Locations: Simplr Bar, Street
# Characters: MC (Outfit: 9), EMMY (Outfit: 1)
# Time: Afternoon

label v13s25:
    scene v13s25_1 # TPP. Mc walks over to Emmy's table, slight smile, mouth closed, Emmy looking at Mc slight smile, mouth closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 25.mp3" fadein 2
   
    scene v13s25_2 # TPP. Mc grabbing chair looking at Emmy, Mc's back turned to camera, Emmy looking at Mc, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s25_3 # FPP. Emmy looking at Mc, head slightly tilted, slight smile, mouth closed
    with dissolve

    u "So... What'd I say that made you raise your hand?"

    scene v13s25_3a # FPP. Emmy head straight, slight smile, mouth open
    with dissolve

    emmy "That you're on the \"no kids kind of vibe\". *Chuckles*"

    scene v13s25_3
    with dissolve

    u "I was a little worried about saying that, but I wanted to be honest."

    scene v13s25_3a
    with dissolve

    emmy "And look where honesty got us. *Laughs*"

    scene v13s25_3
    with dissolve

    u "To a date at a bar in Amsterdam. *Chuckles*"

    scene v13s25_3
    with dissolve

    u "I can hear them asking me now, \"Why did you travel all the way across the world?\" And my answer will be, \"To go on a date with a woman... A woman named Emmy.\""

    scene v13s25_3b # FPP. Same as v13s25_3a Emmy full smile, one eyebrow raised
    with dissolve

    emmy "*Laughs* Okay, don't start getting all soft on me. Tell me this, can you fight?"

    scene v13s25_3
    with dissolve

    u "Of course you wouldn't know but, fighting is a pretty central part of my life."

    scene v13s25_3b 
    with dissolve

    emmy "Oh, really? How so?"

    scene v13s25_3
    with dissolve

    u "Back on campus, my frat and our rivals continue to fight nonstop. We even have tournaments where a fight king is announced."

    scene v13s25_3c # FPP. Same as v13s25_3b Emmy has one finger on corner of lower lip, and thumb under chin
    with dissolve

    emmy "Oh, wow... So, do you like to fight? Like, you enjoy it?"

    menu:
        "Yes":
            $ reputation.add_point(Reputations.TROUBLEMAKER)
          
            scene v13s25_3d # FPP. Same as v13s25_3c Emmy's finger has moved from corner of lip to just under the lip, mouth closed
            with dissolve

            u "I love it, you can't get the thrill of fighting from anywhere else."

            scene v13s25_3c
            with dissolve

            emmy "I love fighters. You guys just seem so strong and fearless."

            scene v13s25_3d
            with dissolve

            u "You have to be, because at the end of the fight someone's going home hurt and sad, while the other goes home proud and happy."

            scene v13s25_3a
            with dissolve

            emmy "So, you'd fight for me?"

            scene v13s25_3
            with dissolve

            u "Of course, haha. I wouldn't let some punk try to fuck with you."

            scene v13s25_3
            with dissolve

            u "The only one who's going to be fucking you is me. *Chuckles* Was that too much?"

            scene v13s25_4 # TPP. Emmy blushes and looks away as she touches her ear
            with dissolve

            pause 0.5

            scene v13s25_3c
            with dissolve

            emmy "Not at all, it was actually pretty hot. *Chuckles*"

            scene v13s25_5 # TPP. Emmy looks one direction, slight smile, mouth closed
            with dissolve

            pause 0.5

            scene v13s25_6 # TPP. Emmy looks the other direction, slight smile, mouth closed
            with dissolve

            pause 0.5

            if v12s24_emmymatch or kct == "confident": 
                if not v12s24_emmymatch:
                    call screen reputation_popup

                scene v13s25_3c
                with dissolve

                emmy "You know what? Fuck it."

                scene v13s25_7 # TPP. Emmy grabs MC's hand and pulls him away to a secluded area, Both have slight smiles, mouths closed
                with dissolve

                pause 0.5

                scene v13s25_8 # TPP. Emmy slight smile, mouth open, leans her body into MC, one hand pressed against his chest, the other hand unzipping his pants, Mc slight shocked, mouth open, one hand at the side of Emmy's face
                with dissolve

                pause 0.5

                scene v13s25_9 # FPP. Emmy head tilted slighty down, looking up at Mc, biting her lip
                with dissolve

                u "Right here? Right now?"

                scene v13s25_10 # FPP. Emmy head raised slightly up, Full smile, mouth open
                with dissolve

                emmy "Right here, right now."

                menu:
                    "Let her":
                        $ reputation.add_point(Reputations.TROUBLEMAKER)
                        label v13s25_emmysg:

                        scene v13s25_9
                        with dissolve

                        u "(Fuck it, let's do it.)"

                        scene v13s25_10 
                        with dissolve

                        emmy "Don't be gentle."

                        stop music fadeout 3

                        if config_censored:
                            call screen censored_popup("v13s25_nsfwSkipLabel1")

                        jump v13_emmy_sex

                    "Stop her":
                        $ reputation.add_point(Reputations.BOYFRIEND)

                        scene v13s25_9
                        with dissolve

                        u "No. no. no, not here. Maybe we can go back to your place?"

                        scene v13s25_10a # FPP. same as v13s25_10 Emmy is angry
                        with dissolve

                        emmy "Ugh, really?!"

                        scene v13s25_10b # FPP. same as v13s25_10a Emmy mouth closed
                        with dissolve

                        u "Yeah, I was thinking we could-"

                        scene v13s25_10c # FPP. Emmy steps back, is angry, mouth open, one finger pointed up
                        with dissolve

                        emmy "Just stop there, pretty boy."

                        scene v13s25_10d # FPP. Same as v13s25_10c Emmy separates a finger and a thumb indicating Mc has a small dick
                        with dissolve

                        emmy "I'm not gonna let some scaredy cat, bitch-boy fuck me. Hit me up when your balls drop, yeah?"

                        scene v13s25_11 # FPP. Emmy storms off, back turned, flipping off the mc
                        with dissolve

                        u "(So you'll fuck me in an open bar, but not at your place? Maybe I dodged a bullet on that one.)"

                        scene v13s25_12 # TPP. Mc walks back into initial area, slight frown, mouth closed
                        with dissolve

                        u "(These women are crazy.)"

                        pause 0.75

                        scene v13s25_13 # TPP. MC Walking back to boys, slight frown, mouth closed
                        with dissolve

                        pause 0.75

                        scene v13s25_14 # TPP. Sits with the boys, slight frown, mouth closed
                        with dissolve

                        jump v13s25_no_sex

            else:
                call screen reputation_popup(required_reputation="confident")
                
                scene v13s25_3a
                with dissolve

                emmy "You're very attractive, don't get me wrong. *Chuckles*"

                scene v13s25_3
                with dissolve

                u "I sense a \"but\" coming..."

                scene v13s25_3a
                with dissolve

                emmy "But... Chuckles I don't know if our energy levels are quite the same. I might be too much for you."

                scene v13s25_3a
                with dissolve

                emmy "Too much for me? Haha."

                scene v13s25_3a
                with dissolve

                emmy "Ah, see? Now I know for sure. Laughs Maybe in another life. It was nice meeting you, cutie."
                
                scene v13s25_11a # FPP. Same as v13s25_11, Emmy walking away, smiling, waving at MC, mouth closed
                with dissolve

                u "(What... Just... Happened?)"


                scene v13s25_13
                with dissolve

                pause 0.75

                scene v13s25_14
                with dissolve

                pause 0.75
                
                jump v13s25_no_sex

        "No":
            $ reputation.add_point(Reputations.BOYFRIEND)
            scene v13s25_3
            with dissolve

            u "Who would like fighting? *Chuckles*"

            scene v13s25_3e # FPP. Same as v13s25_3 Emmy is slightly angry
            with dissolve

            u "When you have to, you have too. But you would have to be a little bit crazy to actually enjoy beating up other people."

            scene v13s25_3f # FPP. Same as v13s25_3e Emmy is angry, mouth open
            with dissolve

            emmy "So, you think I'm crazy?"

            scene v13s25_3e
            with dissolve

            u "Oh no, I wasn't-"

            scene v13s25_3f
            with dissolve

            emmy "No, it's fine. Ha... You didn't seem like the kind of guy who's wild enough for me anyway."

            scene v13s25_3b
            with dissolve

            emmy "Maybe I would've had better luck with your friend Imre. *Chuckles* Have a nice night, pussy."

            scene v13s25_15 # TPP. Mc Gets up and leaves Emmy at the table, slight frown, mouth closed
            with dissolve

            u "(What the fuck was that?)"

            scene v13s25_13
            with dissolve

            pause 0.75

            scene v13s25_14
            with dissolve

            pause 0.75

            scene v13s25_16 # TPP. Mc sitting, slight frown, mouth closed, Mc see's Emmy
            with dissolve

            pause 0.75

            scene v13s25_17 # TPP. same as v13s25_7 Instead of Mc it is a random person, or possibly Imre or Ryan based off of context
            with dissolve

            pause 0.75

            scene v13s25_18 # TPP. Mc still sitting, slight anger, mouth closed
            with dissolve

            pause 0.75

label v13s25_no_sex:
    scene v13s25_98 # TPP. Show MC leaving the simplr bar, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v13s25_99 # TPP. Show MC walking through the streets, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v13sa25_100 # TPP. Show MC sitting on bench, neutral expression, mouth closed
    with fade

    pause 0.75

    stop music fadeout 3

    jump v13s27
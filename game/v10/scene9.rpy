# SCENE 9: MC and Frat leave. MC back in room
# Locations: MC Apes/Wolves Room
# Characters: Ryan (Outfit 2), Sam (Outfit 2),MC (Outfit 7), Grayson (Outfit 3),Imre (Outfit 4), Sebastian (Outfit 1),Cameron (Outfit 3),Chris (Outfit 2)
# Time: Sunday Morning
label v10_leave_fight:
    play music "music/v10/Track Scene 9.mp3" fadein 2
    if joinwolves:
        scene v10sraf1 # TPP. MC sits down on bed in his room.
        with fade
        pause 0.5

        if v10_ryan_win: # RCS - MC is a Wolf and won the fight.
            scene v10sraf1a # TPP. Same camera as v10swaf1. Show MC sitting on the bed in his room. MC looks proud, mouth closed.
            with dissolve

            u "(What a fucking day! Definitely didn't expect any of this when I came to college. So many ups, so many downs. Crazy shit.)"

        else:
            scene v10sraf1b # TPP. Same camera as v10swaf1. Show MC sitting on the bed in his room. MC looks disappointed, mouth closed.
            with dissolve

            u "(Today really didn't go as planned... This is the worst fucking feeling.)"

        if v10_ryan_fight:
            scene v10sraf1c # TPP. Same camera as v10swaf1. Show MC sitting on bed in his room. MC reacts to someone knocking on his door.
            with dissolve

            play sound "sounds/knock.mp3"

            pause 0.5

            menu:
                "Act like you're asleep":
                    scene v10sraf1c
                    with dissolve

                    u "(Enough for today, I'm going to sleep.)"

                    scene v10sraf2 # TPP. Show MC sitting in bed. He gets in the bed, deciding to go to sleep.
                    with dissolve
                    pause 0.5
           
                "Answer the door":
                    scene v10sraf3 # FPP. Show the door in MC's Wolves room. MC is sitting on the bed.
                    with dissolve

                    u "Yeah?"

                    if v10_ryan_win: # RCS - MC is a Wolf and won the fight.
                        scene v10sraf3a # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre entering MC's room. They are all smiling.
                        with dissolve

                        pause 0.5
                    
                        scene v10sraf3b # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre. All smiling, Chris mouth open.
                        with dissolve

                        ch "If I ever have a son I'm naming him [name]! I'm so proud of you right now."

                        scene v10sraf3c # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre. All smiling, Sebastian mouth open.
                        with dissolve

                        se "Looks like guys really belong into the Wolves. Well done."

                        scene v10sraf3d # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre. All smiling, all mouths closed.
                        with dissolve

                        u "Imre either turned into a beast out there or his opponent was just trash."

                        scene v10sraf3e # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre. All smiling, Imre mouth open.
                        with dissolve

                        imre "*Laughs* That guy had no fucking chance, classic Apes. So much shit talk and no backing it up."

                        scene v10sraf3b
                        with dissolve

                        ch "Really well done guys, you're absolutely crushing it."

                        scene v10sraf3d
                        with dissolve

                        u "Thanks."

                        scene v10sraf3b
                        with dissolve

                        ch "Try to get some sleep, I'm sure it's the only privacy you're gonna have after a fight like that. *Chuckles*"

                        scene v10sraf3f # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre leaving MC's room.
                        with dissolve

                        u "(Damn, I'm really THAT guy now!)"

                        scene v10sraf2
                        with dissolve

                        pause 0.5
                
                    else: # RCS - MC is a Wolf and lost the fight
                        scene v10sraf3g
                        with dissolve
                        pause 0.5
                    
                        scene v10sraf3h
                        with dissolve

                        ch "I don't know if it's true, but one of the guys mentioned that you might have held back cause you were friends with your opponent. There are no friends in the ring, [name]."

                        scene v10sraf3i
                        with dissolve

                        se "Yeah, that shit's not okay. You can't get your ass kicked by an Ape."

                        scene v10sraf3j
                        with dissolve

                        u "I'm sorry guys. He was just better on the day."

                        scene v10sraf3h
                        with dissolve

                        ch "Try to get some sleep now, no use beating yourself up over it."

                        scene v10sraf3f
                        with dissolve
                        pause 0.5

                        scene v10sraf3f
                        with dissolve

                        u "(Damn, I really dropped the ball there...)"

                        scene v10sraf2
                        with fade

                        pause 0.5

    else: # RCS - MC is an Ape
        scene v10sraf4 # TPP. MC sits down on bed in his room. Apes.
        with fade
        
        pause 0.5

        if v10_imre_win: # RCS - MC is an Ape and won the fight
            scene v10sraf4a # TPP. Same camera as v10sraf4. Show MC sitting on the bed in his room. MC looks proud, mouth closed.
            with dissolve

            u "(What a fucking day! Definitely didn't expect any of this when I came to college. So many ups, so many downs. Crazy shit.)"

        else:
            scene v10sraf4b # TPP. Same camera as v10sraf4. Show MC sitting on the bed in his room. MC looks disappointed, mouth closed.
            with dissolve

            u "(Today really didn't go as planned... This is the worst fucking feeling.)"

        if v10_imre_win: # RCS - MC is an Ape and won the fight
            scene v10sraf4c # TPP. Same camera as v10sraf4. Show MC sitting on bed in his room. MC reacts to someone knocking on his door.
            with dissolve

            play sound "sounds/knock.mp3"

            pause 0.5

            menu:
                "Act like you're asleep":
                    scene v10sraf4c
                    with dissolve

                    u "(Enough for today, I'm going to sleep.)"

                    scene v10sraf5 # TPP. Show MC sitting in bed. He gets in the bed, deciding to go to sleep.
                    with fade
                    pause 0.5

                "Answer the door":
                    scene v10sraf6 # FPP. Show the door in MC's Apes room. MC is sitting on his bed.
                    with dissolve

                    u "Yeah?"
                    scene v10sraf6a # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan entering MC's room. They are all smiling.
                    with dissolve
                    pause 0.5

                    scene v10sraf6b # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan. All smiling, Grayson mouth open.
                    with dissolve

                    gr "Great job tonight [name], I fucking knew you were gonna destroy him."

                    scene v10sraf6c # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan. All smiling, Cameron mouth open.
                    with dissolve

                    ca "Actually turning into a fighter... not a horrible performance today."

                    scene v10sraf6d # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan. All smiling, all mouths closed.
                    with dissolve

                    u "Thanks guys. Ryan killed it too though."

                    scene v10sraf6e # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan. All smiling, Ryan mouth open.
                    with dissolve

                    ry "We both did, man. Apes all the way!"

                    scene v10sraf6b
                    with dissolve

                    gr "That's fucking right."

                    scene v10sraf6d
                    with dissolve

                    u "Haha, I appreciate the compliments, but I'm super exhausted, so I think I'm just gonna head to bed if that's alright."

                    scene v10sraf6b
                    with dissolve

                    gr "You've earned it."

                    scene v10sraf6f # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan leaving MC's room.
                    with dissolve

                    pause 0.5

        else:
            scene v10sraf5
            with fade

            pause 0.5

    stop music fadeout 3
    jump v10_sun_morn
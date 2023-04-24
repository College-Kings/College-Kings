# SCENE 39a: Pool With Ryan
# Locations: Area with Pool table
# Characters: RYAN (Outfit: 1), MC (Outfit: 5), EMILY (Outfit: 3), AUBREY (Outfit: 2)
# Time: Night

label v13s39a:
    scene v13s39a_1 # TPP. Show mc and ryan waking up to a pool table, slight smiles. mouths closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 39a.mp3" fadein 2

    scene v13s39a_2 # TPP. show mc racking the balls on the pool table
    with dissolve

    pause 0.75

    scene v13s39a_3 # FPP. show mc looking at ryan looking intensely at which pool stick to choose from, no expression, mouth closed
    with dissolve

    pause 0.75

    scene v13s39a_4 # FPP. show ryan looking at mc, holding a pool stick, slight smile mouth open
    with dissolve

    ry "Where were you guys just coming from?"

    scene v13s39a_4a # FPP. ryan mouth closed
    with dissolve

    u "We were at a little garden place."

    scene v13s39a_4
    with dissolve

    ry "Gayyyyyy! *Laughs* You went on a little date, huh?"

    scene v13s39a_4a
    with dissolve

    u "The girls were there too, so if chilling with girls is gay then I guess that's what I am. *Chuckles*"

    scene v13s39a_4
    with dissolve

    ry "Speaking of girls..."

    if v10s33_ryan_flirt_emily and emily_europe:
        scene v13s39a_4b # FPP same as v13s39a_4 ryan slightly looks away from mc, slightly shy
        with dissolve

        ry "I have a favor to ask."

        scene v13s39a_4a
        with dissolve

        u "Shoot."

        scene v13s39a_4
        with dissolve

        ry "I wanna go on a date with Emily, but I wanna ease into it with a double date."

        scene v13s39a_4a
        with dissolve

        u "So you're asking me to go on a double date with you and Emily?"

        scene v13s39a_4
        with dissolve

        ry "It sounds crazy when I say it out loud, but yeah, that's what I'm asking."

        scene v13s39a_4a
        with dissolve

        u "That would be the most awkward date, Ryan."

        if CharacterService.is_girlfriend(chloe):  
            scene v13s39a_5a # FPP. same as v13s39a_5 a dreamlike image of chloe is shown on the screen
            with dissolve

            u "I definitely wouldn't want to bring my girl."   

        elif CharacterService.is_girlfriend(lauren) and not v11_lauren_caught_aubrey: #second part of check only for compatibility purposes
            scene v13s39a_5 # FPP. a dreamlike image of lauren is shown on the screen
            with dissolve

            u "I definitely wouldn't want to bring my girl."
            
        scene v13s39a_4
        with dissolve

        ry "I was thinking you could bring Riley with you. She and Emily get along, and Riley would be the one most willing to go."

        scene v13s39a_4a
        with dissolve

        u "I don't know, man."

        scene v13s39a_4
        with dissolve

        ry "Answer me after the game."

        scene v13s39a_4a
        with dissolve

        u "Deal."

        scene v13s39a_6 # TPP. mc standing next to the table, ryan breaks the balls up, both slight smiles, mouths closed
        with dissolve

        pause 0.75

        scene v13s39a_7 # FPP. close up shot of the cue ball making contact and the balls are scattered
        with dissolve

        pause 0.75
    
        scene v13s39a_8 # FPP. close up shot of the 2 ball going into a pocket
        with dissolve

        pause 0.75

        scene v13s39a_6a # TPP. same as v13s39a_6 show ryan lining up a shot, mc stnding next to the table, the balls are scattered, only the 1, 3, 4, 5, 8, 9, 10, 11, and 15 balls are shown on the table
        with dissolve

        pause 0.75

        scene v13s39a_6b # TPP. same as v13s39a_6a show MC lining up a shot, ryan stnding next to the table, the balls are scattered, all balls are on the table except the 2 ball
        with dissolve

        pause 0.75

        scene v13s39a_6c # TPP. same as v13s39a_6b only the 3, 4, 8, 10, and 15 balls are shown on the table
        with dissolve

        pause 0.75

        scene v13s39a_6d # TPP. same as v13s39a_6c show only the 8, 15 ball, and the cue ball are shown on the table, mc lines up to shoot at the 15 ball
        with dissolve

        pause 0.75

        scene v13s39a_9 # FPP. show MC aiming at the cue ball to put the 15 ball to put it into a pocket, ryan standing on the other side of the table, slight smile, mouth closed
        with dissolve

        u "It's gonna be game over now."

        scene v13s39a_8a # FPP. same as v13s39a_8 close up shot of the 15 ball going into a pocket
        with dissolve

        pause 0.75

        scene v13s39a_9a # FPP. same as v13s39a_9 MC is looking at the cue ball in front of the 8 ball to put it into either a left pocket or right pocket, pool stick is not visible, ryan standing between the pockets
        with dissolve

        menu:
            "Shoot left pocket":
                scene v13s39a_9b # FPP. same as v13s39a_9a pool stick is now visible and mc is aiming the pool stick at the cue ball to put the 8 ball into the left pocket
                with dissolve

                u "Left pocket!"

                scene v13s39a_8b # FPP. same as v13s39a_8 close up shot of the 8 ball bouncing off the wall and not going in
                with dissolve

                u "Damn!"

                scene v13s39a_10 # FPP. mc is looking at ryan aiming at the cue ball to put the 8 ball into a right pocket
                with dissolve

                ry "Too bad! Right pocket. *Chuckles*"

                scene v13s39a_8c # FPP. same as v13s39a_8 close up shot of the 8 ball going into a pocket
                with dissolve

                ry "And, that's game!"

                scene v13s39a_4a # FPP. same as v13s39a_4a ryan has a full smile
                with dissolve

                u "You got lucky. *Chuckles*"

            "Shoot right pocket":
                scene v13s39a_9c  # FPP. same as v13s39a_9a pool stick is now visible and mc is aiming the pool stick at the cue ball to put the 8 ball into the right pocket
                with dissolve

                u "Right pocket!"

                scene v13s39a_8c
                with dissolve
                
                pause 1

                scene v13s39a_4d # FPP. same as v13s39a_4a ryan slight angry
                with dissolve

                u "Yessir!"

                scene v13s39a_4e # FPP. same as v13s39a_4d ryan mouth open
                with dissolve

                ry "You said you haven’t played in a long time, dickhead."

                scene v13s39a_4d
                with dissolve

                u "I haven’t."

                scene v13s39a_4
                with dissolve

                ry "Then I guess you just got lucky."

                scene v13s39a_4a
                with dissolve

                u "Or I'm just good. *Laughs*"

        scene v13s39a_4
        with dissolve

        ry "Sureee... *Chuckles*"

        scene v13s39a_4
        with dissolve

        ry "Alright, so what's your answer man? Willing to do the date?"

        scene v13s39a_4a
        with dissolve

        menu:
            "Sure":
                u "Sure man, I guess I don't see what's so bad about it."

                scene v13s39a_4c
                with dissolve

                ry "For real? You'll do it?"

                scene v13s39a_4a
                with dissolve

                u "Yeah, I don't see why not."

                scene v13s39a_4c
                with dissolve

                ry "Wow, that's not what I expected. Thanks dude, really."

                scene v13s39a_4a
                with dissolve

                u "Yeah, for sure."

            "Sorry, but no":
                scene v13s39a_4f # FPP. same as v13s39a_4a ryan is slightly sad
                with dissolve
                
                u "Sorry man, but no. I'm not trying to throw myself in the fire like that."

                scene v13s39a_4g # FPP. same as v13s39a_4f ryans mouth is open
                with dissolve

                ry "Yeah I get it. That's kinda what I expected but I had to ask."

                scene v13s39a_4f
                with dissolve

                u "I'm sorry."

                scene v13s39a_4
                with dissolve

                ry "It's all good."

        scene v13s39a_11 # FPP. Mc sees emily and aubrey playing pool at another table, emily and aubrey looking at each other, slight smiles, emily mouth open
        with dissolve

        u "(Speak of the devil.)"

        scene v13s39a_11a # FPP. same as v13s39a_11 emily and aubrey look at mc, emily waves at mc
        with dissolve

        u "(What the fuck? I thought she was trying to avoid me.)"

        scene v13s39a_11a
        with dissolve

        menu:
            "Stare":
                scene v13s39a_11a
                with dissolve

                u "(I don't really know what to do...)"

                scene v13s39a_11b # FPP. same as v13s39a_11a emily stops waving and rolls her eyes and goes back to playing her game
                with dissolve

                u "(Okay...)"

            "Look away":
                scene v13s39a_4h # FPP. same as v13s39a_4a ryan looks concerned, emily and aubrey visible in the background, emily and aubrey looking at each other, slight smiles, mouths closed
                with dissolve
                
                u "(Just ignore her, [name].)"

        scene v13s39a_4i # FPP. same as v13s39a_4h mouth open
        with dissolve

        ry "You good?"

        scene v13s39a_4h
        with dissolve

        u "Yeah man, I'm good."

        scene v13s39a_4i
        with dissolve

        ry "Oh, okay... You just looked distracted."

        scene v13s39a_4j # FPP. ryan looks at emily, full smile, mouth open
        with dissolve

        ry "OH SHIT, THERE'S EMILY!"

        scene v13s39a_4k # FPP. same as v13s39a_4j ryan looks at mc
        with dissolve

        ry "Later, [name]."

        scene v13s39a_4l # FPP. same as v13s39a_4j ryan goes to emily
        with dissolve

        u "Wow..."

        stop music fadeout 3

        if cuffs in mc.inventory:
            jump v13s40
        else: 
            jump v13s41

    else:
        scene v13s39a_4c
        with dissolve

        ry "I have some news."

        scene v13s39a_4a
        with dissolve

        u "Spill the tea."

        scene v13s39a_4c
        with dissolve

        ry "I'm getting a new car."

        scene v13s39a_4a
        with dissolve

        u "Oh really? What are you getting?"

        scene v13s39a_4c
        with dissolve

        ry "A RoadStar, it's my dad's. My grandfather gave it to him and now he's giving it to me."

        scene v13s39a_4a
        with dissolve

        u "So, it's an old car?"

        scene v13s39a_4c
        with dissolve

        ry "Not old, antique. Plus, it's been remodeled so much that it can't measure up to any modern day sports car."

        scene v13s39a_4a
        with dissolve

        u "Wow, that’s exciting man."

        scene v13s39a_4a
        with dissolve

        menu:
            "Not a sports car fan":
                scene v13s39a_4a
                with dissolve

                u "But, I'm not really a sports car fan."

                scene v13s39a_4c
                with dissolve

                ry "That's your loss."

                scene v13s39a_4a
                with dissolve

                u "*Chuckles*"

            "I love sports cars":
                scene v13s39a_4a
                with dissolve

                u "Can't go wrong with a good sports car."

                scene v13s39a_4c
                with dissolve

                ry "I see you have good taste?"

                scene v13s39a_4a
                with dissolve

                u "*Chuckles*"

        scene v13s39a_4e
        with dissolve

        ry "Man... It looks like Nora and Chris are gonna be back on the market here soon."

        scene v13s39a_4f
        with dissolve

        u "Maybe, maybe not. Why do you bring it up? Trying to take Chris to dinner? *Chuckles*"

        scene v13s39a_4
        with dissolve

        ry "Ahh... Good jab."

        scene v13s39a_4a
        with dissolve

        u "Thank you, I'm here all night. *Laughs*"

        scene v13s39a_4
        with dissolve

        ry "*Chuckles* But no, seriously? It's just crazy. I never expected all that from them two."

        scene v13s39a_4a
        with dissolve

        u "It is a huge surprise, to everyone I think."

        scene v13s39a_4
        with dissolve

        ry "What's really gonna be a surprise is when I beat you during this game. *Chuckles*"

        scene v13s39a_4a
        with dissolve

        u "Haha, good luck!"

        scene v13s39a_6
        with dissolve

        pause 0.75

        scene v13s39a_7
        with dissolve

        pause 0.75
    
        scene v13s39a_8
        with dissolve

        pause 0.75

        scene v13s39a_6a
        with dissolve

        pause 0.75

        scene v13s39a_6b
        with dissolve

        pause 0.75

        scene v13s39a_6c
        with dissolve

        pause 0.75

        scene v13s39a_6d
        with dissolve

        pause 0.75

        scene v13s39a_9
        with dissolve

        u "It's gonna be game over now."

        scene v13s39a_8a
        with dissolve

        pause 0.75

        scene v13s39a_9a
        with dissolve

        menu:
            "Shoot left pocket":
                scene v13s39a_9b
                with dissolve

                u "Left pocket!"

                scene v13s39a_8b
                with dissolve

                u "Damn!"

                scene v13s39a_10
                with dissolve

                ry "Too bad! Right pocket. *Chuckles*"

                scene v13s39a_8c
                with dissolve

                ry "And, that's game!"

                scene v13s39a_4a
                with dissolve

                u "You got lucky. *Chuckles*"

            "Shoot right pocket":
                scene v13s39a_9c
                with dissolve

                u "Right pocket!"

                scene v13s39a_4d
                with dissolve

                u "Yessir!"

                scene v13s39a_4e
                with dissolve

                ry "You said you haven’t played in a long time, dickhead."

                scene v13s39a_4d
                with dissolve

                u "I haven’t."

                scene v13s39a_4
                with dissolve

                ry "Then I guess you just got lucky."

                scene v13s39a_4a
                with dissolve

                u "Or I'm just good. *Laughs*"

        scene v13s39a_4
        with dissolve

        ry "Sureee... *Chuckles*"

        scene v13s39a_4m # FPP. same as v13s39a_4c ryan pulls out his phone and looks at it with a smile
        with dissolve

        ry "Emily's calling, gotta go."

        scene v13s39a_4n # FPP. same as v13s39a_4m Ryan puts the phone to his ear and walks off
        with dissolve

        ry "Hello?"

        u "Wow..."

        stop music fadeout 3

        if cuffs in mc.inventory:
            jump v13s40

        else: 
            jump v13s41
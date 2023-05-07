# SCENE 10: Talk with Amber on the Bus
# Locations: Bus
# Characters: AMBER (Outfit: 1), MC (Outfit: 1), MS. ROSE (Outfit: 1), IMRE (Outfit: 2)
# Time: Evening (Night when specified)
# Phone Images: None

label v12_amber_bus:
    scene v12amb1 # TPP. Show MC and Amber boarding the bus, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    play music "music/v12/Track Scene 10.mp3" fadein 2

    scene v12amb2 # TPP. Show Amber taking a seat (she's on the window seat), MC still standing next to his seat (he will sit next to her), both slight smiles, mouths closed (Ms. Rose sitting on the other aisle with Imre, they're not in shot)
    with dissolve

    pause 0.75

    scene v12amb2a # TPP. Same as v12amb2, Amber sitting down, MC sitting down too, mouths closed, both slightly smiling
    with dissolve

    pause 0.75

    scene v12amb3 # FPP. MC and Amber sitting down, looking at each other, Amber slightly worried, mouth open
    with dissolve

    am "So, earlier I ugh... nah, nevermind."

    scene v12amb3a # FPP. Same as v12amb3, Amber mouth closed, slightly worried
    with dissolve

    u "Well, you can't just not tell me now. I know you wanted to talk about something and now I'm assuming it's important. What's up?"

    scene v12amb3
    with dissolve

    am "I'll just keep it to myself."

    scene v12amb3a
    with dissolve

    menu:
        "Tease her":
            $ v11_tease_amber += 1
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v12amb3b # FPP. Same as v12amb3, Amber slight smile, mouth closed, different pose
            with dissolve

            u "Hmmm, what could I do that would irritate you so much that you caved in and just told me what's going on?"

            scene v12amb3c # FPP. Same as v12amb3b, Amber slight smile, mouth open
            with dissolve

            am "Whatever you did it probably wouldn't get me to say anything, but get you beat up instead. *Chuckles*"

            scene v12amb3b
            with dissolve

            u "I may be willing to take that risk."

        "Convince her":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12amb3b
            with dissolve

            u "Maybe it's worth just getting it off your chest. Unless you'd rather go back and talk to one of your skateboards instead."

            scene v12amb3c
            with dissolve

            am "There's not much of a difference between you and the board. *Chuckles*"

            scene v12amb3b
            with dissolve

            u "How's that?"

            scene v12amb3c
            with dissolve

            am "You figure that one out."

            scene v12amb3d # FPP. Same as v12amb3b, different pose
            with dissolve

            u "I'm so confused. *Chuckles*"

            scene v12amb3e # FPP. Same as v12amb3d, Amber mouth open, slight smile
            with dissolve

            am "And the board would be too."

            scene v12amb3d
            with dissolve

            u "*Laughs*"

    scene v12amb3e
    with dissolve

    am "Since you want to know so bad I guess I'll tell you. I do feel like I need to get it off my chest and I guess you're not the worst person to talk to. *Chuckles*"

    scene v12amb3d
    with dissolve

    u "Thanks. *Chuckles*"

    scene v12amb3
    with dissolve

    am "So ugh, I'm sure you've noticed Riley and I hanging out a lot."

    scene v12amb3b
    with dissolve

    u "Yeah, like a lot a lot."

    scene v12amb3c
    with dissolve

    am "Yeah, it's been nice hanging out and getting to know her better. She's amazing."

    scene v12amb3b
    with dissolve

    u "Yep, I'm not seeing the problem yet."

    scene v12amb3e
    with dissolve

    am "Well, she thinks I'm amazing too."

    scene v12amb3d
    with dissolve

    u "*Cough* Suck up."

    scene v12amb3c
    with dissolve

    am "*Chuckles* But it's not just that, we were hanging out there the other day and she said she wanted to like try stuff with me."

    scene v12amb3f # FPP. Same as v12amb3a, different pose
    with dissolve

    u "Sounds like you'd be into that, no?"

    scene v12amb3g # FPP. Same as v12amb3f, Amber slightly worried, mouth open
    with dissolve

    am "Normally I would be, but I think she's looking for a lot more lovey dovey exploration and a lot less fun messing around kind of stuff."

    scene v12amb3f
    with dissolve

    u "Oh, now I'm getting it. You don't wanna be her teacher."

    scene v12amb3g
    with dissolve

    am "It's not just that, I just feel like this is really serious for her and she wants to experiment with other girls and she's all fragile and shit."
    
    am "I just wanna have fun. I just don't think we're a good match, you know? On the ferry we talked about it a little bit, but got interrupted by Mr. Lee."
    am "So I didn't really get to fully explain and I think she may be upset."

    scene v12amb3a
    with dissolve

    u "Riley's not really the hold a grudge and hate you forever type."

    scene v12amb3
    with dissolve

    am "I'm hoping so, cause I'd still like to be cool with her, but just as friends foolin' around like we have been, none of that serious stuff."

    scene v12amb3a
    with dissolve

    u "When are you planning to sit and explain things to her?"

    scene v12amb3g
    with dissolve

    am "I don't know if I am, I may just leave it as it is."

    scene v12amb3f
    with dissolve

    menu:
        "Stay out of it":
            u "It's all your decision, I don't wanna sway you either way. It's gotta be your choice."

            scene v12amb3g
            with dissolve

            am "*Sighs* I appreciate that, but I think part of me was hoping to be pushed one way or the other."

            scene v12amb3b
            with dissolve

            u "At the end of the day you're gonna do what you want though no matter what I say right?"

            scene v12amb3c
            with dissolve

            am "*Chuckles* Yeah that's true."

            scene v12amb3b
            with dissolve

            u "Exactly."

        "Say something":
            $ reputation.add_point(RepComponent.BRO)

            u "You should just get it over with and tell her what's up."

            scene v12amb3g
            with dissolve

            am "And if she doesn't respond well or I hurt her feelings?"

            scene v12amb3a
            with dissolve

            u "Then at least you were honest with her, and with yourself."

            scene v12amb3
            with dissolve

            am "..."

            scene v12amb3b
            with dissolve

            u "What? *Chuckles*"

    scene v12amb3c
    with dissolve

    am "You think you know me pretty well huh?"

    scene v12amb3d
    with dissolve

    u "Yeah, your personality is written on your forehead. *Chuckles*"

    scene v12amb3e
    with dissolve

    am "If that was the case, how would you know anything about me? You can't read."

    scene v12amb3d
    with dissolve

    u "See, my point exactly. *Laughs* You always show your true self."

    scene v12amb3c
    with dissolve

    am "Never a reason not to."

    scene v12amb3b
    with dissolve

    u "This is kinda weird, I gotta be honest."

    scene v12amb3c
    with dissolve

    am "What?"

    scene v12amb3h # FPP. Same as v12amb3d, different pose
    with dissolve

    u "Having a heart to heart conversation with you, I just never would've expected that."

    scene v12amb3i # FPP. Same as v12amb3h, Amber mouth open, slight smile
    with dissolve

    am "Don't get used to it, this was a special occasion."

    scene v12amb3h
    with dissolve

    u "And you think you're safe from any more special occasions?"

    scene v12amb3i
    with dissolve

    am "Maybe not, but I'll be a bit more vigilant from now on."

    scene v12amb3d
    with dissolve

    u "Woah, big words. Was that your word of the day or something? *Chuckles*"

    scene v12amb3e
    with dissolve

    am "Vigilant is not a big word, you just have a fifth grade education."

    scene v12amb3h
    with dissolve

    u "Spell it, smartass."

    scene v12amb3c
    with dissolve

    am "Why? I obviously know the word and know how to use it, so why do I need to spell it?"

    scene v12amb3b
    with dissolve

    u "Since you wanna talk shit go ahead and spell the word."

    scene v12amb3i
    with dissolve

    am "What makes you think I can't?"

    scene v12amb3h
    with dissolve

    u "Cause you pronounce it funny as hell."

    scene v12amb3i
    with dissolve

    am "Fine, it's V-I-G-I-L-I-N-T, vigilant."

    scene v12amb3d
    with dissolve

    u "*Laughs*"

    scene v12amb3e
    with dissolve

    am "What's so funny? I spelt it right."

    scene v12amb3d
    with dissolve

    u "No you didn't. *Laughs* It's \"lant\" not \"lint\". You kept saying lint so I knew you'd spell it wrong. *Laughs*"

    scene v12amb3i
    with dissolve

    am "There's no way!"

    scene v12amb3h
    with dissolve

    u "So what, superheroes are \"vigilinties\"? *Laughs*"

    scene v12amb3j # FPP. Same as v12amb3, Amber leaning forwards, looking across the aisle to Ms. Rose, Amber neutral expression, mouth open
    with dissolve

    am "How do you spell vigilant?"

    scene v12amb4 # FPP. MC looking at Ms. Rose, Ms. Rose sitting on across from MC, show Imre leaning forward, both of them smiling, Ms. Rose mouth open, Imre mouth closed, both of them looking at Amber's direction
    with dissolve

    ro "Sound it out."

    scene v12amb4a # FPP. Same as v12amb4, Ms. Rose mouth closed, Imre mouth open, both smiling
    with dissolve

    imre "*Laughs*"

    scene v12amb3k # FPP. Same as v12amb3j, Amber looking at Imre's direction, Amber slightly annoyed, mouth open
    with dissolve

    am "Shut up."

    scene v12amb4a
    with dissolve

    imre "She said \"sound it out\" like you were in elementary school."

    scene v12amb3k
    with dissolve

    am "Okay fine, maybe I am wrong, it's not my fault people around me don't know how to talk."

    scene v12amb3l # FPP. Same as v12amb3k, Amber looking at MC, Amber slightly annoyed, mouth closed
    with dissolve

    u "Don't pass the blame, cause \"you have a fifth grade education\"."

    play sound sound.hit
    scene v12amb3m # FPP. Same as v12amb3i, Amber slightly annoyed, mouth closed, punching MC in the arm
    with vpunch

    u "Ow!"

    scene v12amb3n # FPP. Same as v12amb3m, Amber not punching MC anymore, Amber slightly annoyed, mouth open
    with dissolve

    am "Anymore jokes and I'll hit you harder than Grayson did."

    scene v12amb4a
    with dissolve

    imre "*Laughs*"

    scene v12amb3h
    with dissolve

    u "Not cool."

    scene v12amb3i
    with dissolve

    am "Yeah, not so funny anymore huh? *Chuckles*"

    scene v12amb3d
    with dissolve

    u "Yeah, whatever."

    scene v12amb2b # TPP. Same as v12amb2a, Show MC and Amber sitting in their seats, Amber looking out the window, MC looking forward, both neutral expressions, mouths closed
    with dissolve

    pause 0.75

    scene v12amb2c # TPP. Same as v12amb2b, Show Amber looking at her phone, MC looking out the window, both neutral expressions, mouths closed
    with fade

    pause 0.75

    scene v12amb3i
    with fade

    am "Thanks for being a good friend, [name]."

    scene v12amb3h
    with dissolve

    u "You too."

    scene v12amb3
    with dissolve

    am "I think I'm gonna talk to her and just be straight up about it."

    scene v12amb3a
    with dissolve

    u "That's probably best."

    scene v12amb3
    with dissolve

    am "Hopefully her and I are still cool."

    scene v12amb3a
    with dissolve

    u "I'm sure it'll be fine."

    scene v12amb3o # FPP. Same as v12amb3, MC and Amber sitting down in the bus, Amber laying her head on MC's shoulder, looking slightly at MC, Amber mouth closed, slight smile
    with dissolve

    u "*Chuckles* Worse than a toddler."

    scene v12amb3p # FPP. Same as v12amb30, Amber mouth open, slight smile
    with dissolve

    am "Hush and be a good pillow."

    scene v12amb2d # TPP. Same as v12amb2c, Amber laying her head on MC's shoulder sleeping, MC sleeping too, both mouths closed (Night time here)
    with dissolve

    pause 1.25

    scene v12amb2e # TPP. Same as v12amb2d, Show MC and Amber yawning as they wake up (Night time here)
    with fade

    pause 1

    scene v12amb2f # TPP. Show MC and Amber getting off the bus (Camera inside bus, MC and Amber have their backs to the camera, night time here)
    with fade

    pause 1

    stop music fadeout 3

    jump v12_paris_hotel #scene 11
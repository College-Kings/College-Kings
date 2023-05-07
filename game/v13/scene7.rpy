# SCENE 7: The Ticket Transfer
# Locations: Hotel
# Characters: MR. LEE (Outfit: 1), MC (Outfit: 2), PENELOPE (Outfit: 1), AUBREY (Outfit: 2)
# Time: Morning 

label v13_ticket_transfer:
    play music "music/v13/Track Scene 7.mp3" fadein 2

    if v12_murder_count >= 5: # -If 5+ kills
        scene v13s7_1 # TPP Show MC in lobby, looking around and wondering what to do next
        with dissolve

        lee "[name], my boy!"

        scene v13s7_2 # FPP Show Mr. Lee walking toward MC, smiling with mouth open
        with dissolve

        u "Yes?"

        scene v13s7_2a # FPP Same angle as v13s7_2, Mr. Lee closer now, smiling with mouth open
        with dissolve

        lee "A lot has been going on lately. With the trip, things back on campus, and with students who I wish required less attention so that I could focus on students I'd much rather focus on... Like you."

        scene v13s7_2b # FPP Same angle as v13s7_2, Mr. Lee closer now, smiling with mouth closed
        with dissolve

        u "Me? *Chuckles* Why me?"

        scene v13s7_2a
        with dissolve

        lee "It's not everyday you find a skilled murderer amongst your students."

        scene v13s7_2b
        with dissolve

        u "Oh, that... *Laughs*"

        scene v13s7_2a
        with dissolve

        lee "Give yourself more credit than you have! You accomplished something that is not so easily accomplished."

        scene v13s7_2b
        with dissolve

        u "Well... Thank you."

        scene v13s7_2c # FPP Same angle as v13s7_2, Mr. Lee closer now with a curious expression, mouth open
        with dissolve

        lee "Of course. Hmm, I'm curious... Are you familiar with the story of Genghis Khan?"

        scene v13s7_2b
        with dissolve

        u "Somewhat..."

        scene v13s7_2a
        with dissolve

        lee "Well, in my opinion, you and him share many similar characteristics. Many of which you demonstrated on the ferry."

        scene v13s7_2b
        with dissolve

        u "Okay... I don't get it."

        scene v13s7_2c
        with dissolve

        lee "Let me explain my thoughts."

        scene v13s7_2a
        with dissolve

        lee "Genghis, though considered by some to be a barbarian, had patience, a father's perception skill, and sheer brilliance in enacting his plans. That was you!"

        scene v13s7_2d # FPP Same angle as v13s7_2, Mr. Lee closer now with his eyebrow raised, mouth open
        with dissolve
        lee "I'm not familiar with your love life, but it's also known that he had thousands of women which he called his wives."

        scene v13s7_2b
        with dissolve

        u "(Ha, I think I like being compared to this guy.)"

        scene v13s7_2a
        with dissolve

        lee "All in all, Genghis set in motion his plans and then reaped what he sowed. So, I felt it was appropriate that you do as well."

        scene v13s7_3 # TPP Show Mr. Lee standing in front of MC, Lee handing MC a pair of tickets
        with dissolve

        pause 0.75

        scene v13s7_4 # FPP MC looking down at tickets in his hand
        with dissolve

        u "What's this?"

        scene v13s7_2a
        with dissolve

        lee "They are tickets to a nearby concert. I felt someone your age would enjoy them."

        scene v13s7_2b
        with dissolve

        u "Wow, thanks. I'm surprised you got me these, haha."

        scene v13s7_2a
        with dissolve

        lee "Frankly, it wasn't what I had originally gotten for you."

        scene v13s7_2b
        with dissolve

        u "(He probably got some old history thing the first time.)"

        scene v13s7_2d
        with dissolve

        lee "I had gotten you an old medallion that was significant to the real world event, but it appears it's been misplaced or worse... stolen."

        scene v13s7_2b
        with dissolve

        u "(Yep, an old history thing.)"

        u "*Chuckles* This was really nice of you, Mr. Lee. You didn't have to do this. I'm pretty sure these were expensive..."

        scene v13s7_2e # FPP Same angle as v13s7_2, Mr. Lee closer now, laughing
        with dissolve

        lee "*Laughs* Have you ever heard me complain about money?"

        scene v13s7_2b
        with dissolve

        u "Well... No."

        scene v13s7_2f # FPP Same angle as v13s7_2, Mr. Lee closer now, winking with mouth open
        with dissolve

        lee "And you never will. Money isn't ever an issue."

        scene v13s7_2a
        with dissolve

        lee "Now, have a good time at the concert."

        scene v13s7_2g # FPP Same angle as v13s7_2, Mr. Lee walking away
        with dissolve

        u "*Laughs* (Did he just lowkey flex on me and then walk off? Haha, he gave me two concert tickets as well...)"

        # NEED NUMBER FOR ALL KILLS - REPLACE IN NEXT TWO CHECKS
        if (v12_murder_count >= 10 and v12_murder_count < v12s7_victims): # -if 10+ kills but not all
            scene v13s7_4
            with dissolve

            u "(And these have backstage passes! Holy shit, he really went all out.)"

        elif v12_murder_count == v12s7_victims: # -if all kills
            scene v13s7_4
            with dissolve

            u "(Wait what?! Including backstage passes and after party access?! Holy shit, Mr. Lee... Definitely a flex, but I'll take it, nonetheless.) *Chuckles*"

        scene v13s7_4a # FPP Same angle as v13s7_4, MC now holding a ticket in each hand
        with dissolve

        u "(Who should I take with me?)"

        scene v13s7_5 # FPP Show Aubrey sitting in the lobby
        with dissolve

        pause 0.75

        if v11_pen_goes_europe: # -If Penelope is in Europe

            scene v13s7_6 # FPP Show Penelope walking into the lobby
            with dissolve

            pause 0.75

            scene v13s7_7 # FPP Show a split-screen view of Aubrey and Penelope
            with dissolve

            menu:
                "Aubrey":
                    $ aubrey.points += 1

                "Penelope":
                    $ penelope.points += 1
                    $ v13_penelope_concert = True

                    scene v13s7_6
                    with dissolve

                    u "(She deserves a break.)"

                    scene v13s7_8 # TPP Show MC walking up to Penelope, who is smiling at him
                    with dissolve

                    pause 0.75

                    scene v13s7_99 # FPP Show Penelope looking at MC, smiling with mouth closed
                    with dissolve

                    u "Hey, so the weirdest thing just happened, haha..."

                    scene v13s7_8a # FPP Same angle as v13s7_8, Penelope smiling with mouth open
                    with dissolve

                    pe "Uh, oh..."

                    scene v13s7_8
                    with dissolve

                    u "No, nothing bad! *Laughs* For some reason I really impressed Mr. Lee with the murder thing on the ferry, and he gave me these two tickets as a reward."

                    scene v13s7_8a
                    with dissolve

                    pe "Oh, wow! A concert in Amsterdam... That's so cool, [name], congrats."

                    scene v13s7_8
                    with dissolve

                    u "Well, thanks. *Chuckles* But look, I know they've been keeping you busy, but I was hoping you could go with me."

                    scene v13s7_8a
                    with dissolve

                    pe "You want me to go? Over everyone else?"

                    scene v13s7_8
                    with dissolve

                    u "You deserve to have a good night out."

                    scene v13s7_8a
                    with dissolve

                    pe "Things must be looking up for me because Ms. Rose just said the same thing..."

                    pe "Her and Mr. Lee agreed to give me a night out whenever I wanted while we're in Amsterdam. So yes, I'll definitely go! Thank you so much for asking me, [name]."

                    scene v13s7_8
                    with dissolve

                    u "Of course. I can't wait for this."

                    if CharacterService.is_dating(penelope):
                        scene v13s7_9 # TPP Show Penelope kissing MC
                        with dissolve

                        play sound sound.kiss
                        pause 1.5

                        scene v13s7_9a # TPP Same angle as v13s7_9, Penelope leaning back after kissing MC, Penelope smiling with mouth open
                        with dissolve

                        pe "My serial killer hero."

                        scene v13s7_8
                        with dissolve

                        u "*Chuckles*"

                    scene v13s7_8a
                    with dissolve

                    pe "Well, I don't want them changing their mind after thinking I'm fooling around so, I'll see you later."

                    scene v13s7_8
                    with dissolve

                    u "Haha, okay Miss Rule Follower. Go get the job done!"

                    scene v13s7_8a
                    with dissolve

                    pe "Haha."

                    scene v13s7_8b # FPP Same angle as v13s7_8, Penelope walking away
                    with dissolve

                    pause 0.75

                    jump v13s7_end_scene

        # -There is no choice and Aubrey is forced if Penelope isn't there-
        $ v13_aubrey_concert = True

        scene v13s7_10 # TPP Show MC walking over to Aubrey, who is looking up at him from her seat, mouth open
        with dissolve

        au "Surprised to see you up this early... Are you sick or something?"

        scene v13s7_11 # FPP Show Aubrey sitting in front of MC, smiling with mouth closed
        with dissolve

        u "I could say the same to you. *Chuckles* I got up for food, you?"

        scene v13s7_11ax # FPP Same angle as v13s7_11, Aubrey smiling with mouth open
        with dissolve

        au "I slept really well on the bus so I wasn't super sleepy when we arrived. Eventually I just got out of bed and I went to the spa and everything. Luuk actually just let me in."

        scene v13s7_11
        with dissolve

        u "Oh, you met Luuk?"

        scene v13s7_11ax
        with dissolve

        au "Yeah, he's nice, isn't he?"

        scene v13s7_11
        with dissolve

        u "Definitely a character. *Laughs*"

        scene v13s7_11ax
        with dissolve

        au "So, what's up? I saw you talking to Mr. Lee."

        scene v13s7_11
        with dissolve

        u "Yeah, so uhh... He did a bit of flexing and gave me these concert tickets as a little reward for the murder mystery."

        scene v13s7_11b # FPP Same angle as v13s7_11, Aubrey looking shocked with mouth open
        with dissolve

        au "Don't tell me these are the tickets I think they are..."

        scene v13s7_12 # FPP Aubrey, now standing, looking at tickets in MC's hand, Aubrey looks shocked with mouth open
        with dissolve

        au "Oh my fucking god! I wanted to go to this concert but they said it was sold out when I looked online!"

        scene v13s7_12a # FPP Same angle as v13s7_12, Aubrey looking at MC, smiling with mouth closed
        with dissolve

        u "Guess I don't have to ask if you'd wanna go? *Chuckles*"

        scene v13s7_12b # FPP Same angle as v13s7_12, Aubrey looking at MC with a big, excited smile, mouth open
        with dissolve

        au "Of course I wanna go! Thank you so so so much for even thinking of me..."

        scene v13s7_12
        with dissolve

        au "I can't believe this... How'd even you know I'd be into this?"

        scene v13s7_12a
        with dissolve

        u "I try my best to pay attention to your interests, you know."

        scene v13s7_12b
        with dissolve

        au "That's pretty nice of you. *Chuckles* I'm gonna go and practice her songs, I can never remember the lyrics."

        scene v13s7_13 # FPP Show Aubrey running off out of lobby
        with dissolve

        u "*Chuckles*"

    elif (v12_murder_count < 5 and v11_pen_goes_europe): # -If less than 5 kills and Penelope is there
        $ v13_penelope_concert = True

        scene v13s7_6a # FPP Same angle as v13s7_6, Penelope smiling at MC from across the lobby, mouth open
        with dissolve

        pe "There you are!"

        scene v13s7_14 # TPP Show Penelope running up to MC
        with dissolve

        pause 0.75

        scene v13s7_8
        with dissolve

        u "What's wrong?"

        scene v13s7_8a
        with dissolve

        pe "Nothing, I've just been looking for you."

        scene v13s7_8
        with dissolve

        u "Because...?"

        scene v13s7_8c # FPP Same angle as v13s7_8, Penelope holding out a pair of tickets, smiling with mouth open
        with dissolve

        pe "Because of these."

        scene v13s7_4
        with dissolve

        u "What are these?"

        scene v13s7_8a
        with dissolve

        pe "Concert tickets."

        pe "Mr. Lee and Ms. Rose gave these to me as a little reward for doing a lot for them while we've been on the trip, and said I could take whoever I wanted."

        scene v13s7_8d # FPP Same angle as v13s7_8, Penelope laughing
        with dissolve

        pe "I think they were the \"reward\" that you were supposed to get for doing really well during the murder mystery, but since you didn't do really well... *Chuckles* They gave them to me."

        scene v13s7_8
        with dissolve

        u "Haha, then why are you asking me to go instead of someone else?"

        scene v13s7_8a
        with dissolve

        pe "Because you're who I wanna go with, and they didn't make it a rule that I couldn't take you so..."

        scene v13s7_8
        with dissolve

        u "Haha, well I definitely wanna go with you."

        scene v13s7_8a
        with dissolve

        pe "GREAT! I was so worried you wouldn't want to, haha! You keep the tickets, 'cause I will most definitely lose them."

        scene v13s7_8
        with dissolve

        u "Haha, I can do that. Thanks for inviting me by the way."

        if CharacterService.is_dating(penelope):
            scene v13s7_8a
            with dissolve

            pe "Of course! You're the only person I'd want to spend the entire night with. *Chuckles*"

            scene v13s7_8e # FPP Same angle as v13s7_8, MC tucking a piece of Penelope's hair behind her ear, Penelope is smiling and blushing with mouth closed
            with dissolve

            u "Good, that feeling is mutual."

            scene v13s7_8a
            with dissolve

            pe "Well, I gotta get back to work before they think I'm slacking and try to take those back. Bye, [name]."

        else:
            scene v13s7_8a
            with dissolve

            pe "Of course, I gotta get back to work before they think I'm slacking and try to take those back. Bye, [name]."

        scene v13s7_8
        with dissolve

        u "Of course, haha. Later."

        scene v13s7_8b
        with dissolve

        u "Wow! This is gonna be sick..."

        scene v13s7_15 # TPP Show Luuk standing next to MC, both looking at Penelope walk away, Luuk's mouth open
        with dissolve

        luuk "She's a cute one."

        scene v13s7_16 # FPP MC looking at Luuk, who is looking at Penelope, his mouth open
        with dissolve

        u "What? *Chuckles*"

        scene v13s7_16a # FPP Same angle as v13s7_16, Luuk looking at MC, mouth open
        with dissolve

        luuk "Relax, I never combine work and play."

        scene v13s7_16
        with dissolve

        u "(Bold guy...)"

    label v13s7_end_scene:
        stop music fadeout 3
        jump v13s8
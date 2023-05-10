# SCENE 27: MC Hotel Bar talk with barkeeper
# Location: Bar, Hotel Corridor Outside Room
# Characters: MC (Outfit 1), Bartender (Outfit 1)
# Time: Night

label v11_bartender_hotel_chat:
    scene v11hbc1 # FPP. MC is sitting at the bar, looking at the bartender, the bartender is slightly smiling, mouth open
    with dissolve
    play music music.ck1.v11.Track_Scene_5_6 fadein 2
    bartender "You're the most company I've had all year long... most people go to an actual bar."

    scene v11hbc1a # FPP. Same as v11hbc1, Bartender slightly smiling, mouth closed
    with dissolve

    u "Why leave when the same stuff is right here?"

    scene v11hbc1
    with dissolve

    bartender "*Chuckles* That's what I've been saying for years."

    scene v11hbc1a
    with dissolve

    u "Years? You say that like you're old. You can't be far off from my age."

    scene v11hbc1
    with dissolve

    bartender "Well thank you, but all the credit goes to good genes. I'm in my thirties."

    scene v11hbc1a
    with dissolve

    u "Wow, you look great."

    scene v11hbc1b # FPP. Same as v11hbc1a, Bartender looks suspicious, raising one of their eyebrows. mouth closed
    with dissolve

    u "Ugh, I meant good as in like... you look a lot younger than in your thirties."

    scene v11hbc1c # FPP. Same as v11hbc1, the bartender is now leaning on the bar, slight seductive look, mouth closed
    with dissolve

    pause 0.75

    scene v11hbc1d # FPP. Same as v11hbc1c, bartender leaned over, slight seductive look, mouth open
    with dissolve

    bartender "You're not so bad looking either. What's your name?"

    scene v11hbc1c
    with dissolve

    u "My name is [name]."

    scene v11hbc1d
    with dissolve

    bartender "I like that, it's cute. You're kinda cute too."

    scene v11hbc1c
    with dissolve

    u "Oh, uhm... thank you."

    scene v11hbc1d
    with dissolve

    bartender "Do you have a girlfriend?"

    scene v11hbc1c
    with dissolve

    menu:
        "Yeah":
            scene v11hbc1a
            with dissolve

            u "Yeah I do."

            scene v11hbc1
            with dissolve

            bartender "Oh too bad."

            scene v11hbc1a
            with dissolve

            u "Why is that bad?"

            scene v11hbc1
            with dissolve

            bartender "*Chuckles* Means I won't be making any young lady upset."

            scene v11hbc1a
            with dissolve

            u "Haha."

            scene v11hbc1
            with dissolve

            bartender "I've seen a lot of cute girls with you on the trip, I'm sure you think they're really pretty too. So, what about me?"

            scene v11hbc1a
            with dissolve
            
            menu:
                "Yes":
                    scene v11hbc1e # FPP. Same as v11hbc1, Bartender behind the bar, back turned to MC, she's bending down to grab a bottle, focus on her ass
                    with dissolve

                    pause 1.25

                    scene v11hbc1f # FPP. Same as v11hbc1, Bartender has a bottle in her hand, pouring a drink in a cup, seductive look, mouth closed
                    with dissolve

                    u "You're very pretty."

                    scene v11hbc1
                    with dissolve

                    bartender "That's sweet of you. I know you live in a whole other country, but I could be your little European girlfriend."

                    scene v11hbc1a
                    with dissolve

                    u "My girl wouldn't be too happy about that."

                    scene v11hbc1
                    with dissolve

                    bartender "Look at that, a loyal one."

                    jump v11s27_bartender_yes

                "No":
                    jump v11s27_bartender_no

        "No":
            scene v11hbc1a
            with dissolve

            u "No I don't."

            scene v11hbc1
            with dissolve

            bartender "Well that's good."

            scene v11hbc1a
            with dissolve

            u "How is that good?"

            scene v11hbc1
            with dissolve

            bartender "Well I wouldn't want to make anyone jealous by flirting with you."

            scene v11hbc1a
            with dissolve

            u "Haha."
    
            scene v11hbc1
            with dissolve

            bartender "I've seen a lot of cute girls with you on the trip, I'm sure you think they're really pretty too. So, what about me?"

            scene v11hbc1a
            with dissolve

            menu:
                "Yes":
                    scene v11hbc1e # FPP. Same as v11hbc1, Bartender behind the bar, back turned to MC, she's bending down to grab a bottle, focus on her ass
                    with dissolve

                    pause 1.25

                    scene v11hbc1f # FPP. Same as v11hbc1, Bartender has a bottle in her hand, pouring a drink in a cup, seductive look, mouth closed
                    with dissolve

                    u "You're very pretty."

                    scene v11hbc1
                    with dissolve

                    bartender "That's sweet of you. I know you live in a whole other country, but I could be your little European girlfriend."

                    scene v11hbc1a
                    with dissolve

                    u "Is that so?"

                    scene v11hbc1
                    with dissolve

                    bartender "It is."
                    
                    jump v11s27_bartender_yes

                "No":
                    jump v11s27_bartender_no

label v11s27_bartender_yes:
    scene v11hbc1g # FPP. Same as v11hbc1, Bartender looking at MC, seductive look, mouth open
    with dissolve

    bartender "I don't think you could handle a woman my age."

    scene v11hbc1h # FPP. Same as v11hbc1, Bartender looking at MC, seductive look, mouth closed
    with dissolve

    u "That feels a little insulting..."

    scene v11hbc1g
    with dissolve

    bartender "*Chuckles* So you think you could?"

    scene v11hbc1h
    with dissolve

    u "Well..."

    scene v11hbc1g
    with dissolve

    bartender "What would you do with a woman like me?"

    scene v11hbc2 # TPP. Show MC looking to his right (Still seated in bar), slightly worried expression, mouth closed
    with dissolve

    pause 0.75

    scene v11hbc2a # TPP. Same as v11hbc2, but MC looking to his left
    with dissolve

    pause 0.75

    scene v11hbc1h
    with dissolve

    u "(What is going on with her?)"

    scene v11hbc1g
    with dissolve

    bartender "You look flustered."

    scene v11hbc1i # FPP. Show the bartender leaning in, this time she is very close to MC's face, slight smile, mouth open
    with dissolve

    bartender "*Whisper* It's too bad I have a boyfriend."

    scene v11hbc1a
    with dissolve

    u "What was all that for then?"

    scene v11hbc1
    with dissolve

    bartender "*Laughs* I'm a bored bartender and I love teasing guys like you. It's what makes this job worth it."

    scene v11hbc1a
    with dissolve

    u "I'll have to remember that when I go to bars from now on."

    scene v11hbc1
    with dissolve

    bartender "Haha, are you drinking anything else?"

    scene v11hbc1a
    with dissolve

    u "Not tonight."

    scene v11hbc1
    with dissolve

    bartender "Well if you're done being a loner here at my counter I'd love to get to cleaning."

    scene v11hbc1a
    with dissolve

    u "My bad."

    scene v11hbc3 # FPP. MC is now standing by the bar, the bartender is on the other side of the bar, looking at him, slight smile, mouth open
    with dissolve

    bartender "It was nice chatting, have a good night love."

    scene v11hbc3a # FPP. Same as v11hbc3, Bartender slight smile, mouth closed
    with dissolve

    u "You too."

    scene v11hbc4 # TPP. Show MC walking away from the bar, tired, mouth closed, bartender in the backrgound, slight grin, mouth closed
    with dissolve

    pause 0.75

    scene v11hbc5 # TPP. Show MC walking through the corridor outside his hotel room
    with fade

    pause 0.75

    scene v11hbc6 # TPP. Show MC walking through hotel room door, room is dark, MC tired, mouth closed (do not show roommate)
    with dissolve

    pause 0.75

    scene v11hbc7 # TPP. Show MC pulling his shirt off in hotel room, room dark, MC tired, mouth closed (do not show roommate)
    with dissolve

    pause 0.75

    scene v11hbc8 # TPP. Show MC lying in his bed, in underwear (could be under his covers), sleeping
    with dissolve

    pause 0.75

    stop music fadeout 3
    jump v11_hotel_room

            
label v11s27_bartender_no:
    scene v11hbc1a
    with dissolve

    u "Well, you're not my type, but people like what they like."

    scene v11hbc1j # FPP. Same as v11hbc1, Bartender slightly angry, mouth open 
    with dissolve

    bartender "So I'm ugly?"

    scene v11hbc1k # FPP. Same as v11hbc1, Bartender slightly angry, mouth closed
    with dissolve

    u "That's not what I said."

    scene v11hbc1j
    with dissolve

    bartender "That's how it came off."

    scene v11hbc1k
    with dissolve

    u "Can we just not talk?"

    scene v11hbc1j
    with dissolve

    bartender "So you just call a girl ugly and then don't want to talk anymore?"

    scene v11hbc1k
    with dissolve

    u "I didn't call you ugly, but if I did, why would you want to talk to me?"

    scene v11hbc1j
    with dissolve

    bartender "So you did call me ugly!"

    scene v11hbc1k
    with dissolve

    u "I'm just gonna go..."

    scene v11hbc4a # Same cam as v11hbc4, MC is walking away from the bar, Bartender in background, angry, mouth open, MC tired, mouth closed
    with dissolve

    bartender "I'm married anyway you jerk!"

    scene v11hbc5
    with fade

    pause 0.75

    scene v11hbc6 
    with dissolve

    pause 0.75

    scene v11hbc7
    with dissolve

    pause 0.75

    scene v11hbc8 
    with dissolve

    pause 0.75

    stop music fadeout 3
    jump v11_hotel_room
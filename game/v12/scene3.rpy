# SCENE 3: Penelope Meeting on the Roof
# Location: Roof
# Characters: MC (Outfit X), Penelope (Outfit X)
# Time: 

label v12_penelope_roof:
    scene v12penr1 # TPP Show MC sitting on his bed looking down at his phone, in his hand
    with fade

    play sound sound.vibrate
    pause 1

    play music music.ck1.v12.Track_Scene_3_1 fadein 2

    $ MessengerService.new_message(penelope, "Hey, are you up still?")
    $ MessengerService.new_message(penelope, "If you are, can you meet me in the hallway?")

    u "(It's Penelope.)"

    call screen phone

    menu:
        "Reply":
            if CharacterService.is_dating(penelope):
                $ reputation.add_point(RepComponent.BOYFRIEND)

            $ MessengerService.add_reply(penelope, "Yeah, one sec")

            while MessengerService.has_replies(penelope):
                call screen phone
                if MessengerService.has_replies(penelope):
                    u "(I should probably reply.)"

            scene v12penr2 # TPP Show MC leaving his hotel room
            with dissolve

            pause 1

            stop music fadeout 3
            play music music.ck1.v12.Track_Scene_3_2 fadein 2

            scene v12penr3 # FPP Show Penelope in hotel room hallway, embarrassed expression, mouth closed
            with dissolve

            u "What's up?"

            scene v12penr3a # FPP Same angle as v12penr3, Penelope with embarrased expression, mouth open
            with dissolve

            pe "I... Okay. Don't make fun of me, but I'm kinda nervous to be by myself."

            scene v12penr3
            with dissolve

            u "Because of the mugger and everything?"

            scene v12penr3a
            with dissolve

            pe "Yes. And I know it's not like he's gonna run into the hotel and snatch me or something. I'm not that paranoid, but I'd still rather not be by myself."

            scene v12penr3
            with dissolve

            u "I gotcha. So you called your one and only hero to protect you, right?"

            scene v12penr3b # FPP Same angle as v12penr3, Penelope smiling with mouth open
            with dissolve

            pe "Haha, don't start getting too big of a head. I can always call someone else."

            scene v12penr3c # FPP Same angle as v12penr3, Penelope smiling with mouth closed
            with dissolve

            u "No need for all that. *Chuckles* What are you wanting to do?"

            scene v12penr3b
            with dissolve

            pe "I don't know, just something that gets my mind off of all this."

            scene v12penr3c
            with dissolve

            u "Hmm, wanna go to the roof?"

            scene v12penr3d # FPP Same angle as v12penr3, Penelope looking worried with mouth open
            with dissolve

            pe "Is that even allowed?"

            scene v12penr3e # FPP Same angle as v12penr3, Penelope with neutral expression, mouth closed
            with dissolve

            u "We're allowed to explore, right? Since it's so late and nothing is open, our only option is the hotel. So let's explore walking up to the roof. *Chuckles*"

            scene v12penr3b
            with dissolve

            pe "I'm here because I got into trouble and you want me to do something silly like this."

            scene v12penr3c
            with dissolve

            u "Well, we could always just go our separate ways and get some sleep."

            scene v12penr3b
            with dissolve

            pe "Nope, roof it is."

            scene v12penr3c
            with dissolve

            u "*Laughs*"

            scene v12penr4 # TPP Show MC and Penelope walking down hotel hallway
            with dissolve

            pause 0.75

            scene v12penr5 # TPP Show MC and Penelope arriving at door to the roof
            with dissolve

            pause 0.75

            scene v12penr5a # TPP Same angle as v12penr5, Penelope pulling on the door to the roof, Penelope's mouth open
            with dissolve

            pe "It won't open."

            scene v12penr6 # FPP MC up next to Penelope, hand out pulling on door to roof, Penelope watching with mouth closed
            with dissolve

            u "*Grunts*"

            scene v12penr6a # FPP Same angle as v12penr6, door to roof opening
            with dissolve

            u "Well, would you look at that..."

            scene v12penr6b # FPP Same angle as v12penr6, door to roof is open, Penelope smiling with mouth open
            with dissolve

            pe "Okay, Hulk."

            scene v12penr7 # TPP Show MC and Penelope exiting door onto the hotel roof
            with dissolve

            pause 1

            stop music fadeout 3
            play music music.v12_Track_Scene_3_3 fadein 2

            scene v12penr8 # TPP Show MC and Penelope out on hotel roof in the process of sitting down
            with dissolve

            pause 1

            scene v12penr9 # TPP Show MC and Penelope laying on hotel roof, view is from above, both looking up, Penelope's mouth open
            with dissolve

            pe "This is... beautiful."

            scene v12penr10 # FPP View of MC, who is laying on his back, looking over at Penelope. She is laying down and looking up, her mouth closed
            with dissolve

            menu:
                "Sure is":
                    $ reputation.add_point(RepComponent.BRO)
                    scene v12penr11 # FPP View of MC, who is laying on his back looking up at the stars
                    with dissolve

                    u "It really is."

                "You sure are":
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                    u "Yes, you are."

                    scene v12penr10a # FPP Same angle as v12penr10, Penelope looking back at MC, neutral expression, mouth open
                    with dissolve

                    pe "Huh?"

                    scene v12penr10b # FPP Same angle as v12penr10, Penelope looking back at MC, neutral expression, mouth closed
                    with dissolve

                    u "Oh, nothing. *Chuckles*"

                    scene v12penr10c # FPP Same angle as v12penr10, Penelope looking back at MC, smiling with mouth open
                    with dissolve

                    pe "Haha, I heard you, goofball. I just wanted to see if you'd repeat yourself, handsome."

            scene v12penr10d # FPP Same angle as v12penr10, Penelope looking up at stars, neutral expression, mouth open
            with dissolve

            pe "I have to be honest, I can't stand how the world is today."

            scene v12penr10
            with dissolve

            u "What do you mean?"

            scene v12penr10d
            with dissolve

            pe "There's just so many bad people out there."

            scene v12penr10
            with dissolve

            u "Hasn't the world always been like that?"

            scene v12penr10d
            with dissolve

            pe "Maybe, you're right. Either way though, I can't stand it. It's like people don't take their victims into consideration."

            scene v12penr10a
            with dissolve

            pe "Sure, I may have done some bad things before, but I could never do something bad that resulted in someone being a victim."

            scene v12penr10b
            with dissolve

            u "There's only one way to get away from all the bad stuff in the world."

            scene v12penr10a
            with dissolve

            pe "And what's that?"

            scene v12penr10b
            with dissolve

            u "Don't be in it."

            scene v12penr10d
            with dissolve

            pe "Well, that's not an option. I'm just trying to enjoy my life."

            scene v12penr10
            with dissolve

            u "Exactly, it's not an option. So rather than focusing on the bad people we just have to do our best to be a good person, and like you said, try to enjoy our lives."

            scene v12penr10c
            with dissolve

            pe "Mr. Lee tell you that?"

            scene v12penr10e # FPP Same angle as v12penr10, Penelope looking back at MC, smiling with mouth closed
            with dissolve

            u "*Chuckles* What? No, what makes you say that?"

            scene v12penr10c
            with dissolve

            pe "Along with all the chores he gives me, he makes sure he has time to dive into deep philosophical conversations. *Laughs*"

            scene v12penr10e
            with dissolve

            u "*Mocking tone* \"The past is in the past, so leave it there. But right now is a gift, that's why it's called the present.\" How was that? *Chuckles*"

            scene v12penr10f # FPP Same angle as v12penr10, Penelope looking back at MC, laughing with mouth open
            with dissolve

            pe "*Laughs* That may just be an exact quote from him."

            scene v12penr10e
            with dissolve

            u "Haha. Mr. Lee has his moments, but he really is a good guy."

            scene v12penr10d
            with dissolve

            pe "Yeah, not many of those in our generation."

            scene v12penr10
            with dissolve

            u "Do you think I'm a good guy?"

            if (v11_lauren_caught_aubrey) or (v7_emily_bowling) or (not costumeaubrey and v2_caughtpeeking):
                scene v12penr10a
                with dissolve

                $ grant_achievement("good_vs_evil")
                pe "I think you struggle with right and wrong just like everyone does, but that doesn't mean you're good or bad. It means you're human."

            else:
                scene v12penr10c
                with dissolve

                pe "With you, it's like watching someone try to pick up everyone's fallen pieces and helping them solve their own puzzles. Selfless, caring, and loyal... To me, you're a good guy."

            scene v12penr10e
            with dissolve

            u "Thanks Penelope, that means a lot to me."

            scene v12penr10c
            with dissolve

            pe "Always."

            if CharacterService.is_dating(penelope):
                pe "I kinda hope I end up marrying a guy like you."

                scene v12penr10e
                with dissolve

                menu:
                    "Be shocked":
                        $ reputation.add_point(RepComponent.BRO)

                        u "*Gulp*"

                        scene v12penr10c
                        with dissolve

                        pe "Oh, I wasn't trying to imply anything. *Chuckles* I just think you'd be a really good guy to spend a lifetime with."

                        scene v12penr10e
                        with dissolve

                        u "Ha, thanks. I can't even begin to think about marriage... I don't even know the Bill of Rights. *Chuckles*"

                        scene v12penr10f
                        with dissolve

                        pe "*Laughs* Yeah, you've got a few other things to figure out before you start thinking about tying the knot."

                    "Be bold":
                        $ reputation.add_point(RepComponent.BOYFRIEND)
                        $ grant_achievement("a_person_like_me")

                        scene v12penr10e
                        #with dissolve

                        u "I'm a guy like me."

                        scene v12penr12 # TPP Show Penelope rolling over on top of MC
                        with dissolve

                        pause 1.5

                        scene v12penr13 # TPP Show close-up of Penelope giving MC a kiss
                        with dissolve

                        play sound sound.kiss

                        pause 1.5

                        scene v12penr14 # FPP Show Penelope, who is laying on top of MC with her face close to his, smiling with mouth open
                        with dissolve

                        pe "I guess you are, huh?"

                        scene v12penr14a # Same angle as v12penr14, Penelope smiling with mouth closed
                        with dissolve

                        u "Yes ma'am. To a T."

                        scene v12penr14
                        with dissolve

                        pe "*Chuckles* I'll try and remember that."

                        scene v12penr12a # TPP Same angle as v12penr12, Penelope rolling back off of MC to where she was before
                        with dissolve

                        pause 1.25

            scene v12penr10e
            with dissolve

            u "I don't know about you, but this wind is making me a little chilly."

            scene v12penr10c
            with dissolve

            pe "It is pretty chilly up here, it's not just you. *Chuckles*"

            scene v12penr10e
            with dissolve

            u "Feel good enough to go back?"

            scene v12penr10c
            with dissolve

            pe "Yeah, I'm good."

            scene v12penr8a # TPP Same angle as v12penr8, MC getting to his feet and helping Penelope up from the roof
            with dissolve

            pause 1.25

            scene v12penr7a # TPP Same angle as v12penr7, MC and Penelope going back inside from the roof
            with dissolve

            pause 1.25

            stop music fadeout 3
            play music music.v12_Track_Scene_3_4 fadein 2

            if CharacterService.is_dating(penelope):
                scene v12penr4a # TPP Same angle as v12penr4, MC and Penelope walking down hotel hallway holding hands
                with dissolve

                pause 0.75

            else:
                scene v12penr4
                with dissolve

                pause 0.75

            scene v12penr15 # FPP Show Penelope, standing outside of her hotel room, smiling with mouth open
            with dissolve

            pe "Thanks for helping me relax my nerves."

            scene v12penr15a # FPP Same angle as v12penr15, Penelope smiling with mouth closed
            with dissolve

            u "Of course."

            scene v12penr15
            with dissolve

            pe "I better get to bed, Mr. Lee wants me up early to help with our departure."

            if CharacterService.is_dating(penelope):
                scene v12penr16 # TPP Outside of Penelope's hotel room, show Penelope kissing MC
                with dissolve

                play sound sound.kiss

                pause 1.5

                scene v12penr15
                with dissolve

                pe "Goodnight."

            else:
                pe "Goodnight."

            scene v12penr15a
            with dissolve

            u "Goodnight."

            scene v12penr17 # FPP Show Penelope going into her hotel room
            with dissolve

            pause 0.75

            scene v12penr18 # TPP Show MC walking back to his hotel room
            with dissolve

            pause 0.75

            scene v12penr1a # TPP Same angle as v12penr1, MC sitting down on his bed
            with dissolve

            pause 0.75

        "Don't reply":
            $ reputation.add_point(RepComponent.BRO)

            scene v12penr19 # FPP MC's view sitting on his bed, looking down at his phone, which he just turned off
            with dissolve

            if not v12_chase_robber:
                u "(Don't wanna take the chance that she may be needing help with the laundry or something... Haha.)"            
            else:
                u "(Don't wanna take the chance that she may be needing help with one of her little Mr. Lee chores.)"

            scene v12penr1b # TPP Same angle as v12penr1, MC putting his phone away
            with dissolve

            pause 0.75
    
    stop music fadeout 3

    jump v12_roomate_talk # Scene 4
# SCENE 2) Nora and Chloe Conversations
# Locations: college hallway
# Characters: MC (smart outfit from scene 1), Chloe (outfit 2), Nora (outfit 1)
# Time: Thursday morning

label v11_nora_chloe_hallway:
    scene v11nohall1 # TPP. Show MC walking in the hallway, camera should be behind MC, Nora is supposed to be in the background looking at the bulleting board
    with fade

    play music music.ck1.v11.Track_Scene_2 fadein 2

    pause 0.75

    scene v11nohall2 # FPP. MC is now next to Nora, Nora is still looking at the bulleting board (mouth closed, happy expression, if her face is visible)
    with dissolve

    u "Hey Nora, are there a lot of people going on the trip?"

    if v8_nora_likes_mc:
        scene v11nohall2a # FPP. Same as 2, but now Nora is looking at MC, Nora mouth open, happy expression
        with dissolve

        no "Yeah, there's plenty. I'm surprised we actually got enough people."

    else:
        scene v11nohall2a # FPP. Same as 2, but now Nora is looking at MC, Nora mouth open, happy expression
        with dissolve

        no "Plenty. I'm surprised we actually got enough people."

    scene v11nohall2b # FPP. Same as 2, but now Nora is looking at MC, Nora mouth closed, happy expression
    with dissolve

    u "And yet you don't seem too psyched about it."

    scene v11nohall2c # FPP. Same as 2, but now Nora is looking at MC, Nora mouth open, slightly sad expression
    with dissolve

    no "Well, Chris and I have been having... moments. So that could cause unneeded stress. Then there's Chloe."

    scene v11nohall2d # FPP. Same as 2, but now Nora is looking at MC, Nora mouth closed, slightly sad expression
    with dissolve

    u "Sounds like you're having a bit of a rough time?"

    scene v11nohall2c
    with dissolve

    no "Well, I asked Mr. Lee and Ms. Rose to put out a sign up sheet because I was afraid I wasn't going to get enough people."

    no "It kinda got out of hand and with everything going on it's all just a bit stressful."

    scene v11nohall2d
    with dissolve

    u "I'm sure things with you and Chris will be better in Europe... I mean it's Europe after all."

    scene v11nohall2c
    with dissolve

    no "You would think, but he said he's gonna be glued to his phone the entire time. The most I can hope for is a good conversation on the plane."

    scene v11nohall2d
    with dissolve

    menu:
        "I'll be there":
            $ nora.points += 1
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene v11nohall2b
            with dissolve

            u "Well I'll be there, I hope that's something good. *Chuckles*"

            if v8_nora_likes_mc:
                scene v11nohall2a
                with dissolve

                no "*Chuckles* It's definitely something."

            else:
                scene v11nohall2a
                with dissolve

                no "I just wish he'd make more of an effort."

        "Have a good time":
            $ reputation.add_point(RepComponent.BRO)

            scene v11nohall2d
            with dissolve

            u "Just try to enjoy yourself anyway."

            if v8_nora_likes_mc:
                scene v11nohall2c
                with dissolve

                no "Thanks for trying, but I think it's clear where his priorities are."

            else:
                scene v11nohall2c
                with dissolve

                no "Yeah. Right."

    scene v11nohall2d
    with dissolve

    u "What about Chloe? Think you two can make up?"

    scene v11nohall2c
    with dissolve

    no "I don't think being in another country is gonna make a difference."

    scene v11nohall2d
    with dissolve

    menu:
        "Defend Chloe":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ nora.points -= 1

            scene v11nohall2d
            with dissolve

            u "I really think you should try to work things out with her. I mean... you guys are sorority sisters, you're supposed to stick together..."

            scene v11nohall2c
            with dissolve

            no "And? That doesn't change that she's fake. I can't get along with fake people. What are you, her publicist?"

            scene v11nohall2d
            with dissolve

            u "No I just... nevermind."

        "Don't defend Chloe":
            $ nora.points += 1

            scene v11nohall2b
            with dissolve

            u "This trip was your thing, don't let her or anyone else mess that up."

            scene v11nohall2a
            with dissolve

            no "I'll try my best."

    scene v11nohall10 # FPP. Show Nora looking to the side at Carlie walking up to Nora, nora mouth open, charli mouth closed
    with dissolve

    no "Oh, hey Charli."

    scene v11nohall11 # FPP. Show charlie looking to towards nora (out of shot) mouth open
    with dissolve

    charli "Hey there."

    scene v11nohall2a # (already rendered in main scene)
    with dissolve

    no "Have you two had a chance to meet yet?"

    scene v11nohall2b # (already rendered in main scene)
    with dissolve

    u "Umm, I don't think so."

    scene v11nohall2a
    with dissolve

    no "Well, while you guys do that, I'm gonna run."

    scene v11nohall2b
    with dissolve

    u "*Chuckles* Alright, catch you later."

    scene v11nohall11a # FPP. Same 11, mouth open, slight smile
    with dissolve

    charli "Well, nice to meet you. Like Nora said, my name's Charli."

    scene v11nohall11b # FPP. Same 11, mouth closed, slight smile
    with dissolve

    u "I'm [name]. So you're a student here?"

    scene v11nohall11a
    with dissolve

    charli "Yeah, an exchange student. I've been here since the start of the year, but I'm living off campus so I don't know that many students."
    charli "Nora and I have talked a few times, but that's about it as I'm often tied up doing other things..."

    scene v11nohall11b
    with dissolve
    scene v11nohall11a
    with dissolve
    
    charli "So, are you going on this Europe trip? Mr. Lee invited me to go. But I'm not sure I actually want to."

    scene v11nohall11b
    with dissolve

    u "Yeah, I'll be there. What are you unsure of? It's gonna be a great time and there's some really cool events planned. Plus, you can meet all the students you haven't met."

    scene v11nohall11a
    with dissolve

    charli "Well, I have to admit that's pretty convincing. *Chuckles* I guess I should start packing."

    scene v11nohall11b
    with dissolve

    u "Haha, that's probably a good idea."

    scene v11nohall11a
    with dissolve

    charli "Are you close with anyone that's going on the trip?"

    scene v11nohall11b
    with dissolve

    u "Yeah, a few people. I'm closer with some more than others though."

    scene v11nohall11a
    with dissolve

    charli "*Chuckles* You said you're closer with some more than others? I can tell you're close with Nora, but who else?"

    charli "Anyone you'd recommend for me to start getting to know? Or even avoid?"

    scene v11nohall11b
    with dissolve

    u "Depends on the company you like to keep..."

    u "If you're looking for a more mellow time then Lauren or Lindsey may be nice to talk to, but if you have a more wild side then getting to know Amber or Aubrey is probably right up your alley."

    if joinwolves:
        u "In terms of people to avoid, It's always best to avoid Grayson. *Laughs*"

    else:
        u "In terms of people to avoid, It's always best to keep a good distance between yourself and Cameron. *Laughs*"

    scene v11nohall11a
    with dissolve

    charli "And what kind of company are you?"

    menu:
        "Mellow":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v11nohall11c # same 11b, just change pose a little so conversation isn't stale
            with dissolve

            u "I mean, I like to have fun, but I wouldn't consider myself as wild as some of my friends are."

        "Wild":
            scene v11nohall11c
            with dissolve

            u "Haha... I guess you could say I'm here for the full college experience."

    scene v11nohall11d # same 11a, just change pose a little so conversation isn't stale
    with dissolve

    charli "Nora mentioned that we'll have some time to do our own thing and explore. Anything you're looking forward to?"

    menu:
        "Hanging with the girls":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene v11nohall11c
            with dissolve

            u "Well, we'll be in another country surrounded by beautiful women... I'm sure you can imagine what I plan on doing. *Chuckles* Really though, I just wanna have fun no matter what."

            scene v11nohall11d
            with dissolve

            charli "With that attitude there's no way this will be a boring trip! *Laughs*"

        "Sleeping":
            scene v11nohall11c
            with dissolve

            u "I don't know... sleeping? *Chuckles*"

            scene v11nohall11d
            with dissolve

            charli "Oh, you're a fan of hotel mattresses? Haha."

            scene v11nohall11c
            with dissolve

            u "There's nothing better than going to sleep and waking up in a fresh hotel bed. *Chuckles*"

            scene v11nohall11d
            with dissolve

            charli "That's something I can definitely agree with and they clean up after you."

            scene v11nohall11c
            with dissolve

            u "Haha, exactly."

            scene v11nohall11d
            with dissolve

    charli "Well, as much as I'm enjoying this, I guess I should go start packing for the trip... See you around?"

    scene v11nohall11c
    with dissolve

    u "For sure!"

    scene v11nohall12 # FPP. Show Charli walking off
    with dissolve

    u "(Hmm, he must be off campus a lot. I'm pretty sure I've never seen him before. He seems pretty nice.)"

    scene v11clhall1 # FPP. MC is looking at the end of the hallway now, hallway is empty
    with dissolve

    pause 0.75

    scene v11clhall1a # FPP. Same cam as clhall1, Chloe is now in the hallway, walking, neutral expression, mouth closed, not looking at MC
    with dissolve

    pause 0.75

    scene v11clhall1b # FPP. Same as clhall1a, Chloe is now close to MC, mouth closed, neutral expression, not looking at MC (Chloe should be in talking distance at this point)
    with dissolve

    menu:
        "Leave her alone":
                scene v11clhall1
                with dissolve

                u "(I need to get home and pack.)"

        "Say something":
            if CharacterService.is_mad(chloe):
                scene v11clhall1c # FPP. Same as clhall1a, Chloe and MC are now looking at each other, Chloe's mouth is closed, she is annoyed
                with dissolve

                u "Hey Chloe."

                scene v11clhall1d # FPP. Same as clhall1a, Chloe and MC are now looking at each other, Chloe's mouth is open, she is annoyed
                with dissolve

                cl "Why do you keep trying to talk to me?"

                scene v11clhall1c
                with dissolve

                menu:
                    "Apologize":
                        $ CharacterService.set_relationship(chloe, Relationship.FRIEND, mc)
                        $ CharacterService.remove_mood(chloe, Moods.MAD)
                        $ reputation.add_point(RepComponent.BOYFRIEND)

                        scene v11clhall1c
                        with dissolve

                        u "I'm sorry, you know? Sorry for how things went. I know you're mad at me, but I really want us to move past this and at least be friends."

                        scene v11clhall1e # FPP. Same as clhall1d, Chloe and MC looking at each other, Chloe's mouth is open, she has a slight smile
                        with dissolve

                        cl "*Sighs* I'm not even really that mad anymore."

                        scene v11clhall1f # FPP. Same as clhall1e, Chloe and MC looking at each other, Chloe's mouth is closed, she has a slight smile
                        with dissolve

                        u "But you just..."

                        scene v11clhall1e
                        with dissolve

                        cl "Sometimes I get a little carried away keeping up appearances."

                        scene v11clhall1f
                        with dissolve

                        u "You were definitely doing a good job, I thought you were still pissed."

                        scene v11clhall1e
                        with dissolve

                        cl "Yeah no, I'm sorry. You know, I have a few minutes before my next class. Wanna go outside and talk for a few minutes?"

                        scene v11clhall1f
                        with dissolve

                        menu:
                            "Yes":
                                $ reputation.add_point(RepComponent.BOYFRIEND)
                                $ chloe.points += 1

                                scene v11clhall1f
                                with dissolve

                                u "Sure."

                                scene v11clhall2 # TPP. Show MC and Chloe walking side by side, both mouths closed and they are both happy
                                with dissolve

                                pause 0.75

                                scene v11clb1 # FPP. MC and Chloe are sitting on a bench outside, they are looking at each other, Chloe is happy, mouth open
                                with fade

                                cl "Are you excited for the trip?"

                                scene v11clb1a # FPP. Same as clb1, but Chloe is happy, mouth closed
                                with dissolve

                                u "Of course."

                                scene v11clb1
                                with dissolve

                                cl "I am too. I'm a little nervous knowing I'm going to have to be around some people that I don't really get along with, but I'll still have fun."

                                scene v11clb1a
                                with dissolve

                                u "Yeah, no reason not to enjoy yourself..."

                                scene v11clb1
                                with dissolve

                                cl "I wonder what will be the crazy thing that happens."

                                scene v11clb1a
                                with dissolve

                                u "What do you mean?"

                                scene v11clb1
                                with dissolve

                                cl "You know how every time you go on a trip something crazy always happens that everyone talks about? I went on a class trip a couple years ago and one of our classmates had a baby."

                                cl "*Laughs* She didn't even know she was pregnant."

                                scene v11clb1a
                                with dissolve

                                u "*Chuckles* That's horrible."

                                scene v11clb1
                                with dissolve

                                cl "Yeah, it was pretty bad at the time. I guess we'll see what people will talk about after Europe..."

                                scene v11clb1a
                                with dissolve

                                u "Maybe you'll trip over the Queen's gown while we're in London... That'd be funny now and a few years later."

                                scene v11clb1
                                with dissolve

                                cl "If it isn't caught on camera it never happened."

                                scene v11clb1a
                                with dissolve

                                u "Hashtag Chloe caught in 4K. *Laughs*"

                                scene v11clb1
                                with dissolve

                                cl "I'd be mad at you for real if that ever happened."

                                scene v11clb1a
                                with dissolve

                                u "I'll just blame it on someone else and swoop in like the hero."

                                scene v11clb1
                                with dissolve

                                cl "How Prince Charming of you."

                                scene v11clb1a
                                with dissolve

                                u "My lady. *Laughs*"

                                scene v11clb1
                                with dissolve

                                cl "I want to see if there's any new clothes I can get. I don't even know the latest European fashion trends."

                                scene v11clb1a
                                with dissolve

                                u "That's something you keep up with?"

                                scene v11clb1
                                with dissolve

                                cl "It is now."

                                scene v11clb1a
                                with dissolve

                                u "Haha."

                                scene v11clb1
                                with dissolve

                                cl "Just don't leave me all alone in Europe, there's hardly anyone I can hang out with."

                                scene v11clb1a
                                with dissolve

                                u "I get it, you just want to hang out with me, no need to make up excuses."

                                scene v11clb1
                                with dissolve

                                cl "You make good company... well, sometimes."

                                scene v11clb1a
                                with dissolve

                                u "Haha, well I won't be good company if I'm not there so I'm gonna go get packing."

                                scene v11clb1
                                with dissolve

                                cl "Alright, it was good talking to you."

                                scene v11clb1a
                                with dissolve

                                u "You too."

                                scene v11clb2 # TPP. Show MC walking away from the bench, MC is smiling, mouth closed, Chloe is walking the other direction in the background (Show MC's from the front and Chloe from behind)
                                with dissolve

                                pause 0.75

                            "No":
                                scene v11clhall1f
                                with dissolve

                                u "I wish, but I need to get started packing for the trip."

                                scene v11clhall1e
                                with dissolve

                                cl "Oh okay, well I'll see you later then."

                                scene v11clhall1f
                                with dissolve

                                u "See ya."

                                scene v11clhall3 # TPP. Show MC and Chloe walking in opposite directions, show MC from the front and Chloe from behind, MC mouth closed, neutral expression (Chloe should walk towards same direction as clhall1a)
                                with dissolve

                                pause 0.75

                    "Give up":
                        scene v11clhall1c
                        with dissolve

                        u "*Sighs* Nevermind."

                        scene v11clhall3
                        with dissolve

                        pause 0.75

            else:
                if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
                    scene v11clhall1f
                    with dissolve

                    u "Hey, cutie."

                else:
                    scene v11clhall1f
                    with dissolve

                    u "Hey Chloe."

                if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
                    scene v11clhall1e
                    with dissolve

                    cl "Oh, hey handsome. What's up?"

                else:
                    scene v11clhall1e
                    with dissolve

                    cl "Oh, hey [name]. What's up?"

                scene v11clhall1f
                with dissolve

                u "Not much, I was just seeing who's all going all the trip."

                scene v11clhall1e
                with dissolve

                cl "It's a lot of people."

                scene v11clhall1f
                with dissolve

                u "More than I expected. I hope everyone gets along. But I doubt it."

                scene v11clhall1e
                with dissolve

                cl "Haha, me too. You know, I have a few minutes before my next class. Wanna go outside and talk for a bit?"

                menu:
                    "Yes":
                        $ reputation.add_point(RepComponent.BOYFRIEND)
                        $ chloe.points += 1

                        scene v11clhall1f
                        with dissolve

                        u "Sure."

                        scene v11clhall2
                        with dissolve

                        pause 0.75

                        scene v11clb1
                        with fade

                        cl "Are you excited for the trip?"

                        scene v11clb1a
                        with dissolve

                        u "Of course."

                        scene v11clb1
                        with dissolve

                        cl "I am too. I'm a little nervous knowing I'm going to have to be around some people that I don't really get along with, but I'll still have fun."

                        scene v11clb1a
                        with dissolve

                        u "Yeah, no reason not to enjoy yourself..."

                        scene v11clb1
                        with dissolve

                        cl "I wonder what will be the crazy thing that happens."

                        scene v11clb1a
                        with dissolve

                        u "What do you mean?"

                        scene v11clb1
                        with dissolve

                        cl "You know how every time you go on a trip something crazy always happens that everyone talks about? I went on a class trip a couple years ago and one of our classmates had a baby."

                        cl "*Laughs* She didn't even know she was pregnant."

                        scene v11clb1a
                        with dissolve

                        u "*Chuckles* That's horrible."

                        scene v11clb1
                        with dissolve

                        cl "Yeah, it was pretty bad at the time. I guess we'll see what people will talk about after Europe..."

                        scene v11clb1a
                        with dissolve

                        u "Maybe you'll trip over the Queen's gown while we're in London... That'd be funny now and a few years later."

                        scene v11clb1
                        with dissolve

                        cl "If it isn't caught on camera it never happened."

                        scene v11clb1a
                        with dissolve

                        u "Hashtag Chloe caught in 4K. *Laughs*"

                        scene v11clb1
                        with dissolve

                        cl "I'd be mad at you for real if that ever happened."

                        scene v11clb1a
                        with dissolve

                        u "I'll just blame it on someone else and swoop in like the hero."

                        scene v11clb1
                        with dissolve

                        cl "How Prince Charming of you."

                        scene v11clb1a
                        with dissolve

                        u "My lady. *Laughs*"

                        scene v11clb1
                        with dissolve

                        cl "I want to see if there's any new clothes I can get. I don't even know the latest European fashion trends."

                        scene v11clb1a
                        with dissolve

                        u "That's something you keep up with?"

                        scene v11clb1
                        with dissolve

                        cl "It is now."

                        scene v11clb1a
                        with dissolve

                        u "Haha."

                        scene v11clb1
                        with dissolve

                        cl "Just don't leave me all alone in Europe, there's hardly anyone I can hang out with."

                        scene v11clb1a
                        with dissolve

                        u "I get it, you just want to hang out with me, no need to make up excuses."

                        scene v11clb1
                        with dissolve

                        cl "You make good company... well sometimes."

                        scene v11clb1a
                        with dissolve

                        u "Haha, well I won't be good company if I'm not there so I'm gonna go get packing."

                        if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
                            scene v11clb1
                            with dissolve

                            cl "I need to run but I can't wait to spend some more time with you in Europe."

                        else:
                            scene v11clb1
                            with dissolve

                            cl "Alright, it was good talking to you."

                        if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
                            scene v11clb1a
                            with dissolve

                            u "See you later, beautiful."

                        else:
                            scene v11clb1a
                            with dissolve

                            u "You too."

                        scene v11clb2
                        with dissolve

                        pause 0.75

                    "No":
                        scene v11clhall1f
                        with dissolve

                        u "I wish, but I need to get started packing for the trip."

                        scene v11clhall1e
                        with dissolve

                        cl "Oh okay, well I'll see you later then."

                        scene v11clhall1f
                        with dissolve

                        u "See ya."

                        scene v11clhall3
                        with dissolve

                        pause 0.75
    stop music fadeout 3

    if joinwolves:
        jump v11_wolves_packing_chris
    else:
        jump v11_samantha_packing
# SCENE 16: Lauren Airport Convo
# Locations: airport
# Characters: MC (outfit 1), Lauren (outfit 1) Ms Rose (outfit1)
# Time: around 3am sunday morning (dark outside)

label v11_lauren_airport_convo:
    play music "music/v11/Track Scene 16.mp3" fadein 2
    if v11_lauren_caught_aubrey:
        scene v11laac1 # TPP. Show Lauren standing in the airport, looking at her phone, she is very angry, mouth closed, MC is in the background looking at her, walking towards her direction (he is relatively far away), MC mouth closed, worried expression (make sure diff location in airport to v11noac1)
        with fade

        pause 0.75

        scene v11laac1a # TPP. Same as v11laac1, but MC is now closer to Lauren
        with dissolve

        pause 0.75

        scene v11laac1b # TPP. Same as v11laac1a, but MC is right behind Lauren
        with dissolve

        pause 0.75

        scene v11laac2 # FPP. Show MC tapping Lauren's shoulder, she has her back turned to him, MC is very close to her now
        with dissolve

        pause 0.75

        scene v11laac2a # FPP. Same cam as v11laac2, Lauren is now looking at MC, very angry, tears in her eyes, mouth closed
        with dissolve

        u "Can we talk?"

        scene v11laac2b # FPP. Same as v11laac2a, Lauren is very angry, tears in her eyes, mouth open
        with dissolve

        la "Leave me alone, asshole."

        scene v11laac2c # FPP. Same cam as v11laac2, Lauren is now walking away from MC, she is still pretty close
        with dissolve

        pause 0.75

        scene v11laac2d # FPP. Same as v11laac2c, Lauren is now further away from MC
        with dissolve

        pause 0.75

        scene v11laac3 # TPP. Ms Rose is looking at the students, she is smiling, mouths open
        with dissolve

        ro "C'mon everyone, the shuttles are ready. Grab your bags."

    elif "v11_aubrey" in sceneList: #and not lauren rs
        scene v11laac1c # TPP. Show Lauren standing in the airport, she is smiling, mouth closed, MC is in the background looking at her, walkingtowards her direction (he is relatively far away), MC mouth closed, slight smile (make sure diff location in airport to v11noac1)
        with dissolve

        pause 0.75

        scene v11laac1d # TPP. Same as v11laac1, but MC is now closer to Lauren
        with dissolve

        pause 0.75

        scene v11laac1e # TPP. Same as v11laac1a, but MC is right behind Lauren
        with dissolve

        pause 0.75

        scene v11laac2
        with dissolve

        pause 0.75

        scene v11laac2e # FPP. Same cam as v11laac2, Lauren is now looking at MC, she is slightly nervous, mouth closed
        with dissolve

        u "Hey."

        scene v11laac2f # TPP. Same as v11laac2e, Lauren is slightly nervous, mouth open
        with dissolve

        la "Hey... so uhm, you and Aubrey are a thing?"

        scene v11laac2e
        with dissolve

        menu:
            "Yes":
                scene v11laac2e
                with dissolve

                u "Yeah kinda, we've been hooking up."

                scene v11laac2f
                with dissolve

                la "Are you guys dating?"

                scene v11laac2e
                with dissolve

                u "Not officially, no."

                scene v11laac2f
                with dissolve

                la "Do you want to?"

                scene v11laac2e
                with dissolve

                menu:
                    "Yes":
                        $ add_point(KCT.TROUBLEMAKER)

                        scene v11laac2e
                        with dissolve

                        u "It would be nice, yeah."

                        scene v11laac2f
                        with dissolve

                        la "I didn't even know you guys really knew each other."

                        scene v11laac2e
                        with dissolve

                        u "We met at a party at the start of the year."

                    "Why so many questions?":
                        scene v11laac2e
                        with dissolve

                        u "Why so many questions? *Chuckles*"

                        scene v11laac2f
                        with dissolve

                        la "I'm just curious."

                        scene v11laac2e
                        with dissolve

                        u "Well, we're just good friends."

                        scene v11laac2f
                        with dissolve

                        la "That also have sex."

                        scene v11laac2e
                        with dissolve

                        u "Uh, yeah."
               
            "Not really":
                scene v11laac2e
                with dissolve

                u "No not really, we're just really close friends."

                scene v11laac2f
                with dissolve

                la "That also have sex."

                scene v11laac2e
                with dissolve

                u "Uh, yeah."
            
        scene v11laac2f
        with dissolve
        
        la "Oh okay... well, I guess I'll see you in London."

        scene v11laac2e
        with dissolve

        u "Of course. What are you most excited to do while we're here?"

        scene v11laac2f
        with dissolve

        la "I don't know, but I'm not going to waste this opportunity."

        scene v11laac2e
        with dissolve

        u "What do you mean?"

        scene v11laac2f
        with dissolve

        la "While I'm here I want to explore and try new things."

        scene v11laac2e
        with dissolve

        u "Like?"

        if lauren.relationship >= Relationship.KISS:
            scene v11laac2g # FPP. Same as v11laac2e, Lauren has a slightly seductive look, mouth open
            with dissolve

            la "Well I was hoping maybe we could explore some things... together."

            scene v11laac2g
            with dissolve

            la "If it doesn't interfere with your plans with Aubrey..."

            menu:
                "Play it cool":
                    $ add_point(KCT.BRO)

                    scene v11laac2h # FPP. Same as v11laac2e, Lauren has a slightly seductive look, mouth closed
                    with dissolve

                    u "*Smirks* Sounds nice."

                "Act clueless":
                    $ add_point(KCT.BOYFRIEND)

                    scene v11laac2h
                    with dissolve

                    u "Of course we can, they'll probably take us to some landmarks or something."

        scene v11laac2i # FPP. Same as v11laac2e, Lauren is smiling, mouth open
        with dissolve

        la "Haha, do you know who you're rooming with?"

        scene v11laac2j # FPP. Same as v11laac2e, Lauren is smiling, mouth closed
        with dissolve

        u "I never put in any preferences, I assumed they'd just put me with someone random anyways."

        scene v11laac2i
        with dissolve

        la "They put me with Amber, she's definitely... a character."

        scene v11laac2j
        with dissolve

        u "Haha, I know."

        scene v11laac3
        with dissolve

        ro "C'mon everyone, the shuttles are ready. Grab your bags."

        scene v11laac2i
        with dissolve

        la "Time to go."

    elif lauren.relationship >= Relationship.KISS: #and not plane sex scene
        scene v11laac1c 
        with dissolve

        pause 0.75

        scene v11laac1d 
        with dissolve

        pause 0.75

        scene v11laac1e 
        with dissolve

        pause 0.75

        scene v11laac2
        with dissolve

        pause 0.75

        scene v11laac2j
        with dissolve

        u "If it isn't my favorite person."

        scene v11laac2i
        with dissolve

        la "Favorite? Wow, I feel so special. *Chuckles*"

        scene v11laac2j
        with dissolve

        u "You excited?"

        scene v11laac2i
        with dissolve

        la "More than that. I'm gonna get out of my comfort zone on this trip."

        scene v11laac2j
        with dissolve

        u "Sounds like you're planning something."

        scene v11laac2i
        with dissolve

        la "I have some things I'd like to try."

        scene v11laac2j
        with dissolve

        u "Like?"

        scene v11laac2k # FPP. Same as v11laac2e, Lauren's face is now very close to MC's, she is smiling, mouth open
        with dissolve

        la "*Whisper* I'll show you soon."

        play sound "sounds/kiss.mp3"

        scene v11laac4 # TPP. Same positioning as v11laac2, but Lauren is kissing MC on the cheek, MC is slightly surprised, mouth closed
        with dissolve

        u "Oh, someone's out of character."

        scene v11laac2i
        with dissolve

        la "I sat with Amber on the plane since she's also my assigned roommate... She may have rubbed off on me a tiny bit."

        scene v11laac2j
        with dissolve

        u "I'm noticing. *Chuckles*"

        scene v11laac2i
        with dissolve

        la "She's actually pretty fun."

        scene v11laac2j
        with dissolve

        u "Yeah... she is."

        scene v11laac3
        with dissolve

        ro "C'mon everyone, the shuttles are ready. Grab your bags."

        scene v11laac2i
        with dissolve

        la "Time to go."

    else: #not plane sex scene but also no relationship of any kind with Lauren
        scene v11laac1c 
        with dissolve

        pause 0.75

        scene v11laac1d 
        with dissolve

        pause 0.75

        scene v11laac1e 
        with dissolve

        pause 0.75

        scene v11laac2
        with dissolve

        pause 0.75

        scene v11laac2j
        with dissolve

        u "Hey possum."

        scene v11laac2i
        with dissolve

        la "Possum? Wow, I feel so special having a nickname. *Chuckles*"

        scene v11laac2j
        with dissolve

        u "*Laughs* That was the plan. You excited?"

        scene v11laac2i
        with dissolve

        la "More than that. I'm gonna get out of my comfort zone on this trip."

        scene v11laac2j
        with dissolve

        u "Sounds like you're planning something."

        scene v11laac2i
        with dissolve

        la "I have some things I'd like to try."

        scene v11laac2j
        with dissolve

        u "Like?"

        scene v11laac2i
        with dissolve

        la "Well I sat with Amber on the plane since she's also my assigned roommate... and she's kinda been opening my mind up to more \"exciting things\"."

        scene v11laac2j
        with dissolve

        u "And how'd she do that?"

        scene v11laac2i
        with dissolve

        la "She said she'd make my trip, and I quote, \"a living hell\" if I don't try some new things."

        scene v11laac2j
        with dissolve

        u "Haha, so you caved?"

        scene v11laac2i
        with dissolve

        la "Sure did. I have no interest in getting teased, pranked or bullied the entire time we're in Europe."

        scene v11laac2j
        with dissolve

        u "Sooo, was there something specific you planned to do?"

        scene v11laac2i
        with dissolve

        la "As long as I get to do something I'll never forget, I'm good."

        scene v11laac2j
        with dissolve

        u "Haha, that's a low bar."

        scene v11laac3
        with dissolve

        ro "C'mon everyone, the shuttles are ready. Grab your bags."

        scene v11laac2i
        with dissolve

        la "Time to go."

        scene v11laac2j
        with dissolve

        u "Let's go."

    if not v11_check_on_nora:
        scene v11nca2a
        with dissolve
        
        pause 0.75
        
        scene v11nca2b
        with dissolve
        
        pause 0.75
        
        scene v11nca2
        with dissolve
        
        u "(What the...?!)"
        u "*Whisper* Fucking asshole!"

        scene v11nca10 # FPP. Show Riley rushing over to MC, mouth open
        with dissolve

        ri "*Whisper* [name]! Why'd you say that to him?"

        scene v11nca10a # FPP. same 10, now right infront of mc, slightly annoyed, mouth closed
        with dissolve

        u "Cause it's true, he's pissing me off."

        scene v11nca10b # FPP. same 10, now right infront of mc, slightly annoyed, mouth open
        with dissolve

        ri "He didn't even do anything wrong. You know he's gay, right?"

        scene v11nca10a
        with dissolve

        u "No, I didn't know that, but I still don't fuck with him. He just comes out of nowhere and all of a sudden he's buddied up to everyone. Like what the fuck?"

        scene v11nca10b
        with dissolve

        ri "Well, I've gotten to know him pretty well, [name], he's really not that bad. At least try and get to know him, alright?"
        ri "I can get why you may feel the way you do, but get all the info before you pop off on someone like that."

        scene v11nca10a
        with dissolve

        u "*Sighs* If you say so."

        scene v11nca10b
        with dissolve

        ri "Now be happy! We're on vacation, grumpy man. Now let's go, they're waiting for us already at the shuttle."

    scene v11laac5 # TPP. Show Lindsey getting on the shuttle
    with dissolve

    pause 0.75

    scene v11laac5a # TPP. Same cam as v11laac5, show MC getting on the shuttle
    with dissolve

    pause 0.75

    scene v11laac5b # TPP. Same cam as v11laac5, show Nora getting on the shuttle
    with dissolve

    pause 0.75

    scene v11laac6 # TPP. Show the shuttle on the road (european background if possible)
    with dissolve

    pause 0.75

    scene v11laac7 # TPP. Show the shuttle stopped in front of the hotel (door closed)
    with dissolve

    pause 0.75

    scene v11laac7a # TPP. Show the shuttle stopped in front of the hotel (door open) and Ms Rose getting off the shuttle
    with dissolve

    pause 0.75

    scene v11laac8 # FPP. MC is walking through the door to the lobby of the hotel, he sees Riley, Aubrey and Chloe, the girls are talking between themselves, all smiling
    with dissolve

    pause 0.75
    stop music fadeout 3
    jump v11_arrive_hotel
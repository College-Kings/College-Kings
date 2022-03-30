# SCENE 3: Back at Riley's Place
# Locations: Riley's Dorm
# Characters: RILEY (Outfit: 2), MC (Outfit: 1)
# Time: Night

label v16s3:
    play music "music/v15/Track Scene 1_3.mp3" fadein 2
    play sound "sounds/dooropen.mp3"

    scene v16s3_1 # TPP. Show Riley walking into her dorm while opening the door, MC following in right behind her, both neutral face, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/doorclose.mp3"

    scene v16s3_1a # TPP. Riley Off-camera, Just MC stepped into the dorm and shutting the door, neutral face, mouth closed.
    with dissolve

    pause 0.75

    scene v16s3_2 # FPP. In Riley's dorm, MC looking at Riley, Riley looking at MC, Riley neutral face, mouth open.
    with dissolve

    ri "Just relax. Go sit on my bed."

    scene v16s3_2a # FPP. MC looking at Riley, Riley looking at MC, Riley neutral face, mouth closed.
    with dissolve

    u "You don't have to tell me twice."

    scene v16s3_2
    with dissolve

    ri "I'll be right back."

    scene v16s3_3 # TPP. Show MC sitting on Riley's bed, neutral face, mouth closed.
    with dissolve
    
    pause 0.75

    play sound "sounds/dooropen.mp3"

    scene v16s3_4 # FPP. MC sitting on Riley's bed, MC looking at the Dorm door watching Riley leave, neutral face, mouth closed.
    with dissolve

    pause 0.75

    scene v16s3_3a # TPP. Show MC laying on Riley's bed, with his eyes closed, neutral face, mouth closed.
    with fade

    u "(Damn, I'm tired. I could fall asleep right now.)"

    play sound "sounds/dooropen.mp3"

    scene v16s3_3b # TPP. Show MC laying on Riley's bed, with his eyes open, neutral face, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/doorclose.mp3"

    scene v16s3_3
    with dissolve
    
    pause 0.75

    scene v16s3_3c # TPP. Show MC now sitting on Riley's bed again, Riley sitting down next to him and handing him the frozen icepack (Whatever asset we can use :D), MC neutral face, mouth closed, Riley neutral face, mouth open.
    with dissolve

    ri "Here you go. This is all I could find."

    scene v16s3_5 # FPP. MC looking at Riley holding up the ice pack, Riley looking at MC and holding up the Ice pack, Riley, neutral face, mouth closed
    with dissolve

    pause 0.75

    if v16_wintom:
        scene v16s3_5a # FPP. MC's hand taking the icepack from Riley, Riley looking at MC, MC looking at Riley, Riley slight smile, mouth closed.
        with dissolve

        u "Thanks, but I'm sure Tom needs it more than me, haha."

    else:
        scene v16s3_5a
        with dissolve

        u "Fuck, that's cold!"

        scene v16s3_5b # FPP. MC holding the icepack on his head, MC looking at Riley, Riley looking at MC, Riley slight smile, mouth open.
        with dissolve

        ri "Yeah, [name]. Frozen things tend to have that effect, haha."

        scene v16s3_5c # FPP. MC holding the icepack on his head, MC looking at Riley, Riley looking at MC, Riley slight smile, mouth closed.
        with dissolve

        u "Thanks, Riley. I'm starting to feel better already."

        scene v16s3_5b
        with dissolve

        ri "Well, I do have some bad news..."

        scene v16s3_5c
        with dissolve

        u "Oh no..."

        scene v16s3_5b
        with dissolve

        ri "I don't have any ice cream."

        scene v16s3_5c
        with dissolve

        u "..."

        u "I'm leaving."

        scene v16s3_5b
        with dissolve

        ri "Haha, no! I'm sorry! I'll make it up to you some other time, I promise."

        scene v16s3_5c
        with dissolve

        u "You better! I risk my life for you and there's no ice cream in the end? What's a guy to do?"

        scene v16s3_5b
        with dissolve

        ri "Yeah, yeah. Poor you... *Giggles*"

    scene v16s3_6 # TPP. MC throwing the icepack off somewhere, MC slight smile, mouth closed, Riley slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v16s3_5d # FPP. MC no longer holding the icepack, MC looking at Riley, Riley looking at MC, Riley slight smile, mouth open.
    with dissolve

    ri "I'm glad you came home with me."

    scene v16s3_5e # FPP. MC no longer holding the icepack, MC looking at Riley, Riley looking at MC, Riley slight smile, mouth cloesd.
    with dissolve

    u "Me too."

    if riley.relationship >= Relationship.FWB: # [Checkpoint 1.1]
        scene v16s3_5d
        with dissolve

        ri "The way you fought for me... I've never been so..."

        scene v16s3_5f # FPP. MC looking at Riley, Riley looking at MC, Riley winking, slight smile, mouth open.
        with dissolve

        ri "Turned on. By like, fighting... Haha."

        scene v16s3_5e
        with dissolve

        u "Ha, yeah?"

        scene v16s3_5d
        with dissolve

        ri "Yeah..."

        scene v16s3_7 # FPP. MC looking down and seeing Riley's hand on his thigh.
        with dissolve

        pause 1.5

        scene v16s3_5d
        with dissolve

        ri "It just shows how much you really care about me."

        scene v16s3_5e
        with dissolve

        u "I was just doing what any good guy would've done."

        scene v16s3_5d
        with dissolve

        ri "Well, now it's my turn..."

        ri "I want to show you how much I care about you."

        scene v16s3_5g # FPP. MC looking at Riley, Riley leaning closer and pucking her lips.
        with dissolve

        menu:
            "Kiss her":
                $ add_point(KCT.BOYFRIEND)

                jump v16s3a

            "Too tired":
                $ add_point(KCT.BRO)

                scene v16s3_5h # FPP. MC looking at Riley, Riley looking at MC, Riley slight frown, mouth closed.
                with dissolve

                u "Sorry, Riley... After the day I've had, and the fight with Tom, I just want to get some rest."

                scene v16s3_5i # FPP. MC looking at Riley, Riley looking at MC, Riley slight frown, mouth open.
                with dissolve

                ri "Oh, yeah. Okay... I understand."

                if aubrey_riley_awkward:
                    scene v16s3_5d
                    with dissolve

                    ri "I guess that means we can talk about Aubrey."

                    scene v16s3_5e
                    with dissolve

                    u "Well, she is one of your favorite subjects."

                    scene v16s3_5d
                    with dissolve

                    ri "Haha, it's not like that! I just..."

                    ri "I just wanted to say that I understand where she was coming from about the polygamy thing."

                    if aubrey_boyfriend_threesome:
                        ri "But I remember her saying something about an old boyfriend of hers turning down a threesome, and she was angry about it."

                        scene v16s3_5e
                        with dissolve

                        u "Yeah, it seems she has a very different view on threesomes now."

                        scene v16s3_5d
                        with dissolve

                        ri "Yeah, people change, I guess. It's just a little confusing, you know..."

                        ri "You think you have a good understanding of someone and what they want, and then..."

                        scene v16s3_5e
                        with dissolve

                        u "Humans. We're all a little unpredictable at times."

                        scene v16s3_5d
                        with dissolve

                        ri "Yeah, you're right."

                    scene v16s3_5d
                    with dissolve

                    ri "I'll just move on from it all."

                    scene v16s3_5e
                    with dissolve

                    u "Yeah, that's probably for the best."

        # [End of Checkpoint 1.1. Continues to Checkpoint 2]

    else: # [Checkpoint 1.2]
        scene v16s3_5d
        with dissolve

        ri "I don't want to think about Tom anymore."

        scene v16s3_5e
        with dissolve

        u "I bet. Neither do I."

        scene v16s3_5d
        with dissolve

        ri "I've been meaning to ask you about Amber, actually. How's she doing?"

        if not v14_amber_clean:
            scene v16s3_5e
            with dissolve

            u "As crazy as ever, haha. She's started performing at a strip club."

            scene v16s3_5d
            with dissolve

            ri "No way!"

            scene v16s3_5e
            with dissolve

            u "Yup. I can't make it up. Apparently she loves it too."

            scene v16s3_5d
            with dissolve

            ri "Well, she's got the body for it..."

            scene v16s3_5e
            with dissolve

            u "Ha, true."

            scene v16s3_5d
            with dissolve

            ri "And the attitude. *Chuckles* I'm sure she's making good money."

        else:
            scene v16s3_5e
            with dissolve

            u "Well, she's stopped with all the drugs, so..."

            scene v16s3_5d
            with dissolve

            ri "Oh, wow! Sounds like she's really turned a corner."

            scene v16s3_5e
            with dissolve

            u "Yeah, she's doing great. It's different, but it's a good difference."

        scene v16s3_5e
        with dissolve

        u "Why are you asking about her?"

        scene v16s3_5d
        with dissolve

        ri "Oh, I was just thinking about her the other day..."

        ri "It'd be nice to hang out with her soon. It's been a while."

        scene v16s3_5e
        with dissolve

        u "I'm sure she'd love to, but she might try to talk you into getting a job, haha."

        scene v16s3_5d
        with dissolve

        ri "Ha, that's fine because I've actually been thinking about getting one."

        scene v16s3_5e
        with dissolve

        u "Really?"

        scene v16s3_5d
        with dissolve

        ri "Yeah, I mean... I'm not stretching for cash or anything, I just want to have a hobby, or..."

        ri "I want to be involved somewhere and have a routine, I think. Sometimes you need that."

        scene v16s3_5e
        with dissolve

        u "I can see where you're coming from, yeah."

    # [End of Checkpoint 1.2. Continues to Checkpoint 2]

    # [Checkpoint 2]

    scene v16s3_5e
    with dissolve

    u "Well, it's getting late, so think I'll head home, get into bed, and pass the fuck out. *Laughs*"

    if not v16_wintom:
        scene v16s3_5d
        with dissolve

        ri "Yeah, you seem okay. Just a little shaken."

        scene v16s3_5e
        with dissolve

        u "It doesn't take long for me to bounce back from a beating, haha."

        scene v16s3_5d
        with dissolve

        ri "Ah, so this happens often. *Giggles*"

    else:
        scene v16s3_5d
        with dissolve

        ri "Well, I would say \"be safe\", but I think you know how to defend yourself..."

        scene v16s3_5e
        with dissolve

        u "Haha, yup! I've got two fists and a couple of brain cells left... I'll be fine."

        scene v16s3_5d
        with dissolve

        ri "*Laughs*"

    scene v16s3_5e
    with dissolve

    u "(Should I mention Tom again?)"

    menu:
        "Reassure her":
            u "And don't worry anymore about Tom. We'll make sure he doesn't bother you again."

            scene v16s3_5d
            with dissolve

            ri "Okay. I'll try my best. Thanks, [name]."
            
        "Don't bring it up":
            scene v16s3_5e
            with dissolve

            u "(Don't want to put her head in a spiral.)"

            scene v16s3_5d
            with dissolve

            ri "Hope you sleep well, goodnight!"

            scene v16s3_5e
            with dissolve

            u "Yeah, you too. Night, Riley."

    scene v16s3_8 # TPP. Show MC and Riley sitting on the bed and hugging.
    with dissolve

    pause 0.75

    scene v16s3_9 # TPP. Show MC walking towards the dorm door to leave, slight smile, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/dooropen.mp3"

    scene v16s3_10 # TPP. Show MC opening the door and leaving, slight smile, mouth closed.
    with dissolve
    play sound "sounds/dooropen.mp3"
    pause 0.75

    scene v16s3_11 # TPP. Shot of just the door closed.
    with dissolve

    pause 0.75

    jump v16s4
# SCENE 41a: APES Meeting
# Locations: Apes Living Room
# Characters: GRAYSON (Outfit: 3), MC (Outfit: 1), CAMERON (Outfit: 3), RYAN (Outfit: 1)
# Time: Morning

label v14s41a:
    scene v14s41a_1 # TPP. Show mc waking up in bed shocked expression, mouth open
    with fade

    gr "[name!u]! GET DOWN HERE!"

    play music "music/v13/Track Scene 10.mp3" fadein 2

    scene v14s41a_1a # TPP. same as v14s41a_1 mc is sitting on the side of his bed, slightly mad, mouth closed
    with dissolve

    u "(The fuck?)"

    scene v14s41a_1b # TPP. same as v14s41a_1a mc has gotten out of bed and is putting on pants
    with dissolve

    pause 0.75

    scene v14s41a_2 # TPP. mc is coming down the apes frat house stairwell, putting on his shirt
    with dissolve

    pause 0.75

    scene v14s41a_3 # FPP. mc stands in between Ryan on his left and Cameron on his right, Grayson is standing next to the TV in the Apes Frat House Living Room, the TV is off, Ryan has no expression, mouth closed, Cameron has a slightly annoyed expression mouth closed, Grayson has a slight smile mouth closed, all of them are looking at mc
    with dissolve

    u "What's happening?"

    scene v14s41a_3a # FPP. same as v14s41a_3 Ryan and Cameron are now looking at Grayson, Grayson's mouth is open
    with dissolve

    gr "Frat meeting!"

    # Make sure variable is Chloe Seduced Grayson if: chloe seduced grayson

    if v14s31bTrustChloe:
        scene v14s41a_4 # FPP. Mc is looking to his right and sees a close-up shot of just Cameron, looking at Grayson, slightly annoyed, mouth open.
        with dissolve

        ca "You said there was big news, so let's get to it before my class starts."

        scene v14s41a_5 # FPP. Mc is looking straight ahead and see's a full body shot of Grayson, Grayson is standing just to the side and within reach of the TV without blocking the TV's screen, Grayson has a half angry expression, mouth open, looking at Cameron
        with dissolve

        gr "Don't fucking rush me, Cam."

        scene v14s41a_4a # FPP. same as v14s41a_4 close up shot of just Cameron rolling his eyes, fully annoyed, mouth open
        with dissolve

        pause 0.75

        scene v14s41a_5a # FPP. Grayson is looking at MC, slight smile, mouth open
        with dissolve

        gr "Anyway, I got some news about the Chicks race."

        scene v14s41a_4
        with dissolve

        ca "Seriously? That's what we're here for?"

        scene v14s41a_5
        with dissolve

        gr "We're here for whatever I say we're here for. I don't know what's gotten into you lately, man."

        scene v14s41a_4b # FPP. same as v14s41a_4 Cameron avoids looking at Grayson, no expression, mouth closed
        with dissolve

        pause 0.75

        scene v14s41a_6 # FPP. MC looks to his left and see's a close-up shot of just Ryan looking at Grayson, Ryan's mouth is open, Ryan has a slight smile
        with dissolve

        ry "Umm... Anyway, if you're talking about the race that means you must've found a way to take Chloe down. Ha!"

        scene v14s41a_5b # FPP. same as v14s41a_5a Grayson is looking at Ryan, slight smile, mouth open
        with dissolve

        gr "Opposite of that, actually. Despite the rough past that Chloe and I have, we will not be sabotaging her in the race."

        scene v14s41a_6a # FPP. same as v14s41a_6 Ryan is slightly confused
        with dissolve

        ry "Not at all?"

        scene v14s41a_5b
        with dissolve

        gr "Not at all."

        scene v14s41a_6b # FPP. same as v14s41a_6 Ryan is slightly angry
        with dissolve

        ry "But... Why the fuck not?"

        scene v14s41a_5c # FPP. same as v14s41a_5 Grayson is looking at Ryan, grayson is slightly annoyed
        with dissolve

        gr "Because I said so, that's why."

        scene v14s41a_6a
        with dissolve

        ry "Yeah, but like... Why are you saying so? You said it yourself, you guys have a rough past."

        scene v14s41a_4
        with dissolve

        ca "You just told us last week to get ready for some sabotage, ha."

        scene v14s41a_5c
        with dissolve

        gr "Look... Going against Chloe here isn't a good look for the Apes."
        gr "If she ends up winning and we went after her, it'd backfire instantly and I don't want that. Make sense?"

        scene v14s41a_6
        with dissolve

        ry "Makes perfect sense."

        scene v14s41a_4
        with dissolve

        ca "I guess."

        scene v14s41a_3a
        with dissolve

        gr "Good, so everyone's clear that the Apes are neutral. Now, go do what you gotta do."

        scene v14s41a_7 # TPP. Close up of mc, slightly annoyed, mouth close, walking out of the living room
        with dissolve

        u "(Made a big scene just to say that? *Sighs* I gotta get to class.)"

        scene v14s41a_8 # TPP. outside view of the Apes Frat House, MC is walking out of the front door, no expression, mouth closed
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v14s43

    else:
        scene v14s41a_5d # FPP. same as v14s41a_5a Grayson has a devlish full smile, looking at MC, mouth closed
        with dissolve

        pause 0.75

        scene v14s41a_4
        with dissolve

        ca "We're all here now, what's the news?"

        scene v14s41a_5e # FPP. same as v14s41a_5d Grayson is looking at Cameron, mouth open
        with dissolve

        gr "It's time for us to have some fun."

        scene v14s41a_6
        with dissolve

        ry "This is about the Chicks race, isn't it?"

        scene v14s41a_5f # FPP. same as v14s41a_5a Grayson looks towards his pants and pulls his phone from his pocket
        with dissolve

        gr "Heh..."

        scene v14s41a_6c # FPP. same as v14s41a_6 Ryan increases to a full smile, mouth open
        with dissolve

        ry "Fuck yeah! I've been waiting for this."

        scene v14s41a_5g # FPP. same as v14s41a_5f Grayson holds his phone in front of him chest level, Grayson is looking at Ryan, half smile, mouth open
        with dissolve

        gr "The image I have on this phone is the one shot we needed to knock Chloe down a peg."

        scene v14s41a_6c
        with dissolve

        ry "Oh shit, I gotta see this."

        scene v14s41a_5h # FPP. same as v14s41a_5g Grayson looks at the TV screen and reaches up to turn on the TV.
        with dissolve

        gr "I'm gonna project it, get ready."

        scene v14s41a_5i # FPP. same as v14s41a_5h TV screen is on and says phone connected, Grayson is looking down at his phone, and tapping the screen
        with dissolve

        pause 0.75

        scene v14s41a_3b # FPP. same as v14s41a_3a A picture of Chloe in very seductive lingerie is projected on the TV screen, Ryan is looking at the TV screen and throws both his hands up in the air in excitement full smile mouth open, Cameron is looking, laughing, and pointing at the TV screen, Grayson is holding his phone in one hand with his other raised at the TV screen palm outward with a smug/grinning look on his face mouth closed
        with dissolve

        pause

        scene v14s41a_5j # FPP. same as v14s41a_5i Grayson is looking at MC, Grayson is still holding his phone, the image from v14s41a_3b is now on the TV screen behind Grayson, Grayson has a smug/grinning expression, mouth closed
        with dissolve

        u "(Oh... shit!)"

        if chloe.relationship >= Relationship.GIRLFRIEND:
            scene v14s41a_9 # FPP. A close up view of just the TV with the image from v14s41a_3b being projected on the screen
            with dissolve

            u "Wait..."

        scene v14s41a_5h
        with dissolve

        pause 0.75

        scene v14s41a_5f
        with dissolve

        pause 0.75

        scene v14s41a_6c
        with dissolve

        ry "Holy... Ffffffuck yeah, dude! How the hell did you get that?"

        scene v14s41a_5b
        with dissolve

        gr "It's from back in the day when we used to date, but that's not the point. The point is, this is what's gonna fuck Chloe up and make Lindsey win."

        scene v14s41a_4
        with dissolve

        ca "What does Lindsey winning have anything to do with the Apes?"

        scene v14s41a_5e
        with dissolve

        gr "Glad you asked. The Greek life is turning a new page and we can either turn with it or get left behind."

        scene v14s41a_5a
        with dissolve

        gr "When Lindsey wins, she's not going to rock with frats like ours if we don't support her in some way now."

        scene v14s41a_6
        with dissolve

        ry "Makes sense."

        scene v14s41a_5a
        with dissolve

        gr "Good. So I'm gonna send this picture to all of you, and I want you to post it to your Kiwiis right now."

        scene v14s41a_5d
        with dissolve

        u "Wait, isn't that a bit far?"

        scene v14s41a_5k # FPP. same as v14s41a_5 Grayson is looking at MC, fully angry expression, mouth open
        with dissolve

        gr "Okay fine. Everyone except pussy boy here, post it."

        gr "Happy now?"

        scene v14s41a_5l # FPP. same as v14s41a_5k Grayson's mouth is closed
        with dissolve

        menu:
            "Stay quiet":
                $ add_point(KCT.TROUBLEMAKER)

                if v14_chloe_cameron:
                    u "(Even Cameron isn't speaking up, and he has an incentive to help Chloe win. I shouldn't press this further...)"

                scene v14s41a_5a
                with dissolve

                gr "Post the pictures when I send 'em to you."

                scene v14s41a_5d
                with dissolve

                u "*Sighs* Whatever."

            "Stand up for Chloe":
                $ add_point(KCT.BOYFRIEND)
                $ v14s41a_standup = True

                scene v14s41a_5l
                with dissolve

                u "I don't think anyone should be posting it."

                scene v14s41a_5k
                with dissolve

                gr "Why?"

                scene v14s41a_5l
                with dissolve

                u "If you don't want her to win then fine, we'll stay out of the race."
                u "But sabotaging her isn't fair, it's not cool, and this photo is a complete invasion of privacy."

                scene v14s41a_6d # FPP. same as v14s41a_6b Ryan is now looking at mc, slightly angry, mouth open
                with dissolve

                ry "Oh my god, here we go..."

                scene v14s41a_6e # FPP. same as v14s41a_6d Ryan's mouth is closed
                with dissolve

                u "What?"

                scene v14s41a_6d
                with dissolve

                ry "You're supporting Chloe all over again."

                scene v14s41a_6e
                with dissolve

                u "I just don't think it's fair."

                scene v14s41a_5k
                with dissolve

                gr "Give me one specific reason why we shouldn't post this picture, [name]."

                scene v14s41a_5l
                with dissolve

                menu:
                    "Bad look for Apes":
                        $ add_point(KCT.BRO)
                        $ v14_ApesPostChloePics = False

                        u "You of all people should know that doing something like this is gonna give us a bad look."
                        u "Putting something out there publically like that is just asking for a shitty situation."

                        scene v14s41a_4c # FPP. same as v14s41a_4 Cameron is looking at MC, no expression, mouth open
                        with dissolve

                        ca "Fair point."

                        scene v14s41a_5k
                        with dissolve

                        gr "*Sighs* Fine! Fuck it all, forget it."

                        scene v14s41a_3c # TPP. same as v14s41a_3 Grayson storms off with his phone, walking between Mc and Cameron, Grayson not looking at anyone, Grayson is half angry mouth closed, Ryan, Mc, and Cameron no expression, mouth closed all looking at Grayson
                        with dissolve

                        u "Okay..."

                    "Not fair to Chloe":
                        $ add_point(KCT.BOYFRIEND)

                        u "As I said, it's not fair to Chloe, having that photo posted all over Kiwii."
                        u "And especially by all of her ex-boyfriend's frat members, it would be a horrible experience for her."

                        scene v14s41a_5a
                        with dissolve

                        gr "*Laughs* We don't give a fuck about all that. Feelings don't mean shit, [name]."

                        if kct == "confident" or v14_chloe_cameron:
                            if not v14_chloe_cameron:
                                call screen kct_popup
                        
                            $ v14_ApesPostChloePics = False
                            scene v14s41a_6a
                            with dissolve

                            ry "Feelings don't mean shit...?"

                            scene v14s41a_5c
                            with dissolve

                            gr "What are you whispering about, roastie?"

                            scene v14s41a_5l
                            with dissolve

                            u "Feelings don't mean shit. That's what he said."

                            scene v14s41a_5c
                            with dissolve

                            gr "Exactly."

                            scene v14s41a_4
                            with dissolve

                            ca "I mean, fuck Chloe. And honestly, fuck Lindsey too. I don't really give a shit about who wins."

                            call screen kct_popup
                            scene v14s41a_4d # FPP. same as v14s41a_4 Cameron has a concerned expression
                            with dissolve

                            ca "But I would give a shit if someone posted a photo like that of me, or even worse... Sam. Not sure if I can do this one, man."

                            if v14_chloe_cameron:
                                u "(Thanks for the help, bro. Looks like that pep talk got to him...)"

                            scene v14s41a_5
                            with dissolve

                            gr "*Scoffs* Okay. Great. I'll do it myself then."

                            scene v14s41a_6f # FPP. same as v14s41a_6 Ryan has a concerned expression
                            with dissolve

                            ry "Nah, that'll look bad for all of us. You really should-"

                            scene v14s41a_5m # FPP. same as v14s41a_5k Grayson is looking at Ryan
                            with dissolve

                            gr "FUCK! We won't do it then! Happy?!"

                            scene v14s41a_5l
                            with dissolve

                            u "Yes."

                            scene v14s41a_3c
                            with dissolve

                            pause 0.75

                        else:
                            call screen kct_popup(required_kct="confident")
                            scene v14s41a_5a
                            with dissolve

                            gr "Post the pictures when I send 'em to you."

                            scene v14s41a_3c
                            with dissolve

                            u "*Sighs*"

    scene v14s41a_7
    with dissolve

    u "(Off to class.)"

    scene v14s41a_8
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s43
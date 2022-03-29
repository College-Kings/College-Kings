# SCENE 67: Polly Acoustic Event in Cafeteria
# Locations: School Cafeteria
# Characters: POLLY (Outfit: Concert Outfit), LINDSEY (Outfit: 3), MC (Outfit: 2), CROWD (Outfit: Random), KOBE (Outfit: 1), AUTUMN (Outfit: 2), RILEY (Outfit: 3), PENELOPE (Outfit: 2)
# Time: Thursday Evening

label v16s67:
    scene v16s67_1 # TPP. The whole room is candlelit as the power outage is still going on. People (no expressions, and mouths open or closed, and looking at renderer's discretion) are sat at the tables. Penelope (no expression, mouth is closed, looking at the stage) is sitting at the front. Everyone is watching as Polly (slight smile, mouth is closed, looking at the crowd) enters the room from another door, carrying an acoustic guitar
    with dissolve

    pause 0.75

    if not v16s12_chloe_planboard_decide_newspaper_cover: # -if MC walked with Lindsey in Scene 66

        scene v16s67_2 # TPP. MC and Lindsey (both slight smiles, mouths are closed, looking towards the stage (stage is not shown)) enter the cafeteria and stay standing by the main entrance door to watch for the moment. At least 5 other people (no expressions, mouths open or closed, and looking at the (stage is not shown)) leaning against the wall in the background
        with dissolve

        pause 0.75

    else: # -if MC walked alone in Scene 66

        scene v16s67_2a # TPP. same as v16s67_2 just remove Lindsey from the render
        with dissolve

        pause 0.75

    scene v16s67_3 # FPP. Camera angle is a side view of the stage with only the front row also visibly shown, Show Polly (slight smile, mouth is open, looking into the crowd) up on the stage, her guitar is sitting on a guitar stand on stage, and Penelope (slight smile, mouth is closed, looking at Polly) sitting in the front row with one empty seat next to her, with a couple random people (slight smiles, mouths are closed, looking at Polly)
    with dissolve

    polly "Hey everyone! I'm so happy I found time in my schedule to play a couple of songs for you."

    scene v16s67_3a # FPP. Camera angle is a side view of the stage with only the front row also visibly shown, Show Polly (slight smile, mouth is open, looking at Penelope) up on the stage extending her arm and hand palm up towards Penelope, and Penelope (slight smile, mouth is closed, looking at Polly) sitting in the front row with one empty seat next to her, with a couple random people (slight smiles, mouths are closed, looking at Polly)
    with dissolve

    polly "You all have my friend Penelope here for this."

    scene v16s67_3b # FPP. Camera angle is a side view of the stage with only the front row also visibly shown, Show Polly (slight smile, mouth is open, looking at Penelope), and Penelope (slight smile/shy expression, mouth is closed, trying to hide fer hace) sitting in the front row with one empty seat next to her, with a couple random people (slight smiles, mouths are closed, looking at Penelope)
    with dissolve

    pause 0.75

    scene v16s67_3
    with dissolve

    polly "Obviously, it sucks that we don't have power right now, but the show must go on, as they say. *Chuckles*"

    polly "And luckily, I always have my trusty acoustic guitar with me wherever I go."

    if not v16s12_chloe_planboard_decide_newspaper_cover and v16s28_lindsey_pb_intereview_polly_choice: # -if MC is with Lindsey but did not go to Polly's hotel room

        scene v16s67_4 # FPP. Show just Lindsey (slight smile, mouth is open, looking at MC) 
        with dissolve

        li "Oh, Penelope's over there! I'm gonna go sit with her so we can do some hardcore fangirling."

        scene v16s67_4a # FPP. Show just Lindsey (slight smile, mouth is closed, looking at MC) 
        with dissolve

        u "Haha, okay. Have fun."

        scene v16s67_2b # TPP. same as v16s67_2 Just MC is standing still and Lindsey is walking away
        with dissolve

        pause 0.75

    elif not v16s12_chloe_planboard_decide_newspaper_cover and not v16s28_lindsey_pb_intereview_polly_choice: # -if MC is with Lindsey and they went to Polly's hotel room

        scene v16s67_3
        with dissolve

        polly "Before I play my first song, I just want to say a few words about a girl I met earlier. Her name was Lindsey..."

        scene v16s67_4
        with dissolve

        li "Oh, my God! It's happening!"

        if v16s59_polly_endorse_lindsey: # -if MC and Lindsey went to Polly's hotel room and succeeded

            scene v16s67_3
            with dissolve

            polly "I heard that she's running for President of her sorority, and I just wanted to say..."

            polly "If I was a member of the Chicks, she'd have my vote. So, if you're eligible to vote for Lindsey, I suggest you do it."

            $ set_presidency_percent( v14_lindsey_popularity + 5) # -(LindseyPopularity gains 5)

            scene v16s67_4b # FPP. Show just Lindsey (full smile, mouth is open with excitement, looking at MC) 
            with dissolve

            u "(Holy shit! Lindsey's got this presidency in the fucking bag.)"

            scene v16s67_3
            with dissolve

            polly "You won't be disappointed."

            scene v16s67_4b
            with dissolve

            li "She said it! She actually said it and she loves me!"

            scene v16s67_4a
            with dissolve

            u "Easy now... I don't think she said anything about love, haha."

            scene v16s67_4b
            with dissolve

            li "We'll be best friends forever after this. Just wait!"

            scene v16s67_4
            with dissolve

            li "I'm gonna go sit with Penelope so we can freak out together."

            scene v16s67_4a
            with dissolve

            u "Haha, okay, go ahead. I'm not much of a fan girl."

            scene v16s67_4c # FPP. Show just Lindsey (slight smile, mouth is open booing MC, looking at MC) 
            with dissolve

            li "Booo!"

            scene v16s67_2b
            with dissolve

            pause 0.75

        else: # -if MC and Lindsey went to Polly's hotel room and failed

            scene v16s67_3
            with dissolve

            polly "I love all my fans, but there's a line between love and... um... obsession?"

            scene v16s67_4d # FPP. Show just Lindsey (slight scared expression, mouth is closed, looking at MC) 
            with dissolve

            u "(Oh, shit...)"

            scene v16s67_3
            with dissolve

            polly "So, Lindsey, if you're here tonight, please don't try to kidnap me. I have pepper spray. *Chuckles*"

            scene v16s67_3c # FPP. same as v16s67_3 but the entire crowd is laughing and looking at Polly
            with dissolve

            pause 0.75

            $ set_presidency_percent (v14_lindsey_popularity -3) # (LindseyPopularity loses 3)

            scene v16s67_4e # FPP. Show just Lindsey (fully shocked expression, mouth is open, looking at MC) 
            with dissolve

            li "Wha... What? Why would she say that?"

            scene v16s67_4f # FPP. Show just Lindsey (slightly sad expression, mouth is closed, looking at MC) 
            with dissolve

            u "I mean, we did probably make her uncomfortable at the hotel. Maybe she's just nervous?"

            scene v16s67_4g # FPP. Show just Lindsey (slightly sad expression, mouth is open, looking at MC) 
            with dissolve

            li "But... I love her...?"

            scene v16s67_3
            with dissolve

            polly "But hey, no hard feelings. You must be a hardcore fan of mine if you can track me down at a private hotel and knock on my door uninvited, ha."

            scene v16s67_2c # TPP. same as v16s67_2 MC (no expression, mouth is closed, looking at Lindsey,) Lindsey (shocked expression, mouth is open, looking at the people looking at her,) 2 random characters (slight smiles, 1 mouth closed 1 is open, looking at Lindsey) are speaking with each other with the 1 with their mouth open pointing at Lindsey, 2 random characters are (laughing, looking, and pointing at Lindsey,) the 5th random character (slight smile, mouth is closed, looking at Lindsey) has a cellphone out and is recording Lindsey's reaction 
            with dissolve

            pause 0.75

            scene v16s67_4e
            with dissolve

            li "She's going to kill my campaign! I need to go explain this to the Chicks before they hear it themselves. Fuck!"

            scene v16s67_2d # TPP. same as v16s67_2c except Lindsey (her back is turned to the render) is now running out of the cafeteria
            with dissolve

            u "(Damn, we never should've gone to that hotel.)"

        # -Regardless of all that-

    scene v16s67_3
    with dissolve

    polly "Now, let's get into my first song!"

    polly "This one's called Sunshine."

    scene v16s67_3d # FPP. same as v16s67_3 Polly (slight smile, mouth is closed, looking at her guitar) grabs her Guitar, The crowd including Penelope all stand up and start cheering all looking at Polly
    with dissolve

    crowd "*Cheering*"

    scene v16s67_5 # FPP. Camera angle is a side view of just the stage and Polly, Close up shot of Polly (singing, mouth open, looking into center crowd)
    with dissolve

    polly "*Singing* The sun shines through my window on a rainy day..."

    scene v16s67_5a # FPP. Camera angle is a side view of just the stage and Polly, Close up shot of Polly (singing, mouth open, looking towards her left into the crowd)
    with dissolve

    polly "*Singing* And then I follow the double rainbow all the way..."

    scene v16s67_5b # FPP. Camera angle is a side view of just the stage and Polly, Close up shot of Polly (singing, mouth open, looking towards her right into the crowd)
    with dissolve

    polly "*Singing* To your heeeart! To your heeeart, my love! Yeah, yeah, yeah..."

    scene v16s67_2e # TPP. same as v16s67_2a Except Kobe (sarcastic/smirking expression, mouth is closed, looking towards the stage (stage is still not shown)), a rocker dude with long hair, dark skin, and tattoos, wearing a band t-shirt, enters the room. He stands next to MC, watching Polly perform
    with dissolve

    pause 0.75

    scene v16s67_6 # FPP. Show just Kobe (sarcastic/smirking expression, mouth is open, looking towards the stage (stage is still not shown))
    with dissolve

    kobe "Oh, man... I had to come hear her for myself."

    scene v16s67_6a # FPP. Show just Kobe (sarcastic/smirking expression, mouth is closed, looking at MC)
    with dissolve

    u "Yeah? You like Polly?"

    scene v16s67_6b # FPP. Show just Kobe (slight angry expression, mouth is open, looking at MC)
    with dissolve

    kobe "*Scoffs* Are you serious? Are you even listening to her finger work on those strings?"

    scene v16s67_6c # FPP. Show just Kobe (sinister smile, mouth is open, looking at MC)
    with dissolve

    kobe "I should go up there and smash it into the ground. Put the poor thing out of its misery."

    scene v16s67_6d # FPP. Show just Kobe (slight angry expression, mouth is closed, looking at MC)
    with dissolve

    u "Ha, really? She sounds fine to me."

    scene v16s67_6b
    with dissolve

    kobe "Well, I'm a trained musician. You're obviously not."

    scene v16s67_6d
    with dissolve

    u "(I can play the harmonica, but you don't hear me bragging...)"

    scene v16s67_6c
    with dissolve

    kobe "My ears are finely tuned, and when she plays a chord, all I hear is a cat screaming."

    scene v16s67_5a
    with dissolve

    polly "*Singing* On cloudy days I wonder if you're thinking of me..."

    scene v16s67_6b
    with dissolve

    kobe "Fuck, man! This is so bad, haha!"

    scene v16s67_6c
    with dissolve

    menu:

        "Keep talking to him":

            scene v16s67_6e # FPP. Show just Kobe (sinister smile, mouth is closed, looking towards the stage (stage is still not shown)) takes out his phone and holds it up to film Polly (off camera)
            with dissolve

            pause 0.75

            scene v16s67_5a
            with dissolve

            polly "*Singing* Then the rain comes again, and I suddenly see..."

            scene v16s67_6e
            with dissolve

            u "Are you filming her?"

            scene v16s67_6f # FPP. Show just Kobe (sinister smile, mouth is open, looking at MC) still has his phone held up in the stages direction to film Polly (Not Shown)
            with dissolve

            kobe "Yeah, I need to post about this. Show my followers the trainwreck. Know what I mean?"

            scene v16s67_6e
            with dissolve

            u "How many followers do you have?"

            scene v16s67_6f
            with dissolve

            kobe "Fourteen, but it's growing quick. My numbers doubled in the last month. It takes time and hard work, my friend."

            scene v16s67_6e
            with dissolve

            u "Oh, yeah... Fourteen? You're doing pretty well. *Laughs*"

            scene v16s67_6f
            with dissolve

            kobe "Hey, don't make fun of me. You'll be in my comment section in a few months, just wait."

            scene v16s67_6e
            with dissolve

            u "What?"

            scene v16s67_6g # FPP. Show just Kobe (slight angry expression, mouth is open, looking at MC) still has his phone held up in the stages direction to film Polly (Not Shown)
            with dissolve

            kobe "If you can just shut up, I'm trying to record this video."

            scene v16s67_6h # FPP. Show just Kobe (slight angry expression, mouth is closed, looking at MC) still has his phone held up in the stages direction to film Polly (Not Shown)
            with dissolve

            u "You started this conversation!"

            scene v16s67_6g
            with dissolve

            kobe "And now I'm ending it!"

            scene v16s67_6e
            with dissolve

            u "(Fuck this guy!)"

        "Walk away":

            scene v16s67_6e
            with dissolve

            u "(I need to get away from this idiot.)"
        
            scene v16s67_2f # TPP. same as v16s67_2f Except MC (annoyed expression, mouth is closed) is walking away from Kobe (sinister smile, mouth is open, looking towards the stage) with his phone out recording Polly (Not Shown,) All the Random characters (slight smiles, mouths open, cheering on Polly, looking at the stage)
            with dissolve

            pause 0.75

    # -Regardless-

    scene v16s67_7 # TPP. MC (slight smile, mouth is closed, looking into the crowd) sees two spare seats One is next to Autumn (slight smile, mouth is open, looking at and cheering on Polly) And further away, the other one is next to Riley (slight smile, mouth is open, looking at and cheering on Polly,) Place random characters (all slight smiles, all mouth are opens, looking at and cheering on Polly) in other seats besides the spare seats to fill them up
    with dissolve

    menu:

        "Sit with Autumn":

            scene v16s67_8 # FPP. Camera Angle is a standing position, Show Auntumn (slight smile, mouth is open, looking at and cheering on Polly) sitting down
            with dissolve

            pause 0.75

            scene v16s67_9 # FPP. Camera Angle is a seated position, Show just Auntumn (slight smile, mouth is open, looking at and cheering on Polly) sitting down
            with dissolve

            u "Hey, Autumn. Enjoying the show?"

            scene v16s67_9a # FPP. Show just Auntumn (slight smile, mouth is open, looking at MC)
            with dissolve

            aut "Oh, hey! Yeah, so far."

            scene v16s67_10 # FPP. Show just Polly (singing, mouth is open, looking into the center crowd) up on stage singing and playing her guitar
            with dissolve

            polly "*Singing* To your heeeart! To your heeeart! Yeah, yeah, yeah..."

            if autumn.relationship == Relationship.KISS: # -if AutumnRS

                scene v16s67_9a 
                with dissolve

                aut "I'm happy you're here. I wanted to ask... Is that agreement of ours still on the table?"

                scene v16s67_9b # FPP. Show just Auntumn (slight smile, mouth is closed, looking at MC)
                with dissolve

                u "Agreement?"

                scene v16s67_9a
                with dissolve

                aut "Yeah... The sex?"

                scene v16s67_9b 
                with dissolve

                u "Oh, well... (Am I still interested in having sex with Autumn?)"

                scene v16s67_9b
                with dissolve

                menu:
                    "Yeah, I am":
                        $ v15s67_mc_remains_interested_autumn_sex = 2
                        
                        u "Yeah, I'm in if you are."

                        scene v16s67_9a
                        with dissolve

                        aut "Good. I wanted to talk about taking things beyond a kiss..."
                        
                        aut "Let's sort something out soon?"

                        scene v16s67_9b
                        with dissolve

                        u "Okay, yeah. We will."

                        scene v16s67_9a
                        with dissolve

                        aut "Great."

                    "Not anymore": # -this takes away AutumnRS, giving the players the option to back out if they want to-
                        $ autumn.relationship = Relationship.TRUST
                        $ v15s67_mc_remains_interested_autumn_sex = 1

                        scene v16s67_9b
                        #with dissolve

                        u "Not anymore...? I think I've changed my mind about being more than friends. I'm sorry."

                        scene v16s67_9a
                        with dissolve

                        aut "No, it's totally fine. That's exactly why I wanted to ask, haha."

                        aut "There were a lot of emotions flying that night and... Anyway, I'm glad we're on the same page."

                        scene v16s67_9b
                        with dissolve

                        u "Yeah, thank you. Me too."

            scene v16s67_10a # FPP. Show just Polly (singing, mouth is open, looking into left of center crowd) up on stage singing and playing her guitar
            with dissolve

            polly "*Singing* Rain, rain, is coming down..."

            scene v16s67_10b # FPP. Show just Polly (singing, mouth is open, looking into right of center crowd) up on stage singing and playing her guitar
            with dissolve

            polly "*Singing* The tears of my heart, hitting the ground."

            scene v16s67_10c # FPP. Polly (slight smile, mouth is closed, looking into the crowd) stops playing the guitar, but is still holding it
            with dissolve

            crowd "*Applause*"

            scene v16s67_10d # FPP. Polly (slight smile, mouth is open, looking into the crowd) stops playing the guitar, but is still holding it 
            with dissolve

            polly "Thank you! Thank you, guys!"

            polly "I wish I could stay longer, but this next song is going to be the last one for tonight."

            polly "It's called Take me away."

            scene v16s67_10a
            with dissolve

            polly "*Singing* Bring me cocktails on a beach, somewhere beautiful..."

            scene v16s67_9b
            with dissolve

            u "So how are things going at the dog shelter?"

            scene v16s67_9a
            with dissolve

            aut "Oh, amazing. Business has been booming! We're almost too busy, haha."

            scene v16s67_9b
            with dissolve

            u "Seeing a lot of the Dean?"

            scene v16s67_9a
            with dissolve

            aut "Haha, yeah. How weird? I still can't get over that."

            aut "It was such a badass move. The way she just came in, dealt with that guy, and then adopted Oscar?"

            scene v16s67_9b
            with dissolve

            u "Oh, I know. It was like she grew a heart right in front of my eyes."

            scene v16s67_9c # FPP. Show just Auntumn (full smile, mouth is open, looking at MC)
            with dissolve

            aut "*Laughs* She's a good person underneath that cold exterior."

            scene v16s67_9b
            with dissolve

            u "Apparently, yeah."

            if v16s52_aubrey_kiwii_post_for_donations: # -if Aubrey posted about donations in s52
                scene v16s67_9a
                with dissolve

                aut "And thanks to Aubrey's Kiwii post, we pulled in a lot of donations too. It was way more than I ever thought possible, haha."

                scene v16s67_9b
                with dissolve

                u "That's great to hear, I'm glad that little idea of mine worked... You're welcome by the way."

                scene v16s67_9c
                with dissolve

                aut "Haha, trying to take all the credit?"

                scene v16s67_9b
                with dissolve

                u "It's okay, you can just buy me a drink sometime."

                scene v16s67_9a
                with dissolve

                aut "Haha, okay, funny guy. One juice box, on me."

                scene v16s67_9b
                with dissolve

                u "*Sighs*... I'll take what I can get."

                scene v16s67_9c
                with dissolve

                aut "*Laughs*"

            elif v16s52_mc_dogshelter_kiwii_post or ( not v16s52_mc_dogshelter_kiwii_post and not v16s52_aubrey_kiwii_post_for_donations): # -if MC posted about donations or did sign spinning in s52

                scene v16s67_9a
                with dissolve

                aut "And we managed to get some donations. Not as much as I would've liked, but we raised a few extra dollars thanks to your efforts."

                scene v16s67_9b
                with dissolve

                u "Ha, well, at least it's something. I hope the dogs appreciate it."

                scene v16s67_9a
                with dissolve

                aut "They definitely do. I've never seen so many wagging tails inside of that place before until now."

                scene v16s67_9b
                with dissolve

                u "*Chuckles* That's cute."

            # -Regardless-

            scene v16s67_10a
            with dissolve

            polly "*Singing* I'm lying next to you..."

            scene v16s67_9a
            with dissolve

            aut "I think I actually prefer the acoustic version of this song."

            scene v16s67_9b
            with dissolve

            u "I guess that's a positive way to look at these power outages..."

            scene v16s67_9c
            with dissolve

            aut "Ha, yup! Every cloud has a silver lining."

            scene v16s67_11 # TPP. Show just MC and Autumn (both slight smiles, mouths are closed, looking at Polly) They continue watching, enjoying the music-
            with dissolve

            pause 0.75

        "Sit with Riley":

            scene v16s67_12 # FPP. Camera Angle is a standing position, Show Riley (slight smile, mouth is open, looking at and cheering on Polly) sitting down
            with dissolve

            pause 0.75

            scene v16s67_13 # FPP. Camera Angle is a seated position, Show just Riley (slight smile, mouth is open, looking at and cheering on Polly) sitting down
            with dissolve

            u "Is this seat taken?"

            scene v16s67_13a # FPP. Show just Riley (slight smile, mouth is open, looking at MC)
            with dissolve

            ri "Oh, hey! It is now."

            scene v16s67_10b
            with dissolve

            polly "*Singing* To your heeeart! To your heeeart! Yeah, yeah, yeah..."

            if "v16_riley" in sceneList: # -if Riley blowjob in Scene 3a
                scene v16s67_13b # FPP. Show just Riley (slight smile, mouth is closed, looking at MC)
                with dissolve

                u "By the way, I think I've just about recovered from that amazing blowjob now."

                scene v16s67_13c # FPP. Show just Riley (slight smile/seductive expression, mouth is open, looking at MC) raised eyebrow
                with dissolve

                ri "*Laughs* Oh, yeah? Does that mean you're ready for another one?"

                scene v16s67_13d # FPP. Show just Riley (smirking, mouth is closed, looking at MC)
                with dissolve

                u "Haha, right here? While Polly's singing?"

                scene v16s67_13a
                with dissolve

                ri "Keep it in your pants, tiger. Good things come to those who wait. *Chuckles*"

            # -Regardless of Riley blowjob in Scene 3a-

            scene v16s67_10b
            with dissolve

            polly "*Singing* Rain, rain, is coming down..."

            scene v16s67_10
            with dissolve

            polly "*Singing* The tears of my heart, hitting the ground."

            scene v16s67_10c
            with dissolve

            crowd "*Applause*"

            scene v16s67_10d
            with dissolve

            polly "Thank you, guys! Wow, you're amazing."

            polly "I wish I could stay longer, but this next song is going to be the last one for tonight."

            polly "It's called Take me away."

            scene v16s67_10
            with dissolve

            polly "*Singing* Bring me cocktails on a beach, somewhere beautiful..."

            scene v16s67_13b
            with dissolve

            u "I don't want to spoil the mood, but I must ask..."

            scene v16s67_13e # FPP. Show just Riley (no expression, mouth is closed, looking at MC)
            with dissolve

            u "Have you had any more trouble with Tom?"

            scene v16s67_13f # FPP. Show just Riley (no expression, mouth is open, looking at MC)
            with dissolve

            ri "Oh... him. No, I haven't even seen him on campus. Have you?"

            scene v16s67_13e
            with dissolve

            u "No. Fortunately."

            scene v16s67_13f
            with dissolve

            ri "I just hope that what happened was the beginning and the end of it."

            scene v16s67_13
            with dissolve

            u "Yeah, maybe he realized how much of a dick he was being."

            scene v16s67_13f
            with dissolve

            ri "I really hope so..."

            ri "Anyway, I don't want to think about it."

            scene v16s67_13a
            with dissolve

            ri "Let's enjoy the show!"

            scene v16s67_13b
            with dissolve

            u "Haha, great idea."

            scene v16s67_10b
            with dissolve

            polly "*Singing* I'm lying next to you and everything's wonderful..."

            scene v16s67_13a
            with dissolve

            ri "I love how it's all candlelit... It makes it feel so intimate."

            scene v16s67_13b
            with dissolve

            u "Yeah, it's a cozy vibe."

            scene v16s67_13a
            with dissolve

            ri "Exactly. I love it. It's like we have Polly all to ourselves."

            scene v16s67_14 # TPP. Show just MC and Riley (both slight smiles, mouths are closed, looking at Polly) They continue watching, enjoying the music-
            with dissolve

            pause 0.75

        # -Regardless of who MC sat next to-

    scene v16s67_10a
    with dissolve

    polly "*Singing* And now I'm back home, side by side with you..."

    scene v16s67_10
    with dissolve

    polly "*Singing* For the rest of our lives, what shall we do?"

    scene v16s67_10c
    with dissolve

    crowd "*Applause*"

    scene v16s67_10d
    with dissolve

    polly "Well, that's all the time I have for you guys. I've enjoyed this so much! I hope you have too."

    polly "Goodnight, everyone!"

    scene v16s67_10e # FPP. Show Just Polly (full smile, mouth is closed, looking into the crowd) waving to the crowd with one hand and holding her guitar with the other
    with fade
        
    pause 0.75

    scene v16s67_15 # TPP. Show MC (slight smile, mouth is closed, looking at the exit) walking towards the exit of the cafeteria alone, other random characters (slight smiles, mouths are closed) are also shown exiting the cafeteria
    with fade

    pause 0.75

    jump v16s68 # -Transition to Scene 68-
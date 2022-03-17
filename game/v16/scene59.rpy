# SCENE 59: Talk to Polly at her hotel room with Lindsey
# Locations: Hotel Hallway
# Characters: LINDSEY (Outfit: 3/ ROOM SERVICE UNIFORM), MC (Outfit: 2/ ROOM SERVICE UNIFORM), POLLY (Outfit: Ask Mozzart), BODYGUARD (Outfit: 1)
# Time: Thurdsay Afternoon

label v16s59:

    if v16s28_lindsey_pb_pretend_roomservice: # -if MC chose Pretend to be room service

        scene v16s59_1 # TPP. MC (slight smile, mouth closed, looking forward) and Lindsey (slight smile, mouth closed, looking forward) in hotel uniforms appear from a distance, walking along a hallway, past hotel room doors. They are wearing room service uniforms and MC is carrying a food tray with a domed lid covering the food-
        with dissolve

    else: # -if MC chose Show up as yourselves

        scene v16s59_1a # TPP. same as v16s59_1 MC (slight smile, mouth closed, looking forward) and Lindsey (slight smile, mouth closed, looking forward) walking along the hallway in regular clothes with no food tray-
        with dissolve

    # -Regardless of planning board choice, same dialogue/action for both unless stated-

    scene v16s59_2 # FPP. Show just Lindsey (slight smile, mouth open, looking at MC) from the shoulders up (check with mozzart for the clothes that will be shown on her shoulders since the image must relate to two different scenarios where they are wearing 2 different outfits), MC and Lindsey are walking side by side so her head is turned towards MC, but her body is facing forward
    with dissolve

    li "My friend said it's room seventy-three..."

    li "We've only got a few minutes while her bodyguard is on his break."

    scene v16s59_2a # FPP. Show just Lindsey (slight smile, mouth closed, looking at MC) from the shoulders up(check with mozzart for the clothes that will be shown on her shoulders since the image must relate to two different scenarios where they are wearing 2 different outfits) , MC and Lindsey are walking side by side so her head is turned towards MC, but her body is facing forward
    with dissolve

    u "Don't worry, we'll be quick."

    u "Here we are."

    if v16s28_lindsey_pb_pretend_roomservice:  # -if Pretending to be room service

        scene v16s59_3 # TPP. Full body image of (ROOM SERVICE UNIFORMS) MC (no expression, mouth is open, looking at Lindsey) scratching his chest with one hand, carrying the tray of food in the other, Lindsey (no expression, mouth is closed, looking at MC)
        with dissolve

        u "I appreciate your friend lending us these uniforms, but fuck, they're itchy."

        scene v16s59_3a # TPP. Full body image of (ROOM SERVICE UNIFORMS) MC (no expression, mouth is closed, looking at Lindsey) scratching his chest with one hand, carrying the tray of food in the other, Lindsey (no expression, mouth is open, looking at MC)
        with dissolve

        li "Yeah, I know. They feel like they're made out of cardboard."

        scene v16s59_3
        with dissolve

        u "More like sandpaper."

        u "*Laughs*"

        scene v16s59_3a
        with dissolve

        li "*Shudders* I can't even imagine what that would feel like. *Laughs*"

    # -Regardless of pretending to be room service-

    scene v16s59_4 # FPP. Show Lindsey (full smile, mouth open, looking at MC) just from the shoulders up (check with mozzart for clothing) standing just to the right side of the door, leave enough space so that when the door opens we can keep using the same render for when Polly is introduced. (Polly is not yet introduced at this point)
    with dissolve

    li "Oh, my God. I can't believe I'm about to meet Polly."

    scene v16s59_4a # FPP. Show Lindsey (full smile, mouth closed, looking at MC) just from the shoulders up (check with mozzart for clothing)
    with dissolve

    menu:

        "Calm Lindsey down":
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.BRO)

            scene v16s59_4a
            with dissolve

            u "Just relax. Let's not ruin this by going full fan girl."

            scene v16s59_4
            with dissolve

            li "Haha, I know. It's just a big deal for me, you know?"

            li "Like, a really big deal!"

            scene v16s59_4a
            with dissolve

            u "Just take a deep breath and relax."

            scene v16s59_4b # FPP. Show Lindsey (taking a deep breathe, mouth open, eyes closed) just from the shoulders up (check with mozzart for clothing)
            with dissolve

            li "*Deep breath*"

            scene v16s59_4
            with dissolve

            li "Well, I can't say that I did anything."

            scene v16s59_4a
            with dissolve

            u "Haha, worth a try, I'm just gonna knock now."

        "Just knock":
            $ v16s59_just_knock = True
            $ add_point(KCT.TROUBLEMAKER)

            scene v16s59_4a
            with dissolve

            u "(Lindsey's fine. I'll take the lead anyway.)"

    scene v16s59_5 # FPP. Show just MC's arm and hand in the render knocking on the door to Polly's room, (Polly is not shown yet)
    with dissolve

    pause 0.75

    scene v16s59_4c # FPP. Show Lindsey (full smile, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (no expression, mouth closed, looking at MC) is now shown in the doorway
    with dissolve

    pause 0.75

    scene v16s59_4d # FPP. Show Lindsey (full smile, mouth open, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth closed, looking at Lindsey)
    with dissolve

    li "*Squeaks* Hi, Polly!"

    scene v16s59_4e # FPP. Show Lindsey (full smile, mouth closed, looking at MC) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth closed, looking at MC)
    with dissolve

    u "(Really, Lindsey?!)"

    scene v16s59_4f # FPP. Show Lindsey (full smile, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth open, looking at MC)
    with dissolve

    polly "Um... Hi."

    if v13_penelope_backstage: # -if MC went backstage at Polly concert

        scene v16s59_4g # FPP. Show Lindsey (full smile, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (staring/thinking expression, mouth open, looking at MC) tilts her head and stares at MC, with a hand on her chin
        with dissolve

        pause 0.75

        scene v16s59_4h # FPP. Show Lindsey (full smile, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth open, looking at MC)
        with dissolve

        polly "Hang on... [name], right? You came backstage when I was in Amsterdam!"

        scene v16s59_4i # FPP. Show Lindsey (full smile, mouth closed, looking at MC) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth closed, looking at MC)
        with dissolve

        u "You remember me? I'm so touched!"

        u "(Touched? Now I'm the one fangirling...)"

        scene v16s59_4h
        with dissolve

        polly "Is this just some kind of weird coincidence?"

        scene v16s59_4i
        with dissolve

        menu:

            "Coincidence":
                $ add_point(KCT.BRO)

                scene v16s59_4i
                with dissolve

                u "Yeah, just a coincidence, I guess, haha."

                scene v16s59_4h
                with dissolve

                polly "How funny! Life can be so serendipitous sometimes!"

            "Came to find you":
                $ add_point(KCT.TROUBLEMAKER)

                scene v16s59_4i
                with dissolve

                u "In all honesty, we came to find you."

                scene v16s59_4f
                with dissolve

                polly "Oh... Okay. I have to say, that sounds a bit creepy... Ha."

    else: # -if mc did not meet Polly in Amsterdam

        scene v16s59_4f
        with dissolve

        polly "Can I... Help you guys with something?"


    if v16s28_lindsey_pb_pretend_roomservice: # -if Pretending to be room service

        scene v16s59_4d
        with dissolve

        li "We're here to deliver your meal!"

        if v13_penelope_backstage:  # TODO: Now clue what this means or how its different from meeting polly backstage so reusing it  # -if mc has already met Polly

            scene v16s59_4h
            with dissolve

            polly "You work here? *Giggles*"

            scene v16s59_4i
            with dissolve

            u "Uh, yeah. Temporarily."

        # -end if

        scene v16s59_4d
        with dissolve

        li "Sorry for the weird introduction, I'm just a really big fan and I-"

        scene v16s59_4f
        with dissolve

        polly "I didn't order any food."

        scene v16s59_4j # FPP. Show Lindsey (nervous smile, mouth open, looking at MC) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth closed, looking at MC)
        with dissolve

        li "Oh! It's a gift. Right, [name]?"

        scene v16s59_4f
        with dissolve

        polly "From who?"

        scene v16s59_4e
        with dissolve

        u "(Is the room getting smaller...?)"

        scene v16s59_4k # FPP. Show Lindsey (nervous smile, mouth open, looking at MC with intensity for him to say the "right" answer) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth closed, looking at MC)
        with dissolve

        li "[name]? Who was it again?"

        scene v16s59_4l # FPP. Show Lindsey (nervous smile, mouth closed, looking at MC with intensity for him to say the "right" answer) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth closed, looking at MC)
        with dissolve

        u "Uh, I... It's a gift from-"

        scene v16s59_4l
        with dissolve

        menu:

            "The hotel": # (SUCCESS)
                $ add_point(KCT.BRO)

                scene v16s59_4l
                with dissolve

                u "It's on the house. The chef sent it up."

                scene v16s59_7 # FPP. Show just a tray in one of MC's hand that has a piece of cake with fruit on it, and the lid of the tray in MC's other hand
                with dissolve

                pause 0.75

                scene v16s59_4h
                with dissolve

                polly "Wow, that smells really good... *Sniffs* Okay, I'll take it."

                scene v16s59_4m # FPP. Show Lindsey (full smile, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly has turned around inside of the room with her back turned to the render, she can be seen holding the tray of food and placing it inside of the room
                with dissolve

                pause 0.75

                scene v16s59_4h
                with dissolve

                polly "Is that all?"

                scene v16s59_4i
                with dissolve

                u "Well, there is one small thing."

                scene v16s59_4n # FPP. Show Lindsey (full smile, mouth open, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth closed, looking at Lindsey)
                with dissolve

                li "Yeah, so..."

                scene v16s59_4o # FPP. Show Lindsey (full smile, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth open, looking at Lindsey)
                with dissolve

                polly "Oh, come on! Out with it already, haha. An autograph? A selfie? What do you want?"

                scene v16s59_4n
                with dissolve

                li "I would love both of those but, we're students at SVC-"

                scene v16s59_4o
                with dissolve

                polly "Oh, I'll be swinging by later tonight."

                scene v16s59_4i
                with dissolve

                u "Yeah, we know, haha."

                scene v16s59_4n
                with dissolve

                li "I seriously can't wait for it!"

                li "The thing is, I'm currently campaigning to be president of my sorority, the Chicks, and it would mean the world to me if I could get an endorsement from you."

                scene v16s59_4o
                with dissolve

                polly "*Chuckles* An endorsement, huh? What would I have to do?"

                scene v16s59_4i
                with dissolve

                u "Just say a few words about how Lindsey is the best choice for the Chicks presidency, and she has your support, something like that?"

                scene v16s59_4h
                with dissolve

                polly "Well, I don't know anything about you... But you did go through all of this trouble just to ask, which shows a lot of determination."

                scene v16s59_4n
                with dissolve

                li "Yes, thank you."

                scene v16s59_4p # FPP. Show Lindsey (nervous expression, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth open, looking at Lindsey)
                with dissolve

                polly "...Or you're an insane stalker."

                scene v16s59_4q # FPP. Show Lindsey (nervous expression, mouth closed, looking at MC) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth closed, looking at MC)
                with dissolve

                u "Well-"

                scene v16s59_4p
                with dissolve

                polly "But I'll give you the benefit of the doubt, haha."

                scene v16s59_4o
                with dissolve

                polly "I think I can do that for you, sure."

                scene v16s59_4n
                with dissolve

                li "Oh, my God. Thank you so fucking much! I didn't think I could love you any more than I already do. *Laughs*"

                scene v16s59_4o
                with dissolve

                polly "Haha, it's no problem at all. Just don't make me regret it, ha."

                scene v16s59_8 # FPP. Show full body image of Lindsey (ROOM SERVICE UNIFORM) (nervous expression, mouth closed, looking at MC), and Polly's BodyGuard (PBG) (VERY STERN Expression, mouth closed, looking down at Lindsey) HUGE bodyguard appears directly behind Lindsey, if possible a panning up image like the chloe after hoco scene showing the size differnece between the body guard and Lindsey
                with dissolve

                pause 0.75

                scene v16s59_4r # FPP. Show Lindsey (nervous expression, mouth closed, looking at PBG) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth closed, looking at PBG), Polly's Bodyguard (PBG) (VERY STERN Expression, mouth open, looking at Polly) standing behind Lindsey closer to the doorway next to Polly
                with dissolve

                bdygd "Everything okay here, Polly?"

                scene v16s59_4s # FPP. Show Lindsey (nervous expression, mouth closed, looking at MC) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth closed, looking at MC), Polly's Bodyguard (PBG) (VERY STERN Expression, mouth closed, looking at MC) standing behind Lindsey closer to the doorway next to Polly
                with dissolve

                u "*Gulps* We were just leaving."

                scene v16s59_4t # FPP. Show Lindsey (full smile, mouth open, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth closed, looking at Lindsey), Polly's Bodyguard (PBG) (VERY STERN Expression, mouth closed, looking at Lindsey) standing behind Lindsey closer to the doorway next to Polly
                with dissolve

                li "Oh, shit. Okay. Yeah, thank you Polly!"

                scene v16s59_4u # FPP. Show Lindsey (full smile, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth open, looking at Lindsey), Polly's Bodyguard (PBG) (VERY STERN Expression, mouth closed, looking at Polly) standing behind Lindsey closer to the doorway next to Polly
                with dissolve

                polly "Ha, I'll see you later, guys! And thanks again for the delivery."

                scene v16s59_4v # FPP. Show Lindsey (full smile, mouth closed, looking at MC) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth closed, looking at MC), Polly's Bodyguard (PBG) (VERY STERN Expression, mouth closed, looking at MC) standing behind Lindsey closer to the doorway next to Polly
                with dissolve

                u "Bye, see you soon!"

                scene v16s59_9 # FPP. Close up shot of Polly with her back turned to the render, don't show her face, closing the hotel door
                with dissolve

                pause 0.75

                scene v16s59_4w # FPP. Show Lindsey (full smile, mouth closed, looking at the door) just from the shoulders up (check with mozzart for clothing), Polly is no longer in the doorway and the door is shut, Polly's Bodyguard (PBG) (VERY STERN Expression, mouth closed, looking at Lindsey) standing behind Lindsey closer to the doorway next to Polly
                with dissolve

                u "She's gone, Linds."

                scene v16s59_4x # FPP. Show Lindsey (full smile, mouth closed, looking at PBG) just from the shoulders up (check with mozzart for clothing), Polly is no longer in the doorway and the door is shut, Polly's Bodyguard (PBG) (VERY STERN Expression, mouth open, looking at Lindsey) standing behind Lindsey closer to the doorway next to Polly
                with dissolve

                bdygd "Yeah, and it's time for you to go too."

                scene v16s59_10 # TPP. (ROOM SERVICE UNIFORMS) Show MC (full smile, mouth closed, looking at Lindsey) and Lindsey (full smile, mouth closed, looking at MC) walking away from Polly's hotel room door. The door is still closed. Polly's Bodyguard (VERY STERN Expression, mouth closed, looking at Lindsey and MC) is standing next to Polly's hotel room door
                with dissolve

            ### ERROR: [End of Checkpoint 1.1. Continue to Checkpoint 2]

            "A fan": # (FAILURE)
                $ add_point(KCT.TROUBLEMAKER)

                scene v16s59_4e
                with dissolve

                u "A fan. They wanted us to deliver it specifically to you."

                scene v16s59_4d
                with dissolve

                li "That's right, yes."

                scene v16s59_7
                with dissolve

                pause 0.75

                scene v16s59_4f
                with dissolve

                polly "Oh, so it's... fan-made cake?"

                scene v16s59_4e
                with dissolve

                u "No, they got it from the store. A store. The ingredients I mean... *Coughs*"

                scene v16s59_4d
                with dissolve

                li "Right, but I went ahead and sliced it for you, and I've already had a piece to check for poison... *Awkward chuckle* It's delicious, and safe! Ha..."

                scene v16s59_4f
                with dissolve

                polly "That's very nice of you, to check. But I'm not very hungry right now, so."

                polly "You can just leave it on the floor, if that's okay. My bodyguard might have it when he comes back."

                scene v16s59_4d
                with dissolve

                li "O-of course."

                li "We're also here to ask for a favor."

                scene v16s59_4f
                with dissolve

                polly "A favor?"

                if v13_penelope_backstage: # -if mc met polly in Amsterdam

                    scene v16s59_4f
                    with dissolve

                    polly "Do I owe you something?"

                    scene v16s59_4e
                    with dissolve

                    u "Ha, no. Nothing like that."

                # -end if

                scene v16s59_4e
                with dissolve

                u "Lindsey's currently campaigning to be president of her sorority, the Chicks."

                scene v16s59_4d
                with dissolve

                li "And a little penny told us that you're performing at our college tonight,.. SVC?"

                scene v16s59_4f
                with dissolve

                polly "Oh... Yeah, I was just gonna swing by for a bit and sing for a friend."

                scene v16s59_4d
                with dissolve

                li "Yeah, exactly! We just thought that maybe you could endorse me. You know, say a few good things about my name or whatever."

                scene v16s59_4e
                with dissolve

                u "It doesn't have to be much."

                scene v16s59_4d
                with dissolve

                li "Seriously, anything will help."

                scene v16s59_4p
                with dissolve

                polly "I'm not really sure if that would be appropriate..."

                if v16s59_just_knock: # -if MC also chose Just knock

                    scene v16s59_4y # FPP. Show Lindsey (nervous expression, mouth open, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth closed, looking at Lindsey)
                    with dissolve

                    li "It's a a bit last minute so I know you can't dedicate a song to me or anything, but..."

                    scene v16s59_4q
                    with dissolve

                    u "(What the...?)"

                    scene v16s59_4y
                    with dissolve

                    li "Maybe you could just throw my name into one of your hits?"

                    scene v16s59_4z # FPP. Show Lindsey (nervous expression, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly ("weirded out" expression, mouth open, looking at Lindsey)
                    with dissolve

                    polly "Umm, I don't really do that sort of thing."

                    scene v16s59_4y
                    with dissolve

                    li "Well, you still have a few hours before you perform... Could write a song about a girl named Lindsey who-"

                    scene v16s59_4z
                    with dissolve

                    polly "Ha! No, I won't be doing that."

                    scene v16s59_4q
                    with dissolve

                    u "Yeah, I'm not sure if that's necessary."

                    scene v16s59_4y
                    with dissolve

                    li "Oh, okay. Well-"

                # -Regardless of if MC also chose Just knock-

                scene v16s59_8
                with dissolve

                pause 0.75

                scene v16s59_4r
                with dissolve

                bdygd "Everything okay here, Polly?"

                scene v16s59_4za # FPP. Show Lindsey (nervous expression, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth open, looking at PBG), Polly's Bodyguard (PBG) (VERY STERN Expression, mouth closed, looking at Polly) standing behind Lindsey closer to the doorway next to Polly
                with dissolve

                polly "Just a few fans who somehow found out where we're staying...."

                scene v16s59_4zb # FPP. Show Lindsey (nervous expression, mouth closed, looking at PBG) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth closed, looking at MC), Polly's Bodyguard (PBG) (slightly angry expression, mouth closed, looking at MC) now standing closer to Lindsey, with one hand cupping a fist made with his other hand
                with dissolve

                bdygd "Hmph."

                scene v16s59_4zc # FPP. Show Lindsey (nervous expression, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth open, looking at PBG), Polly's Bodyguard (PBG) (slightly angry expression, mouth closed, looking at MC) now standing closer to Lindsey, with one hand cupping a fist made with his other hand
                with dissolve

                polly "They were just leaving, actually."

                scene v16s59_4zb
                with dissolve

                u "Really?"

                if v13_penelope_backstage: # -if mc met polly in amsterdam

                    scene v16s59_4zb
                    with dissolve

                    u "It's like that, is it?"

                    scene v16s59_4zd # FPP. Show Lindsey (nervous expression, mouth closed, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth open, looking at MC), Polly's Bodyguard (PBG) (slightly angry expression, mouth closed, looking at MC) now standing closer to Lindsey, with one hand cupping a fist made with his other hand
                    with dissolve

                    polly "It is this time, yes. *Laughs*"

                # -end if

                scene v16s59_4ze # FPP. Show Lindsey (nervous expression, mouth open, looking at Polly) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth closed, looking at Lindsey), Polly's Bodyguard (PBG) (slightly angry expression, mouth closed, looking at MC) now standing closer to Lindsey, with one hand cupping a fist made with his other hand
                with dissolve

                li "I thought we were hitting it off, though. I need you, Polly!"

                scene v16s59_4zd
                with dissolve

                polly "Yeah, not gonna happen. Sorry guys. Good luck on your campaign, though!"

                scene v16s59_4zf # FPP. Show Lindsey (nervous expression, mouth closed, looking at PBG) just from the shoulders up (check with mozzart for clothing), Polly (concerned expression, mouth closed, looking at MC), Polly's Bodyguard (PBG) (slightly angry expression, mouth open, looking at MC) now standing closer to Lindsey, with one hand cupping a fist made with his other hand
                with dissolve

                bdygd "Time for you two to go."

                scene v16s59_4zb
                with dissolve

                u "(Shit...)"

                scene v16s59_4ze
                with dissolve

                li "Wait, not yet!"

                scene v16s59_9
                with dissolve

                pause 0.75

                scene v16s59_10a # TPP. (ROOM SERVICE UNIFORMS) Show MC (no expression, mouth closed, looking at Lindsey) just standing a few feet away from Lindsey and PBG, and Lindsey (nervous expression, mouth open, looking at the hotel room door) trying to push past PBG, The door is still closed. Polly's Bodyguard (slightly angry expression, mouth closed, looking at Lindsey) holding Lindsey back from getting near the door
                with dissolve

                li "I love you, Polly! No matter what-"

                li "I still love you!"

                scene v16s59_10b # TPP. (ROOM SERVICE UNIFORMS) Show MC (no expression, mouth closed, looking at forward where PBG is directing him) being directed away from the door with one hand from PBG on his shoulder, and Lindsey (angry expression, mouth open, looking at the PBG) being carried in one arm by PBG, The door is still closed. Polly's Bodyguard (slightly angry expression, mouth open, looking down the hallway) carrying Lindsey in one arm and has his other hand on MC's shoulder directing them away from the hotel room door
                with dissolve

                li "Put me down, you giant idiot!"

                scene v16s59_10c # TPP. (ROOM SERVICE UNIFORMS) Show MC (no expression, mouth open, looking at Lindsey) being directed away from the door with one hand from PBG on his shoulder, and Lindsey (angry expression, mouth open, looking at the PBG) being carried in one arm by PBG, The door is still closed. Polly's Bodyguard (slightly angry expression, mouth closed, looking down the hallway) carrying Lindsey in one arm and has his other hand on MC's shoulder directing them away from the hotel room door, they have all walked slightly further down the hallway away from the door
                with dissolve

                u "Lindsey..."

                scene v16s59_10b
                with dissolve

                li "Polly is my friend, I'm not some psycho fan!"

                u "(At least we're still leaving with some dignity... *Sighs*)"

        ### ERROR: [End of Checkpoint 1.2. Continue to Checkpoint 2]

    else: # -if Showing up as yourselves

        scene v16s59_4y
        with dissolve

        li "I... I'm..."

        scene v16s59_4q
        with dissolve

        u "Look, I know we've kinda just stumbled upon your hotel room and bothered you in whatever you were just doing, but, uh..."

        scene v16s59_4f
        with dissolve

        polly "Yeah, it's very strange. Please, go on."

        scene v16s59_4q
        with dissolve

        u "I promise we'll be quick; we just have a favor to ask."

        scene v16s59_4d
        with dissolve

        li "A super easy-peasy favor!"

        scene v16s59_4f
        with dissolve

        polly "A favor? What do you want, autographs? *Laughs*"

        scene v16s59_4d
        with dissolve

        li "*Gasps* I would love-"

        scene v16s59_4c
        with dissolve

        u "We're here about Lindsey's presidential campaign."

        scene v16s59_4o
        with dissolve

        polly "Hm, and you're Lindsey?"

        scene v16s59_4d
        with dissolve

        li "Yes. Hi, I'm Lindsey. *Awkward chuckle*"

        scene v16s59_4c
        with dissolve

        u "She's currently campaigning to become the president of her sorority and-"

        scene v16s59_4d
        with dissolve

        li "We thought it'd be amazing if you endorsed me somehow when you perform at our college tonight. It'd mean the absolute world to me!"

        li "Like, maybe talk about me and then dedicate a song to me..."

        scene v16s59_4d
        with dissolve

        menu:

            "Interrupt Lindsey": # (SUCCESS)
                $ add_point(KCT.BOYFRIEND)
                $ add_point(KCT.BRO)

                scene v16s59_4q
                with dissolve

                u "Haha, she's joking of course."

                scene v16s59_4z
                with dissolve

                polly "Oh, ha. Is she? I couldn't tell there for a second."

                scene v16s59_4y
                with dissolve

                li "Um..."

                scene v16s59_4q
                with dissolve

                u "Of course, she was! A song dedication is a ridiculous request from a stranger."

                scene v16s59_4y
                with dissolve

                li "Yeah, obviously. Of course. That'd be insane."

                scene v16s59_4q
                with dissolve

                u "...But seriously, a small endorsement just saying Lindsey's campaign has your support, would help us out tremendously."

                scene v16s59_4z
                with dissolve

                polly "Well... *Sighs*"

                scene v16s59_4h
                with dissolve

                polly "Okay. I guess it's an easy thing to do."

                scene v16s59_4n
                with dissolve

                li "Really?! Oh, my God! I'm going to have a heart attack... Oh my-"

                scene v16s59_4o
                with dissolve

                polly "*Laughs* Well, I'm already going to be there tonight so it's not such a huge hassle to say a few words about you."

                polly "Just promise me you're not going to turn out to be some totalitarian dictator sorority president. It'd be bad for my image."

                scene v16s59_4n
                with dissolve

                li "Haha, I promise."

                scene v16s59_8
                with dissolve

                pause 0.75

                scene v16s59_4r
                with dissolve

                bdygd "Are these two bothering you, Polly?"

                scene v16s59_4zg # FPP. Show Lindsey (nervous expression, mouth closed, looking at PBG) just from the shoulders up (check with mozzart for clothing), Polly (slight smile, mouth open, looking at PBG), Polly's Bodyguard (PBG) (VERY STERN Expression, mouth closed, looking at Polly) standing behind Lindsey closer to the doorway next to Polly
                with dissolve

                polly "They were, but it's okay now."

                scene v16s59_4v
                with dissolve

                u "Haha, yeah, sorry again for bothering you."

                scene v16s59_4u
                with dissolve

                polly "No worries. I'll see you later, guys."

                scene v16s59_4t
                with dissolve

                li "Aw, I could just stay here and hangout with you all day... Hehe."

                scene v16s59_4v
                with dissolve

                u "I don't think that's an option, Linds. Let's go."

                scene v16s59_4t
                with dissolve

                li "Okay... Bye Polly, see you! And thank you again, so much."

                scene v16s59_4u
                with dissolve

                polly "Mhmm!"

                scene v16s59_9
                with dissolve

                pause 0.75

                scene v16s59_4zh # FPP. Show Lindsey (full smile, mouth open, looking at the door) just from the shoulders up (check with mozzart for clothing), Polly is no longer in the doorway and the door is shut, Polly's Bodyguard (PBG) (VERY STERN Expression, mouth closed, looking at Lindsey) standing behind Lindsey closer to the doorway next to the closed door
                with dissolve

                li "I love you!"

                scene v16s59_4zi # FPP. Show Lindsey (full smile, mouth closed, looking at PBG) just from the shoulders up (check with mozzart for clothing), Polly is no longer in the doorway and the door is shut, Polly's Bodyguard (PBG) (VERY STERN Expression, mouth open, looking at Lindsey) standing behind Lindsey closer to the doorway next to the closed door
                with dissolve

                bdygd "Yeah, yeah, she loves you too. Now get the hell out of here."

                scene v16s59_10d # TPP. Exactly the same as v16s59_10 Except Mc and Lindsey are wearing their regular clothes
                with dissolve

                ### ERROR: [End of Checkpoint 1.3. Continue to Checkpoint 2]

            "Let her talk": # (FAILURE)
                $ add_point(KCT.TROUBLEMAKER)

                scene v16s59_4d
                with dissolve

                li "*Gasps* You could even write a song about me!"

                scene v16s59_4z
                with dissolve

                polly "Eh."

                scene v16s59_4d
                with dissolve

                li "We can work on it together if you want?!"

                scene v16s59_4e
                with dissolve

                u "(Uh, oh...)"

                scene v16s59_4d
                with dissolve

                li "We can call it \"My best friend\"."

                scene v16s59_4e
                with dissolve

                u "(Oh, god.)"

                scene v16s59_4d
                with dissolve

                li "Oh my- I GOT IT! We just call it... Ready? Get this, \"Lindsey\"."

                scene v16s59_4zj # FPP. Show Lindsey (full smile, mouth closed, looking at MC) just from the shoulders up (check with mozzart for clothing), Polly (extremely "weirded out" expression, mouth closed, looking at MC)
                with dissolve

                u "(Oh, no no no no...)"

                scene v16s59_4d
                with dissolve

                li "Isn't that kind of edgy? Oh, I love it!"

                scene v16s59_4z
                with dissolve

                polly "...Edgy?"

                scene v16s59_4d
                with dissolve

                li "I'm being silly of course... You're the artist. Obviously, you can pick the name of the song."

                scene v16s59_4z
                with dissolve

                polly "Oh, thanks."

                scene v16s59_4d
                with dissolve

                li "But it'd be fun, wouldn't it?"

                scene v16s59_4zj
                with dissolve

                u "(God, please... If you exist, now is the time to strike me d-)"

                scene v16s59_4z
                with dissolve

                polly "Um... No."

                scene v16s59_4d
                with dissolve

                li "What? Yes, it would, I-"

                scene v16s59_4z
                with dissolve

                polly "No! That doesn't sound fun at all!"

                scene v16s59_8
                with dissolve

                pause 0.75

                scene v16s59_4r
                with dissolve

                bdygd "What's going on here?"

                scene v16s59_4zb
                with dissolve

                u "(Aaaaand, we're screwed.)"

                scene v16s59_4za
                with dissolve

                polly "I'm being annoyed."

                scene v16s59_9
                with dissolve

                u "(Oh, bye.)"

                scene v16s59_4zk # FPP. Show Lindsey (nervous expression, mouth closed, looking at PBG) just from the shoulders up (check with mozzart for clothing), Polly has closed the door and is not in the render anymore, Polly's Bodyguard (PBG) (slightly angry expression, mouth open, looking at Lindsey) now standing closer to Lindsey, with one hand cupping a fist made with his other hand
                with dissolve

                bdygd "I think it's time for the two of you to leave the building."

                scene v16s59_10e # TPP. Exactly the same as v16s59_10a except Mc and Lindsey are wearing their regular clothes
                with dissolve

                li "Polly! Polly, wait! Come back out, I can explain!"

                u "Linds, let's just..."

                scene v16s59_10f # TPP. Exactly the same as v16s59_10b except Mc and Lindsey are wearing their regular clothes
                with dissolve

                li "I didn't get to hug you! Polly!!!"

                bdygd "And you never will."

                scene v16s59_10g # TPP. Exactly the same as v16s59_10c except Mc and Lindsey are wearing their regular clothes
                with dissolve

                li "You don't understand, I'd do anything for her. I really need her help with-"

                li "Hey, stop it! Put me down!"

                scene v16s59_11 # TPP. Show a close up shot of MC (no expression, mouth is closed) with PBG's hand on his shoulder, the rest of PBG is not shown
                with dissolve

                u "(Something tells me we didn't get the endorsement...)"

                ### ERROR: [End of Checkpoint 1.4. Continue to Checkpoint 2]

    # -Regardless of all-

    ### ERROR: [Checkpoint 2]

    jump v16s61 # -Transition to Scene 61-
# SCENE 19: Roommates
# Location: Hotel lobby/room
# Characters: MC(outfit 1)/Riley(outfit 2)/Chloe(outfit 5)
# Time: Late Night (Day when specified in render description)

label v11_roommate:
    #scene v11rm1 # TPP. Show MC walking in the lobby, he is slightly smiling, mouth closed ###ERROR WRONG OUTFIT
    #with fade
    play music "music/v11/Track Scene 19_1.mp3" fadein 2
    #pause 0.75

    scene v11rm2 # FPP. MC is standing in the lobby, he can see Chloe and Riley in the background (slightly close to the counter), Chloe is looking at her phone, Riley is reading a brochure
    with dissolve

    pause 0.75

    if not v11_riley_roomate:
        scene v11rm3 # FPP. Show MC approaching Chloe, she is still looking at her phone, slightly smiling, mouth closed
        with dissolve

        pause 0.75

        if CharacterService.is_mad(chloe):
            scene v11rm4 # FPP. MC is now in talking distance to Chloe, Chloe is now looking at MC, Chloe is slightly annoyed, mouth closed (make sure counter is in backrgound)
            with dissolve

            u "Hey."

            scene v11rm4a # FPP. Same as v11rm4, Chloe slightly annoyed, mouth open
            with dissolve

            cl "*Sighs* Hey, did you really have to room with me?"

            scene v11rm4
            with dissolve

            u "I thought it'd be a good way for us to try and work through things..."

            scene v11rm4a
            with dissolve

            cl "Yeah... maybe."

            scene v11rm4b # FPP. Same cam as v11rm4, MC is looking at Chloe walking towards the counter
            with dissolve

            pause 0.75

            scene v11rm4c # FPP. Same cam as v11rm4, Chloe is now at the counter, talking to a receptionist, receptionist smiling, mouth open
            with dissolve

            pause 0.75

            scene v11rm4d # FPP. Same cam as v11rm4, Chloe is now walking towards MC, neutral expression, mouth closed, she has 2 keycards in her hand
            with dissolve

            pause 0.75

            scene v11rm4e # FPP. Same as v11rm4, Chloe still slightly annoyed, she is giving MC the keycard, Chloe mouth open
            with dissolve

            cl "Here's your key."

            scene v11rm4
            with dissolve

            u "Thanks."

            scene v11rm5 # TPP. Show MC and Chloe walking side by side with their luggage, both tired, mouths closed
            with dissolve

            pause 0.75

            scene v11rm6 # TPP. Show MC and Chloe going inside the room, still carrying their luggage, slight smiles, mouths closed
            with dissolve

            pause 0.75

            scene v11rm7 # FPP. MC is sitting on his bed, Chloe is standing next to her's, she is dropping her luggage on the floor, she is tired, mouth closed
            with dissolve

            pause 0.75

            scene v11rm7a # FPP. Same cam as v11rm7, Chloe is now lying in her bed, she is looking at MC, mouth closed, tired expression
            with dissolve

            u "You wanna hang a bit before we go to sleep?"

            scene v11rm7b # FPP. Same as v11rm7a, Chloe mouth open, tired expression
            with dissolve

            cl "[name], it's late."

        elif chloe.relationship >= Relationship.FWB:
            scene v11rm4f
            with dissolve

            u "Hey."

            scene v11rm4g
            with dissolve

            cl "Hey."

            scene v11rm4f
            with dissolve

            u "Please don't be a boring roommate and make me regret my choice."

            scene v11rm4g
            with dissolve

            cl "Haha. Me? Boring? I should be saying that about you. You're probably ready to go straight to sleep."

            scene v11rm4f
            with dissolve

            u "Well, it is like, three in the morning."

            scene v11rm4g
            with dissolve

            cl "And?"

            scene v11rm4f
            with dissolve

            u "And we just had a long ass flight..."

            scene v11rm4g
            with dissolve

            cl "Who's the boring one again? *Chuckles*"

            scene v11rm4f
            with dissolve

            u "What do you have in mind?"

            scene v11rm4i # FPP. Same as v11rm4f, but Chloe is leaning in towards MC, seductive smile, mouth open
            with dissolve

            cl "*Whisper* I'm sure we can think of a few things..."

            scene v11rm4f
            with dissolve

            u "Oh, okay."

            scene v11rm4b
            with dissolve

            pause 0.75

            scene v11rm4c
            with dissolve

            pause 0.75

            scene v11rm4d
            with dissolve

            pause 0.75

            scene v11rm4h
            with dissolve

            cl "Here's your key."

            scene v11rm4f
            with dissolve

            u "Thanks."

            scene v11rm5a
            with dissolve

            pause 0.75

            scene v11rm6
            with dissolve

            pause 0.75

            scene v11rm7
            with dissolve

            pause 0.75

            scene v11rm7d
            with dissolve

            u "Wait, you're going to sleep?"

            scene v11rm7e
            with dissolve

            cl "Haha, that's what you get for calling me boring."

            scene v11rm7d
            with dissolve

            u "Oh, wow. *Chuckles* Goodnight."

            scene v11rm7e
            with dissolve

            cl "Goodnight."

            $ v11s19_kiwiiPost2 = KiwiiPost(chloe, "phone/kiwii/Posts/v11/v11_chloemcselfie.webp", _("My Europe roommate!"), number_likes=756)
            $ v11s19_kiwiiPost2.newComment(aubrey, _("Look at you two!"), number_likes=renpy.random.randint(100, 200))
            $ v11s19_kiwiiPost2.addReply(_("I think I made the correct choice of roommate ;)"), number_likes=321)
            $ v11s19_kiwiiPost2.addReply(_("Glad to have you as my roommate Chloe!"), number_likes=334)

        else:
            scene v11rm4f # FPP. Same as v11rm4, but Chloe is smiling, mouth closed
            with dissolve

            u "Hey."

            scene v11rm4g # FPP. Same as v11rm4f, but Chloe mouth open
            with dissolve

            cl "Hey."

            scene v11rm4f
            with dissolve

            u "Please don't be a boring roommate and make me regret my choice."

            scene v11rm4g
            with dissolve

            cl "Haha. Me? Boring? I should be saying that about you. You're probably ready to go straight to sleep."

            scene v11rm4f
            with dissolve

            u "Well, it is like, three in the morning."

            scene v11rm4g
            with dissolve

            cl "And?"

            scene v11rm4f
            with dissolve

            u "And we just had a long ass flight..."

            scene v11rm4g
            with dissolve

            cl "Who's the boring one again? *Chuckles*"

            scene v11rm4f
            with dissolve

            u "What do you have in mind?"

            scene v11rm4g
            with dissolve

            cl "Nothing. *Laughs* Just wanted to tease you for trying to call me boring."

            scene v11rm4f
            with dissolve

            u "Haha."

            scene v11rm4b
            with dissolve

            pause 0.75

            scene v11rm4c 
            with dissolve

            pause 0.75

            scene v11rm4d
            with dissolve

            pause 0.75

            scene v11rm4h # FPP. Same as v11rm4e, but Chloe is slightly smiling, mouth open
            with dissolve

            cl "Here's your key."

            scene v11rm4f
            with dissolve

            u "Thanks."

            scene v11rm5a # TPP. Same as v11rm5, but they're both smiling instead
            with dissolve

            pause 0.75

            scene v11rm6
            with dissolve

            pause 0.75

            scene v11rm7
            with dissolve

            pause 0.75

            scene v11rm7d # FPP. Same as v11rm7a, but Chloe is smiling, mouth closed
            with dissolve

            u "Just like that?"

            scene v11rm7e # FPP. Same as v11rm7b, but Chloe is smiling, mouth open
            with dissolve

            cl "Haha, just like that."

            $ v11s19_kiwiiPost1 = KiwiiPost(chloe, "phone/kiwii/Posts/v11/v11_chloemcselfie.webp", _("My Europe roommate!"), number_likes=756)
            $ v11s19_kiwiiPost1.newComment(aubrey, _("Look at you two!"), number_likes=renpy.random.randint(100, 200))
            $ v11s19_kiwiiPost1.addReply(_("I think I made the correct choice of roommate ;)"), number_likes=321)
            $ v11s19_kiwiiPost1.addReply(_("Glad to have you as my roommate Chloe!"), number_likes=334)

        scene v11rm7c # FPP. MC looks as Chloe is turned around with her back to him, sleeping
        with dissolve

        pause 0.75
        stop music fadeout 3
        play music "music/v11/Track Scene 19_2.mp3" fadein 2
        scene v11rm8 # TPP. Show MC and Chloe sleeping (lights turned off now)
        with fade

        pause 0.75

        scene v11rm8a # TPP. Same as v11rm8, MC and Chloe switched sleeping positions
        with dissolve

        pause 0.75

        scene v11rm8b # TPP. Same as v11rm8, different sleeping positions, and it's day
        with dissolve

        pause 0.75

        scene v11rm9 # FPP. MC lying in his bed, looking at the door to the hallway (day)
        with dissolve

        play sound "sounds/knock.mp3"

        u "Huh?"

        ri "[name] come on! I've knocked on every door and embarrassed myself enough... get up and come out!"

        u "Just a minute!"

        scene v11rm10 # TPP. Show MC putting his shirt over his head (He already has the pants from that outfit) (MAKE SURE ONLY MC IS IN SHOT) (day)
        with dissolve

        pause 0.75

        scene v11rm11 # FPP. Show MC reaching for the door handle (Day)
        with dissolve

        pause 0.75

        play sound "sounds/dooropen.mp3"

        scene v11rm11a # FPP. Same cam as v11rm11, Door now open, MC looking at Riley, Riley slight smile, mouth closed (Day)
        with dissolve

        u "What's up?"

        scene v11rm11b # FPP. Same as v11rm11a, Riley slight smile, mouth open (day)
        with dissolve

        ri "Ready to go check out this treasure hunt?"

        if chloe.relationship >= Relationship.FWB:
            scene v11rm12 # FPP. MC still standing by the door, he looks back at Chloe who is still sleeping, show some of her boobs slipping out from her outfit (Day)
            with dissolve

            pause 1

            scene v11rm11a
            with dissolve

            u "*Whisper* Yeah, let's go, but don't wake up Chloe. She was really tired last night."

            scene v11rm11b
            with dissolve

            ri "Haha, okay. Let's go."

        else:
            scene v11rm11a
            with dissolve

            u "If we have to..."

            scene v11rm11b
            with dissolve

            ri "*Chuckles* Let's go."

        jump v11_treasure_hunt

    else: # If rooming with Riley
        scene v11rm13 # FPP. Show MC approaching Riley, she is still reading her brochure, slightly smiling, mouth closed
        with dissolve

        pause 0.75

        if riley.relationship < Relationship.FWB:
            scene v11rm14 # FPP. MC is now in talking distance to Riley, Riley is now looking at MC, Riley is smiling, mouth closed (make sure counter is in backrgound)
            with dissolve

            u "Hey."

            scene v11rm14a # FPP. Same as v11rm14, Riley smiling, mouth open
            with dissolve

            ri "Hey, I'm surprised you chose to room with me over Chloe."

            scene v11rm14
            with dissolve

            u "Why?"

            scene v11rm14a
            with dissolve

            ri "Most guys would leap at an opportunity like that with her. But I guess you're not most guys."

            scene v11rm14
            with dissolve

            u "Guess not."

            scene v11rm14a
            with dissolve

            ri "Oh! Just so you know, every night before I go to sleep I have to listen to my favorite album out loud."

            scene v11rm14
            with dissolve

            u "What?"

            scene v11rm14a
            with dissolve

            ri "I've been doing it forever."

            scene v11rm14
            with dissolve

            u "Are you serious?"

            scene v11rm14b # FPP. Same cam as v11rm14, Riley has her eyes closed, she is dancing, with her hand close to her mouth as if she was holding a microphone, mouth open, smiling
            with dissolve

            ri "*Singing* \"Some people spend most of their lives looking for someone to lean on.\""

            scene v11rm14c # FPP. Same cam as v11rm14b, change Riley's dance position
            with dissolve

            ri "*Singing* \"I have had dreams, once or twice, with no one to lean on.\""

            scene v11rm14d # FPP. Same cam as v11rm14c, change Riley's dance position, her mouth is now only slightly open
            with dissolve

            ri "*Humming* HMMM, HMMM HMMM HMMM."

            scene v11rm14
            with dissolve

            u "You forgot the words to a song you hear every night? *Chuckles*"

            scene v11rm14a
            with dissolve

            ri "Haha, I'm just messing with you. I do really like that album though. I'll show you some time."

            scene v11rm14e # FPP. Same cam as v11rm14, MC is looking at Riley walking towards the counter
            with dissolve

            pause 0.75

            scene v11rm14f # FPP. Same cam as v11rm14, Riley is now at the counter, talking to a receptionist, receptionist smiling, mouth open
            with dissolve

            pause 0.75

            scene v11rm14g # FPP. Same cam as v11rm14, Riley is now walking towards MC, slight smile, she has 3 keycards in her hand
            with dissolve

            pause 0.75

            scene v11rm14h # FPP. Same as v11rm4, Riley slightly smiling, she is giving MC the keycard, Riley mouth open
            with dissolve

            ri "Here's the key, I asked for an extra one because I'll probably end up losing mine."

            scene v11rm14
            with dissolve

            u "*Laughs* Thanks."

            scene v11rm15 # TPP. Show MC and Riley walking side by side with their luggage, both smiling, mouths closed
            with dissolve

            pause 0.75

            scene v11rm16 # TPP. Show MC and Riley going inside the room, still carrying their luggage, slight smiles, mouths closed
            with dissolve

            pause 0.75

            scene v11rm17 # TPP. Show MC setting down his luggage in front of his bed
            with dissolve

            pause 0.75

            scene v11rm18 ## TPP. Show MC lying down in bed, mouth closed, looking up at the ceiling.
            with dissolve

            pause 0.75

            scene v11rm19 # FPP. MC lying down in his bed, looking at Riley, Riley is sitting on her bed, looking at MC, mouth open, slight smile
            with dissolve

            ri "Uhm okay Mr. Boring... you're just gonna go to sleep?"

            scene v11rm20 # TPP. Show MC sitting down in his bed, he's looking at Riley who is sitting on her bed, MC slight smile, mouth closed
            with dissolve

            pause 0.75

            scene v11rm21 # FPP. MC is now sitting down in his bed in front of Riley, Riley sitting on her bed, looking at MC, Riley mouth closed, slight smile
            with dissolve

            u "What else can we do at four in the morning?"

            scene v11rm21a # FPP. Same cam as v11rm21, Riley slight smile, mouth open
            with dissolve

            ri "Talk? *Chuckles* I'm not tired yet."

            scene v11rm21
            with dissolve

            u "Alright, well, what would you like to talk about? And please make it interesting or else I'll fall asleep on you."

            scene v11rm21a
            with dissolve

            ri "Hmm, interesting... Well, you know how I'm, like, interested in girls? *Chuckles*"

            if ending == "riley" and not "v8_riley" in sceneList:
                scene v11rm21
                with dissolve

                u "Yeah, I remember."

                scene v11rm21a
                with dissolve

                ri "I think it's been confirmed. *Chuckles*"

                scene v11rm21
                with dissolve

                u "Haha, by who?"            
            
            else:
                scene v11rm21
                with dissolve

                u "Uh, yeah...?"

                scene v11rm21a
                with dissolve

                ri "You look interested and awake now. *Chuckles* But yeah for real, I'm bi."

                scene v11rm21
                with dissolve

                u "Well, congrats. How'd you find that out?"

            scene v11rm21a
            with dissolve

            ri "Aubrey. *Chuckles* We've spent a lot of time together and I just keep getting tempted."

            scene v11rm21
            with dissolve

            u "Aubrey does have that magic."

            scene v11rm21b # FPP. Same as v11rm21, but Riley nervous, mouth open
            with dissolve

            ri "I'm nervous though. I can't just come out and tell her. I want to ease into it."

            scene v11rm21c # FPP. Same as v11rm21b, Riley mouth closed
            with dissolve

            menu:
                "Just tell her":
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                    $ riley.points += 1

                    scene v11rm21c
                    with dissolve

                    u "Just tell her, I'm sure she'd be cool either way."

                    scene v11rm21b
                    with dissolve

                    ri "You're probably right."

                "Ease into it":
                    $ reputation.add_point(RepComponent.BRO)

                    scene v11rm21c
                    with dissolve

                    if upstairs == "aubrey":
                        u "Maybe you'll have to ease into it."
                    else:
                        u "I've never heard her mention anything about girls, maybe you'll have to ease into it."

                    scene v11rm21b
                    with dissolve

                    ri "How?"

                    scene v11rm21c
                    with dissolve

                    u "Get a dude in the mix. *Chuckles*"

                    scene v11rm21d # FPP. Same as v11rm21b, but Riley has her eyebrow raised
                    with dissolve

                    ri "Uhm, like who?"

                    scene v11rm22 # TPP. Show MC getting up from his bed and walking towards the mirror, he has a smug expression, mouth closed
                    with dissolve

                    pause 0.75

                    scene v11rm23 # FPP. MC is standing in front of the mirror, looking at his reflection, he is trying to show off his biceps, mouth open, smug expression
                    with dissolve

                    u "Look, I think I found someone."

                    scene v11rm24 # FPP. MC still standing where he was in v11rm19, but he is now looking at Riley, she is smiling, mouth open
                    with dissolve

                    ri "Okay, now I'm going to sleep. *Chuckles*"

                    scene v11rm24a # FPP. Same as v11rm24, but Riley mouth closed
                    with dissolve

                    u "*Laughs*"

        else:
            scene v11rm14a
            with dissolve

            ri "Oh! Just so you know, every night before I go to sleep I have to listen to my favorite album out loud."

            scene v11rm14
            with dissolve

            u "What?"

            scene v11rm14a
            with dissolve

            ri "I've been doing it forever."

            scene v11rm14
            with dissolve

            u "Are you serious?"

            scene v11rm14b
            with dissolve

            ri "*Singing* \"Some people spend most of their lives looking for someone to lean on.\""

            scene v11rm14c
            with dissolve

            ri "*Singing* \"I have had dreams, once or twice, with no one to lean on.\""

            scene v11rm14d
            with dissolve

            ri "*Humming* HMMM, HMMM HMMM HMMM."

            scene v11rm14
            with dissolve

            u "You forgot the words to a song you hear every night? *Chuckles*"

            scene v11rm14a
            with dissolve

            ri "Haha, I'm just messing with you. I do really like that album though. I'll show you some time."

            scene v11rm14e
            with dissolve

            pause 0.75

            scene v11rm14f
            with dissolve

            pause 0.75

            scene v11rm14g
            with dissolve

            pause 0.75

            scene v11rm14h
            with dissolve

            ri "Here's the key, I asked for an extra one because I'll probably end up losing mine."

            scene v11rm14
            with dissolve

            u "*Laughs* Thanks."

            scene v11rm15
            with dissolve

            pause 0.75

            scene v11rm16
            with dissolve

            pause 0.75

            scene v11rm17
            with dissolve

            pause 0.75

            scene v11rm18
            with dissolve

            pause 0.75

            scene v11rm19
            with dissolve

            ri "Uhm okay Mr. Boring... you're just gonna go to sleep?"

            scene v11rm20
            with dissolve

            pause 0.75

            scene v11rm21
            with dissolve

            u "What else can we do at four in the morning?"

            scene v11rm21a
            with dissolve

            ri "Talk? *Chuckles* I'm not tired yet."

            scene v11rm21
            with dissolve

            u "Alright, well, what would you like to talk about? And please make it interesting or else I'll fall asleep on you."

            scene v11rm21a
            with dissolve

            ri "Hmm, interesting... Well, you know how I'm, like, interested in girls? *Chuckles*"

            scene v11rm21
            with dissolve

            u "Uh, yeah..."

            scene v11rm21a
            with dissolve

            ri "You look interested and awake now. *Chuckles* But yeah for real, I'm bi."

            scene v11rm21
            with dissolve

            u "Well, congrats. How'd you find that out?"

            scene v11rm21a
            with dissolve

            ri "Aubrey. *Chuckles* We've spent a lot of time together and I just keep getting tempted."

            scene v11rm21
            with dissolve

            u "Aubrey does have that magic."

            scene v11rm21b
            with dissolve

            ri "I'm nervous though. I can't just come out and tell her. I want to ease into it."

            scene v11rm21c
            with dissolve

            menu:
                "Just tell her":
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                    $ riley.points += 1
                    
                    scene v11rm21c
                    with dissolve

                    u "Just tell her, I'm sure she'd be cool either way."

                    scene v11rm21b
                    with dissolve

                    ri "You're probably right."

                    scene v11rm21c
                    with dissolve

                "Ease into it":
                    $ reputation.add_point(RepComponent.BRO)

                    scene v11rm21c
                    with dissolve

                    if upstairs == "aubrey":
                        u "Maybe you'll have to ease into it."
                    else:
                        u "I've never heard her mention anything about girls, maybe you'll have to ease into it."

                    scene v11rm21b
                    with dissolve

                    ri "How?"

                    scene v11rm21c
                    with dissolve

                    u "Get a dude in the mix. *Chuckles*"

                    scene v11rm21d
                    with dissolve

                    ri "Uhm, like who?"

                    scene v11rm22
                    with dissolve

                    pause 0.75

                    scene v11rm23
                    with dissolve

                    u "I think I found someone."

                    scene v11rm24
                    with dissolve

                    ri "Hmm... He is kinda cute, but I don't know if he could handle us."

                    scene v11rm23a # Same as v11rm23, but change MC's pose, he is still showing off
                    with dissolve

                    u "Oh, I'm sure he could."

                    scene v11rm24
                    with dissolve

                    ri "...And all of a sudden I'm tired. *Chuckles*"

        $ v11s19_kiwiiPost3 = KiwiiPost(riley, "phone/kiwii/Posts/v11/v11_rileymcselfie.webp", _("Roll on Europe!"), number_likes=456)
        $ v11s19_kiwiiPost3.newComment(ryan, _("Good roommate pick!"), number_likes=renpy.random.randint(100, 300))
        $ v11s19_kiwiiPost3.addReply(_("Europe's gonna be a blast!"), number_likes=321)
        $ v11s19_kiwiiPost3.addReply(_("Glad to have you as my roommate Riley!"), number_likes=334)

        pause 0.75

        scene v11rm26 # TPP. Show Riley and MC sleeping (lights turned off)
        with fade

        pause 0.75

        scene v11rm26a # TPP. Same as v11rm26, but different sleeping positions
        with dissolve

        pause 0.75

        scene v11rm26b # TPP. Same as v11rm26a, different sleeping positions, now daytime
        with dissolve

        pause 0.75

        scene v11rm27 # FPP. MC is lying down in his bed, looking at Riley, who is standing next to his bed, looking at MC, Riley mouth open, slightly smiling (day)
        with fade

        ri "C'mon, get up, we're going to check out the treasure hunt thing!"

        scene v11rm27a # FPP. Same as v11rm27, but Riley mouth closed, very slightly annoyed (day)
        with dissolve

        u "*Groans* Five more minutes..."

        scene v11rm28 # TPP. Show Riley slapping MC on the arm, he is still lying down, he is startled (Day)
        with dissolve

        pause 0.75

        scene v11rm29 # TPP. Show MC sitting on his bed, he is holding his arm where Riley slapped him, mouth closed, slightly annoyed (day)
        with dissolve

        pause 0.75

        scene v11rm30 # FPP. MC is sitting on his bed, Riley is standing next to the door looking at MC, her mouth is open, slight smile (day)
        with dissolve

        ri "Get up! Let's go."

        scene v11rm30a # FPP. Same as v11rm30, Riley mouth closed, slight smile (day)
        with dissolve

        u "*Sighs* Okay, I'm coming."

        scene v11rm10 
        with dissolve

        pause 0.75

        scene v11rm31 # TPP. Show Riley opening the door to the hallway, MC is standing closely behind her (day)
        with dissolve

        pause 0.75
        stop music fadeout 3
        jump v11_treasure_hunt
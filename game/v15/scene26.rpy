# SCENE 26: Watch a movie in Chicks' theatre room with Aubrey & Riley
# Locations: Chicks' house; theater room
# Characters: RILEY (Outfit: 4), MC (Outfit: 9), AUBREY (Outfit: 3), MALE ACTOR (Outfit: x), FEMALE ACTOR (Outfit: x)
# Time: Saturday evening

label v15s26:
    play music "music/v12/Track Scene 33_2.mp3" fadein 2

    scene v15s26_1 # TPP Show MC knocking on the door to the Chicks' house
    with dissolve

    pause 1

    play sound "sounds/knock.mp3"

    scene v15s26_2 # FPP Riley at the open door to the Chicks' house, smiling at MC, mouth open
    with dissolve

    ri "[name]!"

    scene v15s26_2a # FPP Same angle as 2, Riley at the open door to the Chicks' house, smiling at MC, mouth closed
    with dissolve

    u "Hey, Riley...?"
    u "Wait, are you a Chick now? *Laughs*"

    scene v15s26_2
    with dissolve

    ri "Haha, not officially. I'm an honorary Chick for now, I guess."

    scene v15s26_2a
    with dissolve

    u "The Chicks' mascot?"

    scene v15s26_2
    with dissolve

    ri "Just without the sweaty costume, haha."

    scene v15s26_3 # FPP Now in the hallway of the Chicks' house, Aubrey smiling at MC with mouth open, Riley smiling at MC with mouth closed
    with dissolve

    au "Hey! So, are you ready for your big surprise?"

    scene v15s26_3a # FPP Same angle as 3, now in the hallway of the Chicks' house, Aubrey smiling at MC with mouth closed, Riley smiling at MC with mouth closed
    with dissolve

    u "I think so... *Laughs*"

    scene v15s26_3
    with dissolve

    au "*Chuckles* Follow me!"

    scene v15s26_4 # TPP Show Aubery, Riley, and MC, in that order, going up the stairs in the Chicks house
    with dissolve

    pause 0.75

    scene v15s26_5 # FPP Show door to theather room, which is closed and has a sign saying "Our Secret Place"
    with dissolve

    pause 0.75

    if v14_help_lindsey and not v14_lindsey_sell: # -if MC went to Chloe's room to try and steal money
        u "(I remember this door... I guess I'm about to find out what's behind it.)"

    scene v15s26_6 # FPP Show Aubrey and Riley in hallway by door to theater room, both smiling at MC with mouths closed
    with dissolve

    u "Our Secret Place? Sounds very... mysterious..."

    scene v15s26_6a # FPP Same angle as 6, Aubrey and Riley in hallway by door to theater room, both smiling at MC, Aubrey's mouth open
    with dissolve

    au "Hehe, it is indeed. It's also the best room in the house."

    scene v15s26_6
    with dissolve

    u "Okay..."

    scene v15s26_6b # FPP Same angle as 6, Aubrey and Riley in hallway by door to theater room, looking at each other and smiling, mouths closed
    with dissolve

    u "So? What are we waiting for?"

    scene v15s26_6c # FPP Same angle as 6, Aubrey and Riley in hallway by door to theater room, both smiling at MC, Riley's mouth open
    with dissolve

    ri "*Laughs* You have to say the magic words."

    scene v15s26_6
    with dissolve

    u "*Sighs* What words?"

    scene v15s26_6a
    with dissolve

    au "What? We can't just tell you..."

    scene v15s26_6b
    with dissolve

    pause 0.75

    scene v15s26_6c
    with dissolve

    ri "That's against the rules, you don't want to break a rule."

    scene v15s26_6a
    with dissolve

    au "Definitely not. Poor Jessica..."

    scene v15s26_6
    with dissolve

    u "Jessica?"
    u "What the hell are you guys talking about?"

    scene v15s26_6c
    with dissolve

    ri "That was it! You did it! *Chuckles*"

    scene v15s26_6d # FPP Same angle as 6, Aubrey and Riley looking at each other in fake surprise, Aubrey's mouth open
    with dissolve

    au "Holy shit! Hehe..."

    scene v15s26_6
    with dissolve

    u "What did I... What?"

    scene v15s26_6c
    with dissolve

    ri "Go on, what are you waiting for?!"

    scene v15s26_7 # TPP Show Riley pushing open the door to the theater room and ushering Aubrey and MC in
    with dissolve

    u "(Am I high?)"

    scene v15s26_8 # FPP View of the screen of the theater room from the door
    with dissolve

    u "(Holy...)"

    scene v15s26_9 # FPP Another view of the theater room from the door, this time looking toward the couch
    with dissolve

    u "Damn... A theater room?"

    stop music fadeout 3
    
    play music "music/v15/Track Scene 26_2.mp3" fadein 2

    scene v15s26_10 # FPP Aubrey, now in theater room, with a big, excited smile, mouth open
    with dissolve

    au "Yessss!"

    scene v15s26_10a # FPP Same angle as 10, Aubrey in theater room, slight smile with eyebrow raised, mouth open
    with dissolve

    au "And you should feel very lucky to be inside. We don't open the door for just anyone, you know."

    scene v15s26_10b # FPP Same angle as 10, Aubrey in theater room, slight smile, mouth closed
    with dissolve

    u "Right, just the ones who say an unknown magic word."

    scene v15s26_10c # FPP Same angle as 10, Aubrey laughing at MC, mouth open
    with dissolve

    au "Oh, ha... There's no magic word you goober. You actually fell for that?"

    scene v15s26_11 # FPP Aubrey and Riley, in theater room, laughing and giving each other a high five
    with dissolve

    u "Wow. Good one."

    scene v15s26_12 # FPP Riley, in theater room, looking at MC with a slight smile, mouth open
    with dissolve

    ri "Really though, you're a lucky guy, [name]. Barely anyone has been here, let alone knows of its existence."

    scene v15s26_12a # FPP Same angle as 12, Riley in theater room with a slight smile, mouth closed
    with dissolve

    u "Really? It's a secret?"

    scene v15s26_10a
    with dissolve

    au "It's a secret to those who it should be kept from. You're not one of them."

    scene v15s26_10b
    with dissolve

    u "(Hmm... Okay?)"

    scene v15s26_13 # TPP They sit down on the couch. MC is in the middle of the two girls. There is popcorn on the table, one big bucket, riley's mouth open
    with dissolve

    ri "So, there's a movie I've been really wanting to watch with you guys."

    scene v15s26_14 # FPP Aubrey on the couch, looking across MC at Riley, neutral expression, mouth open
    with dissolve

    au "What's it called again?"

    scene v15s26_15 # FPP Riley on the couch, looking across MC at Aubrey, neutral expression, mouth open
    with dissolve

    ri "The Poly Dilemma."

    scene v15s26_15a # FPP Same angle as 15, Riley looking at MC, neutral expression, mouth open
    with dissolve

    ri "It's about this guy who has two wives, and then he gets a third wife, and it causes all sorts of problems in their marriages."

    scene v15s26_15b # FPP Same angle as 15, Riley looking at MC, neutral expression, mouth closed
    with dissolve

    u "Haha. Sounds like it'll be funny."

    scene v15s26_15a
    with dissolve

    ri "Well, it's more of a serious drama actually..."

    scene v15s26_15b
    with dissolve

    u "Oh... (Oh?)"

    scene v15s26_14
    with dissolve

    au "How long is it?"

    scene v15s26_15
    with dissolve

    ri "Two hours...? I think."

    scene v15s26_14a # FPP Aubrey on the couch, looking across MC at Riley, slight smile with mouth open
    with dissolve

    au "That's one hell of a commitment, haha..."

    scene v15s26_15c # FPP Same angle as 15, Riley looking across MC at Aubrey, slight smile with mouth open
    with dissolve

    ri "I know, I know."

    scene v15s26_14
    with dissolve

    au "I'll trust your judgement..."

    scene v15s26_14a
    with dissolve

    au "For now."

    scene v15s26_16 # FPP Aubrey looking at Riley with a fake angry face, pointing a finger at each of her eyes, like this: https://i.kym-cdn.com/photos/images/original/000/679/161/255.jpg
    with dissolve

    pause 0.75

    scene v15s26_16a # FPP Same angle as 16, Aubrey pointing the same two fingers at Riley, like this: https://qph.fs.quoracdn.net/main-qimg-df014581e2c1b8f49acdd7b7ca1e18ea
    with dissolve

    pause 0.75

    scene v15s26_15c
    with dissolve

    ri "Haha, thank you..." 
    
    scene v15s26_15a
    with dissolve

    ri "What about you, [name]? Are you feeling up for it?"

    scene v15s26_15b
    with dissolve

    menu:
        "Yeah, let's watch":
            $ add_point(KCT.BOYFRIEND)
            
            u "Yeah, I don't have anything else to do. We can watch."

            scene v15s26_14a
            with dissolve

            au "Same, haha. I just hope it's worth my time."
        
        "Do we have to?":
            $ add_point(KCT.BRO)
            
            scene v15s26_15b
            #with dissolve

            u "Do we really have to watch it?"

            scene v15s26_15a
            with dissolve

            ri "But-"

            scene v15s26_15b
            with dissolve

            u "We could just pretend like we did. *Laughs*"

            scene v15s26_14a
            with dissolve

            au "Haha! Actually, that's a good idea..."

            scene v15s26_15
            with dissolve

            ri "Guys..."

            scene v15s26_14a
            with dissolve

            au "I'm kidding! We're..."

            scene v15s26_14b # FPP Same angle as 14, Aubrey looking at MC with neutral expression and eyebrow raised, mouth closed
            with dissolve

            pause 0.75

            scene v15s26_14a
            with dissolve

            au "We're kidding."

            scene v15s26_15b
            with dissolve

            u "Right... It was just a joke..."

            scene v15s26_14a
            with dissolve

            au "It better be worth our time, that's all."

    scene v15s26_15d # FPP Same angle as 15, Riley looking toward the screen of the theater room, slight smile, mouth open
    with dissolve

    ri "Okay... No pressure, Riley! Ha."

    scene v15s26_15b
    with dissolve

    u "*Chuckles* Let's start it."

    scene v15s26_14a
    with dissolve

    au "Lights off, then. Let's get cozy, cuties."

    scene v15s26_17 # TPP Aubrey standing up at the light switch, Riley holding the remote pointing it at the theater screen
    with dissolve

    pause 0.75

    stop music fadeout 3
    
    play music "music/v15/Track Scene 26_3.mp3" fadein 2

    # -We see some opening credits, white text on black screen (be creative, use patron names, talk to Steve about what he would like to add here. 
    # Cheex suggests high-tier patrons can be listed? If not, let's stick to people from the team for the credits)

    scene v15s26_18a # FPP Same angle as 18, view of the screen showing a pastoral view, with the title "The Poly Dilemma" in pretty script
    with dissolve

    pause 1
  
    # and from then on we only see MC, Riley, Aubrey sitting on the couch with the screen flickering/shining on them. A few images as they switch around in positions-
    scene v15s26_19 # TPP Side view of MC, Riley, and Aubrey sitting on the couch watching the movie, lit up by the light from the screen
    with dissolve

    pause 1

    # -I would love it if Aubrey/Riley/MC had some different positions in these images while they're watching. 
    # MC is sitting in the middle so if threesome, they can all be holding hands/cuddling. If aubreyTamed and not riley RS, just Aubrey holding hands. 
    # Or if just Riley RS, no Aubrey, just Riley/MC holding hands. If this is too much work for one small image, I get it. But it would be a cute bonus here. Ask cheex for questions-
    if "v14_threesome" in sceneList:
        scene v15s26_20 # TPP Show MC, Riley, and Aubrey all cuddling and holding hands, lit up by the movie screen
        with dissolve

        pause 0.75
    
    elif aubrey.relationship >= Relationship.TAMED and riley.relationship < Relationship.FWB:
        scene v15s26_20a # TPP Show MC cuddling and holding hands with Aubrey, while Riley sits forward and watches the movie, all lit up by the movie screen
        with dissolve

        pause 0.75

    elif riley.relationship >= Relationship.FWB and aubrey.relationship < Relationship.TAMED:
        scene v15s26_20b # TPP Show MC cuddling and holding hands with Riley, while Aubrey leans back on the couch watching the movie, looking a little bored, all lit up by the movie screen
        with dissolve

        pause 0.75

    else:
        scene v15s26_20c # TPP Show MC, Riley, and Aubrey all leaning back on the couch watching the movie, all lit up by the movie screen
        with dissolve

        pause 0.75

    scene v15s26_21 # FPP MC picking up the popcorn bucket to set it in his lap
    with dissolve

    pause 0.75
    
    scene v15s26_19a # TPP Same angle as 19, side view of the everyone on the couch watching the movie, Aubrey and Riley grabbing popcorn from the bucket on MC's lap
    with dissolve

    pause 0.75

    scene v15s26_18b # FPP Same angle as 18, view of the screen showing a high shot of beautiful rural farm
    with dissolve

    mactor "Last year, my life was so simple. I had a gorgeous house, a few acres of land, a great job, and two wives."
    mactor "Why, oh, why didn't I just stick with two wives? I just had to get greedy. I had to meet her. Wife number three. Or so I hoped."

    scene v15s26_18c # FPP Same angle as 18, view of screen showing male actor looking out over his land
    with dissolve

    mactor "Boy, do I regret that now."

    scene v15s26_18d # FPP Same angle as 18, view of screen showing a pretty girl, "Angelique," who is looking off into the distance
    with dissolve

    mactor "Angelique was her name. I'll always regret ever hearing that name."
    mactor "This is my story. The story of a man who lost it all... for a woman called Angelique."

    # -Quick series of shots showing the trio watching the film and occasionally eating popcorn. Riley is focused on the film throughout. MC and Aubrey show different levels of interest, shifting body positions. 
    # The popcorn gets lower as we go through the shots, you can reuse hand holding images after the popcorn is empty, whatever is needed-
    scene v15s26_19b # TPP Same angle as 19, side view of everyone on the couch watching the movie. Riley is leaning forward in interest, Aubrey is getting popcorn from bucket on MC's lap and winking at him
    with dissolve

    mactor "Lou-Ann, please talk to me. Why are you saying you want to leave me now?"
    mactor "You're the best second wife a man could ever wish for! Things have been good for us, haven't they?"

    scene v15s26_19c # TPP Same angle as 19, Riley grabbing popcorn while still watching the screen, Aubrey leaning back against the couch
    with dissolve

    factor "Yeah, and now that a third wife is being brought into the mix... I'm feeling less important to you."
    factor "I hardly see you anymore. *Sobbing* This isn't what I signed up for!"

    scene v15s26_18e # FPP Same angle as 18, view of screen showing male actor in a dramatic pose, mouth open
    with dissolve

    mactor "But it is! This is exactly what you signed up for!"
    
    stop music fadeout 3
    
    play music "music/v13/Track Scene 52.mp3" fadein 2

    scene v15s26_22 # FPP Show Aubrey holding the remote control pointed forward, pausing the movie
    with dissolve

    ri "Ugh, hey!"

    scene v15s26_15
    with dissolve

    ri "Why did you pause? It was just getting super dramatic-y... *Sighs*"

    scene v15s26_14
    with dissolve

    au "I'm just trying to wrap my head around this whole polygamy thing..."

    scene v15s26_15
    with dissolve

    ri "Oh."

    scene v15s26_14
    with dissolve

    au "You're telling me that there are people in this world who are happily married into that... arrangement?"

    scene v15s26_15
    with dissolve

    ri "Oh, yeah! This isn't uncommon anymore."

    scene v15s26_15b
    with dissolve

    u "I'm sure the men in those relationships are really happy about it... *Laughs*"

    scene v15s26_14a
    with dissolve

    au "Yeah, I bet they are! *Chuckles*"

    scene v15s26_14
    with dissolve

    au "But I don't see how a woman could want to be in a marriage like that. It's just..."

    scene v15s26_14c # FPP Same angle as 14, Aubrey looking at MC with a neutral expression, mouth open
    with dissolve

    au "It's kind of weird to me. You know?"

    scene v15s26_15a
    with dissolve

    ri "I mean, no. I don't know..."

    scene v15s26_15
    with dissolve

    ri "It kind of intrigues me in some... strange way."

    if "v14_threesome" in sceneList: # -if they had threesome (AwkwardRiley&Aubrey is now consistent in this playthrough, remember variable)
        $ aubrey_riley_awkward = True

        scene v15s26_15a
        with dissolve

        ri "Like, what if the three of us had a relationship like that?"

        scene v15s26_15b
        with dissolve

        u "(Sheeeeeeesh...)"

        scene v15s26_15c
        with dissolve

        ri "Wouldn't that be, like... Amazing? Ha..."

        scene v15s26_14
        with dissolve

        au "Not a serious relationship, Riley... No."

        scene v15s26_15
        with dissolve

        ri "But-"

        scene v15s26_15b
        with dissolve

        u "(Am I witnessing their break-up right now, or...)"

        scene v15s26_15
        with dissolve

        ri "I don't understand... Why?"

        scene v15s26_14
        with dissolve

        au "Why what exactly?"

        scene v15s26_15
        with dissolve

        ri "We all get along so well, and we enjoy each other sexually, so-"

        scene v15s26_14a
        with dissolve

        au "For fun, though. *Chuckles*"

        scene v15s26_14
        with dissolve

        au "If I'm going to be in a committed relationship, it would have to be monogamous."

        scene v15s26_14e # FPP Same angle as 14, Aubrey looking away, neutral expression, mouth closed
        with dissolve

        u "(Hmm, noted...)"

        scene v15s26_14
        with dissolve

        au "I'm not sharing that person with anyone, and I shouldn't have to."

        scene v15s26_15b
        with dissolve

        u "Remember guys, this is all hypothetical, ha..."

        scene v15s26_15a
        with dissolve

        ri "Okay, but what if it wasn't hypothetical?"

        scene v15s26_15b
        with dissolve

        u "(Alright, this is happening, [name]...) *Sighs*"

        scene v15s26_15
        with dissolve

        ri "That threesome was-"

        scene v15s26_14a
        with dissolve

        au "I know, Riley! It was great. Amazing. All of the above."

        scene v15s26_15c
        with dissolve

        ri "Yes, and I really care about both of you, Aubrey..."

        scene v15s26_14b
        with dissolve

        pause 0.75

        scene v15s26_23 # TPP Show MC looking over at Aubrey - MC looks like a deer in the headlights, no idea what to do
        with dissolve

        pause 0.75

        scene v15s26_15a
        with dissolve

        ri "Taking things to the next level, all three of us, could be something special."

        scene v15s26_14
        with dissolve

        au "No, Riley. I'm sorry."

        scene v15s26_14a
        with dissolve

        au "Short term, this is amazing, and I'm loving it... but a serious relationship? *Scoffs*"

        scene v15s26_14
        with dissolve

        au "That's a totally different context."

        scene v15s26_20d # TPP Same angle as 20, Riley with her arms across her chest, head down looking at her feet, like she's trying to hide tears. Aubrey looking at Riley with concern, mouth open
        with dissolve

        au "Sorry, Riley... It's just not for me."

        scene v15s26_15
        with dissolve

        ri "Yeah... Okay."

        scene v15s26_15a
        with dissolve

        ri "What about you, [name]? I mean for what it's worth, would you have wanted something like this?"

        scene v15s26_15b
        with dissolve

        menu:
            "Side with Riley":
                $ add_point(KCT.TROUBLEMAKER)
                $ RileyLoyal = True
                $ grant_achievement("polycurious")

                u "I mean, I've never tried it, so...I wouldn't know for sure, haha. But I don't see any problems with it personally."

                scene v15s26_15f # FPP Same angle as 15, Riley looking at MC with a slight smile, mouth closed
                with dissolve

                u "Plus, you know... Fun can turn into love."

                scene v15s26_14f # FPP Same angle as 14, Aubrey looking away and rolling her eyes
                with dissolve

                pause 0.75

                scene v15s26_15a
                with dissolve

                ri "Exactly! And, for me it has already."

                scene v15s26_15b
                with dissolve

                u "(Did she just admit that she's in love with both of us? Wait a sec...)"

                scene v15s26_14a
                with dissolve

                au "Okay, then I guess I'm just wired differently than you guys are. *Laughs*"

                scene v15s26_14
                with dissolve

                au "There's no way I could share the person I love with someone else."

                if aubrey.relationship > Relationship.FWB: # -if Aubrey Tamed she gives a stern look to MC, but continue regardless-
                    $ aubrey.relationship = Relationship.FWB

                    scene v15s26_14d # FPP Same angle as 14, Aubrey looking at MC with a stern expression, mouth open
                    with dissolve

                    au "One hundred percent, that's never happening."

            "Side with Aubrey": # -event2 Side with Aubrey, Pro-Monogamy (No variable change)
                $ add_point(KCT.BOYFRIEND)
                
                scene v15s26_15b
                #with dissolve

                u "I'm with Aubrey on this one..."

                scene v15s26_15g # FPP Same angle as 15, Riley looking away with a sad expression, mouth closed
                with dissolve

                u "We can continue having fun together, but I don't think there should be any pressure to get more serious."

                scene v15s26_15b
                with dissolve

                u "I don't think it'd work out in the end."

                scene v15s26_14g # FPP Same angle as 14, Aubrey looking at MC with a small smile, mouth closed
                with dissolve

                pause 0.75

                scene v15s26_15
                with dissolve

                ri "Well, I guess I have my answer then. *Sighs*"

                scene v15s26_15a
                with dissolve

                ri "Can I ask, though... Why do you guys think it won't work?"

                scene v15s26_15b
                with dissolve

                menu:
                    "Polygamy isn't healthy": # RileyUpset
                        $ add_point(KCT.BRO)
                        $ v15_RileyUpset = True
                        
                        u "Honestly, it doesn't seem healthy."

                        scene v15s26_14
                        with dissolve

                        au "*Whispers* At all."

                        scene v15s26_15f
                        with dissolve

                        u "I can see how it might look great, especially to men, haha."

                        scene v15s26_15g
                        with dissolve

                        u "But, Riley... The more people involved, the more emotions there are to balance."

                        scene v15s26_15a
                        with dissolve

                        ri "Well... Yeah, but-"

                        scene v15s26_15b
                        with dissolve

                        u "Someone always ends up feeling left out in the long run."

                        scene v15s26_15g
                        with dissolve

                        u "Like this movie, it's only a matter of time before it gets too dramatic to handle and everything turns to shit."

                        scene v15s26_15a
                        with dissolve

                        ri "This is a movie, [name]. It's not real life."

                        scene v15s26_14a
                        with dissolve

                        au "Ha, exactly."

                        scene v15s26_15g
                        with dissolve

                        u "Which makes it even more unrealistic."

                        scene v15s26_20e # TPP Same angle as 20, Riley with her arms across her chest, looking away from MC and Aubrey with an angry, hurt expression, mouth closed
                        with dissolve

                        pause 1

                    "I only want one partner": # -event2 I only want one partner
                        $ add_point(KCT.BOYFRIEND)
                        
                        u "Basically, exactly what Aubrey said. I just couldn't commit like that to more than one person."

                        if aubrey.relationship >= Relationship.TAMED: # -Aubrey soft smile, if AubreyTamed can she do something a little extra like a wink or idk be cute-
                            scene v15s26_14h # FPP Same angle as 14, Aubrey with a small smile, winking at MC
                            with dissolve

                            pause 0.75

                        else:
                            scene v15s26_14g
                            with dissolve

                            pause 0.75

                        scene v15s26_14
                        with dissolve

                        au "Exactly."

                        scene v15s26_15
                        with dissolve

                        ri "Well, I think we're really missing out on something special, but..."

                        scene v15s26_14e
                        with dissolve

                        pause 0.75

                        scene v15s26_15c
                        with dissolve

                        ri "I guess I have to be okay with it, ha. I can respect your opinions."

                        scene v15s26_15f
                        with dissolve

                        u "We're all still friends having good times together. Let's not rock the boat. *Laughs*"

                        scene v15s26_15h # FPP Same angle as 15, Riley looking at MC with a slight smile, mouth open
                        with dissolve

                        ri "Yeah... *Chuckles*"

    else: # -if they didn't have threesome (AubreyRileyAwkward variable does not exist, the girls are on good terms, and could possibly have another threesome with MC in the far far far far far far future-
        scene v15s26_15a
        with dissolve

        ri "What do you think, [name]?"

        scene v15s26_15b
        with dissolve

        menu: 
            "Side with Riley, pro-polygamy": #if AubreyTamed it becomes AubreyFwB, gain RileyLoyal; she's committed to MC as friends, romantic, TilDeathDoUsPart, all of the above
                $ add_point(KCT.TROUBLEMAKER)
                $ grant_achievement("polycurious")
                
                if aubrey.relationship >= Relationship.TAMED:
                    $ aubrey.relationship = Relationship.FWB
                $ RileyLoyal = True
                
                u "I think you're onto something here, Riley..."

                scene v15s26_14c
                with dissolve

                au "*Scoffs*"

                scene v15s26_14e
                with dissolve

                u "Why would you not want to be in a loving relationship with multiple people, if it's possible?"

                scene v15s26_14f
                with dissolve

                u "That's like... Getting the cake and then eating it too, you know. *Chuckles*"

                scene v15s26_15c
                with dissolve

                ri "Haha! See?"

                scene v15s26_15h
                with dissolve

                ri "I knew you'd agree with me. Sharing the love is beautiful."

                scene v15s26_14
                with dissolve

                au "I'm not doubting that it works for some people... I guess."

                scene v15s26_14c
                with dissolve

                au "It's just definitely not something I want."

            "Side with Aubrey, pro-monogamy": # -if Side with Aubrey, Pro-Monogamy
                $ add_point(KCT.BOYFRIEND)

                scene v15s26_15b
                #with dissolve

                u "I agree with Aubrey."

                scene v15s26_15i # FPP Same angle as 15, Riley looking away with a sad expression, mouth open
                with dissolve

                ri "Oh..."

                scene v15s26_14a
                with dissolve

                au "*Chuckles*"

                scene v15s26_15b
                with dissolve

                u "I also think that marriage should be a commitment between just two people."

                scene v15s26_15g
                with dissolve

                u "Anything more and it'd just get too messy, and people would get hurt."

                scene v15s26_14
                with dissolve

                au "Exactly. Someone always gets hurt."

                scene v15s26_15d
                with dissolve

                ri "Okay, that's fine..."

                scene v15s26_15
                with dissolve

                ri "We can agree to disagree... *Sighs*"

                scene v15s26_14a
                with dissolve

                au "Were you planning a big proposal tonight? Hehe..."

                scene v15s26_15c
                with dissolve

                ri "Haha, maybe I was!"

                scene v15s26_15f
                with dissolve

                u "*Laughs*"

    # -Regardless-
    if "v14_threesome" in sceneList: # -if they had threesome
        scene v15s26_14a
        with dissolve

        au "Anyway... I think I've had enough of this movie, so..."

        scene v15s26_24 # FPP Aubrey getting up off the couch. She has a slight smile, mouth open
        with dissolve

        au "I'm gonna go do something else. See you guys!"

        scene v15s26_25 # FPP Aubrey leaving the theater room, closing the door behind her
        with dissolve

        pause 0.75

        scene v15s26_15a
        with dissolve

        ri "Wait, what? Did I do something to upset her?"

        scene v15s26_15b
        with dissolve

        u "No... I think she was just bored of your shitty movie *Laughs*"

        scene v15s26_15h
        with dissolve

        ri "Hey! *Chuckles* Fucker..."

        scene v15s26_15d
        with dissolve

        ri "I was really looking forward to watching this too. I guess two hours really is too much of a commitment for her..."

        scene v15s26_15f
        with dissolve

        u "Yeah, maybe."
        u "I should probably get going anyway. It's been a long day and my eyes are starting to drag, ha."

        scene v15s26_15d
        with dissolve

        ri "Okay, no worries. I'll probably finish it by myself."

        if v15_RileyUpset: # -if RileyUpset
            scene v15s26_26 # FPP View of MC, now standing, looking at Riley, who is looking at the theater screen
            with dissolve

            u "Well, I hope you enjoy it. See you later?"

            scene v15s26_26a # FPP Same angle as 26, Riley does not look at MC, she just picks up the remote and un-pauses the movie
            with dissolve

            pause 0.75

            scene v15s26_26
            with dissolve

            u "Hello?"

            scene v15s26_26b # FPP Same angle as 26, Riley still not looking at MC, neutral expression, mouth open
            with dissolve

            ri "You can shut the door behind you."

            scene v15s26_26
            with dissolve

            u "Ah... Okay. *Scoffs*"

            scene v15s26_27 # FPP MC's view as he opens the door of the theater room to leave
            with dissolve

            u "(Damn, she's actually upset that the conversation didn't go the way she wanted it to... Yikes.)"

        else: # -if not RileyUpset
            scene v15s26_28 # TPP MC and Riley standing up in front of the couch, hugging
            with dissolve

            pause 0.75
        
            scene v15s26_26
            with dissolve

            u "Enjoy it, weirdo."

            scene v15s26_26c # FPP Same angle as 26, Riley looking at MC, slight smile, mouth open
            with dissolve

            ri "Yeah, yeah. Bye."

            scene v15s26_26a
            with dissolve

            pause 0.75

        scene v15s26_27
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v15s27

    else: # -if they didn't have threesome
        scene v15s26_14a
        with dissolve

        au "Anyway, Riley..."

        scene v15s26_24
        with dissolve

        au "I need a break from this torture. Two hours is one hour too long! *Giggles*"

        scene v15s26_29 # FPP Aubrey standing up in front of the couch, smiling down at Riley and MC, mouth closed
        with dissolve

        u "Haha... Yeah, it feels like we've been here for a week."

        scene v15s26_15j # FPP Same angle as 15, Riley looking up at Aubrey who is now standing, Riley smiling with mouth open
        with dissolve

        ri "*Laughs* You two are awful. We're only an hour in!"

        scene v15s26_15h
        with dissolve

        ri "But sure, we can finish it another time."

        scene v15s26_28a # TPP MC, Aubrey, and Riley standing in front of the couch smiling at each other
        with dissolve

        pause 0.75

        scene v15s26_30 # FPP Aubrey, now standing near the couch, looking at Riley who is also standing, slight smile, mouth open
        with dissolve

        au "Yeah, I'm sorry. I guess I really do have a short attention span."

        scene v15s26_31 # FPP Riley, now standing near the couch, looking at Aubrey who is also standing, slight smile, mouth open
        with dissolve

        ri "That's okay. At least it inspired a fun conversation."

        scene v15s26_31a # FPP Same angle as 31, Riley looking at MC with a slight smile, mouth closed
        with dissolve

        u "That is very true."

        scene v15s26_30a # FPP Same angle as 30, Aubrey looking at MC, slight smile, mouth open
        with dissolve

        au "I'll catch you guys later, okay? I need food, ASAP."

        scene v15s26_30b # FPP Same angle as 30b, Aubrey looking at MC with a slight smile, mouth closed
        with dissolve

        u "Yeah, I'm gonna get some rest."

        scene v15s26_31
        with dissolve

        ri "Okay, have a good night, guys."

        scene v15s26_30
        with dissolve

        au "You too!"

        scene v15s26_32 # TPP Aubrey leaving the theater room just ahead of MC # -Aubrey leaves first, MC follows waving goodbye to Riley who is staying behind to continue the movie once they both leave-
        with dissolve

        pause 0.75

        scene v15s26_32a # TPP Same angle as 32, MC leaving the theater room, looking back at Riley and waiving
        with dissolve

        pause 0.75

        scene v15s26_26d # FPP Same angle as 26, Riley looking at MC, smiling and waiving, mouth closed
        with dissolve

        pause 0.75
    
        stop music fadeout 3
    
        jump v15s27
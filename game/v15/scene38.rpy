# SCENE 38: Limo Ride Sebastian or Grayson
# Locations: Limo
# Characters: LINDSEY (Outfit: 4), MC (Outfit: 10), GRAYSON (Outfit: Nice suit), SEBASTIAN (Outfit: Nice suit), AUBREY (Outfit: 8), AUTUMN (Outfit: 3)
# Time: Sunday

label v15s38:
    play music "music/v15/Track Scene 38.mp3" fadein 2

    scene v15s38_1 # FPP The limo parks curbside
    with dissolve

    pause 0.75

    play sound "sounds/honk.mp3"

    scene v15s38_2 # TPP View from inside limo as MC ducks to get in the door, MC smiling and looking around
    with dissolve

    pause 0.75

    scene v15s38_3 # FPP Seated in the limo already are Lindsey, Aubrey, and Autumn. There is an empty seat next to Aubrey
    with dissolve

    pause 0.75

    scene v15s38_4 # TPP MC takes the seat next to Aubrey and locks eyes with her
    with dissolve

    pause 0.75

    # Different reaction based on AubreyTamed, AubreyFriend, and/or if mc got caught with Naomi. If she's happy she'll smile, if not she won't react, and if they're dating she will be flirty-
    if aubrey.relationship >= Relationship.TAMED:
        scene v15s38_5 # FPP Aubrey gives MC a sexy smile and winks at him
        with dissolve

        pause 0.75
    
    elif "v15_naomi" in sceneList:
        scene v15s38_5a # FPP Same angle as 5. Aubrey looking away, neutral expression
        with dissolve

        pause 0.75
    
    else: 
        scene v15s38_5b # FPP Same angle as 5. Aubrey smiling at MC
        with dissolve

        pause 0.75

    if not v15_lindsey_inviteseb: # -if MC chose Grayson, Grayson is also in the limo
        scene v15s38_6
        with dissolve

        pause 0.75

    else: # -if MC chose Sebastian, Sebastian is also in the limo
        scene v15s38_6z # FPP Same as v15s38_6, instead of Grayson, it's Sebastian, Sebastian looking at MC, neutral expression, mouth closed
        with dissolve

        pause 0.75
    
    # -They all have drinks in hand. They will either be cocktails or mocktails in dialogue, but will look exactly the same-
    scene v15s38_7 # FPP Lindsey looking at MC and holding a drink, smiling with mouth open
    with dissolve

    li "Hey, [name], welcome to the VIP party limo!"

    scene v15s38_7a # FPP Same angle as 7. Lindsey still looking at MC, but taking a drink
    with dissolve

    u "Hey! I see you're all already in the party mood."

    if not v15_lindsey_inviteseb: # If Grayson chosen
        if v15_lindsey_alcohol: # VERIFY # -if alcohol and Grayson
            scene v15s38_6a # FPP Same angle as 6, Grayson with a slight smile, holding a drink, looking at MC with mouth open
            with dissolve

            gr "Yeah, drink as much as you can! It's all included in the price."

        else: # -if no alcohol and Grayson
            scene v15s38_6b # FPP Same angle as 6, Grayson looking slightly annoyed, looking at MC with mouth open
            with dissolve

            gr "Yeah, it's more like a kid's party limo with all this juice and soda. *Scoffs*"

        if joinwolves: # -if wolves
            scene v15s38_6
            with dissolve

            u "Ha, sup Grayson? Good to see you."

            scene v15s38_6a
            with dissolve

            gr "Pfft, no it's not! *Laughs* But yeah, you too... I guess."

        else: # -if apes
            scene v15s38_6
            with dissolve

            u "Ha, nice of you to join us, Grayson."

            scene v15s38_6a
            with dissolve

            gr "Yeah, yeah... I can socialize when I want to."

    else: # -if Sebastian
        scene v15s38_8 # FPP Show Sebastian looking at MC, smiling with mouth open
        with dissolve

        se "Hey, [name]!"

        if joinwolves: # -if wolves
            scene v15s38_8a # FPP Same angle as 8, Sebastian looking at MC, smiling with mouth closed
            with dissolve

            u "Hey, Seb. Glad you could make it."

            scene v15s38_8
            with dissolve

            se "Are you kidding, bro? When Lindsey said we're going clubbing, for free, in a limo... You being here is just a cherry on top!"

            scene v15s38_8a
            with dissolve

            u "Haha, I'm glad you're looking forward to it."

        else: # -if apes
            scene v15s38_8a
            with dissolve

            u "Hey, Sebastian. Good to see you."

            scene v15s38_8
            with dissolve

            se "Yeah, you too. It's not often that we get to hangout without Chris and Grayson pushing us to argue. *Chuckles*"

            scene v15s38_8a
            with dissolve

            u "Ha, true!"

    # -Regardless-
    if aubrey.relationship >= Relationship.TAMED: # -if AubreyTamed
        scene v15s38_5c # FPP Same angle as 5, Aubrey smiling at MC, mouth open
        with dissolve

        au "Hey, handsome."

        scene v15s38_5b
        with dissolve

        u "Hello, gorgeous. Fancy meeting you here..."

        scene v15s38_5d # FPP Same angle as 5, Aubrey blushing and turning her head slightly, looking at MC and smiling
        with dissolve

        pause 0.75

    elif "v15_naomi" in sceneList: # -if MC accepted Naomi blowjob
        scene v15s38_5a
        with dissolve

        u "Hey."

        scene v15s38_5e # FPP Same angle as 5, Aubrey looking at MC with a neutral expression, mouth open
        with dissolve

        au "*Whispers* I'm still pissed at you, but I'll try to be civil. Just for tonight, okay?"

        scene v15s38_5f # FPP Same angle as 5, Aubrey looking at MC with a neutral expression, mouth closed
        with dissolve

        u "*Whispers** Okay, thanks... I really don't like it when things are weird between us."

        scene v15s38_5e
        with dissolve

        au "Yeah..."

        scene v15s38_5g # FPP Same angle as 5, Aubrey looking away. She has a hurt expression, mouth open
        with dissolve

        au "Me either."

    else: # -if AubreyFriend, and no Naomi blowjob, so she's not mad at MC
        scene v15s38_5b
        with dissolve

        u "Hey, you. It feels like it's been forever since we last saw each other..."

        scene v15s38_5c
        with dissolve

        au "Haha, right... We're gonna sleep so well tonight, dude."

        scene v15s38_5b
        with dissolve

        u "Ain't that the truth. *Chuckles*"

    # -Regardless-
    if not v15_lindsey_inviteseb: # -if Grayson
        scene v15s38_6c # FPP Same angle as 6, Grayson looking at Autumn, slight smile, mouth open
        with dissolve

        gr "How are things going with the Deer, Autumn?"

        scene v15s38_9 # FPP Autumn looking at Grayson, slight smile, mouth open
        with dissolve

        aut "Oh! Yeah, it's going great, thanks."

        scene v15s38_6c
        with dissolve

        gr "I'm only asking because I never hear a damn thing about your sorority, ha!"

        gr "Nobody likes a President that just cruises along doing nothing."

        scene v15s38_7b # FPP Same angle as 7, Lindsey looking at Grayson, slight smile, mouth open
        with dissolve

        li "Autumn is the hardest working President I know."

        scene v15s38_9b # FPP Same angle as 9, Autumn looking at Lindsey, embarrassed expression, mouth open
        with dissolve

        aut "Thanks, Linds..."

        scene v15s38_6c
        with dissolve

        gr "Okay, whatever... What do you even do?"

        scene v15s38_9
        with dissolve

        aut "What do you mean?"

        scene v15s38_6c
        with dissolve

        gr "What's your ethos, Autumn?"

        scene v15s38_9
        with dissolve

        aut "Everyone knows what the Deer are about, Grayson. Same as people know what the Apes are about."

        aut "Which is mostly that their President can be a real dick sometimes."

        scene v15s38_10 # TPP Wide shot of everyone in the limo, Grayson rolling his eyes, everyone else laughing, Aubrey's mouth open
        with dissolve

        au "Only sometimes, haha?"

        scene v15s38_6d # FPP Same angle as 6, Grayson looking at Aubrey, neutral expression, mouth open
        with dissolve

        gr "Hey, Aubrey. I'm talking to Autumn here."

        scene v15s38_5h # FPP Same angle as 5, Aubrey looking at Grayson, neutral expression, mouth open
        with dissolve

        au "No, you're being a dick to Autumn here."

        scene v15s38_7b
        with dissolve

        li "Hey, okay- Let's just chill and enjoy the night guys, okay?"

        scene v15s38_6e # FPP Same angle as 6, Grayson looking at Lindsey, neutral expression, mouth open
        with dissolve

        gr "Autumn started it."

        menu:
            "Stay quiet":
                $ add_point(KCT.BRO)
                
                scene v15s38_6f # FPP Same angle as 6, Grayson looking at Autumn, neutral expression, mouth closed
                with dissolve

                u "(Maybe it wasn't such a good idea to invite Grayson. I doubt Sebastian would be causing drama like this.)"

            "Change the subject":
                $ add_point(KCT.BOYFRIEND)
                
                scene v15s38_6f
                with dissolve

                u "I wonder what the club is going to look like."

                scene v15s38_6a
                with dissolve

                gr "There better be loads of hot girls. That's the only reason I'm going, haha."

                scene v15s38_7b
                with dissolve

                li "You're already with a bunch of hot girls!"

                scene v15s38_6f
                with dissolve

                pause 0.75

                scene v15s38_6a
                with dissolve

                gr "Hmm, that's questionable. *Laughs*"

        # -Regardless
        scene v15s38_6c
        with dissolve

        gr "So, who's getting laid tonight? Come on, show me your hands!"

        scene v15s38_6g # FPP Same angle as 6, Grayson holding both of his hands in the air
        with dissolve

        menu:
            "Raise your hands":
                $ add_point(KCT.BOYFRIEND)
                
                scene v15s38_11 # TPP Show MC holding both of his hands in the air, smiling with mouth closed
                with dissolve

                pause 0.75

                if aubrey.relationship >= Relationship.TAMED: # -if AubreyTamed, she raises hers after she sees MC raise his, and she winks at him-
                    scene v15s38_5i # FPP Same angle as 5, Aubrey raising both of her hands, smiling and winking at MC
                    with dissolve

                    pause 0.75

                else: # -if else, MC is the only other person to raise their hands-
                    scene v15s38_10b # TPP Same wide shot of everyone as 10, MC and Grayson each have both hands in the air, smiling, Aubrey rolling her eyes at MC
                    with dissolve

                    pause 0.75

                if not joinwolves: # -if Apes
                    scene v15s38_6a
                    with dissolve

                    gr "That's my boy right there."

                else: # -if Wolves
                    scene v15s38_6a
                    with dissolve

                    gr "That's right, [name], get those hands in the air! I guess you're okay for a pussy wolf, haha."

                scene v15s38_7
                with dissolve

                li "Guys, that's not what tonight is about."

                scene v15s38_6h # FPP Same angle as 6, Grayson looking at Lindsey, smiling with mouth open
                with dissolve

                gr "It is for us, haha."

                scene v15s38_7c # FPP Same angle as 7, Lindsey looking at Grayson. She looks annoyed, mouth closed
                with dissolve

                pause 0.75
            
            "Don't raise them":
                $ add_point(KCT.BOYFRIEND)
                
                scene v15s38_10a # TPP Same wide shot of everyone as 10, everyone looking at Grayson. Grayson with annoyed expression, mouth open
                with dissolve

                gr "You guys are so fucking boring!"

    else: # -if Sebastian
        scene v15s38_8b # FPP Same angle as 8, Sebastian looking at Lindsey, smiling with mouth open
        with dissolve

        se "I've been working so hard on things with the Wolves lately. This night out is seriously needed, haha."

        scene v15s38_7d # FPP Same angle as 7, Lindsey looking at Sebastian, smiling with mouth open
        with dissolve

        li "Oh, I know exactly what you mean."

        scene v15s38_9c # FPP Same angle as 9, Autumn looking at Lindsey, smiling with mouth open
        with dissolve

        aut "Campaigning is the hardest though. Regular work is hard, but I would hate to have to campaign again!"

        scene v15s38_5j # FPP Same angle as 5, Aubrey looking at Autumn, neutral expression, mouth open
        with dissolve

        au "All this talk about hard work. Imagine what'll be like when we leave college and go out into the adult world... Ugh."

        scene v15s38_5b
        with dissolve

        u "Yeah, no thanks... That's a scary thought. *Chuckles*"

        scene v15s38_8
        with dissolve

        se "You're telling me, haha."

        scene v15s38_8b
        with dissolve

        se "I wonder what careers we'll all end up having."

        menu:
            "Be encouraging":
                $ add_point(KCT.BOYFRIEND)
                
                scene v15s38_8a
                with dissolve

                u "I think everyone here will be successful whatever we choose to do."

                scene v15s38_12 # TPP Wide shot of everyone in the limo with Sebastian, everyone looking at MC. MC gesturing to everyone, slight smilie, mouth open
                with dissolve

                u "I mean, just look at us tonight. Not everyone's a VIP at college, and we're taking a limo to an all-inclusive club."

                scene v15s38_7
                with dissolve

                li "Haha! Cheers to that!"

                scene v15s38_12a # TPP Same wide shot of everyone as 12, Everyone holding their drinks in the air in a "cheers" gesture
                with dissolve

                pause 1
            
            "Make a joke":
                $ add_point(KCT.BRO)
                
                scene v15s38_8a
                with dissolve

                u "We'd be lucky to get any career at all... *Scoffs*"

                scene v15s38_9d # FPP Same angle as 9, Autumn looking at MC, smiling with mouth open
                with dissolve

                aut "Hey! I'm smart, okay?"

                scene v15s38_8b
                with dissolve

                se "Yeah, she is... But the rest of us, well... He might be right."

                scene v15s38_5k # FPP Same angle as 5, Aubrey looking at Sebastian, smiling with eyebrow raised, mouth open
                with dissolve

                au "No way. I'm gonna be so successful that the rest of my family will be on their knees begging for money."

                scene v15s38_5l # FPP Same angle as 5, Aubrey looking at Sebastian, slight smile with mouth closed
                with dissolve

                u "(Sheesh...)"

                if v15s33_cheese: # -if ate Uncle Ricky's cheese at the wedding, and had a deep convo with him about Aubrey
                    scene v15s38_5b
                    with dissolve

                    u "Even Uncle Ricky?"

                    scene v15s38_5c
                    with dissolve

                    au "Hehe, no. Uncle Ricky can have as much cheese as he wants."

                    scene v15s38_8c # FPP Same angle as 8, Sebastian looking at Aubrey, neutral expression, mouth open
                    with dissolve

                    se "What the hell is an Uncle Ricky...?"

                    scene v15s38_12b # TPP Same wide shot of everyone as 12, MC and Aubrey laughing really hard, everyone else smiling and looking at them like they're crazy
                    with dissolve

                    pause 1

                # -if did not eat the cheese, continue regardless

    # -Regardless of whether Grayson or Sebastian-
    scene v15s38_9c
    with dissolve

    aut "So, how's your campaign going, Lindsey?"

    scene v15s38_7e # FPP Same angle as 7, Lindsey looking at Autumn, smiling with mouth open
    with dissolve

    li "Great so far! Thanks for asking, Autumn."

    scene v15s38_5m # FPP Same angle as 5, Aubrey looking at Lindsey, slight smile with mouth open
    with dissolve

    au "You seem to be working really hard and people are recognizing that."

    scene v15s38_7f # FPP Same angle as 7, Lindsey looking at Aubrey, slight smile with mouth open
    with dissolve

    li "Aw, thanks for saying that. I really have been putting everything I have into this."

    scene v15s38_7
    with dissolve

    li "And [name] has been an amazing help too."

    scene v15s38_7g # FPP Same angle as 7, Lindsey looking at MC, smiling with mouth closed
    with dissolve

    u "Of course, I'm happy to help. It's been kinda fun actually."

    scene v15s38_9c
    with dissolve

    aut "You can work so hard that there's never any time for anything else, though."

    scene v15s38_7e
    with dissolve

    li "Yeah, I haven't even thought about anything else."

    scene v15s38_5m
    with dissolve

    au "And no time for relationships, I bet."

    scene v15s38_7f
    with dissolve

    li "Haha, well... No, no sex. *Giggles*"

    scene v15s38_5m
    with dissolve

    au "That's got to be frustrating, haha."

    if not v15_lindsey_inviteseb: # -if Grayson
        scene v15s38_6h
        with dissolve

        gr "Oh, Lindsey's still a virgin anyway."

        scene v15s38_7b
        with dissolve

        li "Shut up, Grayson. I am not."

        scene v15s38_6h
        with dissolve

        gr "*Laughs*"

        scene v15s38_6c
        with dissolve

        gr "I bet someone here still is though."

        scene v15s38_6i # FPP Same angle as 6, Grayson looking at Aubrey, smiling with mouth open
        with dissolve

        gr "Definitely not Aubrey. Not according to everyone on campus... Haha!"

        scene v15s38_6j # FPP Same angle as 6, Grayson grinning at MC, mouth closed
        with dissolve

        u "Dude."

        scene v15s38_5h
        with dissolve

        au "You're such a fucking dick. One day you're gonna choke on your own bullshit."

        scene v15s38_6c
        with dissolve

        gr "Now, Autumn's the mystery..."

        scene v15s38_9e # FPP Same angle as 9, Autumn looking at Grayson, annoyed expression, mouth closed
        with dissolve

        gr "I've never seen you with anyone. No guys. Not even a girl."

        scene v15s38_9f # FPP Same angle as 9, Autumn looking at Grayson, annoyed expression, mouth open
        with dissolve

        aut "Well Grayson, not that it's any of your business, but..."

        scene v15s38_9b
        with dissolve

        aut "I'm asexual."

        scene v15s38_6c
        with dissolve

        gr "A... What-now?"

    else: # -if Sebastian
        scene v15s38_8b
        with dissolve

        se "Is it possible to live without sex, haha?"

        scene v15s38_9g # FPP Same angle as 9, Autumn looking at Sebastian, smiling with mouth open
        with dissolve

        aut "Well, I might know a thing or two about that, haha."

        scene v15s38_8d # FPP Same angle as 8, Sebastian looking at Autumn, smiling with mouth open
        with dissolve

        se "Oh, really?"

        scene v15s38_9g
        with dissolve

        aut "I haven't made it public knowledge or anything like that, but I don't mind telling you guys about it..."

        scene v15s38_9b
        with dissolve

        aut "I'm asexual."

        scene v15s38_5j
        with dissolve

        au "Wait. What does that mean exactly?"

    # -Regardless of Grayson or Sebastian
    scene v15s38_9h # FPP Same angle as 9, Autumn looking at Aubrey, slight smile, mouth open
    with dissolve

    aut "It basically means I don't desire sex. I'm not controlled by those... Primal urges you all have."

    scene v15s38_9i # FPP Same angle as 9, Autumn looking at MC, slight smile, mouth closed
    with dissolve

    u "Sounds like a superpower. *Chuckles*"

    # -depending on Grayson or Sebastian, show an image of their confused reaction to Autumn's confession-
    if not v15_lindsey_inviteseb: # if Grayson
        scene v15s38_6k # FPP Same angle as 6, Grayson looking at Autumn, confused, mouth closed
        with dissolve

        pause 0.75

    else: # if Sebastian
        scene v15s38_8e # FPP Same angle as 8, Sebastian looking at Autumn, confused, mouth closed
        with dissolve

        pause 0.75

    scene v15s38_7e
    with dissolve

    li "So, you've never tried it?"

    scene v15s38_9c
    with dissolve

    aut "Nope. I haven't ever felt like I wanted to."

    scene v15s38_5n # FPP Same angle as 5, Aubrey looking at Autumn, smiling with mouth open
    with dissolve

    au "Ha, what? You're missing out. Sex is amazing!"

    scene v15s38_9h
    with dissolve

    aut "Haha, I'll just have to take your word for it."

    if not v15_lindsey_inviteseb: # -if Grayson
        scene v15s38_6c
        with dissolve

        gr "Just get laid tonight and get it over with! You don't want that hanging over you forever..."

        gr "Who the hell wants to stay a virgin all their life? *Laughs*"

        scene v15s38_7h # FPP Same angle as 7, Lindsey looking at Grayson, neutral expression, mouth open
        with dissolve

        li "You're such an insensitive twat, Grayson."

        scene v15s38_6e
        with dissolve

        gr "Um-"

        scene v15s38_5h
        with dissolve

        au "Grayson, just keep quiet. Adults are talking."

        scene v15s38_6d
        with dissolve

        gr "*Groans* Whatever."

    else: # -if Sebastian
        scene v15s38_8d
        with dissolve

        se "Have you ever been in a relationship?"

        scene v15s38_9g
        with dissolve

        aut "Not really, no."

        scene v15s38_8d
        with dissolve

        se "Man, that must be difficult."

    # -Regardless of Grayson or Sebastian-
    scene v15s38_9c
    with dissolve

    aut "It's difficult finding people who understand."

    scene v15s38_5j
    with dissolve

    au "Do you think you'll ever want to have sex with someone?"

    scene v15s38_9h
    with dissolve

    aut "Well, it might happen one day, I guess. Never say never. *Giggles*"

    scene v15s38_5n
    with dissolve

    au "You should probably try it to see if you like it, though."

    scene v15s38_9j # FPP Same angle as 9, Autumn looking down. She looks uncomfortable, mouth open
    with dissolve

    aut "Maybe..."

    scene v15s38_9e
    with dissolve

    u "(I think she might be finished with this convo...)"

    menu:
        "Stop the questioning": # -if Stop the questioning (and helped Autumn with boxes at dog shelter and/or went to the protest with her in Act1, creates AutumnTrust)
            $ add_point(KCT.BOYFRIEND)
            
            if protest or v15_autumn_lunchbreak: # Went to protest
                $ AutumnTrust = True
            
            u "Okay, I think that's enough questions for right now, haha."

            scene v15s38_9i
            with dissolve

            u "It's probably not an easy thing to talk about in front of everyone."

            scene v15s38_5j
            with dissolve

            au "Oh, yeah. Of course! Sorry, Autumn."

            scene v15s38_9h
            with dissolve

            aut "No, it's fine... I brought it up anyway, didn't I? Ha."

            scene v15s38_9d
            with dissolve

            aut "Thanks, [name]."

            scene v15s38_9i
            with dissolve

            u "No problem."

        "Ask a question": # -if Ask a question
            $ add_point(KCT.TROUBLEMAKER)

            u "So, who would you try it out with? A guy or a girl?"

            scene v15s38_9j
            with dissolve

            aut "Um..."

            scene v15s38_5n
            with dissolve

            au "Ooh, a girl might actually be better for your first time..."

            if not v15_lindsey_inviteseb: # -if Grayson
                scene v15s38_6d
                with dissolve

                gr "What the fuck? How?! Don't tell her that!"

            else: # -if Sebastian
                scene v15s38_8c
                with dissolve

                se "Wait... Really?"

            # -regardless-
            scene v15s38_7f
            with dissolve

            li "I think that's enough questions for now."

            scene v15s38_7e
            with dissolve

            li "You don't have to keep talking about it if you don't want to."

            scene v15s38_9c
            with dissolve

            aut "Thanks, Lindsey."

            scene v15s38_9i
            with dissolve

            u "Oh, right. Sorry, Autumn."

            scene v15s38_9d
            with dissolve

            aut "Ah, no worries. I'm the one who brought it up anyway, ha."

    # -Regardless-
    if not v15_lindsey_inviteseb: # -if Grayson
        scene v15s38_6c
        with dissolve

        gr "Well, for the record, I'd happily volunteer to help you out with that, Autumn."

        scene v15s38_9e
        with dissolve

        pause 0.75

        scene v15s38_5h
        with dissolve

        au "Wow. How very honorable of you, Grayson."

        scene v15s38_6i
        with dissolve

        gr "Hey, I'm just trying to be a more considerate guy, you know? *Laughs*"

    else: # -if Sebastian
        scene v15s38_8d
        with dissolve

        se "Whatever you decide, just know there'll be guys lining up to take you out on a first date."

        scene v15s38_9g
        with dissolve

        aut "Aww, that's sweet. Thanks, Sebastian. *Chuckles*"

        scene v15s38_7e
        with dissolve

        li "Oh, don't let his amazing personality fool you. Seb is one fart away from murdering all of us."

        scene v15s38_8f # FPP Same angle as 8, Sebastian looking at Lindsey, shocked expression, mouth open
        with dissolve

        se "Linds! Quit fucking saying that to so many people... Haha!"

        scene v15s38_7g
        with dissolve

        u "Haha, wait what? Is that actually true?"

        scene v15s38_7d
        with dissolve

        li "His ex was my best friend and not only did I hear a countless number of stories, I also heard her throwing up... Twice!"

        scene v15s38_5o # FPP Same angle as 5, Aubrey looking at Sebastian, laughing with mouth open
        with dissolve

        au "Ugh! Oh my god, Seb..."

        scene v15s38_8c
        with dissolve

        se "I'm lactose-intolerant! I made a mistake, okay?"

        scene v15s38_9g
        with dissolve

        aut "Twice?"

        scene v15s38_7d
        with dissolve

        li "More times than that!"

        scene v15s38_8g # FPP Same angle as 8, Sebastian looking down in embarrassment, mouth closed
        with dissolve

        u "*Laughs* This is too good. You finally have a flaw, Fabio."

        scene v15s38_8h # FPP Same angle as 8, Sebastian looking down in embarrassment, mouth open
        with dissolve

        se "*Sighs*"

        if joinwolves: # -if Wolves
            scene v15s38_8g
            with dissolve

            u "Don't worry, man. Your stinky secret is safe with me."

            scene v15s38_7d
            with dissolve

            li "Not with me, haha!"

    # -Regardless of Grayson or Sebastian-
    scene v15s38_5n
    with dissolve

    au "Well, personally, I'd vote for [name]. I think he'd be a good choice for your first time."

    if "v12_lindsey" in sceneList:
        scene v15s38_7e
        with dissolve

        li "Yeah... Uh, I would second that. *Giggles*"

    # -Regardless-
    scene v15s38_5b
    with dissolve

    u "Well, nice to know I have the female vote... *Chuckles*"

    if v15_lindsey_inviteseb: # -if Sebastian
        scene v15s38_8
        with dissolve

        se "Damn, [name]. How do I get your reputation?"

    else: # -if Grayson
        scene v15s38_6d
        with dissolve

        gr "What the hell are you guys drinking?! [name]? Seriously?"

        scene v15s38_10c # TPP Same wide shot of everyone as 10, girls looking at MC, Aubrey biting her lip, Lindsey winking, Autumn smiling. Grayson looking around confused
        with dissolve

        pause 1

        scene v15s38_6d
        with dissolve

        gr "What the fuck...?"

    # -regardless-
    scene v15s38_9h
    with dissolve

    aut "Haha, okay. I'll keep all of this in mind. Let's change the subject now, please?"

    scene v15s38_13 # FPP Show Lindsey turning her head to look out the window, mouth open
    with dissolve

    li "Don't worry, Autumn. It looks like we're here!"

    scene v15s38_9c
    with dissolve

    aut "Oh, good!"

    if not v15_lindsey_inviteseb: # -if Grayson
        scene v15s38_6e
        with dissolve

        gr "It's about damn time!"

    else: # -if Sebastian
        scene v15s38_8b
        with dissolve
        
        se "Let's get our groove on, baby!"

    # -Regardless-
    # -would be cute to end with a final cheers from the entire group, they're smiling, and finish off their drinks
    if not v15_lindsey_inviteseb: # if Grayson
        scene v15s38_10d # TPP Same wide shot of everyone as 10, Everyone holding their drinks in the air in a "cheers" gesture
        with dissolve

        pause 0.75

        scene v15s38_10e # TPP Same wide shot of everyone as 10, everyone finishing off their drinks
        with dissolve

        pause 0.75

    else: # if Sebastian
        scene v15s38_12a
        with dissolve

        pause 0.75

        scene v15s38_12c # TPP Same wide shot of everyone as 12, everyone finishing off their drinks
        with dissolve

        pause 0.75

    stop music fadeout 3

    jump v15s39
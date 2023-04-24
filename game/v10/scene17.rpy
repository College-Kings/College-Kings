# SCENE 17: At Aubrey's/Aubrey Sex Scene
# Locations: MC bedroom, Chicks house
# Characters: MC(Outfit 1 ), Aubrey(outfit 3), Nora (outfit 1)
# Time: Sunday evening

label v10_aubrey_house:
    play music "music/v10/Track Scene 17_1.mp3" fadein 2
    scene v10auh1 # FPP Show Aubrey, walking on sidewalk in the evening, slight smile, mouth closed
    with dissolve

    u "Look at me, walking you home, out of the kindness of my heart."

    if CharacterService.is_fwb(aubrey): # If in relationship with Aubrey
        scene v10auh1a # FPP Same angle as v10auh1, Aubrey with slight smile and eyebrow raised, mouth open
        with dissolve
        
        au "Just walking me home, huh? No ulterior motive?"

        menu:
            "Maybe":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                scene v10auh1b # FPP Same angle and expression as v10auh1a,, Aubrey mouth closed
                with dissolve

                u "Well... I may have one or two ideas on what could be done once we're actually at your place."

                scene v10auh1a
                with dissolve

                au "Really? How about you tell me some of your ideas?"

                scene v10auh1b
                with dissolve

                u "How about I just show you when we get there?"

                scene v10auh1c # FPP Same angle as v10auh1, Aubrey smiling, mouth open
                with dissolve

                au "*Chuckles* Alright, you got me excited there..."

            "Just a walk":
                scene v10auh1
                with dissolve
    
                u "A walking companion you asked for and a walking companion you got."

                scene v10auh1a
                with dissolve

                au "Oh, that's too bad. I was hoping for just a little more. *Laughs*"

                scene v10auh1b
                with dissolve

                u "*Chuckles* We'll see how the walk goes."

                scene v10auh1c
                with dissolve

                au "*Chuckles*"

    else: # Not in relationship with Aubrey
        scene v10auh1c
        with dissolve

        au "Yeah, hot girls can't be out walking all alone. Who knows what could happen."

        scene v10auh1
        with dissolve

        u "*Chuckles*"

    scene v10auh1d # FPP Same angle as v10auh1, Aubrey expressionless, mouth closed
    with dissolve

    u "So... was the gym busy?"

    scene v10auh1e # FPP Same angle and expression as v10auh1d, Aubrey mouth open
    with dissolve

    au "It kinda was. Usually it's really quiet around this time, but all of the sudden it was packed."
    au "I left early to keep from beefing with this one girl."

    scene v10auh1d
    with dissolve

    u "What happened?"

    scene v10auh1e
    with dissolve

    au "Some chick walked over to me, I have no clue who she was but apparently she knew me."
    au "Called me a slut and started telling me her whole life story." 
    
    au "Something about me sleeping with her boyfriend at the start of the year and me being the reason they're no longer together, bla bla bla."

    scene v10auh1
    with dissolve

    u "How is she gonna be upset with you? You're not the one that cheated, he did. *Laughs*"

    scene v10auh1c
    with dissolve

    au "That's exactly what I told her. It's not my fault your boyfriend has to stray cause you can't please him in bed... *Laughs*"

    scene v10auh1b
    with dissolve

    u "Have you always been so uhm... exciting, adventurous... whatever you wanna call it?"

    scene v10auh1c
    with dissolve

    au "Oh God no, I was actually super shy growing up."
    au "In high school, girls used to make fun of me because I was super dorky and none of the guys wanted to talk to me."
    
    au "I had a major glow up senior year."

    scene v10auh1
    with dissolve

    menu:
        "Compliment her":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene v10auh1f # FPP Same angle as v10auh1, Aubrey has a big smile, mouth closed
            with dissolve

            u "What? You're saying you weren't always this hot?"

            scene v10auh1c
            with dissolve

            au "I was always hot on the inside. *Laughs*"

            scene v10auh1f
            with dissolve

            u "*Laughs*"

        "Make a joke":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene v10auh1b
            with dissolve

            u "So what, after your dorky phase was over you just slept with all their boyfriends?"

            scene v10auh1a
            with dissolve

            au "Oh, funny."

            scene v10auh1b
            with dissolve

            u "So I've been told."

    scene v10auh1d
    with dissolve

    u "What gave you all the confidence? Most people struggle with that shit, especially girls..."

    scene v10auh1e
    with dissolve

    au "Honestly I think it's mostly due to my older sister."
    au "She's a Kiwii model. She went through a lot of the same gossip and drama stuff that I went through."

    au "But if you saw her today you would never guess it."
    au "She could spend a whole day going through messages from guys trying to talk to her and still wouldn't be done with them."

    scene v10auh1d
    with dissolve

    u "Damn, sounds like your sister is fun to be around. Maybe I should message her and see if she could boost my confidence too."

    scene v10auh1g # FPP Same angle as v10auh1, Aubrey looks annoyed, mouth open
    with dissolve

    au "Haha, get in line."

    scene v10auh1h # FPP Same angle and expression as v10auh1g, Aubrey mouth closed
    with dissolve

    u "What did you say your sister's name was again?"

    scene v10auh1a
    with dissolve

    au "*Laughs* I didn't. Don't worry, you may get a chance to meet her soon. I'm pretty sure she's coming to visit."

    scene v10auh1d
    with dissolve

    u "Do you see your family often?"

    scene v10auh1e
    with dissolve

    au "Not really, I really wanted to go to this school, but it's pretty far from home."
    au "I talk to my family on the phone, but it really isn't that big of a deal to me." 
    
    au "I'm just trying to have fun right now."

    scene v10auh1d
    with dissolve

    menu:
        "Ask about her":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            
            scene v10auh1
            with dissolve

            u "How's that going for you?"

            if CharacterService.is_fwb(aubrey): # If in a relationship with Aubrey
                scene v10auh1a
                with dissolve

                au "Pretty good, I'd say we have a lot of fun, wouldn't you?"

                scene v10auh1b
                with dissolve

                u "Oh yes, we do..."

            else: # Not in a relationship with Aubrey
                scene v10auh1a
                with dissolve

                au "Not too bad. *Chuckles*"

        "Ask about her sister":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene v10auh1h
            with dissolve

            u "So your sister... is she like really into parties or what's her deal?"

            scene v10auh1c
            with dissolve

            au "*Laughs* I think that's enough about my family."

    scene v10auh2 # FPP Show Aubrey, inside hallway of Chicks house, Aubrey holding clothes in her hand while wearing gym clothes, mouth open
    with fade

    au "Hey, so I gotta go change, I'll be right back."

    scene v10auh2a # FPP Same angle as v10auh2, show Aubrey, back to MC, opening door to bathroom while holding clothes
    with dissolve

    menu:
        "Ask to watch":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            if CharacterService.is_fwb(aubrey): # Aubrey relationship check
                label v10s17_galleryScene:
                $ sceneList.add("v10_aubrey")
                
                scene v10auh2b # FPP Same angle as v10auh2, show Aubrey at door to bathroom, turning to look at MC, mouth closed
                with dissolve

                u "Can I come watch?"

                scene v10auh2c # FPP Same angle and position as v10auh2b, Aubrey smiling with eyebrow raised, mouth open
                with dissolve
                stop music fadeout 3
                play music "music/v10/Track Scene 17_2.mp3" fadein 2
                au "*Chuckles* Of course."

                scene v10auh3 # TPP Outside bathroom at Chicks house, show Aubrey grabbing MC to pull him toward the bathroom, both smiling
                with dissolve

                pause 0.5
                
                scene v10auh4 # TPP Inside bathroom of Chicks house, MC sitting on closed toilet and looking at Aubrey, Aubrey with eyebrow raised and smiling, Aubrey mouth open
                with dissolve

                au "My sister may be the famous model, but I'm the real star. I could be an actress."

                scene v10auh5 # FPP Show Aubrey, inside Chicks bathroom, eyebrow raised and smiling, mouth closed
                with dissolve

                u "I'd watch all those movies."

                scene v10auh5a # FPP Same angle and expression as v10auh5, Aubrey mouth open
                with dissolve

                au "Okay Mr. Director, how should THIS movie start?"

                menu:
                    "Top":
                        scene v10auh5
                        with dissolve

                        u "How about we start with your top?"

                        if config_censored:
                            call screen censored_popup("v10s17_nsfwSkipLabel1")

                        scene v10auh5b # FPP Same angle as v10auh5, Aubrey removing top with bottoms still on while smiling, mouth open
                        with dissolve

                        au "Anything you want."

                        scene v10auh5c # FPP Same angle as v10auh5, show Aubrey topless, smiling with eyebrow raised, mouth closed
                        with dissolve

                        u "I think our viewers will really appreciate these shots!"

                        scene v10auh5d # FPP Same angle and expression as v10auh5c, Aubrey topless, mouth open
                        with dissolve

                        au "Think I can make it to the big leagues Mr. Director?"

                        scene v10auh5c
                        with dissolve

                        u "Easily!"

                        scene v10auh5e # Same angle as v10auh5, Aubrey completely nude, smiling with mouth open, posing for MC
                        with dissolve

                        au "I'm enjoying the audience."

                    "Bottom":
                        scene v10auh5
                        with dissolve
                        
                        u "Let's start with the bottoms."

                        if config_censored:
                            call screen censored_popup("v10s17_nsfwSkipLabel1")

                        scene v10auh5f # FPP Same angle as v10auh5, Aubrey removing bottoms while top still on, smiling, mouth open
                        with dissolve

                        au "Anything you want."

                        scene v10auh5g # FPP Same angle and expression as v10auh5c, Aubrey bottomless, smiling with eyebrow raised, mouth closed
                        with dissolve

                        u "I think our viewers will really appreciate these shots!"

                        scene v10auh5h # FPP Same angle and expression as v10auh5g, Aubrey bottomless, mouth open
                        with dissolve

                        au "Think I can make it to the big leagues Mr. Director?"

                        scene v10auh5g
                        with dissolve

                        u "Easily!"

                        scene v10auh5e
                        with dissolve

                        au "I'm enjoying the audience."

                scene v10auh5i # FPP Same angle and expression as v10auh5e, Aubrey mouth closed
                with dissolve

                u "I'm enjoying the show."

                scene v10auh5e
                with dissolve

                $ grant_achievement("getting_clean")
                au "Your turn."

                scene v10auh5i
                with dissolve

                u "Someone's eager!"

                show screen v10s17_aubreySexOverlay

                image v10aubbj = Movie(play="images/v10/Scene 17/v10aubbj.webm", loop=True, image= "images/v10/Scene 17/v10aubbjStart.webp", start_image="images/v10/Scene 17/v10aubbjStart.webp") # TPP. Aubrey on her knees giving MC a blowjob who is sat on the toilet.
                image v10aubbjf = Movie(play="images/v10/Scene 17/v10aubbjf.webm", loop=True, image= "images/v10/Scene 17/v10aubbjStart.webp", start_image="images/v10/Scene 17/v10aubbjStart.webp")

                image v10aubbjtpp = Movie(play="images/v10/Scene 17/v10aubbjtpp.webm", loop=True, image= "images/v10/Scene 17/v10aubbjtppStart.webp", start_image="images/v10/Scene 17/v10aubbjtppStart.webp")
                image v10aubbjtppf = Movie(play="images/v10/Scene 17/v10aubbjtppf.webm", loop=True, image= "images/v10/Scene 17/v10aubbjtppStart.webp", start_image="images/v10/Scene 17/v10aubbjtppStart.webp")

                image v10aubcg = Movie(play="images/v10/Scene 17/v10aubcg.webm", loop=True, image= "images/v10/Scene 17/v10aubcgStart.webp", start_image="images/v10/Scene 17/v10aubcgStart.webp") # TPP. Aubrey riding MC cowgirl while he's sat on the toilet.
                image v10aubcgf = Movie(play="images/v10/Scene 17/v10aubcgf.webm", loop=True, image= "images/v10/Scene 17/v10aubcgStart.webp", start_image="images/v10/Scene 17/v10aubcgStart.webp")

                image v10aubll = Movie(play="images/v10/Scene 17/v10aubll.webm", loop=True, image= "images/v10/Scene 17/v10aubllStart.webp", start_image="images/v10/Scene 17/v10aubllStart.webp") # TPP. MC holding Aubreys leg up while he fucks her. 
                image v10aubllf = Movie(play="images/v10/Scene 17/v10aubllf.webm", loop=True, image= "images/v10/Scene 17/v10aubllStart.webp", start_image="images/v10/Scene 17/v10aubllStart.webp")

                image v10aubll2 = Movie(play="images/v10/Scene 17/v10aubll2.webm", loop=True, image= "images/v10/Scene 17/v10aubll2Start.webp", start_image="images/v10/Scene 17/v10aubll2Start.webp")
                image v10aubll2f = Movie(play="images/v10/Scene 17/v10aubll2f.webm", loop=True, image= "images/v10/Scene 17/v10aubll2Start.webp", start_image="images/v10/Scene 17/v10aubll2Start.webp")

                image v10aubfa = Movie(play="images/v10/Scene 17/v10aubfa.webm", loop=True, image= "images/v10/Scene 17/v10aubfaStart.webp", start_image="images/v10/Scene 17/v10aubfaStart.webp") # TPP. Aubrey on her knees giving MC a blowjob who is sat on the toilet.
                image v10aubfaf = Movie(play="images/v10/Scene 17/v10aubfaf.webm", loop=True, image= "images/v10/Scene 17/v10aubfaStart.webp", start_image="images/v10/Scene 17/v10aubfaStart.webp")
                
                label v10s17_aubreyBlowjob:
                    scene v10aubbj # Aubrey starts giving MC a blowjob while he's sitting on the toilet.
                    with dissolve
                    pause

                    u "Holy shit, this is amazing!"

                    u "You really know what you're doing."

                    scene v10aubbjf
                    with dissolve
                    pause

                    u "(Damn, she's good!)"

                    u "Fuck, Aubrey!"

                    scene v10aubbjtpp
                    with dissolve
                    pause

                    u "Oh fuck!"

                    scene v10aubbjtppf
                    with dissolve

                    u "Mhmmmm..."
                    u "That's fucking amazing."

                label v10s17_aubreyCowgirl:
                    scene v10aubcg # Aubrey then gets up and rides MC
                    with dissolve
                    pause

                    au "We're not finished yet!"

                    au "Oh my God it's BIG!"

                    scene v10aubcgf
                    with dissolve
                    pause

                    u "Damn this feels good!"

                    au "*Moaning*"

                label v10s17_aubreyStanding:
                    scene v10aubll # Fades to MC bracing Aubrey against him in standing missionary
                    with dissolve
                    pause

                    u "My turn!"

                    au "OH MY GOD!"

                    scene v10aubllf
                    with dissolve
                    pause

                    au "Faster, [name]!"

                    au "*Moaning*"

                    scene v10aubll2
                    with dissolve
                    pause
                    
                    au "*Groans* Mhmmmmm."

                    au "Fuuuuuuck!"

                    scene v10aubll2f
                    with dissolve
                    pause 

                    au "This feels so good!"

                scene v10aubfa # Aubrey gets on her knees in front MC while he's standing to finish him off
                with dissolve
                pause

                u "Fuck, I'm gonna cum!"

                scene v10aubfaf
                with dissolve
                pause

                au "Yes [name], cum on my face!"

                au "*Laughs* And scene."

                hide screen v10s17_aubreySexOverlay

                scene v10aubfa1 # FPP. camera looking down at Aubrey kneeling, Face covered in cum, mouth closed
                with flash

                pause 

                scene v10auh9 # FPP. Show Aubrey, inside bathroom, facing the door/camera, arms out towards camera as if pushing. Mouth open
                with dissolve

                au "Now get out of here while I clean up!"
                
                scene v10auh3a # TPP Same angle as v10auh3, in hallway outside of bathroom, show MC standing naked
                with fade
                
                u "(What the fuck!)"

                scene v10auh6  # FPP Show inside hallway of Chicks house
                with dissolve

                u "(Oh shit, ughhhh...)"
                $ renpy.end_replay()

                scene v10auh6a # FPP Same Camera as v10auh6, Show Nora, inside hallway of Chicks house, looking down toward MC's junk, Nora looks disgusted, Nora mouth closed
                with dissolve

                u "Nora, it's not what it-"

                scene v10auh6b # FPP Same angle and expression as v10auh6, Nora mouth open
                with dissolve

                no "What the fuck are you doing naked in our hallway!?"

                menu:
                    "Apologize":
                        scene v10auh6a
                        with dissolve

                        u "Look uhm, I'm so sorry."

                        scene v10auh6b
                        with dissolve

                        no "I don't even want to know, just put some clothes on."

                        scene v10auh6c # FPP Same angle as v10auh6, Nora walking away from MC
                        with dissolve

                        u "(Yup. Classic day in my life.) *Chuckles*"

                    "Make a joke":
                        $ reputation.add_point(RepComponent.TROUBLEMAKER)
                        scene v10auh6a
                        with dissolve

                        u "The real question is why are you still clothed?"

                        scene v10auh6d # FPP Same angle as v10auh6, Nora rolling her eyes and looking annoyed, mouth open
                        with dissolve
                  
                        no "You're not funny. Just... ugh."

                        scene v10auh6c
                        with dissolve

                        pause 0.5

                scene v10auh2d # Same angle as v10auh2, show Aubrey in new clothes, slight smile, mouth open
                with dissolve

                au "All cleaned up!!"

                scene v10auh2e # Same angle as v10auh2d, Aubrey mouth closed
                with dissolve

                u "*Laughs* You won't believe what just happened!"

                label v10s17_nsfwSkipLabel1:
                jump v10_aubrey_room

            else: # Not in a relationship with Aubrey
                scene v10auh2b
                with dissolve
                
                u "Can I come watch?"

                scene v10auh2f # FPP Same angle as v10auh2, no characters, show closed bathroom door
                with dissolve

                au "*Laughs* Maybe next time."

                au "I should really go shopping. I want some more cute gym sets."

                scene v10auh5j # FPP Show Aubrey inside Chicks bathroom, neck up only, big smile, mouth closed
                with dissolve

                u "Are you hinting at good gift ideas?"

                scene v10auh6
                with dissolve

                au "Who me? I would never. *Laughs*"

                scene v10auh5k # FPP Same angle as v10auh5j, Aubrey from neck up, slight smile, mouth open
                with dissolve

                u "Haha, what's your favorite brand?"

                scene v10auh6
                with dissolve

                au "I really love Lew's, they always fit me the best."

                scene v10auh5j
                with dissolve

                u "Isn't Lew's the expensive designer brand?"

                scene v10auh6
                with dissolve

                au "Hey you asked what I liked, not what I can afford."

                scene v10auh5j
                with dissolve

                u "*Laughs* True."

        "Say you'll wait":
            scene v10auh2b
            with dissolve

            u "Alright, I'll wait out here."

            if CharacterService.is_fwb(aubrey): # Aubrey relationship check
                scene v10auh2f
                with dissolve

                au "Surprised you're fine not watching, even though you know I'm completely naked behind this door. Someone's being a gentleman all of a sudden."

                scene v10auh5k
                with dissolve

                u "You gotta strike the right balance. Can't be a player 24/7."

                scene v10auh2f
                with dissolve

                au "*Laughs* Too bad, these poses sure would make for some nice views."

                scene v10auh5j
                with dissolve

                u "Now you're just teasing me."

                scene v10auh2f
                with dissolve

                au "Tease? I don't know what you're talking about."

                scene v10auh5j
                with dissolve

                u "Sure you don't."

            else: # Not in a relationship with Aubrey
                scene v10auh3b
                with dissolve

                au "I should really go shopping. I want some more cute gym sets."

                scene v10auh5j
                with dissolve

                u "Are you hinting at good gift ideas?"

                scene v10auh3b
                with dissolve

                au "Who me? I would never. *Laughs*"

                scene v10auh5k
                with dissolve

                u "Haha, what's your favorite brand?"

                scene v10auh2f
                with dissolve

                au "I really love Lew's, they always fit me the best."

                scene v10auh5j
                with dissolve

                u "Isn't Lew's the expensive designer brand?"

                scene v10auh2f
                with dissolve

                au "Hey you asked what I liked, not what I can afford."

                scene v10auh5j
                with dissolve

                u "*Laughs* True."

    scene v10auh2d
    with dissolve

    menu:
        "Compliment":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v10auh2e
            with dissolve

            u "Damn, are those Lew's right there."

            scene v10auh2g # FPP. Same angle as v10auh2d, Aubrey in new clothes, big smile and mouth open
            with dissolve

            au "*Laughs* They might be."

        "Complain":
            scene v10auh2e
            with dissolve

            u "Took you long enough."

            scene v10auh2g
            with dissolve

            au "Oh shush."

    scene v10auh2d
    with dissolve

    au "Let's go to my room."
    
    jump v10_aubrey_room

label v10_aubrey_room:
    scene v10auh7 # TPP Show Aubrey and MC, sitting on bed in Aubrey's room, both with small smiles and mouths closed
    with fade

    pause 0.75
    
    scene v10auh8 # FPP Show Aubrey sitting on her bed, slight smile, mouth closed
    with dissolve

    u "It's kinda unfair... you guys have a way nicer house than we do."

    scene v10auh8a # FPP Same angle as v10auh8, Aubrey with a big smile, mouth open
    with dissolve

    au "Maybe we just take better care of it. *Laughs*"

    scene v10auh8
    with dissolve

    u "Why'd you join the Chicks anyway?"

    scene v10auh8b # FPP Same angle and expression as v10auh8, Aubrey mouth open
    with dissolve

    au "*Smiles* My mom and my sister were both in the Chicks. So it's kind of a family tradition."

    scene v10auh8
    with dissolve

    u "That's pretty impressive, I didn't even know you guys were around that long. Since you're VP, I assume you quite enjoy being one?"

    scene v10auh8a
    with dissolve

    au "Absolutely! I love the girls... I've gotten to know them all pretty well. They really make me laugh sometimes."

    scene v10auh8c # FPP Same angle as v10auh8, Aubrey fake crying with her fists near her eyes
    with dissolve

    au "Hi I'm Chloe and I care too much about what people think so now I'm crying."

    scene v10auh8d # FPP Same angle as v10auh8, Aubrey with a very serious expression on her face, mouth open
    with dissolve

    au "Hi I'm Nora and I don't have time for any bullshit."
    
    scene v10auh8a
    with dissolve

    au "*Laughs* I'm sorry, I'm sorry. I love the girls, but they crack me up. They take things way too seriously."

    menu:
        "Defend them":
            scene v10auh8
            with dissolve

            u "Woah, chill. *Chuckles* Those are your friends."

            scene v10auh8b
            with dissolve

            au "Haha, okay okay. I'm just pulling their leg a bit."

        "Don't defend them":
            scene v10auh8
            with dissolve

            u "You really should do acting! *Laughs*"

            if "v10_aubrey" in sceneList:
                scene v10auh8e # Same angle as v10auh8, Aubrey with eyebrow raised, slight smile, mouth open
                with dissolve

                au "Told you."

            else:
                scene v10auh8a
                with dissolve

                au "Haha, yeah. Maybe."
    
    # Regardless of choices
    scene v10auh8a
    with dissolve

    u "*Chuckles* It's never boring when I spend time with you."

    scene v10auh8e
    with dissolve

    au "Gotta keep up my reputation. *Chuckles*"

    scene v10auh8
    with dissolve

    u "Haha true. Anyways I'm probably gonna head off now, I still got stuff to do, you know? *Laughs*"

    scene v10auh8a
    with dissolve

    au "*Smiles* Okay, see you soon."

    scene v10auh8
    with dissolve

    u "See ya."
    
    stop music fadeout 3

    jump v10_walk_jenny_text

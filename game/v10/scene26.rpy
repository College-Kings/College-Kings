# SCENE 26: Skatepark w/ Amber and Riley
# Locations: side walk walking home, Skatepark
# Characters: MC (Outfit 9), Amber (Outfit 1), Riley (Outfit 1)
# Time: Night

init python:
    def v10s26_reply1():
        setattr(store, "v10_amber_condoms", True)
        add_point(KCT.BOYFRIEND)
        amber.messenger.newMessage("Beer, obviously")


label v10_amber_skatepark:
    play music "music/v10/Track Scene 26_1.mp3" fadein 2

    scene v10sasp14 # TPP. Show MC on sidewalk, walking home from rileys house.
    with fade

    u "(I should get that.)"

    $ amber.messenger.newMessage("Skatepark behind SVC, 10pm, bring a six pack.", force_send=True)
    $ amber.messenger.addReply("Condoms or beer?", v10s26_reply1)
    $ amber.messenger.addReply("Alright sure")

    call screen phone

    scene v10sasp1 # FPP. Show Amber, smiling, mouth closed.
    with fade

    u "Chilling by yourself with a beer in the middle of the night at the skatepark... definitely sounds like you. *Laughs*"

    scene v10sasp1a # FPP. Same camera as v10sasp1. Show Amber, smiling, mouth open.
    with dissolve

    am "Well, if you weren't late, then maybe I wouldn't be by myself."

    scene v10sasp1
    with dissolve

    u "Okay yeah, my bad. *Chuckles* What made you wanna come here?"

    scene v10sasp1a
    with dissolve

    am "I've always liked the skatepark. Where else can you have a drink, see the funniest stuff and no squares ever ruin the mood?"

    scene v10sasp1
    with dissolve

    u "Maybe I should come here more often."

    scene v10sasp1a
    with dissolve

    am "I wouldn't be opposed to that. As long as you bring beer."

    scene v10sasp1b # FPP. Same camera as v10sasp1. Show Amber grabbing the beer that MC is handing her, smiling, mouth closed.
    with dissolve

    u "Of course, here you go."

    if v10_amber_condoms: # variable for MC replying beer or condoms earlier
        scene v10sasp1c # FPP. Same camera as v10sasp1. Show Amber with a beer, smiling, mouth open.
        with dissolve

        am "Did you bring the condoms as well? *Laughs*"

        scene v10sasp1d # FPP. Same camera as v10sasp1. Show Amber with a beer, smiling, mouth closed.
        with dissolve

        u "You said-"

        scene v10sasp1c
        with dissolve

        am "I'm just kidding. *Chuckles*"
            
        if amber.relationship >= Relationship.FWB:
            scene v10sasp1c
            with dissolve

            am "Maybe."

    scene v10sasp2 # TPP. Show MC and Amber looking at Riley as she walks out of the library. MC normal expression, mouth closed. Amber smiling, mouth open.
    with dissolve

    am "Isn't that your red haired girlfriend?"

    scene v10sasp1d
    with dissolve

    u "She's not my-"

    scene v10sasp2
    with dissolve

    am "Hey [name]'s friend!"

    scene v10sasp2a # TPP. Same camera as v10sasp2. Show Riley turn around and start to approach, a little confused but smiling, mouth open. Show MC, normal expression, mouth closed. Show Amber, smiling, mouth closed.
    with dissolve

    ri "Uhm hey..."

    scene v10sasp1e # FPP. Same camera as v10sasp1. Show Amber with a beer and show Riley. Amber looking towards Riley, smiling, mouth open. Riley looking towards Amber, smiling, mouth closed.
    with fade

    am "Hey! My name's Amber."

    scene v10sasp1f # FPP. Same camera as v10sasp1. Show Amber with a beer and show Riley. Amber looking towards Riley, smiling, mouth closed. Riley looking towards Amber, smiling, mouth open.
    with dissolve

    ri "Riley."

    scene v10sasp1g # FPP. Same camera as v10sasp1. Show Amber with a beer and show Riley. Amber and Riley looking at MC, smiling, mouths closed.
    with dissolve

    u "What were you doing in the library?"

    scene v10sasp1h # FPP. Same camera as v10sasp1. Show Amber with a beer and show Riley. Amber looking towards Riley, smiling, mouth closed. Riley looking towards MC, smiling, mouth open.
    with dissolve

    ri "I had to study, I have an assignment and it's honestly killing me. I still have so much more to look over, but I just couldn't focus any longer."

    scene v10sasp1e
    with dissolve

    am "Then hang with us, we can keep you busy."

    scene v10sasp1g
    with dissolve

    menu:
        "Yeah, you should":
            scene v10sasp1g
            with dissolve

            u "Yeah, you should join us."

            scene v10sasp1h
            with dissolve

            ri "Alright. I need a break anyway. Are we drinking?"
        
        "I'm sure she's busy":
            scene v10sasp1g
            with dissolve

            u "I'm sure she's gotta get back to studying soon. I wouldn't wanna distract her."

            scene v10sasp1h
            with dissolve

            ri "It's okay, I need a break anyway. Are we drinking?"

    scene v10sasp1e 
    with dissolve

    am "Most definitely. And we're not just drinking, we're playing a drinking game."

    scene v10sasp1g
    with dissolve

    u "We are?"

    scene v10sasp1i # FPP. Same camera as v10sasp1. Show Amber with a beer and show Riley. Both looking at MC, smiling, Amber mouth open.
    with dissolve

    am "Yep."

    scene v10sasp1f
    with dissolve

    ri "Sounds fun. What are we playing?"

    scene v10sasp1e 
    with dissolve

    am "Never have I ever."

    scene v10sasp1f
    with dissolve

    ri "Uhhh."

    scene v10sasp3 # TPP. Show MC, Amber and Riley. Amber bends over and grabs a beer.
    with dissolve

    pause 0.5

    scene v10sasp3a # TPP. Same camera as v10sasp3. Show MC, Amber and Riley. Show Amber handing a beer to Riley. Smiling, mouths closed.
    with dissolve

    pause 0.5

    scene v10sasp1j # FPP. Same camera as v10sasp1. Show Amber handing a beer to MC, smiling, mouth open. Show Riley watching, smiling, mouth closed.
    with dissolve

    am "Riley start us off. And before you do, since [name] is the only guy let's make him squirm a bit. *Chuckles*"

    scene v10sasp1k # FPP. Same camera as v10sasp1. Show Amber and Riley making mischievous faces at MC.
    with dissolve

    pause 0.5

    scene v10sasp4 # FPP. Show Amber and Riley with beers. Both smiling, Riley mouth open.
    with dissolve

    ri "Now that sounds like a great idea! Never have I ever had sex with a girl."

    scene v10sasp4a # FPP. Same camera as v10sasp4. Show Amber and Riley with beers. Both smiling, mouths closed.
    with dissolve

    u "Okay that's not fair."

    scene v10sasp5 # FPP. Show Amber taking a drink of beer.
    with dissolve

    u "You what? *Chuckles*"

    scene v10sasp5a # FPP. Same camera as v10sasp5. Show Amber, smiling, mouth open.
    with dissolve

    am "What? I like to experiment."

    scene v10sasp6 # FPP. Show Riley, smiling, mouth open.
    with dissolve

    ri "*Laughs*"

    scene v10sasp4a
    with dissolve

    u "*Laughs*"

    scene v10sasp4b # FPP. Same camera as v10sasp4. Show Amber and Riley with beers. Both smiling, Amber mouth open.
    with dissolve

    am "Alright, never have I ever... damn what have I not done? Never had I ever been caught naked in public."

    scene v10sasp4a
    with dissolve

    menu:
        "Drink":
            scene v10sasp7 # TPP. Show MC taking a drink of beer.
            with dissolve

            pause 0.5

            scene v10sasp4a
            with dissolve

            u "It's a long story, but I'd do it again."

            scene v10sasp4
            with dissolve

            ri "Sometime you're gonna have to tell me."

            scene v10sasp4b
            with dissolve

            am "Or show us, that works too. *Laughs*"
        
        "Pass":
            scene v10sasp6
            with dissolve

            ri "What? I definitely never did that."
 
    scene v10sasp4a 
    with dissolve

    u "*Laughs* Okay okay."

    scene v10sasp4a 
    with dissolve

    menu:
        "Stripped":
            scene v10sasp4a 
            with dissolve

            u "Never have I ever stripped."

            scene v10sasp4c # FPP. Same camera as v10sasp4. Show Amber and Riley both taking a drink of beer.
            with dissolve

            pause 0.5

            scene v10sasp1k
            with dissolve

            pause 0.5

            scene v10sasp1l # FPP. Same camera as v10sasp1. Show Amber and Riley looking at each other and making mischievous faces.
            with dissolve

            pause 0.5

            scene v10sasp3b # TPP. Same camera as v10sasp3. Show MC, Amber and Riley. Amber and Riley lean over and take off MC's shirt.
            with dissolve

            pause 0.75

            scene v10sasp4a
            with dissolve

            u "Nnnice."
        
        "Got caught masturbating":
            scene v10sasp4a
            with dissolve

            u "Never have I ever been caught masturbating."

            scene v10sasp4c
            with dissolve

            u "Wait Riley, you too?"

            scene v10sasp6
            with dissolve

            ri "It was a very awkward holiday with my mom!"

            scene v10sasp4
            with dissolve

            u "*Laughs*"

    scene v10sasp4d # FPP. Same camera as v10sasp4. Show Amber and Riley with beers. Both smiling, Riley mouth open.
    with dissolve

    ri "I could hang with you guys all night, but I do have to get back to studying eventually."

    scene v10sasp1e
    with dissolve

    am "Lame. *Laughs*"

    scene v10sasp4d
    with dissolve

    ri "Haha, it was nice meeting you Amber and good seeing you again [name]."

    scene v10sasp6a # FPP. Same camera as v10sasp6. Show Riley, smiling, leaning in and hugging MC.
    with dissolve

    pause 0.5

    scene v10sasp4e # FPP. Same camera as v10sasp4. Show Amber and Riley hugging.
    with dissolve

    u "See you."

    scene v10sasp4f # FPP. Same camera as v10sasp4. Show Riley leaving. Show Amber smiling, mouth open.
    with dissolve

    am "I like her and I see why you do too."

    scene v10sasp4g # FPP. Same camera as v10sasp4. Show Riley leaving. Show Amber smiling, mouth closed.
    with dissolve

    u "*Laughs*"

    if amber.relationship >= Relationship.FWB or kct == "popular":
        label v10_amber_skatepark_sg:
        
        if _in_replay:
            $ amber.relationship = Relationship.FWB

    if amber.relationship >= Relationship.FWB:
        scene v10sasp5b # FPP. Same camera as v10sasp5. Show Amber leaning in to whisper into MC's ear, smiling, mouth open.
        with fade

        am "*Whisper* You know, after getting tipsy and thinking of some of the things I've never done, but always wanted to do, I'm pretty horny right now. *Giggles*"

        scene v10sasp5c # FPP. Same camera as v10sasp5. Show Amber close to MC's face, biting her lip, mouth closed.
        with dissolve

        u "*Whisper* Really? Right now? *Chuckles*"

        scene v10sasp5b
        with dissolve

        am "*Whisper* Yeah, wanna do something about it?"

        scene v10sasp5c
        with dissolve

        u "*Whisper* Here?"

        scene v10sasp5d # FPP. Same camera as v10sasp5. Show Amber looking down and attempting to pull MC's pants down. Smiling, mouth open.
        with dissolve

        am "Why not?"

        scene v10sasp5d # FPP. Same camera as v10sasp5. Show Amber looking down and attempting to pull MC's pants down. Smiling, mouth closed.
        with dissolve
        menu:
            "Let her":
                $ sceneList.add("v10_amber")
                show screen v10s26_amberSexOverlay

                if config_censored:
                    call screen censored_popup("v10s26_nsfwSkipLabel1")

                stop music fadeout 3
                play music "music/v10/Track Scene 26_2.mp3" fadein 2
                image v10ambbj = Movie(play="images/v10/Scene 26/v10ambbj.webm", loop=True, image="images/v10/Scene 26/v10ambbjStart.webp", start_image="images/v10/Scene 26/v10ambbjStart.webp") # TPP Amber sucking MC's cock on the top of the quater pipe
                image v10ambbjf = Movie(play="images/v10/Scene 26/v10ambbjf.webm", loop=True, image="images/v10/Scene 26/v10ambbjStart.webp", start_image="images/v10/Scene 26/v10ambbjStart.webp")

                label v10s26_amberBlowjob:                
                    scene v10ambbj # ignore
                    with dissolve

                    $ grant_achievement("rough_rider")
                    u "Damn Amber!"

                    scene v10ambbj
                    with dissolve

                    u "Holy fuck!"

                    scene v10ambbjf
                    with dissolve

                    u "I didn't know you... oh shit!"

                    scene v10ambbjf
                    with dissolve
                    pause

                scene v10sasp8 # FPP. Same camera as v10sasp8. Show Amber smiling and removing her clothes.
                with dissolve

                pause 0.75

                scene v10sasp8a # FPP. Same camera as v10sasp8. Show Amber inches from MC, naked, smiling and mouth open.
                with dissolve

                am "Fuck me."

                image v10ambrf = Movie(play="images/v10/Scene 26/v10ambrf.webm", loop=True, image="images/v10/Scene 26/v10ambrfStart.webp", start_image="images/v10/Scene 26/v10ambrfStart.webp") # TPP laying behind amber fucking her from behind.
                image v10ambrff = Movie(play="images/v10/Scene 26/v10ambrff.webm", loop=True, image="images/v10/Scene 26/v10ambrfStart.webp", start_image="images/v10/Scene 26/v10ambrfStart.webp")

                label v10s26_amberLying:
                    scene v10ambrf
                    with dissolve

                    am "Oh I needed this!"

                    scene v10ambrff
                    with dissolve

                    am "Fuck me harder [name]!"

                    scene v10ambrff
                    with dissolve

                    am "Oh god!"

                image v10ambda = Movie(play="images/v10/Scene 26/v10ambda.webm", loop=True, image="images/v10/Scene 26/v10ambdaStart.webp", start_image="images/v10/Scene 26/v10ambdaStart.webp") # TPP MC fucking amber in the ass doggystyle
                image v10ambdaf = Movie(play="images/v10/Scene 26/v10ambdaf.webm", loop=True, image="images/v10/Scene 26/v10ambdaStart.webp", start_image="images/v10/Scene 26/v10ambdaStart.webp")

                label v10s26_amberDoggy:
                    scene v10ambda
                    with dissolve

                    am "Oh my God, FASTER!"

                    am "YESSSS!"

                    scene v10ambdaf
                    with dissolve

                    u "Damn this feels good!"

                    am "Oh fuck!"

                image v10ambcg = Movie(play="images/v10/Scene 26/v10ambcg.webm", loop=True, image="images/v10/Scene 26/v10ambcgStart.webp", start_image="images/v10/Scene 26/v10ambcgStart.webp") # TPP MC fucking amber in the ass doggystyle
                image v10ambcgf = Movie(play="images/v10/Scene 26/v10ambcgf.webm", loop=True, image="images/v10/Scene 26/v10ambcgStart.webp", start_image="images/v10/Scene 26/v10ambcgStart.webp")

                label v10s26_amberCowgirl:
                    scene v10ambcg
                    with dissolve

                    am "I could get used to this!"

                    scene v10ambcg
                    with dissolve

                    u "Damn you know what you're doing!"

                    scene v10ambcgf
                    with dissolve

                    am "Oh shit I'm gonna cum!"

                    scene v10ambcgf
                    with dissolve

                    u "Me too."

                    scene v10ambcgf
                    with flash

                    am "Cum in me [name]."

                hide screen v10s26_amberSexOverlay

                scene v10sasp12 # FPP. Show Amber nude, smiling, mouth open.
                with dissolve

                am "That was exciting!"

                scene v10sasp12a # FPP. Same camera as v10sasp12. Show Amber nude, smiling, mouth closed.
                with dissolve

                u "I'm glad you hit me up."

                scene v10sasp12
                with dissolve

                am "Me too."

                scene v10sasp12b # FPP. Same camera as v10sasp12. Show Amber nude, starting to get dressed, smiling, mouth closed.
                with dissolve

                pause 0.75

                scene v10sasp7a # TPP. Same camera as v10sasp7. Show MC nude, starting to get dressed.
                with dissolve

                pause 0.75

                scene v10sasp5a
                with fade

                am "I don't wanna make you feel like a booty call, but I'm pretty tired after that."

                scene v10sasp5f # FPP. Same camera as v10sasp5. Show Amber, smiling, mouth closed.
                with dissolve

                u "Haha, don't worry, me too. Maybe we should call it a night."

                scene v10sasp5a
                with dissolve

                am "Yeah, I'll see you soon."

                scene v10sasp5f
                with dissolve

                u "*Chuckles* Bye."

                scene v10sasp5g # FPP. Same camera as v10sasp5. Show Amber leaving.
                with dissolve

                u "(Damn, that really just happened. That was crazy.)"
           
            "Shut her down":
                $ v10_amber_awkward = True
                scene v10sasp5d
                with dissolve

                u "Woah, let's not do that."

                scene v10sasp5h # FPP. Same camera as v10sasp5. Show Amber with an annoyed expression, mouth open.
                with dissolve

                am "Ugh fine, guess I'll just go home."
                
                scene v10sasp5i # FPP. Same camera as v10sasp5. Show Amber with an annoyed expression, mouth closed.
                with dissolve
                menu:
                    "Okay":
                        scene v10sasp5i
                        with dissolve

                        u "Alright, sorry... it was a nice night though."

                        scene v10sasp5h
                        with dissolve

                        am "Yeah, whatever."
                   
                    "Your place?":
                        scene v10sasp5i
                        with dissolve

                        u "I could come with you and maybe we could continue this there."

                        scene v10sasp5h
                        with dissolve

                        am "Nah, you kinda killed the mood."

                        scene v10sasp5h
                        with dissolve

                        u "Right, sorry."

        scene v10sasp5g 
        with dissolve

        pause 0.5

    else:   
        scene v10sasp5a
        with fade

        am "You skate?"

        scene v10sasp5f 
        with dissolve
        menu:
            "Yes":
                $ skater = True
                scene v10sasp5f 
                with dissolve

                u "Yeah, I love all wheels."

                scene v10sasp5a
                with dissolve

                am "I've always liked guys that skate."

                scene v10sasp5f
                with dissolve

                u "Good to know."
           
            "No":
                scene v10sasp5f
                with dissolve

                u "No, I'm not really into wheels."

                scene v10sasp5a
                with dissolve

                am "Really? I've always liked guys that skate."

                scene v10sasp5f
                with dissolve

                u "I'll keep that in mind."

        scene v10sasp5a
        with dissolve

        am "If I ever settled for a dude he'd be a skater."

        scene v10sasp5f
        with dissolve
        menu:
            "Place hand on her leg":
                if kct == "popular": # kct is popular
                    call screen kct_popup
                    
                    scene v10sasp5j # FPP. Same camera as v10sasp5. Show Amber glancing down at her leg, smiling, mouth closed.
                    with dissolve
                    
                    pause 0.75

                    if not skater:
                        scene v10sasp5j
                        with dissolve
                        
                        u "Maybe I could learn it."

                        scene v10sasp5a
                        with dissolve

                        am "I think that'd be good."

                    else: # mc does skate
                        scene v10sasp5j
                        with dissolve

                        u "Sounds like I'm your type."

                        scene v10sasp5a
                        with dissolve

                        am "It does, doesn't it?"

                    scene v10sasp5b
                    with dissolve

                    am "*Whisper* You know, I'm pretty horny right now. *Giggles*"

                    scene v10sasp5c
                    with dissolve

                    u "*Whisper* Really? Right now? *Chuckles*"

                    scene v10sasp5b
                    with dissolve

                    am "*Whisper* Yeah, wanna do something about it?"

                    scene v10sasp5c
                    with dissolve

                    u "*Whisper* Here?"

                    scene v10sasp5d
                    with dissolve

                    am "Why not?"

                    scene v10sasp5d
                    with dissolve
                    menu:
                        "Let her":
                            $ amber.relationship = Relationship.FWB
                            $ sceneList.add("v10_amber")

                            if config_censored:
                                call screen censored_popup("v10s26_nsfwSkipLabel1")
                                
                            scene v10ambbj
                            with dissolve

                            $ grant_achievement("rough_rider")

                            u "Damn Amber!"

                            scene v10ambbj
                            with dissolve

                            u "Holy fuck!"

                            scene v10ambbjf
                            with dissolve

                            u "I didn't know you... oh shit!"

                            scene v10ambbjf
                            with dissolve
                            pause

                            scene v10sasp8
                            with dissolve

                            pause 0.75

                            scene v10sasp8a
                            with dissolve

                            am "Fuck me."

                            scene v10ambrf
                            with dissolve

                            am "Oh I needed this!"

                            scene v10ambrff
                            with dissolve

                            am "Fuck me harder [name]!"

                            scene v10ambrff
                            with dissolve

                            am "Oh god!"

                            scene v10ambda
                            with dissolve

                            am "Oh my God, FASTER!"

                            scene v10ambdaf
                            with dissolve

                            am "YESSSS!"

                            scene v10ambdaf
                            with dissolve

                            u "Damn this feels good!"

                            scene v10ambdaf
                            with dissolve

                            am "Oh fuck!"

                            scene v10ambcg
                            with dissolve

                            am "I could get used to this!"

                            scene v10ambcg
                            with dissolve

                            u "Damn you know what you're doing!"

                            scene v10ambcgf
                            with dissolve

                            am "Oh shit I'm gonna cum!"

                            scene v10ambcgf
                            with dissolve

                            u "Me too."

                            scene v10ambcgf
                            with flash

                            am "Cum in me [name]."

                            scene v10sasp12
                            with dissolve

                            am "That was exciting!"

                            scene v10sasp12a
                            with dissolve

                            u "I'm glad you hit me up."

                            scene v10sasp12
                            with dissolve

                            am "Me too."

                            scene v10sasp12b
                            with dissolve

                            pause 0.75

                            scene v10sasp7a
                            with dissolve

                            pause 0.75

                            scene v10sasp5a
                            with fade

                            am "I don't wanna make you feel like a booty call, but I'm pretty tired after that."

                            scene v10sasp5f
                            with dissolve

                            u "Haha, don't worry, me too. Maybe we should call it a night."

                            scene v10sasp5a
                            with dissolve

                            am "Yeah, I'll see you soon."

                            scene v10sasp5f
                            with dissolve

                            u "*Chuckles* Bye."

                            scene v10sasp5g
                            with dissolve

                            u "(Damn, that really just happened. That was crazy.)"

                        "Shut her down":
                            $ v10_amber_awkward = True
                            scene v10sasp5d
                            with dissolve

                            u "Woah, let's not do that."

                            scene v10sasp5h
                            with dissolve

                            am "Ugh fine, guess I'll just go home."

                            scene v10sasp5i
                            with dissolve

                            menu:
                                "Okay":
                                    scene v10sasp5i
                                    with dissolve

                                    u "Alright, sorry... it was a nice night though."

                                    scene v10sasp5h
                                    with dissolve

                                    am "Yeah, whatever."
                                
                                "Your place?":
                                    scene v10sasp5i
                                    with dissolve

                                    u "I could come with you and maybe we could continue this there."

                                    scene v10sasp5h
                                    with dissolve

                                    am "Nah, you kinda killed the mood."

                                    scene v10sasp5i
                                    with dissolve

                                    u "Right, sorry."

                    scene v10sasp5g
                    with dissolve

                    pause 0.5

                else:
                    scene v10sasp5k # FPP. Same camera as v10sasp5. Show Amber glancing down at her leg, curious expression, mouth closed.
                    with dissolve

                    pause 0.75
                    
                    scene v10sasp5a
                    with dissolve

                    am "Haha, I think you got the wrong impression."

                    scene v10sasp5f
                    with dissolve

                    u "Oh, uhm sorry."

                    scene v10sasp5a
                    with dissolve

                    am "It's alright."

                    scene v10sasp5f
                    with dissolve

                    u "So..."

                    scene v10sasp5a
                    with dissolve

                    am "On that awkward note let's call it a night. *Chuckles*"

                    scene v10sasp5f
                    with dissolve

                    u "Yeah, it is getting late."

                    scene v10sasp5a
                    with dissolve

                    am "See you."

                    scene v10sasp5g
                    with dissolve

                    pause 0.75
            
            "Make a joke":
                scene v10sasp5f
                with dissolve

                u "Then just call me Tony. *Laughs*"

                scene v10sasp5a
                with dissolve

                am "*Chuckles* Looks like we're out of beer, Tony."

                scene v10sasp5f
                with dissolve

                u "You drank half of it in our little game. *Laughs*"

                scene v10sasp5a
                with dissolve

                am "True. Guess that ends our night. No buzz no fun."

                scene v10sasp5f
                with dissolve

                u "Haha, yeah it is getting late."

                scene v10sasp5a
                with dissolve

                am "I'll see you around."

                label v10s26_nsfwSkipLabel1:
                    scene v10sasp5f
                    with dissolve

                    u "See ya."

                    scene v10sasp5g
                    with dissolve

                    pause 0.75

    $ renpy.end_replay()
    scene v10sasp5g
    with dissolve

    u "(Okay for real this time, I'm going home.)"

    scene v10sasp13 # TPP. Show MC in his dark room, laying in bed, getting ready to sleep.
    with fade

    u "(I'm fucking beat.)"
    
    stop music fadeout 3

    jump v10_econ_class # -Transition to Scene 27-
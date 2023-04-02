# SCENE 9: APES - Manhunt
# Locations: forest (same one we used for meeting grayson in the forest)
# Characters: MC (outfit 9), Grayson(outfit 1), caleb(outfit 1), ryan(outfit 1), Rancher(Ask lew for model and outfit)
# Time: friday evening

label v11_apes_manhunt:
    scene v11amh1 # TPP. Show MC walking in through the Apes house door, he has a neutral expression, mouth closed
    with fade
    play music "music/v11/Track Scene 9_1.mp3" fadein 2
    pause 1

    scene v11amh2 # FPP. MC is in the living room, Cameron and Grayson are sitting on the couch, looking at MC, both of them smiling, mouths closed (Ryan and Caleb are standing nearby, out of shot)
    with dissolve

    pause 0.75

    scene v11amh3 # FPP. Same character positioning as v11amh2, show Cameron looking at MC, mouth open, smiling (only Cameron in shot)
    with dissolve
        
    ca "And he's finally here."

    scene v11amh3a # FPP. Same as v11amh3, Cameron mouth closed, smiling
    with dissolve

    u "What is this?"

    scene v11amh4 # FPP. Same character positioning as v11amh2, show Ryan looking at MC, mouth open, neutral expression (only Ryan in shot)
    with dissolve

    ry "They won't tell us, they just keep sitting there smiling like that."

    scene v11amh3a
    with dissolve

    u "For real, what's going on?"

    scene v11amh5 # FPP. Same character positioning as v11amh2, show Grayson, looking at MC, mouth open, smiling (only Grayson in shot)
    with dissolve

    gr "Let's go to the woods, boys."

    scene v11amh6 # FPP. Same character positioning as v11amh2, MC is looking at Caleb, Caleb looking at Grayson, Caleb mouth open, confused expression (only Caleb is in shot)
    with dissolve

    cal "What?"

    # -Fades to Grayson, Cameron, MC, Ryan and Caleb in the forest-

    scene v11amh7 # FPP. MC, Ryan, Caleb, Grayson and Cameron are in the forest, show MC looking at Grayson, Grayson's mouth closed, grinning (Only Grayson in shot, MC, Ryan and Caleb next to each other, Cameron next to Grayson, Cameron and Grayson are across from MC, Ryan and Caleb)
    with fade
    play music "music/v11/Track Scene 9_2.mp3" fadein 2
    u "Okay, what are we doing out here?"

    scene v11amh8 # FPP. Same character positioning as v11amh7, MC is now looking at Ryan, Ryan looking at Grayson, Ryan mouth open, worried expression (Only Ryan in shot)
    with dissolve

    ry "I think I know, and if I'm right we're not gonna like it."

    scene v11amh7a # FPP. Same as v11amh7, MC is looking at Grayson, Grayson looking at Ryan, Grayson slightly angry, mouth open
    with dissolve

    gr "What do you mean you're not gonna like it? You're not a fan of tradition?"

    scene v11amh8
    with dissolve

    ry "I'm not a fan of getting body slammed."

    scene v11amh9 # FPP. Same character positioning as v11amh7, MC is looking at Caleb, Caleb looking at Grayson, Caleb confused, mouth open (Only Caleb in shot)
    with dissolve

    cal "I still don't know what's going on."

    scene v11amh7b # FPP. Same as v11amh7, Grayson mouth open, grinning, looking at Caleb's direction
    with dissolve

    gr "I'll tell you what's going on. Every year the newbies get taken here and we play manhunt."

    scene v11amh9
    with dissolve

    cal "What's manhunt?"

    scene v11amh9a # FPP. Same as v11amh9, Cameron is now infront of Caleb, both mouths closed, Cameron angry, Caleb a bit scared
    with dissolve

    pause 0.5

    scene v11amh9b # FPP. Same as v11amh9a, now Cameron is raising Caleb by his waist, Caleb has a scared expression, Cameron is angry, both mouths closed
    with dissolve

    pause 0.5

    play sound "sounds/fall.mp3"

    scene v11amh9c # FPP. Same as v11amh9a, now Cameron is throwing Caleb to the ground (Caleb is on the ground at this point), Cameron is angry, Caleb is startled, both mouths closed
    with dissolve

    pause 0.5

    scene v11amh9d # FPP. Same as v11amh9, Cameron is now looking at Caleb on the ground, Cameron's mouth is open, he is angry, Caleb is scared, mouth closed
    with dissolve

    ca "That's manhunt, now stop asking so many damn questions and let him finish explaining."

    #scene v11amh9a
    #with dissolve

    u "(Oh shit!)"

    scene v11amh7c # FPP. Same as v11amh7, Grayson mouth open, grinning
    with dissolve

    gr "You will run, you will hide. If either of us catch you, we will body slam the fuck out of you. The last person standing is the winner."

    scene v11amh10 # FPP. Same character positioning as v11amh7, MC and Cameron looking at each other, Cameron mouth open, slight smile (Only Cameron in shot)
    with dissolve

    ca "And you definitely want to be the last person. There's a wonderful surprise for the losers."

    scene v11amh9
    with dissolve

    cal "What's that?"

    scene v11amh9a 
    with dissolve

    pause 0.5

    scene v11amh9b 
    with dissolve

    pause 0.5

    play sound "sounds/fall.mp3"

    scene v11amh9c 
    with dissolve

    pause 0.5

    scene v11amh9d 
    with dissolve

    ca "STOP. ASKING. QUESTIONS."

    scene v11amh9e # FPP. Same as v11amh9, Caleb is holding his ribs, he is in pain, mouth open (Only Caleb in shot)
    with dissolve

    cal "Oh fuck man, I think you broke something."

    scene v11amh7c
    with dissolve

    gr "This is gonna be fun. Are you guys ready?"

    scene v11amh8a # FPP. Same as v11amh8, Ryan still looking at Grayson, Ryan smiling, mouth open (Only Ryan in shot)
    with dissolve

    ry "Fuck yeah!"

    scene v11amh7
    with dissolve

    menu:
        "Ready":
            $ reputation.add_point(RepComponent.BRO)

            scene v11amh7
            with dissolve

            u "Yeah man, I'm ready!"

        "One last question":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene v11amh7
            with dissolve

            u "Actually, I have a question."

            scene v11amh10a # FPP. Same as v11amh10, Cameron is running at MC, mouth closed, angry
            with dissolve

            pause 0.5

            play sound "sounds/fall.mp3"
            scene v11amh11 # FPP. MC is lying on the ground looking up at Cameron, Cameron looking down at MC, Cameron is angry, mouth open
            with vpunch

            ca "Are you guys deaf? I said no questions!"

    scene v11amh7c
    with dissolve

    gr "READY... SET... GO!"

    scene v11amh12 # TPP. Show MC and Ryan running away, they're next to each other, Caleb is behind them, all of them have scared expressions, mouths closed
    with dissolve

    pause 0.75

    scene v11amh12a # TPP. Same as v11amh12, but they are closer to the camera, Caleb is slipping (mid fall), he has a very startled expression, MC and Ryan continue running
    with dissolve

    pause 0.5

    scene v11amh12b # TPP. Same as v11amh12, MC and Ryan out of shot now, Caleb is now standing up and running, he has a scared expression, mouth closed
    with dissolve

    pause 0.5

    scene v11amh13 # FPP. MC is looking at a bifurcation (left and right) in the forest, no one is in shot
    with dissolve

    u "(Where the fuck should I go?)"

    scene v11amh13
    with dissolve

    menu:
        "Left":
            scene v11amh14 # FPP. MC starts running to the left bifurcation
            with dissolve

            u "(Seems better this way.)"

        "Right":
            scene v11amh15 # FPP. MC starts running to the right bifurcation
            with dissolve

            u "(Seems better this way.)"

    scene v11amh16 # FPP. MC looks back and see Ryan running behind him, Ryan is focused, mouth closed
    with dissolve

    u "Why are you following me?"

    scene v11amh16a # FPP. Same as v11amh16, Ryan mouth open, focused (change the background forest to simulate them running)
    with dissolve

    ry "You look like you know where you're going."

    scene v11amh16b # FPP. Same as v11amh16, Ryan focused, mouth closed (change the background again to simulate them running)
    with dissolve

    u "My guess is as good as yours, I've never been in the fucking forest."

    scene v11amh16b
    with dissolve

    menu:
        "Hide":
            $ v11_manhunt_winner = "Caleb"

            scene v11amh17 # FPP. MC and Ryan stop running, they're looking at each other, Ryan has a neutral expression, mouth closed
            with dissolve

            u "I'm stopping here, I'm tired of running."

            scene v11amh17a # FPP. Same as v11amh17, Ryan mouth open, neutral expression
            with dissolve

            ry "What? We just started! They're gonna catch you, bro."

            scene v11amh17b # FPP. Same cam as v11amh17, Ryan is running away, MC looking at him run
            with dissolve

            pause 0.75

            scene v11amh17c # FPP. Same cam as v11amh17, just the background, no one in shot
            with dissolve

            u "(I don't even hear anyone.)"

            scene v11amh18 # FPP. MC is sitting down, hiding, MC looking at backrground
            with dissolve

            cal "Ahh shit! My back!"

            scene v11amh19 # FPP. Caleb is now sitting next to MC in the hiding spot, they're looking at each other, Caleb mouth closed, neutral expression
            with dissolve

            u "Fuck, you scared me! Did they catch you?"

            scene v11amh19a # FPP. Same as v11amh19, Caleb mouth open, neutral expression
            with dissolve

            cal "Sure did, that's why my back hurts."

            scene v11amh19
            with dissolve

            u "Why are you here then instead of with them and why were you running?"

            scene v11amh19a
            with dissolve

            cal "I came to warn you. Grayson and Cameron are moving together, they heard Ryan and started chasing after him, so you should be safe if you stay right here."

            cal "Just wait for Ryan to scream and you'll know it's game over."

            scene v11amh19
            with dissolve

            u "Thanks man."

            scene v11amh20 # FPP. MC and Caleb looking at each other, Caleb is standing up now, Caleb mouth closed, neutral expression
            with dissolve

            u "Where are you going?"

            scene v11amh20a # FPP. Same as v11amh20, Caleb mouth open, neutral expression
            with dissolve

            cal "Cameron keeps body slamming me even though I already lost so I'm trying to keep away from him."

            scene v11amh20
            with dissolve

            u "Haha, sounds like him."

            scene v11amh20a
            with dissolve

            cal "See ya, good luck man."

            scene v11amh20b # FPP. Caleb is running away, MC looking at him
            with dissolve

            u "*Mocking* Don't ask any questions! Haha, Cameron's such a hardass."

            scene v11amh21 # FPP. MC sees Cameron and Grayson coming out of the bushes
            with dissolve

            pause 0.75

            scene v11amh22 # FPP. Cameron looking at MC, MC now standing up, Cameron mouth open, slight smile
            with dissolve

            ca "What'd you just call me pledge?"

            scene v11amh22a # FPP. Same cam as v11amh22, Cameron mouth closed, slight smile
            with dissolve

            u "I... I-"

            scene v11amh23 # TPP. Show Grayson grabbing MC to bodyslam him (MC is startled, Grayson is smiling, mouths closed)
            with dissolve

            pause 0.75

            play sound "sounds/fall.mp3"
            scene v11amh23a # TPP. Same cam as v11amh23, Show Grayson slamming MC to the ground, MC is startled, Grayson is laughing
            with vpunch

            pause 0.75

            scene v11amh24 # FPP. MC is lying down on floor, looking at Grayson, Grayson smiling, mouth open
            with dissolve

            gr "I'm sure he'll be talking to you real nice now, Cameron. *Chuckles*"

            scene v11amh24a # FPP. Same cam as v11amh24, Grayson smiling, mouth closed
            with dissolve

            u "Ahh fuck man!"

            scene v11amh24
            with dissolve

            gr "Chill out, it didn't hurt that bad. Let's head over to the horse, time for the winner to pick the worst loser."

            scene v11amh25 # FPP. MC is now standing up, looking at Grayson, Grayson mouth closed, smiling
            with dissolve

            u "Damn, I already know Ryan's gonna pick me."

            scene v11amh25a # FPP. Same cam as v11amh25a, Grayson mouth open, smiling
            with dissolve

            gr "How can Ryan pick someone if he got out too?"

            scene v11amh25
            with dissolve

            u "Caleb just spoke to me and said you guys got him and that I should... OH."

            scene v11amh25a
            with dissolve

            gr "*Laughs* Caleb played your ass."

            scene v11amh25
            with dissolve

            u "Yeah, I see that now."

            scene v11amh25a
            with dissolve

            gr "Let's go to the horse."

            scene v11amh26 # FPP. MC is looking at Caleb, who is standing next to the horse, Caleb mouth closed, smiling
            with fade

            u "Just so we're all clear, fuck you Caleb."

            scene v11amh27 # FPP. Ryan is standing a bit further away from the horse, looking at MC, mouth open, annoyed expression
            with dissolve

            ry "Wait, he pulled that \"stay right here trick on you too\"?"

            scene v11amh26a # FPP. Same cam as v11amh26, Caleb mouth open, smiling
            with dissolve

            cal "Look, I got slammed a thousand times before we even started, I wasn't gonna get slammed again."

        "Keep running":
            scene v11amh16b
            with dissolve

            u "(They're probably still too close for me to stop and hide.)"

            scene v11amh16
            with dissolve

            pause 0.75

            scene v11amh16b
            with dissolve

            pause 0.75

            scene v11amh16
            with dissolve

            menu:
                "Hide":
                    scene v11amh28 # FPP. MC is looking at the nature
                    with dissolve

                    u "(Okay, time to find a nice hiding spot.)"

                    scene v11amh29 # FPP. MC is looking at his hiding spot (should be a place next to a bush where Cameron will hide in later on)
                    with dissolve

                    u "(Perfect spot!)"

                    scene v11amh30 # FPP. MC is sitting in his hiding spot, Ryan is standing in front of him, mouth closed, slightly annoyed
                    with dissolve

                    pause 0.75
                    
                    scene v11amh31 # FPP. Ryan is now sitting next to and looking at MC, Ryan mouth closed, slightly annoyed (The bush should be behind Ryan)
                    with dissolve

                    u "Bro, find your own spot."

                    scene v11amh31a # FPP. Same as v11amh31, Ryan mouth open, slightly annoyed
                    with dissolve

                    ry "A good spot is a good spot, I'm not leaving."

                    scene v11amh31
                    with dissolve

                    menu:
                        "Stay":
                            scene v11amh31
                            with dissolve

                            u "What? They'll just catch both of us. Don't be a dick bro, find your own spot."

                            scene v11amh31a
                            with dissolve

                            ry "Nah, I'm good right here."

                            if not v10s33_ryan_flirt_emily:

                                scene v11amh31
                                with dissolve

                                u "I swear, you're always going after something I got."

                                scene v11amh31a
                                with dissolve

                                ry "What's that supposed to mean?"

                                scene v11amh31
                                with dissolve

                                u "You know exactly what I mean."

                                scene v11amh31a
                                with dissolve

                                ry "So you know I've been texting Emily?"

                                scene v11amh31
                                with dissolve

                                u "I do now."

                                scene v11amh31a
                                with dissolve

                                ry "Why do you care anyway? It's not like you guys are dating."

                                scene v11amh31
                                with dissolve

                                u "Who said I did care?"

                                scene v11amh31a
                                with dissolve

                                ry "You brought it up so you must."

                                scene v11amh31
                                with dissolve

                                u "No, I brought up the fact that you're following me around like a fucking puppy."

                                scene v11amh31a
                                with dissolve

                                ry "You don't own this spot."
                            
                            scene v11amh31b # FPP. Same as v11amh31, Ryan mouth closed, slightly annoyed, Cameron can be seen hiding in the bush, Cameron slight smile, mouth closed
                            with dissolve

                            menu:
                                "Run":
                                    $ v11_manhunt_winner = "Caleb"
                                    $ reputation.add_point(RepComponent.TROUBLEMAKER)

                                    scene v11amh31b 
                                    with dissolve

                                    u "Enjoy the spot!"

                                    scene v11amh32 # FPP. MC is now standing, a bit far away from the hiding spot, looking at Ryan, Cameron has Ryan grabbed by the waist
                                    with dissolve

                                    pause 0.75

                                    play sound "sounds/fall.mp3"
                                    scene v11amh32a # FPP. Same cam as v11amh32, but Ryan is now on the ground, Cameron is looking down on him, Cameron is laughing
                                    with dissolve

                                    u "Guess it wasn't a good spot."

                                    scene v11amh33 # FPP. MC is looking straight at Grayson (who was behind MC in v11amh32), Grayson is smiling, mouth open
                                    with dissolve

                                    pause 1

                                    scene v11amh23
                                    with dissolve

                                    pause 0.5

                                    play sound "sounds/fall.mp3"
                                    scene v11amh23a
                                    with vpunch

                                    pause 1

                                    scene v11amh24
                                    with dissolve

                                    gr "No, it really wasn't."

                                    scene v11amh34 # FPP. MC is standing up, looking at Cameron, Cameron is smiling, mouth open
                                    with dissolve

                                    ca "Time for the horse."

                                "Warn him":
                                    $ v11_manhunt_winner = "Caleb"
                                    $ reputation.add_point(RepComponent.BRO)

                                    scene v11amh31b
                                    with dissolve

                                    u "Bro, Cameron's behind you."

                                    scene v11amh31c # FPP. Same as v11amh31b, Ryan mouth open, slightly annoyed, Cameron still in bushes
                                    with dissolve

                                    ry "Not falling for your shit today."

                                    scene v11amh32
                                    with dissolve

                                    pause 0.75

                                    play sound "sounds/fall.mp3"
                                    scene v11amh32a
                                    with dissolve

                                    pause 0.75

                                    scene v11amh33a # FPP. Same as v11amh33, Grayson smiling, mouth closed
                                    with dissolve

                                    u "Oh fuck!"

                                    scene v11amh33
                                    with dissolve

                                    gr "Don't worry, I just slammed Caleb."

                                    scene v11amh33a
                                    with dissolve

                                    u "So I won?"

                                    scene v11amh33
                                    with dissolve

                                    gr "Sike."

                                    scene v11amh23
                                    with dissolve

                                    pause 0.5

                                    play sound "sounds/fall.mp3"
                                    scene v11amh23a
                                    with vpunch

                                    pause 0.5

                                    scene v11amh35 # FPP. MC is standing up, looking at Ryan, Ryan has his hand on his ribs, he is in pain, mouth open
                                    with dissolve

                                    ry "That shit hurt, I should've believed you, [name]."

                                    scene v11amh35a # FPP. Same as v11amh35a, Ryan has hand on ribs, he is in pain, mouth closed
                                    with dissolve

                                    u "Please don't talk right now."

                                    scene v11amh34 # FPP. MC is standing up, looking at Cameron, Cameron is smiling, mouth open
                                    with dissolve

                                    ca "Alright, horse time."

                        "Leave":
                            $ v11_manhunt_winner = "Ryan"

                            scene v11amh31
                            with dissolve

                            u "Fuck you, bro."

                            scene v11amh36 # FPP. MC sees the rancher holding the horse in the distance 
                            with dissolve

                            pause 0.75

                            scene v11amh37 # FPP. MC is now in talking distance with the Rancher, Rancher looking at MC, neutral expression, mouth open
                            with dissolve

                            ran "You must be Grayson, here's the Bronco for the manhunt. Have him back by morning."

                            scene v11amh37a # FPP. Same cam as v11amh37, the rancher is walking away
                            with dissolve

                            u "(What the fuck was that?)"

                            scene v11amh37b # FPP. MC is looking at the horse
                            with dissolve

                            u "You must be a present for the losers. Maybe if I stay by you I'll be good."

                            scene v11amh38 # FPP. MC can see Cameron running after Ryan in the distance, Ryan mouth open, scared expression, Cameron smiling, mouth closed
                            with dissolve

                            ry "Look man, you don't have to slam me!"

                            scene v11amh38a # FPP. Same cam as v11amh38, Ryan is now a further ahead, Ryan mouth closed, scared, Cameron slightly behind Ryan, smiling, mouth open
                            with dissolve

                            ca "GET OVER HERE!"

                            scene v11amh38b # FPP. Same cam as v11amh38, Ryan is now even further ahead, scared, mouth open, Cameron now a bit further behind Ryan, smiling, mouth closed
                            with dissolve

                            ry "AHHHHHHH!"

                            scene v11amh38c # FPP. Same cam as v11amh38, no one in shot anymore, MC just looking at the background 
                            with dissolve

                            u "I feel like he deserved that!"

                            scene v11amh38c
                            with fade

                            u "It's been 20 minutes, and I'm starting to get hungry. I'm so hungry I could eat a horse."

                            scene v11amh37b
                            with dissolve

                            u "You know what I mean."

                            scene v11amh39 # FPP. MC can see Grayson and Cameron running after Caleb, Caleb mouth open, scared, Grayson and Cameron mouths closed, both smiling
                            with dissolve

                            cal "SOMEONE PLEASE HELP ME!"

                            scene v11amh39a # FPP. Same cam as v11amh39, Grayson is lifting Caleb by the waist
                            with dissolve

                            pause 0.5

                            play sound "sounds/fall.mp3"
                            scene v11amh39b # FPP. Same cam as v11amh39, Caleb is on the ground, Grayson and Cameron are chest bumping, Grayson smiling, mouth open, Cameron smiling, mouth closed
                            with dissolve

                            gr "FUCK YEAH!!!"

                            scene v11amh39c # FPP. Same cam as v11amh39, Caleb still on ground, Cameron and Grayson looking at each other, Grayson mouth open, smiling, Cameron has his back turned to camera
                            with dissolve

                            gr "Now where's the lucky one?"

                            scene v11amh39d # FPP. Same as v11amh39c, both mouths closed, smiling, Cameron and Grayson looking at MC now
                            with dissolve

                            u "Uhm, I'm right here."

                            scene v11amh39e # FPP. Same as v11amh39c, Cameron mouth open, smiling, Grayson mouth closed, smiling
                            with dissolve

                            ca "You've been hiding here in the open? Are you an idiot?"

                            scene v11amh39f # FPP. Grayson and Cameron get closer to MC, both smiling, mouths closed
                            with dissolve

                            pause 0.75

                            scene v11amh40 # FPP. MC and Grayson looking at each other, Grayson smiling, mouth open
                            with dissolve

                            gr "I saw you earlier, but I thought you were the rancher."

                            scene v11amh40a # FPP. Same as v11amh40, Grayson smiling, mouth closed
                            with dissolve

                            u "That's what I was going for."

                            scene v11amh40
                            with dissolve

                            gr "Well, nice try, but it didn't work."

                            scene v11amh23
                            with dissolve

                            pause 0.5

                            play sound "sounds/fall.mp3"
                            scene v11amh23a
                            with vpunch

                            pause 1

                            scene v11amh24a
                            with dissolve

                            u "Ahh, fuck! What was that for? I had already won. You just got Caleb and I heard you get Ryan."

                            scene v11amh41 # FPP. Cameron is now standing next to the horse, looking at MC (MC standing up now), Cameron smiling, mouth open
                            with dissolve

                            ca "I never got Ryan, he escaped."

                            scene v11amh41a # FPP. Same as v11amh41, Cameron smiling, mouth closed
                            with dissolve

                            u "What the fuck?"

                            scene v11amh42 # FPP. Ryan is running out of the woods, smiling, mouth open
                            with dissolve

                            ry "And that's game."

                "Keep running":
                    $ v11_manhunt_winner = "Ryan"

                    scene v11amh36  
                    with dissolve

                    pause 0.75

                    scene v11amh37 
                    with dissolve

                    ran "You must be Grayson, here's the Bronco for the manhunt. Have him back by morning."

                    scene v11amh37a 
                    with dissolve

                    u "(What the fuck was that?)"

                    scene v11amh37b 
                    with dissolve

                    u "You must be a present for the losers. Maybe if I stay by you I'll be good."

                    scene v11amh38 
                    with dissolve

                    ry "Look man, you don't have to slam me!"

                    scene v11amh38a 
                    with dissolve

                    ca "GET OVER HERE!"

                    scene v11amh38b 
                    with dissolve

                    ry "AHHHHHHH!"

                    scene v11amh38c 
                    with dissolve

                    u "I feel like he deserved that!"

                    scene v11amh38c
                    with fade

                    u "It's been 20 minutes, and I'm starting to get hungry. I'm so hungry I could eat a horse."

                    scene v11amh37b
                    with dissolve

                    u "You know what I mean."

                    scene v11amh39 
                    with dissolve

                    cal "SOMEONE PLEASE HELP ME!"

                    scene v11amh39a 
                    with dissolve

                    pause 0.5

                    play sound "sounds/fall.mp3"
                    scene v11amh39b 
                    with dissolve

                    gr "FUCK YEAH!!!"

                    scene v11amh39c 
                    with dissolve

                    gr "Now where's the lucky one?"

                    scene v11amh39d 
                    with dissolve

                    u "Uhm, I'm right here."

                    scene v11amh39e 
                    with dissolve

                    ca "You've been hiding here in the open? Are you an idiot?"

                    scene v11amh39f 
                    with dissolve

                    pause 0.75

                    scene v11amh40 
                    with dissolve

                    gr "I saw you earlier, but I thought you were the rancher."

                    scene v11amh40a 
                    with dissolve

                    u "That's what I was going for."

                    scene v11amh40
                    with dissolve

                    gr "Well, nice try, but it didn't work."

                    scene v11amh23
                    with dissolve

                    pause 0.5

                    play sound "sounds/fall.mp3"
                    scene v11amh23a
                    with vpunch

                    pause 1

                    scene v11amh24a
                    with dissolve

                    u "Ahh, fuck! What was that for? I had already won. You just got Caleb and I heard you get Ryan."

                    scene v11amh41
                    with dissolve

                    ca "I never got Ryan, he escaped."

                    scene v11amh41a
                    with dissolve

                    u "What the fuck?"

                    scene v11amh42
                    with dissolve

                    ry "And that's game."
                
    scene v11amh7c
    with dissolve

    gr "As fun as that shit was, it's time for some punishment. Winner, choose who our loser is."

    if v11_manhunt_winner == "Caleb":
        scene v11amh26a
        with dissolve

        cal "Sorry [name], but you gotta take this one."

        scene v11amh26
        with dissolve

        u "What, why me?"

    elif v11_manhunt_winner == "Ryan":
        scene v11amh27a # FPP. Same as v11amh27, but Ryan is smiling, mouth open
        with dissolve

        ry "Easy, go ahead, [name]."

        scene v11amh27b # FPP. Same as v11amh, Ryan smiling, mouth closed
        with dissolve

        u "What, why me?"

    scene v11amh10
    with dissolve

    ca "Was that a question I just heard?"

    #scene v11amh10b # FPP. Same as v11amh10, Cameron is smiling, mouth closed
    #with dissolve

    u "..."

    scene v11amh7c
    with dissolve

    gr "Get on the horse."

    scene v11amh43 # TPP. Show MC midway through climbing on the horse (Cameron is standing near the back of the horse, camera should look at MC from behind)
    with dissolve

    pause 0.75

    scene v11amh43a # TPP. Same cam as v11amh43, MC is now on the horse, he is worried, mouth closed
    with dissolve

    pause 0.75

    scene v11amh44 # FPP. MC is now sitting on the horse, he's looking at Cameron, which is near the back of the horse, Cameron smiling, mouth closed
    with dissolve

    u "Now what?"

    scene v11amh44a # FPP. Same as v11amh44, Cameron is smiling, slapping the back of the horse, mouth open
    with dissolve

    ca "GITTY UP COWBOY!"

    scene v11amh45 # FPP. MC is on the horse, looking forwards, the horse is running forwards
    with dissolve

    u "OH FUCK!"

    scene v11amh46 # FPP. MC still on the horse, the horse is now a bit further away
    with dissolve

    menu (fail_label="v11_horse_fall"):
        "Balance":
            scene v11amh47 # FPP. MC still on the horse, horse a bit further away compared to v11amh46
            with dissolve

            u "(I got this!)"

            scene v11amh48 # FPP. MC still on the horse, looking at Caleb, Caleb mouth open, neutral expression, the horse is now a bit further away compared to v11amh47
            with dissolve

            cal "He's doing pretty good."

            scene v11amh49 # FPP. MC still on horse, horse stopped (Cameron, Grayson, Caleb and Ryan are all close by, out of shot)
            with dissolve

            menu:
                "Good horse":
                    scene v11amh49
                    with dissolve

                    u "Good horse."

                    scene v11amh50 # FPP. MC is still on the horse, looking at Ryan (Ryan is to the left of the horse), Ryan slightly annoyed, mouth open
                    with dissolve

                    ry "This doesn't look like a punishment, it looks like fun."

                    scene v11amh49
                    with dissolve

                    u "Are you having fun horse?"

                    scene v11amh51 # TPP. Show MC on the horse, the horse is rearing, MC is in control, smiling, mouth open
                    with dissolve

                    $ grant_achievement("hold_your_horses")
                    u "Woah! *Laughs* Guess he is having a good time."

                    scene v11amh44b # FPP. Same as v11amh44, Cameron is slightly annoyed, mouth open
                    with dissolve

                    ca "Alright, this is bullshit, off the horse."

                    scene v11amh44c # FPP. Same as v11amh44, the horse is kicking Cameron right in the chest, Cameron mouth closed, startled expression
                    with dissolve

                    play sound "sounds/facepunch1.mp3"
                    pause 0.75

                    scene v11amh44d # FPP. Same as v11amh44, Cameron is on the ground, mouth closed, he is in pain
                    with dissolve

                    pause 0.75

                    scene v11amh48
                    with dissolve

                    cal "WOAH! Are you okay? Almost looks as bad as getting body slammed. *Laughs*"

                    scene v11amh44e # FPP. Same as v11amh44, Cameron on the ground, in pain, mouth open
                    with dissolve

                    ca "When I get up, I'm gonna kill you."

                    scene v11amh43b # TPP. Same as v11amh43, Show MC midway through getting off the horse
                    with dissolve

                    pause 0.75

                    scene v11amh43c # TPP. Same as v11amh43, MC is now standing, looking at the horse
                    with dissolve

                    pause 0.75

                    scene v11amh7e # FPP. Same as v11amh7, Grayson slightly angry, mouth closed
                    with dissolve

                    u "I'm kinda glad I lost, I think I made a new friend."

                    scene v11amh7d # FPP. Same as v11amh7, Grayson slightly angry, mouth open
                    with dissolve

                    gr "Next year we're going back to proper punishments. This horse was supposed to give you hell..."

                    jump v11_mc_horse_room

                "Pet horse":
                    scene v11amh49a # FPP. Same as v11amh49, MC is petting the horse (show his hand on the horse's neck)
                    with dissolve

                    pause 0.75

                    scene v11amh51a # TPP. Same as v11amh51, but MC is not in control, he is unbalanced on the horse, mouth closed, startled face
                    with dissolve

                    $ grant_achievement("off_your_high_horse")
                    hor "NEIGHHHHHH!!!"

                    scene v11amh51b # TPP. Same as v11amh51, but MC is midair, startled expression, mouth open
                    with dissolve

                    u "Oh shit!"

                    scene v11amh51c # TPP. Same as v11amh51, but now MC is on the ground, the horse is running away, MC is in pain, mouth closed
                    with vpunch
                    play sound "sounds/fall.mp3"

                    pause 1

                    scene v11amh24a
                    with dissolve

                    ca "*Laughs*"

                    scene v11amh24
                    with dissolve

                    gr "Classic."

                    scene v11amh24a
                    with dissolve

                    u "Fuck, that actually hurt."

                    scene v11amh24
                    with dissolve

                    gr "Oh suck it up, let's get back to the house."

                    jump v11_mc_horse_room
                
        "Fall":
            jump v11_horse_fall

label v11_horse_fall:

    scene v11amh51a
    with dissolve

    $ grant_achievement("off_your_high_horse")
    u "(I can't balance.)"

    scene v11amh51b
    with dissolve

    pause 0.75

    play sound "sounds/fall.mp3"
    scene v11amh51c
    with vpunch

    pause 0.75

    scene v11amh52 # FPP. MC is lying on the ground, Ryan looking down on him, Ryan mouth closed, worried expression
    with dissolve

    u "*Gasping for air*"

    scene v11amh52a # FPP. Same as v11amh52, Ryan mouth open, worried expression
    with dissolve

    ry "Oh shit, are you okay?"

    scene v11amh52
    with dissolve

    u "..."

    scene v11amh52a
    with dissolve

    ry "Bro?"

    scene v11amh52
    with dissolve

    u "I... I'm... I'm fine."

    scene v11amh7c
    with dissolve

    gr "*Laughs* That was better than the time we made all the pledges run through last year's bonfire! Let's head back."

    jump v11_mc_horse_room

label v11_mc_horse_room:

    scene black
    with fade
    pause 0.75

    scene v11amh53 # TPP. MC is standing next to his bed (he is looking at his bed, camera should be behind MC)
    with fade
  
    stop music fadeout 3
    play music "music/v11/Track Scene 9_3.mp3" fadein 2
    u "(I swear they want to kill us. I definitely need a good night's sleep.)"

    scene v11amh53a # TPP. Same cam as v11amh53, MC drops into his bed (similar to s95 in v1)
    with dissolve

    play sound "sounds/impactbed.mp3"

    pause 1

    scene v11amh53b # TPP. Same cam as v11amh53, MC is now sleeping, show him sleeping with his belly upwards
    with dissolve

    pause 1

    scene v11amh53c # TPP. Same cam as v11amh53, MC is still sleeping, he is sleeping with his belly faced downwards now
    with dissolve

    pause 1

    scene v11amh54 # FPP. Ryan is standing next to MC's bed, MC looking at him, Ryan mouth open, slightly worried expression, MC still lying down in bed
    with fade

    ry "Wake up, man."
    stop music fadeout 3
    play music "music/v11/Track Scene 9_4.mp3" fadein 2
    scene v11amh55 # FPP. MC is now sitting on his bed, still looking at Ryan, Ryan mouth open, slightly worried expression
    with dissolve

    ry "We're gonna be late."

    scene v11amh55a # FPP. Same as v11amh55, Ryan mouth closed, slightly worried expression
    with dissolve

    u "For what?"

    scene v11amh55
    with dissolve

    ry "The trip!"

    scene v11amh55a
    with dissolve

    u "Oh shit!"

    scene v11amh56 # TPP. Show MC grabbing his luggage in his room, MC is worried, mouth closed
    with dissolve

    pause 0.75
    
    #scene v11amh57 # TPP. Show Ryan and MC leaving the Apes house with their luggage, both worried, mouth closed
    #with dissolve
    #pause 0.75

    scene v11amh58 # TPP. Show a car on the road
    with dissolve

    pause 0.75

    scene v11amh59 # FPP. Show Ryan walking ahead of MC into the airport, show Ms Rose, Nora and Mr Lee in the backrgound
    with fade

    pause 0.75
    stop music fadeout 3
    jump v11_airport_arrival
# SCENE 12b: The Concert With Penelope
# Locations: Hotel Lobby, Sidewalk, Concert, Hallway
# Characters: PENELOPE (Outfit: 1), MC (Outfit: 2)
# Time: Night 

label v13s12b:
    scene v13s12b_1 # TPP. Show Penelope walking up to MC in the lobby, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 12a_1.mp3" fadein 2

    scene v13s12b_2 # FPP. Penelope standing in front of MC, Penelope slightly worried, mouth open
    with dissolve

    pe "Sorry I took so long... I shouldn't have kept you waiting."

    scene v13s12b_2a # FPP. Same as v13s12b_2, Penelope mouth closed
    with dissolve

    u "Haha, I just got back. You're fine, we have plenty of time."

    scene v13s12b_2
    with dissolve

    pe "Okay, okay... I don't know why I'm stressed... I think my anxiety is acting up, ha. This girl is like... Super famous."

    scene v13s12b_2a
    with dissolve

    u "*Chuckles* Don't worry, if you ever get to the point where you wanna leave, just say the word and we'll go."

    scene v13s12b_2
    with dissolve

    pe "You sure you won't be mad?"

    scene v13s12b_2b # FPP. Same as v13s12b_2a, Penelope slight smile
    with dissolve

    u "Haha, I don't even know the singer's name... How could I be mad?"

    scene v13s12b_2c # FPP. Same as v13s12b_2, Penelope slight smile
    with dissolve

    pe "*Chuckles* You're a goofball. Her name is Polly. She's literally one of the biggest international stars."

    scene v13s12b_2b
    with dissolve

    u "Shows what I know. *Chuckles*"

    scene v13s12b_2c
    with dissolve

    pe "Haha, let's go."

    scene v13s12b_3 # TPP. Show MC and Penelope walking out of lobby to the street, both slight smiles mouths closed
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 12a_2.mp3" fadein 2

    scene v13s12b_4 # TPP. Show MC and Penelope walking on sidewalk, both slight smiles, mouths closed
    with fade

    pause 0.75

    scene v13s12b_5 # TPP. Show MC and Penelope arriving at the concert, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    image ConcertAnimation = Movie(play="images/v13/ConcertAnimation.webm", loop=True) 

    scene ConcertAnimation
    with fade

    pause

    stop music fadeout 3
    play music "music/v13/Track Scene 12a_3.mp3" fadein 2

    scene v13s12b_6 # TPP. MC and Penelope in front of the stage (play with angles so that no other people have to be shown). MC and Penelope looking at each other, both smiling, Penelope mouth open, MC mouth closed (Camera is behind them as to show their shoulders and head) (Polly NOT on stage)
    with dissolve

    pe "Oh my gosh... I was not expecting this many people."

    pe "I mean, I knew there'd be a lot, but... Wow, this is insane."

    scene v13s12b_6a # TPP. Same as v13s12b_6, MC mouth open, Penelope mouth closed
    with dissolve

    u "Yeah... Don't worry about it. We didn't come for them, we came for Polly and a good time."

    scene v13s12b_6
    with dissolve

    pe "*Deep breath* You're right. *Chuckles* You're right..."

    stop music fadeout 3
    play music "music/v13/Track Scene 12b_1.mp3" fadein 2

    scene v13s12b_7 # TPP. Show Polly on stage, holding mic to her mouth, mouth open, smiling, looking at the crowd
    with dissolve
    
    polly "HOW'S EVERYONE DOING TONIGHT?! ARE YOU READY TO HAVE SOME FUN?!"

    scene v13s12b_6b # TPP. Same as v13s12b_6, Polly now on stage (show only her legs)
    with dissolve

    pe "OH WOW, THAT'S SO LOUD!"

    scene v13s12b_6c # TPP. Same as v13s12b_6b, Polly's legs slightly different pose, MC mouth open, Penelope mouth closed
    with dissolve

    u "DO YOU KNOW ALL OF THE SONGS?"

    scene v13s12b_6b
    with dissolve

    pe "WORD FOR WORD!"

    scene v13s12b_7
    with dissolve

    polly "IF YOU'RE OUT WITH YOUR BEST FRIEND TONIGHT CAN I GET A HELL YEAHHHH!"

    scene v13s12b_6d # TPP. Same as v13s12b_6c, MC and Penelope looking up at the stage, both neutral poses, slightly excited, not showing their faces
    with dissolve

    menu:
        "Say hell yeah":
            scene v13s12b_6e # TPP. Same as v13s12b_6d, MC excited, arms up, Penelope same pose
            with dissolve

            u "HELL YEAHHH!!"

            scene v13s12b_6b
            with dissolve

            pe "*Chuckles* Hell yeah!"

            scene v13s12b_6c
            with dissolve

            u "Haha, are you embarrassed of me?"

            scene v13s12b_6b
            with dissolve

            pe "I just don't want people staring at me. *Laughs*"

        "Say nothing":
            u "(I don't want any attention.)"

    scene v13s12b_7a # TPP. Same as v13s12b_7, Polly singing
    with dissolve

    polly "*Singing* LOVE COMES UNEXPECTED, LOVE'S UNNATURAL!"

    scene v13s12b_6f # TPP. Same as v13s12b_6e, Penelope also excited, arms up
    with dissolve

    pe "*SINGING* I CAN FEEL MY HEART BEAT, LOVE IS LIKE A BATTERY, IT POWERS UP MY SOUL!"

    scene v13s12b_6c
    with dissolve

    u "YOU REALLY KNOW THIS STUFF!"

    scene v13s12b_6b
    with dissolve

    pe "TOLD YOU I WAS A FAN!"

    scene v13s12b_6c
    with dissolve

    u "HAHA!"

    scene v13s12b_6b
    with dissolve

    pe "I WISH I COULD SEE..."

    scene v13s12b_6g # TPP. Same as v13s12b_6b, MC and Penelope looking behind them (to someone off screen), Penelope slightly sad, mouth closed, MC slightly angry, mouth closed
    with dissolve

    unknown "ME TOO, SO IF YOU COULD MOVE YOUR BIG ASS HEAD, I'D APPRECIATE IT!"

    scene v13s12b_6h # TPP. Same as v13s12b_6g, Penelope mouth open
    with dissolve

    pe "I'm so sorry... I'll-"

    scene v13s12b_6i # TPP. Same as v13s12b_6g, MC mouth open
    with dissolve

    u "YOU'RE SORRY? BRO, IF YOU DON'T WATCH YOUR MOUTH MY KNUCKLES WILL."

    scene v13s12b_6g
    with dissolve
    
    unknown "S-sorry dude... I don't want any problems..."

    scene v13s12b_6i
    with dissolve

    u "Good."

    scene v13s12b_6b
    with dissolve

    pe "You're always so quick to speak up... *Chuckles*"

    scene v13s12b_6c
    with dissolve

    u "I'm not gonna let someone talk to you like that, crazy. You don't deserve that."

    scene v13s12b_6b
    with dissolve

    pe "You're sweet."

    if penelope.relationship.value >= Relationship.LIKES.value:
        scene v13s12b_6j # TPP. Same as v13s12b_6b, Penelope kissing MC on the lips
        with dissolve
        play sound "sounds/kiss.mp3"

        pause 1.5
    
    else:
        scene v13s12b_6k # TPP. Same as v13s12b_6j, Penelope kissing MC on the cheek
        with dissolve
        play sound "sounds/kiss.mp3"
        pause 1

    scene v13s12b_6b
    with dissolve

    pe "I wish I had a ladder or something... *Laughs*"

    scene v13s12b_6c
    with dissolve

    u "OR SOMETHING, COMING UP!"

    scene v13s12b_6l # TPP. Same as v13s12b_6c, MC leaning down, putting Penelope on his shoulders
    with dissolve

    pause 0.75

    scene v13s12b_8 # FPP. Penelope on MC's shoulder's, he is looking up at her, she is looking down at him, smiling, mouth open
    with dissolve

    pe "Wha- Oh gosh! *Chuckles* This is definitely something else!"

    scene v13s12b_8a # FPP. Same as v13s12b_8, Penelope looking at stage, singing
    with dissolve

    pause 0.75

    scene v13s12b_8b # FPP. Same as v13s12b_8a, Penelope different pose
    with dissolve

    pause 0.75

    scene v13s12b_8a
    with dissolve

    u "(Fuck, I don't know how much longer I can hold her.)"

    scene v13s12b_9 # TPP. Penelope on MC's shoulder's, random guy bumping into him, show Penelope slightly unbalancing on MC's shoulder
    with dissolve
    
    unknown "Oh shit, sorry man."

    menu (fail_label="v13s12b_failed_timer"):
        "Steady":
            scene v13s12b_9a # TPP. Same as v13s12b_9, Penelope still slightly unbalanced, different pose though, random guy not in shot anymore
            with dissolve

            menu (fail_label="v13s12b_failed_timer"):
                "Steady":
                    scene v13s12b_7b # TPP. Same as v13s12b_7, Polly looking at MC and Penelope's direction, smiling, mouth open
                    with dissolve

                    stop music fadeout 3
                    play music "music/v13/Track Scene 12b_2.mp3" fadein 2

                    #polly "THIS GIRL HERE KNOWS ALL OF THE DAMN LYRICS! *Laughs* WHAT'S YOUR NAME, SWEETNESS?"
                    polly "THIS GIRL HERE KNOWS ALL OF THE DAMN LYRICS! *Laughs*"

                    #scene v13s12b_10 # TPP. Close up of Penelope's face, Polly is putting the mic up to Penelope's mouth (show only the mic and hand of Polly). Penelope smiling, mouth open
                    #with dissolve

                    #pe "I-I... I'm Penelope."

                    scene v13s12b_7b
                    with dissolve
                    
                    #polly "That's hot, babe! You and your barstool there, be sure to come hang backstage."
                    polly "You and your barstool there, be sure to come hang backstage."

                    scene v13s12b_10
                    with dissolve

                    pe "Oh... Okay. *Chuckles*"

                    scene v13s12b_6m # TPP. Same as v13s12b_6l, MC putting Penelope down
                    with dissolve

                    pause 0.75

                    scene v13s12b_7
                    with dissolve

                    polly "LET'S GET THE SHOW BACK ON!"

                    stop music fadeout 3
                    play music "music/v13/Track Scene 12a_6.mp3" fadein 2

                    scene v13s12b_7a
                    with dissolve

                    polly "*Singing* LOVE COMES UNEXPECTED, LOVE'S UNNATURAL! I CAN FEEL MY HEARTBEAT, LOVE IS LIKE BATTERY, IT POWERS UP MY SOUL!"

                    scene v13s12b_6b
                    with dissolve

                    pe "That really just happened!?"

                    scene v13s12b_6c
                    with dissolve

                    u "Haha, it really did!"

                    scene v13s12b_6n # TPP. Same as v13s12b_6f, MC and Aubrey dancing
                    with dissolve

                    pause 0.75

                    scene v13s12b_6o # TPP. Same as v13s12b_6n, different dancing pose
                    with dissolve

                    pause 0.75

                    scene v13s12b_6c
                    with dissolve

                    u "Ready to head backstage?"

                    scene v13s12b_6b
                    with dissolve

                    pe "Yeah! Let's go."

                    stop music fadeout 3
                    play music "music/v13/Track Scene 12a_8.mp3" fadein 2

                    scene v13s12b_11 # TPP. MC and Penelope walking into the backstage area, both smiling, mouths closed
                    with fade

                    pause 0.75

                    scene v13s12b_12 # TPP. Show MC and Penelope sitting down in the backstage area, both smiling, mouths closed
                    with fade

                    pause 0.75

                    stop music fadeout 3

                    jump v13s13b

                "Damn":
                    pass
                
        "Oops":
            pass

label v13s12b_failed_timer:
    scene v13s12b_8c # TPP. Same as v13s12b_8b, Penelope falling off MC's shoulders
    with dissolve

    pause 1.25

    scene v13s12b_13 # FPP. MC looking at Penelope, she's on the floor, very embarassed, in pain, mouth closed
    with vpunch
    play sound "sounds/fall.mp3"

    u "Oh shit! I'm so sorry, Penelope... I-"

    scene v13s12b_13a # FPP. Same as v13s12b_13, Penelope mouth open
    with dissolve

    pe "Oww, that hurt..."

    scene v13s12b_13
    with dissolve

    unknown "Way to get noticed. *Laughs*"

    scene v13s12b_14 # TPP. Close up of MC looking towards the back, where the random guy was, MC stern look, mouth closed
    with dissolve

    unknown "Sorry..."

    scene v13s12b_13b # FPP. Same as v13s12b_13, MC pulling Penelope off the ground
    with dissolve

    pause 0.75

    scene v13s12b_6p # TPP. Same as v13s12b_6c, Penelope very embarassed, in slight pain, mouth closed, MC worried, mouth open
    with dissolve

    u "I really am sorry about that. Are you hurt?"

    scene v13s12b_6q # TPP. Same as v13s12b_6p, Penelope mouth open, MC mouth closed
    with dissolve

    pe "Uhh... Actually, I feel like everyone is staring at me. Can we just leave?"

    scene v13s12b_6p
    with dissolve

    u "I had a feeling you'd say that. Are you sure?"

    scene v13s12b_6q
    with dissolve

    pe "I just don't feel as pumped, and I'm kinda embarrassed and my head hurts a bit..."

    scene v13s12b_6p
    with dissolve

    u "Those sound like some good reasons."

    if v12_murder_count < 10:

        u "We can go ahead and go."

        scene v13s12b_6q
        with dissolve

        pe "Thanks..."

        scene v13s12b_6p
        with dissolve

        u "Of course."

        stop music fadeout 3
        play music "music/v13/Track Scene 12a_2.mp3" fadein 2

        scene v13s12b_15 # TPP. Show MC and Penelope leaving the concert venue, Penelope sad, in slight pain, MC worried, mouths closed
        with dissolve

        pause 0.75

        scene v13s12b_16 # TPP. Show MC and Penelope walking on sidewalk back to the hotel, Penelope sad, in slight pain, MC worried, mouths closed
        with fade

        pause 0.75

        scene v13s12b_17 # TPP. Show MC and Penelope walking into the hotel, Penelope sad, in slight pain, MC worried, mouths closed
        with fade

        pause 0.75

        stop music fadeout 3
        play music "music/v13/Track Scene 12a_1.mp3" fadein 2

        scene v13s12b_18 # FPP. MC and Penelope in hotel lobby, looking at each other, Penelope sad, mouth open
        with dissolve

        pe "[name]... I'm really sorry for wanting to leave, again. I probably ruined your night, I'm sure you wish you brought someone else."

        scene v13s12b_18a # FPP. Same as v13s12b_18, Penelope mouth closed
        with dissolve

        u "What? Of course not, I had a great time with you."

        scene v13s12b_18b # FPP. Same as v13s12b_18, Penelope slight smile
        with dissolve

        pe "Really?"

        scene v13s12b_18c # FPP. Same as v13s12b_18a, Penelope slight smile
        with dissolve

        u "*Chuckles* Yes, Penelope."

        scene v13s12b_18b
        with dissolve

        pe "Oh... Okay, good. *Chuckles* Thanks for a fun night out..."

        scene v13s12b_18c
        with dissolve

        u "Anytime."

        scene v13s12b_18b
        with dissolve

        pe "Goodnight, [name]."

        scene v13s12b_18c
        with dissolve

        u "Goodnight Penelope."

        scene v13s12b_19 # TPP. Show Penelope hugging MC, both slight smiles, mouths closed
        with dissolve

        pause 0.75

        scene v13s12b_20 # TPP. Show MC walking through hotel lobby towards the rooms, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v13s12b_21 # TPP. Show MC walking in hotel corridor, slight smile, mouth closed
        with dissolve

        pause 0.75

        stop music fadeout 3

        if v11_riley_roomate:
            jump v13s15a
        else:
            jump v13s15

    else:
        scene v13s12b_6p
        with dissolve

        u "But, instead of going home... Let's use the tickets and go backstage?"

        scene v13s12b_6q
        with dissolve

        pe "That sounds more intimidating than this..."

        scene v13s12b_6p
        with dissolve

        u "Haha, c'mon... I'm not letting you ruin your one night out, and I'll be with you every second of the way."

        stop music fadeout 3
        play music "music/v13/Track Scene 12a_8.mp3" fadein 2

        scene v13s12b_11
        with dissolve

        pause 0.75

        scene v13s12b_12
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v13s13b
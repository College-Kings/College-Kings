# SCENE 12a: Concert With Aubrey
# Locations: Hotel Lobby, Sidewalk, Concert
# Characters: AUBREY (Outfit: 2), MC (Outfit: 2), POLLY (Outfit: 1)
# Time: Night

label v13s12a:
    scene v13s12a_1 # TPP. Show Aubrey walking up to MC in the lobby, both slight smiles, mouths closed
    with fade

    pause 0.75

    play music music.ck1.v13.Track_Scene_12a_1 fadein 2
    
    scene v13s12a_2 # FPP. Aubrey standing in front of MC, looking at MC, slight smile, mouth open
    with dissolve

    au "Ooh, perfect timing! Ready to go?"

    scene v13s12a_2a # FPP. Same as v13s12a_2, mouth closed
    with dissolve

    u "That was exactly an hour?"

    scene v13s12a_2
    with dissolve

    au "*Chuckles* Yeah, where were you?"

    scene v13s12a_2a
    with dissolve

    u "Imre had some... trouble."

    u "Ryan and I were just keeping an eye out for him."

    scene v13s12a_2
    with dissolve

    au "Ahh... Alright, sounds good. Ready?"

    scene v13s12a_2a
    with dissolve

    u "Yeah, let's go."

    scene v13s12a_3 # TPP. Show MC and Aubrey walking out of lobby to the street, both slight smiles mouths closed
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music music.ck1.v13.Track_Scene_12a_2 fadein 2

    scene v13s12a_4 # TPP. Show MC and Aubrey walking on sidewalk, both slight smiles, mouths closed
    with fade

    pause 0.75

    scene v13s12a_5 # TPP. Show MC and Aubrey arriving at the concert, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    image ConcertAnimation = Movie(play="images/v13/ConcertAnimation.webm", loop=True) 

    scene ConcertAnimation
    with fade

    pause
    
    stop music fadeout 3
    play music music.ck1.v13.Track_Scene_12a_3 fadein 2

    scene v13s12a_6 # TPP. MC and Aubrey in front of the stage (play with angles so that no other people have to be shown). MC and Aubrey looking at each other, both smiling, Aubrey mouth open, MC mouth closed (Camera is behind them as to show their shoulders and head) (Polly NOT on stage)
    with dissolve

    au "Wow, haha... There's plenty of people here. I knew it'd be packed."

    scene v13s12a_6a # TPP. Same as v13s12a_6, MC mouth open, Aubrey mouth closed
    with dissolve

    u "This is gonna sound crazy to ask now, but who's the singer again?"

    scene v13s12a_6
    with dissolve

    au "Oh my gosh. *Chuckles* She goes by Polly."

    scene v13s12a_6a
    with dissolve

    u "Where do these artists come up with their names? *Chuckles*"

    scene v13s12a_6
    with dissolve

    au "I'm not sure about everyone, but I know her last name is Lolly and her first name starts with a P, so she mashed it up and went by Polly. *Laughs*"

    scene v13s12a_6a
    with dissolve

    u "That actually makes a little sense. *Chuckles*"

    scene v13s12a_6
    with dissolve

    au "Haha, luckily we got a front row spot. We won't have a problem-"

    stop music fadeout 3
    play music music.ck1.v13.Track_Scene_12a_4 fadein 2

    scene v13s12a_7 # TPP. Show Polly on stage, holding mic to her mouth, mouth open, smiling, looking at the crowd
    with dissolve
    
    polly "HOW'S EVERYONE DOING TONIGHT?! ARE YOU READY TO HAVE SOME FUN?!"

    scene v13s12a_6b # TPP. Same as v13s12a_6, MC and Aubrey looking at Polly on the stage, Aubrey's hands up, she is very excited, MC neutral pose (Show only Poly's legs)
    with dissolve

    au "YEAH!!!"

    scene v13s12a_6c # TPP. Same as v13s12a_6b, Aubrey still very excited, looking at Polly on stage, MC looking over at Aubrey, slight smile, mouth closed
    with dissolve

    u "(She's so excited.)"

    scene v13s12a_6d # TPP. Same as v13s12a_6, but Polly now on stage
    with dissolve

    au "I know all her songs, but I'm not good at remembering lyrics!!!"

    scene v13s12a_6e # TPP. Same as v13s12a_6a, but Polly now on stage, different pose than v13s12a_6d
    with dissolve

    u "I CAN'T HEAR YOU!"

    scene v13s12a_6d
    with dissolve

    au "I SAID, I KNOW ALL HER SONGS, BUT I HAVE TROUBLE REMEMBERING ALL THE LYRICS."

    scene v13s12a_6e
    with dissolve

    u "OH! *Laughs*"

    scene v13s12a_7
    with dissolve

    polly "IF YOU'RE OUT WITH YOUR BEST FRIEND TONIGHT, CAN I GET A HELL YEAHHHH!"

    scene v13s12a_6b
    with dissolve

    menu:
        "Say hell yeah":
            scene v13s12a_6f # TPP. Same as v13s12a_6b, MC also excited, arms up in the air
            with dissolve

            u "HELL YEAHHH!!"

            scene v13s12a_6d
            with dissolve

            au "HELL YEAHHH!!"

            scene v13s12a_6e
            with dissolve

            u "HAHA!"

            scene v13s12a_6d
            with dissolve

            au "*Laughs*"

        "Say nothing":
            u "(I don't want any attention.)"

    scene v13s12a_7a # TPP. Same as v13s12a_7, Polly singing
    with dissolve
    
    polly "*Singing* LOVE COMES UNEXPECTED, LOVE'S UNNATURAL!"

    scene v13s12a_6f
    with dissolve

    au "*SINGING* I CAN *MUMBLE* *MUMBLE* LOVE IS LIKE A BATTERY, IT POWERS UP MY SOUL!"

    scene v13s12a_6e
    with dissolve

    u "STUMBLED THERE A BIT. *Chuckles*"

    scene v13s12a_6d
    with dissolve

    au "CLOSE ENOUGH! *Laughs*"

    scene v13s12a_6d
    with dissolve

    au "I WANT TO GET SOME PICTURES, BUT... IT'S TOO DARK."

    scene v13s12a_6e
    with dissolve

    u "THAT'S WHAT THE FLASH IS FOR!"

    scene v13s12a_6g # TPP. Same as v13s12a_6f, MC and Aubrey both looking to the left (off screen), both mouths closed, slightly angry
    with dissolve

    unknown "YO, SHUT UP! YOU'RE YELLING IN MY FUCKING FACE!"

    scene v13s12a_6h # TPP. Same as v13s12a_6g, Aubrey mouth open
    with dissolve

    au "TRUST ME, NO ONE WANTS TO BE NEAR YOUR NASTY ASS FACE!"

    scene v13s12a_6e
    with dissolve

    u "HAHA!"

    scene v13s12a_6g
    with dissolve

    unknown "YOU GOT A PROBLEM, DUDE!?"

    menu:
        "Say something":
            $ v13_hugged_aubrey = True

            scene v13s12a_6i # TPP. Same as v13s12a_6g, MC mouth open
            with dissolve

            u "LISTEN MY GUY, IF YOU DON'T CHILL THE FUCK OUT AND ENJOY THE SHOW, I'LL KNOCK YOUR TEETH IN."

            u "SOUND FAIR?"

            scene v13s12a_6g
            with dissolve

            unknown "S-SORRY BRO, I DIDN'T MEAN ANYTHING BY IT..."

            scene v13s12a_6i
            with dissolve

            u "GOOD!"

            scene v13s12a_6d
            with dissolve

            au "HAHA!"

            scene v13s12a_6j # TPP. Same as v13s12a_6e, both mouths closed, hugging each other
            with dissolve

            pause 0.75

        "Ignore him":
            u "Hmph!"

            unknown "DON'T FUCKING IGNORE ME, DO YOU KNOW WHO I-"

            scene v13s12a_6h
            with dissolve

            au "SHUT UP YOU PRICK! NO ONE WANTS TO HEAR YOU."

            scene v13s12a_6e
            with dissolve

            u "*Laughs*"

    scene v13s12a_6d
    with dissolve

    au "Now, back to my pictures!"

    scene v13s12a_6k # TPP. Same as v13s12a_6b, Aubrey taking a selfie, slight smile, mouth open, MC looking at her, slight smile, mouth closed
    with flash

    au "People are gonna be so jealous of these!"

    stop music fadeout 3
    play music music.ck1.v13.Track_Scene_12a_5 fadein 2

    scene v13s12a_7b # TPP. Same as v13s12a_7, Polly looking down to where Aubrey would be, slightly annoyed, mouth open
    with dissolve

    polly "My love in the front, could you chill with the camera? What's with all the pictures? People usually use video at concerts these days. *Chuckles*"

    #scene v13s12a_6l # TPP. Same as v13s12a_6b, but Aubrey not excited
    #with dissolve

    #au "*Shocked* I... Uhh..."

    menu:
        "Defend her":
            scene v13s12a_6m # TPP. Same as v13s12a_6l, MC pointing up at Polly as if he were angry, Aubrey looking at MC, Aubrey worried, mouth closed
            with dissolve

            u "HEY, LOOK HERE POLLY POLLY... YOU MAY BE FAMOUS AND ALL, BUT YOU'RE NOT GONNA DISRESPECT MY FRIEND. SHE'S A MASSIVE FAN, BUT I'M HAVING A REALLY HARD TIME SEEING WHY..."

            scene v13s12a_6n # TPP. Same as v13s12a_6m, Aubrey mouth open
            with dissolve

            au "*Whisper* [name]!"

            scene v13s12a_7c # TPP. Same as v13s12a_7b, Polly slight smile
            with dissolve

            polly "Oh, shit... Okay! I like a little bit of sass... How about you two join me backstage, later. *Chuckles*"

            scene v13s12a_6g
            with dissolve

            unknown "WHAT THE FUCK!?"

            scene v13s12a_7c
            with dissolve

            polly "LET'S GET THE SHOW BACK ON!"

            stop music fadeout 3
            play music music.ck1.v13.Track_Scene_12a_6 fadein 2

            scene v13s12a_7a
            with dissolve
            
            polly "*Singing* LOVE COMES UNEXPECTED, LOVE'S UNNATURAL! I CAN FEEL MY HEARTBEAT, LOVE IS LIKE A BATTERY, IT POWERS UP MY SOUL!"

            scene v13s12a_6d
            with dissolve

            au "YOU REALLY STUCK YOUR HEAD OUT THERE FOR ME, YOU CRAZY."

            scene v13s12a_6e
            with dissolve

            u "OF COURSE. *Laughs*"

            scene v13s12a_6o # TPP. Same as v13s12a_6j, Aubrey kissed MC in the lips
            with dissolve
            play sound sound.kiss

            pause 1.25

            scene v13s12a_6d
            with dissolve

            au "Thank you."

            scene v13s12a_6e
            with dissolve

            u "You're... *Voice crack* You're welcome."

            scene v13s12a_6d
            with dissolve

            au "Haha. I can't believe we're going backstage..."

            if v12_murder_count >= 10:
                scene v13s12a_6f
                with dissolve

                u "(Little does Polly know, we already had backstage passes. *Chuckles*)"

            scene v13s12a_6p # TPP. Same as v13s12a_6f, MC and Aubrey dancing
            with dissolve

            pause 0.75

            scene v13s12a_6q # TPP. Same as v13s12a_6p, different dancing pose
            with dissolve

            pause 0.75

            scene v13s12a_7c
            with fade

            polly "You guys have been an amazing crowd! And to my two hotshots up here, I'll see you guys backstage... GOODNIGHT!"

            stop music fadeout 3
            play music music.ck1.v13.Track_Scene_12a_7 fadein 2

            scene v13s12a_6a
            with dissolve

            u "That was actually insane!"

            scene v13s12a_6
            with dissolve

            au "I know! Let's hurry up and get backstage..."

            scene v13s12a_6a
            with dissolve

            u "Haha, alright!"

            stop music fadeout 3
            play music music.ck1.v13.Track_Scene_12a_8 fadein 2

            scene v13s12a_8 # TPP. MC and Aubrey walking into the backstage area, both smiling, mouths closed
            with fade

            pause 0.75

            scene v13s12a_9 # TPP. Show MC sitting down in the backstage area, both smiling, mouths closed
            with fade

            pause 0.75

            stop music fadeout 3

            jump v13s13a

        "Say nothing":
            u "(OH SHIT!)"

            scene v13s12a_7b
            with dissolve

            polly "Just gonna stand there with nothing to say, huh? *Chuckles* Just cool it with the flashes, alright sweetheart?"

            scene v13s12a_7c
            with dissolve

            polly "NOW, LET'S GET THE SHOW BACK ON!"

            stop music fadeout 3
            play music music.ck1.v13.Track_Scene_12a_6 fadein 2

            scene v13s12a_7a
            with dissolve
            
            polly "*Singing* LOVE COMES UNEXPECTED, LOVE'S UNNATURAL! I CAN FEEL MY HEARTBEAT, LOVE IS LIKE BATTERY, IT POWERS UP MY SOUL!"

            scene v13s12a_6l
            with dissolve

            au "That was so embarrassing!"

            scene v13s12a_6g
            with dissolve

            unknown "SHE TOLD YOUR ASS! *Laughs*"

            pause

            unknown "SORRY..."

            scene v13s12a_6r # TPP. Same as v13s12a_6d, both slightly sad
            with dissolve

            au "I... I WANNA GO."

            if v12_murder_count >= 10:
                scene v13s12a_6e
                with dissolve

                u "Aubrey, wait. I have backstage passes... Let's at least go check it out. I'm sure things will be different when she actually meets you."

                scene v13s12a_6d
                with dissolve

                au "*Sighs* If you say so... Even if she is a bitch... I'd still like to meet her. *Laughs*"
                
                stop music fadeout 3
                play music music.ck1.v13.Track_Scene_12a_8 fadein 2
                
                scene v13s12a_8
                with fade

                pause 0.75

                scene v13s12a_9
                with fade

                pause 0.75

                jump v13s13a

            else:
                scene v13s12a_6s # TPP. Same as v13s12a_6e, both slightly sad
                with dissolve

                u "*Sighs* Not the night I expected either... OKAY, LET'S GO."

                stop music fadeout 3
                play music music.ck1.v13.Track_Scene_12a_2 fadein 2

                scene v13s12a_10 # TPP. Show MC and Aubrey leaving the concert venue, both slightly sad, mouths closed
                with dissolve

                pause 0.75

                scene v13s12a_11 # TPP. Show MC and Aubrey walking on sidewalk back to the hotel, slightly sad, mouths closed
                with fade

                pause 0.75

                scene v13s12a_12 # TPP. Show MC and Aubrey walking into the hotel, slightly sad, mouths closed
                with fade

                pause 0.75

                scene v13s12a_13 # FPP. MC and Aubrey standing in hotel lobby, Aubrey slightly sad, mouth open
                with dissolve

                stop music fadeout 3
                play music music.ck1.v13.Track_Scene_12a_1 fadein 2

                au "Well... Tonight definitely isn't a night that I'll be forgetting anytime soon."

                scene v13s12a_13a # FPP. Same as v13s12a_13, mouth closed
                with dissolve

                u "Sorry if that was a nightmare..."

                scene v13s12a_13b # FPP. Same as v13s12a_13, Aubrey slight smile
                with dissolve

                au "Haha, oh my god. It's not your fault at all. Fame is ugly, the stars are beautiful... Goodnight, [name]."

                scene v13s12a_14 # TPP. Aubrey kissing MC on the cheek
                with dissolve
                play sound sound.kiss

                pause 1.25

                scene v13s12a_13c # FPP. Same as v13s12a_13a, Aubrey slight smile
                with dissolve

                u "Haha, goodnight Aubrey."

                scene v13s12a_15 # TPP. Show MC walking through hotel lobby towards the rooms, slight smile, mouth closed
                with dissolve

                pause 0.75

                scene v13s12a_16 # TPP. Show MC walking in hotel corridor, slight smile, mouth closed
                with dissolve

                pause 0.75

                stop music fadeout 3

                if v11_riley_roomate:
                    jump v13s15a
                else:
                    jump v13s15
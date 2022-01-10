# SCENE 23: Ms Rose Sex Scene
# Locations: Hotel Corridor, Hotel Lobby, Street, Paris Living Room, Hotel Room
# Characters: MS. ROSE (Outfit: 1), MC (Outfit: 9), CHLOE (Outfit: 2), RILEY (Outfit: 4)
# Time: Night
# Phone Images: None

label v12_ms_rose_sex: #can only get here if joinwolves
    scene v12msr1 # TPP. Show MC walking out of Riley's room into the hallway, slight smile, mouth closed
    with dissolve

    pause 0.75

    play music "music/v12/Track Scene 23_1.mp3" fadein 2

    scene v12msr2 # FPP. MC and Ms. Rose in the hallway, MC and Ms. Rose looking at each other, Ms. Rose slight smile, mouth open
    with dissolve

    ro "Hey, [name]. Haven't seen you in a while."

    scene v12msr2a # FPP. Same as v12msr2, Ms. Rose slight smile, mouth closed
    with dissolve

    u "I've been around..."

    if ms_rose.relationship >= Relationship.FWB:
        scene v12msr2d # FPP. Same as v12msr2, Ms. Rose, slight smile, mouth open, caressing MC's cheek
        with dissolve

        ro "Well you haven't been around me..."

        scene v12msr2
        with dissolve

        ro "I did my nightly walk around and everyone else is asleep or at least in their rooms."

        scene v12msr2c
        with dissolve

        u "It does feel like I haven't seen you in awhile."

        scene v12msr2b
        with dissolve

        if v11_underground_rose:
            ro "As I said before, I have something special planned for us here in Paris. Want me to show you?"
        else:
            ro "I have something special planned for us here in Paris. Want me to show you?"

        scene v12msr2a
        with dissolve

        menu:
            "Not tonight":
                scene v12msr2c
                with dissolve

                u "Sorry, but... Not tonight. I'm just gonna stay in and get some extra sleep. I'll try to have a more fun-filled day tomorrow, haha."

                scene v12msr2b
                with dissolve

                ro "Oh... That's too bad, but no worries. See you around."

                scene v12msr3
                with dissolve

                pause 0.75

                scene v12msr4
                with dissolve

                u "(I know what she had in mind.)"

                scene v12msr33
                with dissolve

                pause 0.75

                scene v12msr34
                with dissolve

                pause 0.75

            "Let's go":
                $ add_point(KCT.TROUBLEMAKER)
                
                $ sceneList.add("v12_rose")
                $ ms_rose.relationship = Relationship.FWB

                label v12_ms_rose_sex_sg:

                scene v12msr2c
                with dissolve

                u "Let's go."

                scene v12msr2
                with dissolve

                ro "*Chuckles* Follow me to the car."

                scene v12msr5 # TPP. Show MC and Ms. Rose walking in the hotel lobby, both smiling, mouths closed
                with dissolve

                pause 0.75

                scene v12msr6 # TPP. Show MC and Ms. Rose getting into the car (Ms. Rose driving), both smiling, mouths closed
                with dissolve

                pause 0.75

                scene v12msr7 # TPP. Car on road
                with dissolve

                pause 0.75

                scene v12msr8 # TPP. MC and Ms. Rose getting out of the car in front of the Paris Living Room asset, both smiling, mouths closed
                with fade

                pause 0.75

                scene v12msr9 # TPP. Show MC and Ms. Rose walking into the living room, both smiling, mouths closed
                with dissolve

                pause 0.75

                stop music fadeout 3
                play music "music/v12/Track Scene 23_2.mp3" fadein 2

                scene v12msr10 # FPP. MC and Ms. Rose in living room, looking at each other, Ms. Rose slight smile, mouth closed
                with dissolve

                u "This is a beautiful place, Lorraine... How'd you get it?"

                scene v12msr10a # FPP. Same as v12msr10, Ms. Rose slight smile, mouth open
                with dissolve

                ro "I rented it, just for us. I wanted to have a nice little escape of my own while we're here in Paris. Tonight though, there's something else I want all to myself."

                scene v12msr11 # TPP. Show Ms. Rose walking towards the black mantle that has a bottle of wine and 2 glasses, Ms. Rose smiling, mouth closed
                with dissolve

                pause 0.75

                scene v12msr12 # TPP. Show Ms. Rose pouring a glass of wine, Ms. Rose slight smile, mouth closed
                with dissolve

                pause 0.75

                scene v12msr10b # FPP. Same as v12msr10, Ms. Rose handing MC a glass of wine, Ms. Rose slight smile, mouth open, she has her glass in the other hand
                with dissolve

                ro "Here, try this wine."

                scene v12msr13 # TPP. Show MC taking a sip of his wine
                with dissolve

                pause 0.75

                scene v12msr10c # FPP. Same as v12msr10b, Ms. Rose drinking her wine
                with dissolve

                u "Mmm... This is the richest wine I've ever tasted. *Chuckles*"

                scene v12msr10d # FPP. Same as v12msr10c, Ms. Rose holding her glass, Ms. Rose slight smile, mouth open
                with dissolve

                ro "The best that Paris has to offer... It cost me a pretty penny."

                scene v12msr10e # FPP. Same as v12msr10d, Ms. Rose slight smile, mouth closed
                with dissolve

                u "And you decided to share?"

                scene v12msr10d
                with dissolve

                ro "Felt like the perfect time to open it. Now hurry up and drink it. *Chuckles*"

                scene v12msr10c
                with dissolve

                pause 0.75

                scene v12msr14 # TPP. Show Ms. Rose walking over to the mirror, MC following her, both smiling, mouths closed
                with dissolve

                pause 0.75

                scene v12msr15 # FPP. MC standing in front of Ms. Rose, she's in front of the mirror, MC watching as Ms. Rose removes her top, Ms. Rose seductive look, mouth closed
                with dissolve

                u "Good... Fucking... God."

                if config_censored:
                    call screen censoredPopup("v12s23_nsfwSkipLabel1")

                scene v12msr15a # FPP. Same as v12msr15, Ms. Rose topless, seductive look, mouth open
                with dissolve

                ro "Hmm? *Chuckles* Like what you see?"

                scene v12msr15b # FPP. Same as v12msr15a, Ms. Rose removing her skirt, seductive look, mouth closed
                with dissolve

                u "Like it? I lov-"

                scene v12msr15c # FPP. Same as v12msr15b, Ms. Rose pants off, seductive look, mouth open
                with dissolve

                ro "Then show me..."

                scene v12msr16 # TPP. Show Ms. Rose grabbing MC's head and pushing him down to his knees so he gives her oral, both smiling, mouths closed
                with dissolve

                pause

                scene v12msr17 # TPP. Show Ms. Rose still holding MC's head, MC ready to give her oral, both smiling, mouths closed
                with dissolve

                pause

                image v12rosso = Movie(play="images/v12/Scene 23/v12rosso.webm", loop=True, image="images/v12/Scene 23/v12rossoStart.webp", start_image="images/v12/Scene 23/v12rossoStart.webp") # Rose standing oral
                image v12rossof = Movie(play="images/v12/Scene 23/v12rossof.webm", loop=True, image="images/v12/Scene 23/v12rossoStart.webp", start_image="images/v12/Scene 23/v12rossoStart.webp") # Rose standing oral spedup
                image v12rosso2 = Movie(play="images/v12/Scene 23/v12rosso2.webm", loop=True, image="images/v12/Scene 23/v12rosso2Start.webp", start_image="images/v12/Scene 23/v12rosso2Start.webp") # Rose standing oral TPP 2
                image v12rosso2f = Movie(play="images/v12/Scene 23/v12rosso2f.webm", loop=True, image="images/v12/Scene 23/v12rosso2Start.webp", start_image="images/v12/Scene 23/v12rosso2Start.webp") # Rose standing oral TPP 2 spedup

                scene v12rosso # Ignore as animation
                with dissolve
                pause

                ro "That's a good fucking student. Yesss..."

                scene v12rossof # Ignore as animation
                with dissolve
                pause

                ro "Ahhh... Haha, definitely getting an A for this. Mmm..."

                scene v12rosso2 # Ignore as animation
                with dissolve

                ro "*Moans*"

                scene v12rosso2f # Ignore as animation
                with dissolve

                ro "Fuck!"

                scene v12msr18 # TPP. Show MC removing his shirt, standing up now, both smiling, mouths closed
                with dissolve

                pause
                
                scene v12msr19 # TPP. Show MC getting ready to fuck Ms. Rose in standing missionary, kissing her neck
                with dissolve

                pause

                image v12rossm = Movie(play="images/v12/Scene 23/v12rossm.webm", loop=True, image="images/v12/Scene 23/v12rossmStart.webp", start_image="images/v12/Scene 23/v12rossmStart.webp") # Rose standing missionary
                image v12rossmf = Movie(play="images/v12/Scene 23/v12rossmf.webm", loop=True, image="images/v12/Scene 23/v12rossmStart.webp", start_image="images/v12/Scene 23/v12rossmStart.webp") # Rose standing missionary spedup
                image v12rossm2 = Movie(play="images/v12/Scene 23/v12rossm2.webm", loop=True, image="images/v12/Scene 23/v12rossm2Start.webp", start_image="images/v12/Scene 23/v12rossm2Start.webp") # Rose standing missionary TPP 2
                image v12rossm2f = Movie(play="images/v12/Scene 23/v12rossm2f.webm", loop=True, image="images/v12/Scene 23/v12rossm2Start.webp", start_image="images/v12/Scene 23/v12rossm2Start.webp") # Rose standing missionary TPP 2 spedup

                scene v12rossm # Ignore as animation
                with dissolve
                pause

                ro "Someone's eager..."

                scene v12rossmf # Ignore as animation
                with dissolve
                pause

                u "Damn right I am, look at you..."

                scene v12rossm2 # Ignore as animation
                with dissolve
                pause

                ro "Fuck, [name]. I needed you so badly... You have no idea- Ah!"

                scene v12rossm2f # Ignore as animation
                with dissolve
                pause

                u "*Grunts*"

                scene v12msr20 # TPP. Show MC moving Ms. Rose to the back of the white sofa
                with dissolve

                pause

                scene v12msr21 # TPP. Show MC bending Ms. Rose over the back of the white sofa, ready to fuck her doggystyle
                with dissolve

                pause

                image v12rossd = Movie(play="images/v12/Scene 23/v12rossd.webm", loop=True, image="images/v12/Scene 23/v12rossdStart.webp", start_image="images/v12/Scene 23/v12rossdStart.webp") # Rose doggystyle
                image v12rossdf = Movie(play="images/v12/Scene 23/v12rossdf.webm", loop=True, image="images/v12/Scene 23/v12rossdStart.webp", start_image="images/v12/Scene 23/v12rossdStart.webp") # Rose doggystyle spedup
                image v12rossd2 = Movie(play="images/v12/Scene 23/v12rossd2.webm", loop=True, image="images/v12/Scene 23/v12rossd2Start.webp", start_image="images/v12/Scene 23/v12rossd2Start.webp") # Rose doggystyle FPP
                image v12rossd2f = Movie(play="images/v12/Scene 23/v12rossd2f.webm", loop=True, image="images/v12/Scene 23/v12rossd2Start.webp", start_image="images/v12/Scene 23/v12rossd2Start.webp") # Rose doggystyle FPP spedup


                scene v12rossd # Ignore as animation
                with dissolve
                pause

                ro "Ooo, yes baby... I love this!"

                scene v12rossdf # Ignore as animation
                with dissolve
                pause

                ro "F-f-fuckkkkk..."

                scene v12rossd2 # Ignore as animation
                with dissolve
                pause

                u "Ah ah ah... We're not anywhere near being finished."

                scene v12rossd2f # Ignore as animation
                with dissolve
                pause

                ro "*Moans* What are yo-"

                scene v12msr22 # TPP. Show MC grabbing Ms Rose's hands and holding them behind her back
                with dissolve

                pause

                image v12roshh = Movie(play="images/v12/Scene 23/v12roshh.webm", loop=True, image="images/v12/Scene 23/v12roshhStart.webp", start_image="images/v12/Scene 23/v12roshhStart.webp") # Rose hand doggy
                image v12roshhf = Movie(play="images/v12/Scene 23/v12roshhf.webm", loop=True, image="images/v12/Scene 23/v12roshhStart.webp", start_image="images/v12/Scene 23/v12roshhStart.webp") # Rose hand doggy spedup
                image v12roshh2 = Movie(play="images/v12/Scene 23/v12roshh2.webm", loop=True, image="images/v12/Scene 23/v12roshh2Start.webp", start_image="images/v12/Scene 23/v12roshh2Start.webp") # Rose hand doggy FPP
                image v12roshh2f = Movie(play="images/v12/Scene 23/v12roshh2f.webm", loop=True, image="images/v12/Scene 23/v12roshh2Start.webp", start_image="images/v12/Scene 23/v12roshh2Start.webp") # Rose hand doggy FPP spedup

                scene v12roshh # Ignore as animation
                with dissolve
                pause

                u "Fuck yes..."

                ro "I'm loving this... New side of you... [name]... Yes... Please! F-fuck..."

                scene v12roshhf # Ignore as animation 
                with dissolve
                pause

                u "You're... such... a fucking... slut!"

                ro "I... I-I am..."

                scene v12roshh2 # Ignore as animation
                with dissolve
                pause

                ro "Fuck me, [name]... Fast... I'm going to c-"

                ro "*Moans* Mmmnnhh... FUCK! *Gasps*"

                scene v12roshh2f # Ignore as animation
                with dissolve
                pause

                u "I'm... almost there! You're so... FUCKING... HOT!"

                ro "Do it inside, [name]! Fill me up... Please... I..."

                scene v12msr23 # TPP. Show MC cumming in Ms. Rose
                with vpunch

                pause

                scene v12msr24 # TPP. Closeup of Ms. Rose's pussy filled with cum
                with dissolve

                pause


                scene v12msr25 # TPP. Ms. Rose turns around, looking at MC, kissing him
                with dissolve

                pause
                
                scene v12msr26 # TPP. Show MC going to sit down on the couch, smiling, mouth closed
                with dissolve

                pause 0.75

                scene v12msr27 # FPP. MC sitting down on the couch, Ms. Rose standing in front of him, still naked, Ms. Rose smiling, mouth closed
                with dissolve

                u "(Ho... ly... shit)"

                u "I don't know where all that energy came from..."

                scene v12msr27a # FPP. Same as v12msr27, Ms. Rose smiling, mouth open
                with dissolve

                ro "*Chuckles* I told you tonight would be special."

                $ renpy.end_replay()

                scene v12msr28 # FPP. MC looks at the bottle of wine on the black mantle
                with dissolve

                pause 0.75

                scene v12msr27
                with dissolve

                u "Did you give me something?"

                scene v12msr27a
                with dissolve

                ro "Just a little boost..."

                scene v12msr27
                with dissolve

                u "That was more than a little. I felt like a damn bullet!"

                scene v12msr27a
                with dissolve

                ro "*Chuckles* You should be calming down any minute now..."

                scene v12msr27
                with dissolve

                u "*Drowsy* I am starting to feel a little... Slower..."

                scene v12msr27a
                with dissolve

                ro "Just relax, baby... I've got you."

                scene v12msr27b # FPP. Same as v12msr27, screen blurry
                with dissolve

                u "I'm feeling... really..."

                stop music fadeout 3
                play music "music/v12/Track Scene 23_3.mp3" fadein 2

                label v12s23_nsfwSkipLabel1:

                scene black
                with dissolve

                play sound "sounds/dooropen.mp3"

                pause

                scene black
                with dissolve

                play music "sounds/driving1.mp3" fadein 2

                pause

                stop music fadeout 3

                if not v11_riley_roomate:
                    scene v12msr29 # TPP. Chloe in front of MC and Ms. Rose, MC very drunk, Ms. Rose helping him stand up. Show Chloe looking at them, Chloe worried, mouth open (Only Chloe in shot)
                    with dissolve

                    cl "Oh my g- Is he okay?!"

                    scene v12msr30 # TPP. Same positioning as v12msr29, show Ms. Rose supporting MC, Ms. Rose slight smile, mouth open, looking at Chloe
                    with dissolve

                    ro "Yes, honey... He was just drunk downstairs. *Chuckles*"

                    scene v12msr29a # TPP. Same as v12msr29, Chloe slight smile, mouth open
                    with dissolve

                    cl "Oh... Not surprised. I got him. *Chuckles* Thank you, Ms. Rose."

                    scene v12msr30
                    with dissolve

                    ro "Of course."

                    scene v12msr31 # TPP. Show Chloe getting MC into bed, MC in his boxers
                    with dissolve

                    pause 0.75

                else:
                    scene v12msr29b # TPP. Same as v12msr29, instead of Chloe it's Riley, Riley worried, mouth open
                    with dissolve

                    ri "Oh my god, [name]! Is he hurt?!"

                    scene v12msr30
                    with dissolve

                    ro "No honey, just a little tipsy. *Chuckles*"

                    scene v12msr29c # TPP. Same as v12msr29b, Chloe slight smile, mouth open
                    with dissolve

                    ri "Wow, okay... I got him. Thank you so much, I'm sorry."

                    scene v12msr30
                    with dissolve

                    ro "No problem, really. You are on vacation after all... *Chuckles*"

                    scene v12msr31a # TPP. Same as v12msr31, Riley instead of Chloe
                    with dissolve

                    pause 0.75

    else:
        scene v12msr2
        with dissolve

        ro "Hmm, are you busy?"

        scene v12msr2a
        with dissolve

        u "No, not really."

        scene v12msr2
        with dissolve

        ro "How come? I'm sure there's plenty of things you and your friends could be doing."

        scene v12msr2a
        with dissolve

        u "There's just not much going on today I guess. I came out here to see what was up."

        scene v12msr2b # FPP. Same as v12msr2, different pose
        with dissolve

        ro "Well, sorry to disappoint you. But, it's already late and I've just finished walking my rounds around the hotel. Everyone is either asleep or at least in their rooms."

        scene v12msr2c # FPP. Same as v12msr2b, Ms. Rose slight smile, mouth closed
        with dissolve

        u "Oh. Well I guess I might as well just go back to my room too. *Chuckles*"

        scene v12msr2b
        with dissolve

        ro "*Chuckles* Alright, then. Be sure to make tomorrow a more fun-filled day."

        scene v12msr2c
        with dissolve

        u "Will do."

        scene v12msr2
        with dissolve

        ro "Have a good night, [name]."

        scene v12msr2a
        with dissolve

        u "You too."

        scene v12msr3 # TPP. Show Ms. Rose walking away from MC, Ms. Rose slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v12msr4 # TPP. Show MC walking into his room, slight smile, mouth closed
        with dissolve

        u "(And right back to my room.)"

        scene v12msr33 # TPP. Show MC removing his shirt in the room, MC slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v12msr34 # TPP. Show MC getting in bed, slight smile, mouth closed, in his boxers
        with dissolve

        pause 0.75

    scene v12msr32 # TPP. Show MC sleeping on his bed, in his boxers
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v12_simplr_convo #scene 24
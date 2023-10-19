# SCENE 36: Ryan and Imre grappling
# Location: Hotel corridor, Hotel Lobby, Road
# Characters: MC (Outfit 9), Mr Lee (Outfit 1). Ryan (Outfit 1), Imre (Outfit 1)
# Time: Morning

label v11_imre_ryan_grapple:
    scene v11irg1 # FPP. MC looking down the hallway, he can see Imre and Ryan grappling on the floor, both angry, mouths closed, show Mr Lee worried, mouth closed, running towards them
    with dissolve
    play music music.ck1.v10.Track_Scene_10 fadein 2
    pause 0.75

    scene v11irg1a # FPP. Same as v11irg1, Ryan and Imre still grappling on the floor (different pose to v11irg1), Mr Lee's hands on Imre's shoulders, Imre and Ryan angry, mouths closed, Mr Lee worried, mouth closed
    with dissolve

    pause 0.75

    scene v11irg1b # FPP. Same as v11irg1, Ryan and Imre still grappling on the floor (different pose to v11irg1a), Mr Lee trying to break them up, everyone angry, Mr Lee mouth open, Imre and Ryan mouths closed
    with dissolve

    lee "Have you two lost your minds? Behave yourselves!"

    scene v11irg1c # FPP. Same as v11irg1, Ryan and Imre still grappling on the floor (different pose to v11irg1b), Mr Lee trying to break them up (different pose to v11irg1b), everyone angry, mouths closed
    with dissolve

    menu:
        "Intervene":
            $ mr_lee.points += 1

            scene v11irg2 # TPP. Show MC grabbing Imre, Mr Lee grabbing Ryan, everyone angry, mouths closed
            with dissolve

            grant Achievement("dont_just_stand_there", "Break Imre and Ryan apart")
            pause 1.75

            scene v11irg3 # TPP. Show MC holding Imre back, Mr Lee in the middle of Imre and Ryan, Ryan and Imre standing and looking at each other, everyone angry, mouths closed
            with dissolve

            pause 1.25

        "Don't intervene":
            $ mr_lee.points -= 1

            scene v11irg1d # FPP. Same as v11irg1, Ryan and Imre still grappling on the floor (different pose to v11irg1c), Mr Lee trying to break them up (different pose to v11irg1c), everyone angry, Ryan and Imre mouths closed, Mr Lee looking at MC, Lee mouth open
            with dissolve

            lee "[name], are you really going to just stand there?"

            scene v11irg1e # FPP. Same as v11irg1d, Mr Lee looking at MC, angry, mouth closed
            with dissolve

            u "Sorry, I-"

            scene v11irg1f # FPP. Same as v11irg1, Ryan and Imre now standing and looking at each other, Mr Lee has pulled them apart from each other, standing in the middle, everyone angry, mouths closed
            with dissolve

            pause 0.75

    scene v11irg4 # FPP. Mr Lee standing between Imre and Ryan (they're faces are out of shot) Lee mouth open, very angry, looking at Ryan's direction
    with dissolve

    lee "That is enough! Are you two children?! Never would I have thought I'd be separating school yard fights on a college trip."

    scene v11irg5 # FPP. Same positioning as v11irg4, MC looking at Ryan, Ryan pointing and looking at Imre's direction, Ryan is very angry, mouth open (only Ryan in shot)
    with dissolve

    ry "You didn't hear what this smartass said to me!"

    scene v11irg6 # FPP. Same positioning as v11irg4, MC looking at Imre, Imre very angry, mouth open, looking at Ryan (only Imre in shot)
    with dissolve

    imre "I meant what I said, bro."

    scene v11irg3a # TPP. Same as v11irg3, Ryan reaching past Mr Lee, Ryan hitting Imre on the jaw, Imre startled, mouth closed, Ryan angry, mouth closed
    with dissolve

    play sound sound.hit

    pause 0.75

    scene v11irg7 # FPP. MC looking at Imre on the ground, holding his jaw, mouth closed, in pain and angry
    with vpunch

    play sound sound.fall

    pause 0.75

    scene v11irg4a # FPP. Same as v11irg4, Mr Lee grabbing Ryan by the collar, Mr Lee very angry, mouth open, Ryan startled, mouth closed
    with dissolve

    lee "DID YOU NOT HEAR ME?!"

    scene v11irg8 # FPP. Show Ryan on the ground, in pain, mouth closed
    with vpunch

    play sound sound.fall

    pause 0.75

    scene v11irg4b # FPP. Same cam as v11irg4, Imre and Ryan on the ground, out of shot, Mr Lee looking down at Imre, Mr Lee mouth open, very angry
    with dissolve

    lee "Clearly you are both deaf or incompetent. I can't even enjoy my breakfast and a morning coffee? Imre, what did you say to him?"

    scene v11irg7a # FPP. Same as v11irg7, Imre sitting on the ground, very angry, looking towards Ryan's direction (Ryan on the ground), Imre mouth open, very angry
    with dissolve

    imre "I said he was scrawny."

    scene v11irg4b
    with dissolve

    lee "What provoked you to say that?"

    scene v11irg7b # FPP. Same as v11irg7, Imre slight grin, mouth open
    with dissolve

    imre "Facts. *Chuckles*"

    scene v11irg8a # FPP. Same as v11irg8, Ryan sitting on the ground, very angry, looking towards Imre's direction, Ryan mouth open, very anrgy
    with dissolve

    ry "You said it to be an ass. And it's not even that, it's the way he said it. He walked past me and said \"Hey little scrawny bitch\" out of nowhere, for no reason."
    
    ry "I told him to leave me alone and that I didn't have time for his bullshit, then he said it again by mocking me so I knocked the shit out of him."

    scene v11irg7a
    with dissolve

    imre "You say it like you actually landed a hit."

    scene v11irg4b
    with dissolve

    lee "Is this some fraternity instigated altercation?"

    scene v11irg4c # FPP. Same as v11irg4, Mr Lee looking at MC now, Mr Lee angry, mouth closed
    with dissolve

    pause 0.75

    scene v11irg4d # FPP. Same as v11irg4, Mr Lee looking down at Ryan, Mr Lee mouth open, angry
    with dissolve

    lee "I believe I heard you say something about Imre smelling like a wet dog when we were at the airport, am I wrong or am I right, Ryan?"

    scene v11irg8a
    with dissolve

    ry "Yeah, but it was true so I don't see the problem."

    scene v11irg4c
    with dissolve

    u "Look, Mr. Lee. Can we just chalk this up to boys being boys?"

    scene v11irg4e # FPP. Same as v11irg4c, Mr Lee angry, mouth open
    with dissolve

    lee "You're right, boys will be boys, but men such as the three of you should not be acting like boys."

    scene v11irg4c
    with dissolve

    u "(\"Three of you...\", what did I do?)"

    scene v11irg4e
    with dissolve

    lee "Since you all want to act like children, I'll treat you like children. You three are coming with me this morning. I'll be waiting for you in the car, please don't be long."

    scene v11irg4f # FPP. Same as v11irg4, Show Mr Lee walking away, angry, mouth closed
    with dissolve

    pause 0.75

    scene v11irg9 # FPP. MC standing in front of Ryan and Imre, they're all standing up now, MC and Imre looking at each other, Imre mouth closed, angry
    with dissolve

    u "Look what you guys dragged me into."

    scene v11irg9a # FPP. Same as v11irg9, Imre angry, mouth open
    with dissolve

    imre "You got dragged into this when you decided to start being friends with that asshole."

    scene v11irg10 # FPP. Same positioning as v11irg9, MC looking at Ryan, Ryan looking at Imre's direction (Imre out of shot), Ryan slight grin, mouth open
    with dissolve

    ry "*Chuckles* I could say the same about you."

    scene v11irg9b # FPP. Same as v11irg9, Imre slightly sad, mouth closed
    with dissolve

    u "Outside of seeing Mr. Lee get angry like that, there's nothing funny about this. I literally got woken up to the sound of you guys yelling and now I'm being dragged to who knows where."

    scene v11irg9c # FPP. Same as v11irg9b, Imre slightly sad, mouth open
    with dissolve

    imre "Sorry dude."

    scene v11irg10a # FPP. Same as v11irg10, Ryan looking at MC, Ryan mouth open, slightly sad
    with dissolve

    ry "Sorry man."

    scene v11irg10b # FPP. Same as v11irg10a, Ryan slight smile, mouth closed
    with dissolve

    u "*Sighs* Don't worry about it. Maybe if we take too long he'll let it go. *Chuckles*"

    scene v11irg9d # FPP. Same as v11irg9c, Imre slight smile, mouth open
    with dissolve

    imre "That'd be nice, I'd rather go eat."

    scene v11irg11 # TPP. Same positioning as v11irg9, Ryan, MC and Imre looking down the hallway, all slightly startled, mouths closed
    with vpunch

    lee "I'M PRETTY SURE I SAID DON'T BE LONG!"

    scene v11irg9b
    with dissolve

    u "Never mind."

    scene v11irg12 # TPP. Show MC, Ryan and Imre walking down the hallway (show them from behind)
    with dissolve

    pause 0.75

    scene v11irg13 # TPP. Show Mr Lee at the lobby, looking as MC, Ryan and Imre approach, Mr Lee annoyed, mouth closed, camera is behind MC, Ryan and Imre
    with dissolve

    pause 0.75

    scene v11irg14 # FPP. MC standing in lobby, looking at Mr Lee, Mr Lee looking at MC, Lee mouth open, annoyed
    with dissolve

    lee "I want a quiet car ride, so try and get yourselves in a relaxing mood. Let's go."

    scene v11irg15 # TPP. Show Lee, Ryan, Imre and MC leaving the hotel lobby, everyone annoyed, mouths closed
    with dissolve

    pause 0.75

    scene v11irg16 # TPP. Show Mr Lee getting in the car, annoyed, mouth closed, Ryan, MC and Imre are out of the car, annoyed, mouth closed
    with dissolve

    pause 0.75
    
    scene v11irg17 # TPP. Show the car on the road
    with fade
    stop music fadeout 3
    jump v11_walk_park
# SCENE 16: Lauren Cuddling
# Locations: Lauren Hotel Room, Hotel Corridor
# Characters: LAUREN (Outfit: 4), MC (Outfit: 2)
# Time: Night

label v13s16:
    scene v13s16_1 # TPP. Show MC walking in corridor, slight smile, mouth closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 16.mp3" fadein 2

    scene v13s16_2 # TPP. Show MC entering Lauren's room, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s16_3 # FPP. Lauren laying on her bed, looking at MC, MC standing next to the door, Lauren smiling, mouth open
    with dissolve

    la "Yay! You're finally here. *Chuckles*"

    scene v13s16_3a # FPP. Same as v13s16_3, Lauren smiling, mouth closed
    with dissolve

    u "Ha, where's Amber?"

    scene v13s16_3
    with dissolve

    la "Not sure, but she said she's gonna be gone for the night."

    scene v13s16_3a
    with dissolve

    u "Well, perfect. *Chuckles*"

    scene v13s16_4 # TPP. Show MC walking over to Lauren's bed, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s16_5 # TPP. Show MC getting into bed with Lauren, she has her back turned to him, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v13s16_6 # TPP. Show MC and Lauren spooning, smiling, mouths closed
    with dissolve

    pause 0.75

    scene v13s16_7 # TPP. Close-up of Lauren, same positioning as v13s16_6, Lauren smiling, mouth open
    with dissolve

    la "We've come so far, [name]..."

    scene v13s16_7a # TPP. Same as v13s16_7, Lauren smiling, mouth open, head turned to try and look at MC
    with dissolve

    la "I still remember the cute boy that took me out on a little bench date."

    scene v13s16_7b # TPP. Same as v13s16_7a, Lauren smiling, mouth closed
    with dissolve

    u "You're the cute one. *Chuckles*"

    scene v13s16_7c # TPP. Same as v13s16_7, Lauren slightly worried, mouth open
    with dissolve

    la "I was actually kind of worried we wouldn't last this long..."

    scene v13s16_7d # TPP. Same as v13s16_7c, Lauren slightly worried, mouth closed
    with dissolve

    u "Huh? Why's that?"

    scene v13s16_7c
    with dissolve

    la "You just seemed like the kind of guy that entertains a lot of girls."

    scene v13s16_7d
    with dissolve

    u "(What gave that impression? *Chuckles*)"

    scene v13s16_7b
    with dissolve

    u "Look where I am right now. Since day one, I've wanted you."

    scene v13s16_7a
    with dissolve

    la "I'm glad we're so good right now..."

    scene v13s16_7c
    with dissolve

    la "But, what about the future? Is this a forever thing?"

    scene v13s16_7d
    with dissolve

    u "Is this something you've been thinking about recently?"

    scene v13s16_7c
    with dissolve

    la "A little bit. I guess."

    scene v13s16_7e # TPP. Same as v13s16_7a, Lauren slightly worried, mouth open
    with dissolve

    la "After watching what happened between Nora and Chris... I've just had a lot on my mind."

    scene v13s16_7f # TPP. Same as v13s16_7e, Lauren slightly worried, mouth closed
    with dissolve

    u "We won't be like them."

    scene v13s16_7e
    with dissolve

    la "So, you're in this for the long run?"

    scene v13s16_7f
    with dissolve

    menu:
        "Of course":
            $ v13s16_lauren_points += 1
            $ reputation.add_point(Reputations.BOYFRIEND)
            scene v13s16_7b
            with dissolve

            u "Of course I am, Lauren... I wouldn't be here if I wasn't, and you give me many reasons to be."

            play sound "sounds/kiss.mp3"
            scene v13s16_8 # TPP. Show MC and Lauren kissing
            with dissolve

            pause

        "One day at a time":
            scene v13s16_7b
            with dissolve

            u "Based on how things are right now, I'm confident in our relationship."

            scene v13s16_7f
            with dissolve

            u "But, I also believe it's smart to take things one day at a time."

    scene v13s16_7e
    with dissolve

    la "If we do last a long time, do you think you'll be able to put up with my family?"

    scene v13s16_7b
    with dissolve

    u "*Chuckles* Why wouldn't I?"

    scene v13s16_7a
    with dissolve

    la "Haha, well... You know, with them being super religious and everything?"

    scene v13s16_7b
    with dissolve

    menu:
        "I don't see why not":
            $ v13s16_lauren_points += 1
            $ reputation.add_point(Reputations.BOYFRIEND)
            scene v13s16_7f
            with dissolve
            u "I don't see why not. Even if it's just out of respect for you, I'd do what I had to do in order to get along."

        "Might be an issue":
            u "It might be an issue at some point, but who can say they get along with everyone?"

    scene v13s16_7
    with dissolve

    la "Well, I don't even know if I'll get along with my family. *Chuckles*"

    if v13s16_lauren_points == 2:
        scene v13s16_7a
        with dissolve

        la "We definitely have a lot in common, and that's certainly something that'll help ease my mind."

        scene v13s16_7b
        with dissolve

        u "I'm glad I could help. *Chuckles*"
    
    else:
        scene v13s16_7e
        with dissolve

        la "We have a few differences but... That doesn't mean anything. We can't be clones of each other, can we?"

        scene v13s16_7b
        with dissolve

        u "I wouldn't mind dating myself. *Chuckles*"

        scene v13s16_7
        with dissolve

        la "*Chuckles*"

    scene v13s16_7a
    with dissolve

    la "Well then, thank you for being here. Goodnight, [name]."

    scene v13s16_7b
    with dissolve

    u "Goodnight, babe."

    scene v13s16_7a
    with dissolve

    la "I love you."

    scene v13s16_7
    with dissolve

    menu:
        "I love you too":
            scene v13s16_7b
            with dissolve

            u "I love you too."

        "Kiss her head":
            play sound "sounds/kiss.mp3"
            scene v13s16_9 # TPP. Show MC kissing Lauren's head, Lauren smiling, mouth closed
            with dissolve

            pause 1.5

    scene v13s16_10 # TPP. Show MC moving to turn off the light next to the bed, smiling, mouth closed
    with dissolve

    pause 0.75

    scene v13s16_11 # TPP. Show MC removing his shirt, slight smile, mouth closed, room dark
    with dissolve

    pause 0.75

    scene v13s16_12 # TPP. Show MC and Lauren sleeping, spooning
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s17b
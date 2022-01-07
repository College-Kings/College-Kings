# SCENE 28: Emily in the gym lockerroom
# Locations: Gym Lockerroom
# Characters: EMILY (Outfit: 1), MC (Outfit: 2)
# Time: Morning

label v14s28:
    scene v14s28_1 # TPP. Show MC and Emily standing in the Gym Lockerroom (Same room as the Chloe Lockerroom sex scene.), Both nervous smile, mouth closed.
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 32.mp3" fadein 2

    if "v13_emily" in sceneList:
        scene v14s28_2f # FPP. Emily looking at MC, MC Looking at Emily, Emily worried smile, mouth open.
        with dissolve

        em "So... You and I have been on and off, and on and off..."

        em "Seems like you don't mind fucking me but when it comes to actually being a nice person or resurrecting our relationship, you're not for it."

        scene v14s28_2e # FPP. Same as v14s28_2, Emily worried smile, mouth closed.
        with dissolve

        u "I-"

        scene v14s28_2c
        with dissolve

        em "Please, let me finish."

        em "I've made mistakes, not just the cheating either."
        
        scene v14s28_2b
        with dissolve
        
        pause 0.01 #close and open mouth due to many dialogue lines
        
        scene v14s28_2c
        with dissolve

        em "I've made dozens of more mistakes since we've been in college, but regardless of that, I know how I feel and have always felt about you."

        em "I..."

        scene v14s28_2b
        with dissolve
        
        pause 0.01 #close and open mouth due to many dialogue lines
        
        scene v14s28_2c
        with dissolve

        em "I love you, [name]."

        em "Even if you don't feel the same way."

        scene v14s28_2b
        with dissolve
        
        pause 0.01 #close and open mouth due to many dialogue lines
        
        scene v14s28_2c
        with dissolve

        em "But deep down, of course... I hope that you still love me too."

        scene v14s28_2b
        with dissolve

        u "(Oh... Fuck...)"

        menu:
            "I love you too":
                $ add_point(KCT.BOYFRIEND)
                $ v14_emily_ily = True
                
                u "Emily..."

                u "I've had a hard time admitting to myself, let alone expressing to you, how I feel about you."

                u "We've had our bumps in the road but someway, somehow, we always get drawn right back to each other."

                u "That's what tells me that there's something between us, and it is meant to be."

                u "I love you too, Em."

                scene v14s28_2b # FPP. Same as v14s28_2a, Emily slight smile crying, mouth closed.
                with dissolve

                pause 0.75

                scene v14s28_2c # FPP. Same as v14s28_2b, Emily slight smile crying, mouth open.
                with dissolve

                em "Do you really mean that?"

                scene v14s28_2b
                with dissolve

                u "I do."

                scene v14s28_3 # TPP. Show Emily hugging MC tightly, both slight smile, Emily crying, both mouth closed.
                with dissolve

                pause 2

                scene v14s28_2c
                with dissolve

                em "You just made me the happiest I've ever been."

                em "God, I love you so much..."

                scene v14s28_2d # FPP. Same as v14s28_2c, Emily crying, MC wiping away her tears, Emily slight smile, mouth closed.
                with dissolve

                pause 0.75

            "It'll never work between us":
                $ add_point(KCT.TROUBLEMAKER)

                u "I'm not going to be rude or anything, but I have to be honest."

                u "I don't want to be in a relationship with you."

                scene v14s28_2e # FPP. Same as v14s28_2c, Emily looking at the ground, sad expression, mouth closed.
                with dissolve

                u "I feel like I've made that clear in the past few months, but in the event that I haven't, I will now."

                u "Considering you cheat on me, my friend is interested in you, and the fact that I've met other people..."

                u "I just really don't see us working out."

                scene v14s28_2f # FPP. Same as v14s28_2e, Emily looking at the ground, sad expression, mouth open.
                with dissolve

                em "*Sighs*"

                em "I knew that's what you were going to say. And honestly, I'm upset, but..."

                em "This is exactly why I'm doing what I'm doing."

    scene v14s28_2e
    with dissolve

    u "What's the news?"

    scene v14s28_2f
    with dissolve

    em "I've put a lot of thought into what I'm about to say..."

    em "I've talked it over with a lot of people, and I'm set in my decision."

    scene v14s28_2e
    with dissolve

    u "Okay..."

    scene v14s28_2c
    with dissolve

    em "I-I'm transferring schools."

    scene v14s28_2b
    with dissolve

    menu:
        "Stay calm":
            
            u "What? Emily... Why?"

        "Be angry":

            u "You're what? Why the fuck-"

            scene v14s28_2c
            with dissolve
            
            em "I don't want to argue. Please."

            scene v14s28_2b
            with dissolve
            
            u "*Sighs*"

    scene v14s28_2c
    with dissolve

    em "I need a fresh start, [name]."

    em "I came to this school with the wrong focus and it's led me to a bad place and messed up my best relationships."

    em "I need to just start over, I think."

    scene v14s28_2b
    with dissolve

    u "*Sighs*"

    u "This is a really big decision."

    scene v14s28_2c
    with dissolve

    em "You're telling me? *Chuckles*"

    scene v14s28_2b
    with dissolve

    u "You're sure about this?"

    scene v14s28_2c
    with dissolve

    em "Like I said, I'm set on my decision, I just..."

    em "I wanted to tell you in private."

    scene v14s28_2b
    with dissolve

    u "I wasn't aware that you were even considering this."

    scene v14s28_2c
    with dissolve

    em "I know I didn't consult you on what my plans were, and that's just because I wanted to make the decision with a clear head."

    scene v14s28_2b
    with dissolve

    u "I understand you wanting a fresh start, and I'm not gonna hold you back."

    u "Honestly, for you I feel like it's a great idea."

    scene v14s28_2c
    with dissolve

    em "Really?"

    scene v14s28_2b
    with dissolve

    u "I do, yeah. It'll be good for you to start fresh."

    scene v14s28_2c
    with dissolve

    em "I'm happy to hear you say that. *Chuckles*"

    scene v14s28_2b
    with dissolve

    u "Of course, when will you be leaving?"

    scene v14s28_2c
    with dissolve

    em "This weekend."

    scene v14s28_2b
    with dissolve

    u "That soon? Jeez..."

    scene v14s28_2c
    with dissolve

    em "Yeah, honestly... I wasn't even going to tell you. *Laughs* I was just going to leave."

    em "I told myself that if fate wanted you to know, we'd bump into each other. And well, here we are."

    scene v14s28_2b
    with dissolve

    u "Well, I'm glad you did."

    u "Regardless of our relationship, I would've been upset not knowing you'd left."

    scene v14s28_2c
    with dissolve

    em "In that case, I'm glad I told you."

    em "Now, I have a lot of packing and paperwork that needs to be handled, so I really need to get out of here."

    em "This may be the last time I see you for a while, ha. Can I get a hug?"

    scene v14s28_3a # TPP. Same as v14s28_3, Show MC and Emily giving eachother a casual hug, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    if v14_emily_ily:
        scene v14s28_2g # FPP. Same as v14s28_2f, Emily slight smile, mouth open.
        with dissolve

        em "If you want this relationship as much as you say you do, we'll be able to make this long distance thing work."

        em "This is real. So, I know we can."

        scene v14s28_2h # FPP. Emily kissing MC.
        with dissolve

        pause 1.5

        scene v14s28_4 # TPP. Show Emily and MC passionately kissing.
        with dissolve

        play sound "sounds/kiss.mp3"

        pause 2

        scene v14s28_2g
        with dissolve

        em "I love you, [name]."

        scene v14s28_2i # FPP. Same as v14s28_2g, Emily slight smile, mouth closed.
        with dissolve

        u "I love you too, Em."

        scene v14s28_2g
        with dissolve

        em "Bye."

        scene v14s28_2i
        with dissolve

        u "Bye."

        scene v14s28_5 # FPP. Show Emily walking away from MC and out of the Lockerroom.
        with dissolve

        pause 0.75
        
    else:
        scene v14s28_2g
        with dissolve

        em "For what it's worth, it was nice seeing you before I left."

        scene v14s28_2i
        with dissolve

        u "Yeah, you too."

        scene v14s28_2g
        with dissolve

        em "Bye [name]."

        scene v14s28_2i
        with dissolve

        u "Bye, Emily. Good luck."

        scene v14s28_5
        with dissolve

        pause 0.75

    scene v14s28_5a # FPP. Same as v14s28_5, MC looking at the empty Gym Lockerroom.
    with dissolve

    u "(Damn, she's actually gone...)"

    u "(After all our history, our ups and downs on campus... She's actually gone.)"

    if v14_emily_ily:
        u "(I'm sure I'll see her again, but still... It won't be the same around here.)"

    u "(I see why she wanted to talk in private now, I wonder who else she's told.)"

    scene v14s28_6 # TPP. Show MC walking out of the Gym Lockerroom, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s28_7 # TPP. Show MC walking outside, slight smile, mouth closed.
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s29
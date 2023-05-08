# SCENE 3 amendment: cafe with Riley and charli
# Locations: MC's room (apes and wolves), sidewalk, cafe
# Characters: MC (New outfit from scene 1), charli (outfit 1), riley (outfit 3)
# Time: Thursday afternoon

label v11_cafe_with_riley:
    play music music.ck1.v11.Track_Scene_3 fadein 2
    if joinwolves:
        scene v11s3bris1 # TPP. Show MC talking on his phone in his wolves bedroom, sat on the bed, mouth open
        with dissolve

        stop sound
        u "Hello?"

        scene v11s3bris2 # TPP. Show Riley sat in the café, phone to side of head, mouth open
        with dissolve

        ri "Hey [name], it's Riley. I'm over here at the cafe on Stevenson trying to clear my head about some things, and I thought it'd be nice to just talk to someone about it. Mind coming down?"

        scene v11s3bris1
        with dissolve

        u "No I don't mind at all, I'll be there soon."

        scene v11s3bris2
        with dissolve

        ri "Okay cool, thanks. See ya."

        scene v11s3bris1
        with dissolve

        u "Later, Riley."

    else:
        scene v11s3bris3 # TPP.Show MC talking on his phone in his apes bedroom, sat on the bed, mouth open
        with dissolve
        stop sound
        u "Hello?"

        scene v11s3bris2
        with dissolve

        ri "Hey [name], it's Riley. I'm over here at the cafe on Stevenson trying to clear my head about some things, and I thought it'd be nice to just talk to someone about it. Mind coming down?"

        scene v11s3bris3
        with dissolve

        u "No I don't mind at all, I'll be there soon."

        scene v11s3bris2
        with dissolve

        ri "Okay cool, thanks. See ya."

        scene v11s3bris3
        with dissolve

        u "Later, Riley."

    scene v11s3bris4 # TPP. Show MC walking walking along the sidewalk
    with dissolve

    pause 1

    scene v11s3bris5 # TPP. Show MC walking walking along the sidewalk (further along sidewalk)
    with dissolve

    pause 1

    scene v11s3bris6 # TPP. Show MC outside the cafe
    with dissolve

    pause 1

    scene v11s3bris7 # TPP. Show MC now walking inside the cafe
    with dissolve

    pause 1

    scene v11s3bris8 # FPP. Show riley sat at a table in the cafe, mouth closed, nervous smile,
    with dissolve

    u "Hey."

    scene v11s3bris8a # FPP. Same 8, mouth open
    with dissolve

    ri "Hey."

    scene v11s3bris9 # FPP. Show riley, mouth closed nervous smile (camera now as if mc is sat down in front of her)
    with dissolve

    u "So, how do you wanna do this? A little small talk first or just dive right in?"

    scene v11s3bris9a # FPP. same 9 mouth open
    with dissolve

    ri "Haha, I don't wanna keep you forever so I'll just say what's on my mind... I'm kinda nervous about the trip, actually."

    scene v11s3bris9
    with dissolve

    u "Why?"

    scene v11s3bris9a
    with dissolve

    ri "Wait, let me rephrase that... I'm kinda nervous about flying to Europe."

    scene v11s3bris9
    with dissolve

    u "What's got you so freaked out?"

    scene v11s3bris9b # FPP. Same 9, hand on face, worried look, mouth open
    with dissolve

    ri "I've never flown before and I don't know what to expect. Will I get sick? Are there going to be a lot of issues with the plane?"
    ri "I literally know nothing except for the things I've seen in movies. And in movies, there's no middle man. It's either the plane crashes or people are enjoying themselves in first class."
    ri "And although one of those would be nice, it won't be happening... So I really hope the plane doesn't crash."

    menu:
        "Scare her":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v11s3bris9
            with dissolve

            u "Well... Planes don't crash often, but there's usually a lot of turbulence which makes the plane shake pretty hard. That part is a little scary."
            u "It's mostly stable in first class, but in the regular area where we'll be, it can get kinda bad."

            scene v11s3bris9a
            with dissolve

            ri "That doesn't make me feel any better..."

            scene v11s3bris9c # FPP. Same 9, change pose a little so not stale. mouth closed
            with dissolve

            u "Haha, I'm just messing with you. It's really not that bad. You probably won't even notice we're moving."

            scene v11s3bris9d # FPP. Same 9a, change pose a little so not stale. mouth open
            with dissolve

            ri "Amber also said the turbulence makes the plane shake a lot... Now I feel like you're just trying to make me feel better by hiding the truth."

            scene v11s3bris9c
            with dissolve

            u "*Laughs* Well, the truth is I was trying to scare you with something that would be believable. Sounds like Amber had the same idea."
            u "Just download some movies on your phone to watch and for most of it, you'll probably be asleep anyway... You really have nothing to worry about."
            u "I'm pretty sure Imre is scared of heights, but he has no problem with the plane."

        "Reassure her":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v11s3bris9c
            with dissolve
            u "*Chuckles* If you need someone to hold your hand for the whole flight I will, but you really have nothing to worry about."
            u "I've been on multiple planes and know many others that have flown, and we've never had any problems. I just watch movies and sleep the whole time."

            scene v11s3bris9d
            with dissolve

            ri "Be really honest though, what's the worst thing about it?"

            scene v11s3bris9c
            with dissolve

            u "Well, the elevation messes with your ears a bit. Kinda feels like you're underwater. You get rid of it by yawning, but your ears sort of pop. For myself and most people that's the worst part."

            scene v11s3bris9d
            with dissolve

            ri "Your ears pop?! Does it hurt?"

            scene v11s3bris9
            with dissolve

            u "Haha, no Riley, it doesn't hurt. It's just an unusual feeling. I'm sure you've popped your knuckles before. It's like that but with your ear."

            scene v11s3bris9a
            with dissolve

            ri "Okay, I guess that doesn't seem so bad."

            scene v11s3bris9
            with dissolve

            u "See? Nothing to stress over."

    scene v11s3bris9a
    with dissolve

    ri "Alright, I guess I shouldn't worry about it. I am gonna talk to Amber though because I know she tried to scare me with her \"make sure you tuck your feet under the seat so you don't fall out\". *Chuckles*"

    scene v11s3bris9
    with dissolve

    u "*Laughs* Yeah, talking to Amber about your fears probably wasn't a good idea. If I had never flown before and talked to Amber before my first time, I'd be nervous too. She has that kind of power."

    scene v11s3bris9a
    with dissolve

    ri "We should call her Maleficent... *Chuckles*"

    scene v11s3bris9
    with dissolve

    u "What's maleficent?"

    scene v11s3bris9d
    with dissolve

    ri "Oh my god, look it up later."

    scene v11s3bris9e # FPP. Same 9, smiling mouth closed
    with dissolve

    u "*Chuckles* Okay? Hey, I know a way you could get over your fear of flying pretty easily."

    scene v11s3bris9f # FPP. same 9, smiling mouth open
    with dissolve

    ri "Really? How?"

    scene v11s3bris9e
    with dissolve

    u "You should try out that little indoor skydiving thing."

    scene v11s3bris9f
    with dissolve

    ri "What?"

    scene v11s3bris9e
    with dissolve

    u "You know, the thing with the giant air tube that lets you float?"

    scene v11s3bris9f
    with dissolve

    ri "Oh, right! I saw a commercial about that, I did think it kinda looked fun."

    scene v11s3bris9e
    with dissolve

    u "Well, it's safe and probably more stressful than an actual plane ride."

    scene v11s3bris9f
    with dissolve

    ri "Maybe less stressful for you. *Laughs*"

    scene v11s3bris10 # FPP. Show Charli approching the table
    with dissolve

    pause 1 

    scene v11s3bris10a # FPP. same 10, Show charlie now at the table, mouth open
    with dissolve

    charli "Hey [name]! Is this one of the close friends you were telling me about? I love your hair! Is that color natural?"

    scene v11s3bris9g # FPP. same 9, Show riley, smiling, mouth open, looking towards Charli
    with dissolve

    ri "Oh, thank you so much! I'm Riley. And yeah, haha. it's natural... You're a friend of [name]?"

    scene v11s3bris10b # FPP. same10a, looking at riley mouth open, slight smile
    with dissolve

    charli "Yea- well... I don't know, actually. *Chuckles* Would you say we're friends [name]?"

    menu:
        "Not yet":
            scene v11s3bris10c # FPP. same 10a, mouth closed
            with dissolve
            
            u "Haha, maybe not yet, I mean we just met this morning..."

        "Of course":
            $ reputation.add_point(RepComponent.BRO)
            scene v11s3bris10c
            with dissolve
            
            u "Sure, of course. Charli and I actually just met this morning."

    scene v11s3bris9g
    with dissolve

    ri "Well, it's nice to meet you, Charli. Love your energy, so positive."

    scene v11s3bris10b
    with dissolve

    charli "It's my pleasure, really. I was just telling [name] that I needed to find some friends on campus and here you are. *Chuckles*"

    scene v11s3bris9g
    with dissolve

    ri "Haha, yes. Here I am. *Chuckles*"

    scene v11s3bris9e
    with dissolve

    u "Charli here is actually going on the Europe trip with us."

    scene v11s3bris9f
    with dissolve

    ri "Oh yayyy! Now I won't be stuck with just [name]. *Chuckles*"

    scene v11s3bris9e
    with dissolve

    u "Wowww... *Chuckles*"

    scene v11s3bris10a
    with dissolve

    charli "[name] you must be one hell of a guy considering you're surrounded by all these amazing people..."

    scene v11s3bris9f
    with dissolve

    ri "\"Amazing\"? Definitely not. *Chuckles*"

    scene v11s3bris9e
    with dissolve

    u "(\"Amazing\"...)"

    scene v11s3bris9g 
    with dissolve

    ri "How come I've never bumped into you before?"

    scene v11s3bris10b
    with dissolve

    charli "I'm actually an exchange student and I currently stay off campus. But honestly I would have made more of an effort to meet people on campus if I had known you guys were here. *Chuckles*"

    scene v11s3bris9g 
    with dissolve

    ri "Ahh... that would explain a lot... Well, I'm really glad you're going on the trip with us. That'll give us the perfect chance to get to know each other."

    scene v11s3bris10b
    with dissolve

    charli "I'm looking forward to it! I actually wasn't going to go, but [name] convinced me."

    scene v11s3bris9f
    with dissolve

    ri "Well in that case, thank you [name]! *Chuckles*"

    scene v11s3bris10a
    with dissolve

    charli "I should finish getting ready for the long flight tomorrow. See you guys!"

    scene v11s3bris10d # FPP. same 10, show charli leaving
    with dissolve

    u "Later man."

    scene v11s3bris9e
    with dissolve

    u "Someone found a new best friend."

    scene v11s3bris9f
    with dissolve

    ri "Oh don't say it like that, he's sweet. Maybe girls would call you sweet too if you paid them a compliment every once in a while."

    scene v11s3bris9e
    with dissolve

    u "I do give compliments!"

    scene v11s3bris9f
    with dissolve

    ri "Haha, relax! I'm just teasing you... Is someone jealous of the new kid? *Laughs*"

    scene v11s3bris9e
    with dissolve

    u "I'm not jealous, just surprised to see you hit it off like that."

    scene v11s3bris9f
    with dissolve

    ri "Maybe I thought he was cute?"

    scene v11s3bris9e
    with dissolve

    u "Did you?"

    scene v11s3bris9f
    with dissolve

    ri "*Laughs* I'm gonna get on out of here. And now that I think about it, flying is the last thing on my mind, so thank you."

    scene v11s3bris9e
    with dissolve

    u "You're welcome. See you around, Riley."

    scene v11s3bris9f
    with dissolve

    ri "See ya."

    scene v11s3bris11 # FPP. Show Riley leaving the cafe
    with dissolve

    u "(I'm not jealous, I just... I don't know. )"
    stop music fadeout 3

    jump v11_emily_park
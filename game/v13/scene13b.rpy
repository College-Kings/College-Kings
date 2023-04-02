# SCENE 13b: Backstage with Penelope
# Locations: Backstage
# Characters: MC (Outfit: 2), PENELOPE (Outfit: 3)
# Time: Wednesday night

label v13s13b:
    $ v13_concert_backstage = True

    if v12_murder_count == v12s7_victims: # DON'T KNOW NUMBER FOR ALL KILLS; CHANGE TO CORRECT NUMBER
        $ v13_after_party = True

    scene v13s13b_1 # TPP Show MC and Penelope sitting backstage, Polly walking into the room, not looking at MC or Penelope
    with fade

    pause 0.75

    play music "music/v13/Track Scene 13a_1.mp3" fadein 2

    scene v13s13b_2 # FPP Show Polly sitting down near MC and Penelope but not looking their way, Polly looking tired with mouth open
    with dissolve

    polly "*Sighs* Whew! I'm so exhausted..."

    scene v13s13b_2a # FPP Same as 2, Polly sitting, looking very tired, mouth closed
    with dissolve

    u "*Chuckles*"

    scene v13s13b_2b # FPP Same as 2, Polly looking at MC and Penelope, now smiling, mouth open
    with dissolve

    polly "Oh, hey! I didn't even see you two there, haha. What's up, Polly 2.0?"

    scene v13s13b_3 # FPP Show Penelope, looking toward Polly, looking confused with mouth open
    with dissolve

    pe "Huh?"

    scene v13s13b_2b
    with dissolve

    polly "*Chuckles* You're a shy one aren't you? You didn't seem shy when you were singing all my lyrics, though. You knew the songs word for word."

    scene v13s13b_3a # FPP Same as 3, Penelope looking embarassed, mouth open
    with dissolve

    pe "Oh, umm... Yeah. Ha, I like your songs a lot."

    scene v13s13b_2b
    with dissolve

    polly "Girl, loosen up! Why are you so tense?"

    scene v13s13b_3a
    with dissolve

    pe "This is just a little bit... out of my element."
    pe "Like, please don't get me wrong, I love you. I'm just really nervous... *Chuckles*"

    scene v13s13b_2b
    with dissolve

    polly "Haha, well... There's no reason to be nervous. Are you two the only ones back here?"

    scene v13s13b_2c # FPP Same as 2, Polly looking at MC and Penelope, smiling with mouth closed
    with dissolve

    u "Seems so. We've been back here for a minute and I haven't seen a soul."

    scene v13s13b_2b
    with dissolve

    polly "Good..."

    scene v13s13b_2c
    with dissolve

    u "Ha, why is that good?"

    scene v13s13b_2d # FPP Same as 2, Polly looking at Penelope and leaning toward her, Polly smiling with mouth open
    with dissolve

    polly "Because I get to spend more time with my new friend here? Duh! *Chuckles*"

    scene v13s13b_3
    with dissolve

    pe "Me!?"

    scene v13s13b_2d
    with dissolve

    polly "*Laughs* Yes... How could I not be friends with someone who knows my songs as well as you do? What's your name, bestie?"

    scene v13s13b_3a
    with dissolve

    pe "It's Penelope."

    scene v13s13b_2e # FPP Same as 2, Polly looking at Penelope, Polly looks shocked, mouth open
    with dissolve

    polly "No fucking way... You're joking!"

    scene v13s13b_2f # FPP Same angle and expression as 2e, Polly's mouth closed
    with dissolve

    u "Nope, she's being serious. *Chuckles*"

    scene v13s13b_2e
    with dissolve

    polly "Penelope is my real name! Like, I'm not even joking!"

    scene v13s13b_3b # FPP Same as 3, Penelope looking at Polly with shocked expression, mouth open
    with dissolve

    pe "*Shocked* Oh my gosh!"

    scene v13s13b_2d
    with dissolve

    polly "Guess I really did find my twin. No wonder you can sing all my songs! *Chuckles* Sing the star track."

    scene v13s13b_3
    with dissolve

    pe "Now?"

    scene v13s13b_2d
    with dissolve

    polly "Ha, yeah."

    scene v13s13b_3a
    with dissolve

    pe "*Whisper* Okay, uhm... *Singing* Love comes unexpected-"

    scene v13s13b_2d
    with dissolve

    polly "Girl, c'mon, that ain't singing! Put some soul into it."

    scene v13s13b_3c # FPP Same as 3, Penelope looking at Polly, embarrassed, mouth closed, biting her lower lip
    with dissolve

    menu:
        "Encourage her":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ penelope.points += 1

            u "C'mon Penelope, you got this."

            scene v13s13b_4 # FPP Show MC taking Penelope's hand
            with dissolve

            pause 0.75

            scene v13s13b_3d # FPP Same angle as 3, Penelope looking at MC, smiling with mouth closed
            with dissolve

            pause 0.75

            scene v13s13b_3e # FPP Same angle as 3, Penelope looking up and away with eyes closed, mouth wide open, singing loudly
            with dissolve

            pe "*Singing* LOVE COMES UNEXPECTED, LOVE'S UNNATURAL! I CAN FEEL MY HEARTBEAT, LOVE IS LIKE BATTERY, IT POWERS UP MY SOUL!"

            scene v13s13b_2g # FPP Same angle as 2, Polly fist-pumping in excitement, looking at Penelope with a big smile, mouth open
            with dissolve

            polly "Yeah! That's my sister!"

        "Leave her alone":
            u "(I don't want to make it more embarrassing for her.)"

            scene v13s13b_3a
            with dissolve

            pe "I... I-"

            scene v13s13b_2d
            with dissolve

            polly "Ahh, don't worry about it sis. Maybe I'm the more extroverted twin. *Chuckles*"

            scene v13s13b_3f # FPP Same angle as 3, Penelope looking at Polly, smiling with mouth open
            with dissolve

            pe "*Chuckles*"

    # -Regardless of choice scene continued
    scene v13s13b_2b
    with dissolve

    polly "So, have you guys seen my album covers before?"

    scene v13s13b_3f
    with dissolve

    pe "Yes, I actually wanted to ask you about them! I never understand them... *Chuckles*"

    scene v13s13b_2d
    with dissolve

    polly "That's what I'm always going for. *Laughs*"

    scene v13s13b_2h # FPP Same angle as 2, Polly mouth open, making a smiling shrug expression like: https://images.app.goo.gl/RRHGHozyq7H7JhgX7
    with dissolve

    polly "I take a random picture of something that inspires me and boom, that becomes my cover."

    scene v13s13b_3f
    with dissolve

    pe "That's extremely creative."

    scene v13s13b_2d
    with dissolve

    polly "Thanks! I bring it up because when I saw you being lifted up by your friend here, I felt like that was the most beautiful showing of friendship I've ever seen."

    scene v13s13b_2b
    with dissolve

    polly "I was wondering if you guys would be willing to take a picture? Maybe I could use it in the future, haha."

    scene v13s13b_3a
    with dissolve

    pe "Oh umm..."

    scene v13s13b_99 # FPP Same angle as 3, Penelope looking at MC, curious and embarrassed, mouth closed
    with dissolve

    u "I don't see why not."

    scene v13s13b_2i # FPP Same angle as 2, Polly leaning forward in excitement, holding her phone
    with dissolve

    polly "Oh my god, yes! Alright, get together..."

    scene v13s13b_5 # TPP Polly's view, Penelope wrapping her arms around MC and smiling at Polly
    with dissolve

    polly "Ooo, okay! You guys are such a cute couple, I can't get enough."

    scene v13s13b_2j # FPP Same angle as 2, Polly holding her phone like a camera, mouth closed
    with dissolve

    menu:
        "We're not a couple":
            u "We're not really a couple, but thanks. *Chuckles*"

            scene v13s13b_2k # FPP Same as 2j, Polly with phone, smiling, mouth open
            with dissolve

            polly "Could've fooled me."

        "Thanks":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            u "Haha, thanks."

            scene v13s13b_5a # TPP Same angle as 5, Penelope kissing MC on the cheek
            with dissolve
            play sound "sounds/kiss.mp3"

            polly "Too cute!"

    # -Regardless of choice scene continued
    scene v13s13b_5
    with dissolve

    polly "Smile big!"

    play sound "sounds/capture.mp3"
    scene v13s13b_5
    with flash

    pause

    scene v13s13b_2l # FPP Same angle as 2, Polly looking at her phone, smiling with mouth open
    with dissolve

    polly "AMAZING! Definitely gonna find you guys and send you a signed copy."

    scene v13s13b_3g # FPP Same angle as 3, Penelope looking at Polly, smiling with mouth open
    with dissolve

    pe "I'd love that! Thank you so much..."

    scene v13s13b_2c
    with dissolve

    u "When's your birthday, Polly?"

    scene v13s13b_2m # FPP Same angle as 2, Polly looking at MC with a curious expression, mouth open
    with dissolve

    polly "January 1st, why?"

    scene v13s13b_3b
    with dissolve

    pe "*Shocked*"

    scene v13s13b_2d
    with dissolve

    polly "*Chuckles* What?"

    scene v13s13b_3b
    with dissolve

    pe "That... That's my birthday, too."

    scene v13s13b_2e
    with dissolve

    polly "Get. Out. There's no way..."

    scene v13s13b_2f
    with dissolve

    u "This is kinda freaky."

    scene v13s13b_2e
    with dissolve

    polly "Haha! Yeah, we're gonna have to get to the bottom of this..."

    scene v13s13b_2h
    with dissolve

    polly "Maybe our families knew each other or something? *Chuckles*"

    scene v13s13b_3g
    with dissolve

    pe "Maybe. *Laughs*"

    scene v13s13b_2b
    with dissolve

    polly "So... Are you guys into nightclubs?"

    scene v13s13b_2c
    with dissolve

    menu:
        "Not exactly":
            u "Not exactly... Usually spend time at bars, haha."

            scene v13s13b_2b
            with dissolve

            polly "Oh, okay. Gotcha..."

        "Hell yeah!":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ v13_after_party = True

            u "Hell yeah! Who doesn't love a good nightclub?"

            scene v13s13b_2b
            with dissolve

            polly "Perfect. I'm going to an after party, and you guys should come."

            scene v13s13b_3a
            with dissolve

            pe "That sounds... fun."

            scene v13s13b_3c
            with dissolve

            u "*Chuckles*"

            scene v13s13b_2b
            with dissolve

            polly "Haha, good!"

    # -Regardless of choice scene continued

    scene v13s13b_6 # FPP Show Polly standing up, looking at Penelope and MC, smiling with mouth open
    with dissolve

    polly "Well, I gotta get headed over to the party right now."

    scene v13s13b_7 # FPP Show MC and Penelope standing up, looking at Polly
    with dissolve

    pause 0.75

    if v13_after_party: # -If have after party tickets or got invited
        scene v13s13b_8 # FPP Show Polly, standing, looking at MC and Penelope, smiling with mouth closed
        with dissolve

        u "Lead the way."

        scene v13s13b_8a # FPP Same as 8, Polly smiling with mouth open
        with dissolve

        polly "Haha, let's hop in my little escape car."

        scene v13s13b_9 # FPP Show Penelope, now standing, looking at Polly and chuckling
        with dissolve

        pe "*Chuckles*"

        scene v13s13b_10 # TPP Show MC and Penelope following Polly to a small car
        with dissolve

        pause 0.5

        scene v13s13b_11 # TPP Show car, with Polly, MC, and Penelope, pulling up in front of club
        with dissolve

        pause 0.5

        scene v13s13b_12 # TPP Show Polly walking into club, MC and Penelope close behind
        with dissolve

        pause 0.5

        stop music fadeout 3

        jump v13s14b

    else: # -If don't have after party access or not invited
        scene v13s13b_8
        with dissolve

        u "Guess that's our cue to get home."

        scene v13s13b_9a # FPP Same as 9, Penelope smiling at Polly, mouth open
        with dissolve

        pe "It was beyond my expectations, meeting you. If we hadn't already met before... *Chuckles*"

        scene v13s13b_8a
        with dissolve

        polly "You beat me to it."

        scene v13s13b_13 # FPP Show Polly giving Penelope a friendly hug
        with dissolve

        pause 0.75

        scene v13s13b_8
        with dissolve

        u "See you around!"

        scene v13s13b_8a
        with dissolve

        polly "See you guys! Thanks again for coming tonight."

        scene v13s13b_14 # TPP Show MC and Penelope leaving the backstage area
        with dissolve

        pause 0.5

        stop music fadeout 3
        play music "music/v13/Track Scene 12a_2.mp3" fadein 2

        scene v13s13b_15 # TPP Show MC and Penelope getting into a cab
        with dissolve

        pause 0.5

        scene v13s13b_16 # TPP Show MC and Penelope entering hotel lobby through the front door
        with dissolve

        pause 0.5

        scene v13s13b_17 # FPP Show Penelope, in hotel lobby, smiling with mouth open
        with dissolve

        stop music fadeout 3
        play music "music/v13/Track Scene 12a_1.mp3" fadein 2

        pe "Jeez... I didn't know Polly and I had so much in common... *Chuckles*"

        scene v13s13b_17a # FPP Same as 19, Penelope's mouth closed
        with dissolve

        u "It was interesting... Freakishly interesting."

        scene v13s13b_18 # TPP Show Penelope giving MC and big hug, Penelope smiling with mouth open
        with dissolve

        pe "*Chuckles* You really gave me a night to remember, thank you."

        scene v13s13b_17a
        with dissolve

        u "Of course."

        scene v13s13b_17
        with dissolve

        pe "I need to go call my family and get some answers... *Chuckles* Goodnight, [name]."

        scene v13s13b_17a
        with dissolve

        u "Goodnight, P."

        scene v13s13b_19 # TPP Show MC about to enter his room
        with dissolve

        pause 0.75

        stop music fadeout 3

        if v11_riley_roomate:
            jump v13s15a

        else:
            jump v13s15
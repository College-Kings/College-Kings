# SCENE 13a: Backstage with Aubrey
# Locations: Backstage
# Characters: MC (Outfit: 2), AUBREY (Outfit: 1)
# Time: Wednesday Night

label v13s13a:
    $ v13_concert_backstage = True

    if v12_murder_count == v12s7_victims: # DON'T KNOW NUMBER FOR ALL KILLS; CHANGE TO CORRECT NUMBER
        $ v13_after_party = True

    scene v13s13a_1 # TPP Show MC and Aubrey sitting backstage, Polly walking into the room, not looking at MC or Aubrey
    with fade

    pause 0.75

    play music "music/v13/Track Scene 13a_1.mp3" fadein 2

    scene v13s13a_2 # FPP Show Polly sitting down near MC and Aubrey but not looking their way, Polly looking tired with mouth open
    with dissolve

    polly "*Sighs* Whew! I'm exhausted..."

    scene v13s13a_2a # FPP Same as 2, Polly sitting, looking very tired, mouth closed
    with dissolve

    u "*Chuckles*"

    scene v13s13a_2b # FPP Same as 2, Polly looking at MC and Aubrey, now smiling, mouth open
    with dissolve

    polly "Oh! I didn't even see you two there... Hey, hey, picture girl. *Chuckles*"

    scene v13s13a_3 # FPP Show Aubrey, looking toward Polly, smiling with mouth open
    with dissolve

    au "Haha, hey."

    scene v13s13a_2b
    with dissolve

    polly "You two are the only people with backstage access tonight?"

    scene v13s13a_2c # FPP Same as 2, Polly looking at MC and Aubrey, smiling with mouth closed
    with dissolve

    u "I guess so, we've been sitting here for a minute and no one else has come so far."

    scene v13s13a_2b
    with dissolve

    polly "*Sighs* Good..."

    scene v13s13a_3
    with dissolve

    au "Why is that good? *Chuckles*"

    scene v13s13a_2b
    with dissolve

    polly "'Cause that means I don't have to try and impress a ton of people I don't care about... *Laughs* You guys are cool."

    scene v13s13a_2c
    with dissolve

    u "(This pop star just called us cool?)"

    scene v13s13a_2d # FPP Same as 2, Polly looking at Aubrey, Polly looks shocked or surprised, mouth open
    with dissolve

    polly "Wait... A... Flipping... Minute! Aubrey!?"

    scene v13s13a_3a # FPP Same as 3, Aubrey looking confused, mouth open
    with dissolve

    au "Y-Yes... That's my name, how do you know me?"

    scene v13s13a_2e # FPP Same as 2, Polly looking at Aubrey, Polly leaning forward and smiling in excitement, mouth open
    with dissolve

    polly "How do I know you? *Laughs* How could I not?"
    polly "You're the new model that's working with Lew's, right? I saw your Paris shoot, and that shit was amazing!"

    scene v13s13a_3
    with dissolve

    au "Wait, you saw my work!?"

    scene v13s13a_2e
    with dissolve

    polly "Why are you acting surprised? *Chuckles*"

    scene v13s13a_3
    with dissolve

    au "Because that was my first shoot, like ever. If you recognized my sister Naomi then that'd make sense, haha."

    scene v13s13a_2f # FPP Same as 2, Polly looking like she just tasted something bad, mouth open
    with dissolve

    polly "Ewww, ugh... I'm sorry, but..."
    polly "I can't stand your sister. She thinks she's way better than she actually is."

    scene v13s13a_2g # FPP Same angle and expression as 2f, mouth closed
    with dissolve

    menu:
        "Defend her sister":
            u "Oh, come on... She's not that bad."

            scene v13s13a_2b
            with dissolve

            polly "She's not that good either. *Chuckles*"

        "Laugh":
            $ aubrey.points += 1
            u "*Laughs*"

            scene v13s13a_2e
            with dissolve

            polly "See! *Chuckles* I'm not the only one that thinks that..."

    # -Regardless of choice scene continued
    scene v13s13a_3
    with dissolve

    au "My sister definitely has a blunt way of doing things, ha."

    scene v13s13a_2f
    with dissolve

    polly "That's an understatement. But who cares, forget about your sister."

    scene v13s13a_2e
    with dissolve

    polly "Based on what I saw, you're gonna be the Next. Big. Thing. Your first gig is international work in Paris... C'mon now. *Laughs*"

    scene v13s13a_3b # FPP Same angle as 3, Aubrey looking at MC, smiling with mouth open
    with dissolve

    au "I've been trying to tell this goofball here that he better be nice to me or I'm gonna end up forgetting him when I'm famous."

    scene v13s13a_3c # FPP Same as 3b, Aubrey looking at MC and grinning, mouth closed
    with dissolve

    u "*Chuckles* What?"

    scene v13s13a_2b
    with dissolve

    polly "That's the type of energy I like to see. I like you."

    scene v13s13a_2c
    with dissolve

    u "She likes you too."

    scene v13s13a_3d # FPP Same as 3, Aubrey looking at MC, looking shocked, mouth open
    with dissolve

    au "[name]!"

    scene v13s13a_3e # FPP Same angle and expression as 3d, Aubrey's mouth closed
    with dissolve

    u "What? It's true! *Chuckles*"

    scene v13s13a_2b
    with dissolve

    polly "What? *Chuckles* Are you ashamed of liking me now?"

    scene v13s13a_3f # FPP Same as 3, Aubrey looking at Polly with annoyed expression, mouth open
    with dissolve

    au "Not at all. It's just, I know him, and he's talking about a little more than just liking you as an artist."

    scene v13s13a_2b
    with dissolve

    polly "Haha, well sadly... I don't swing that way, but if I did..."

    scene v13s13a_2h # FPP Same angle as 2, Polly winking at Aubrey
    with dissolve

    pause 0.75

    scene v13s13a_3
    with dissolve
    
    au "Haha, thank you."

    scene v13s13a_2b
    with dissolve

    polly "It's [name], right?"

    scene v13s13a_2c
    with dissolve

    u "Yeah."

    scene v13s13a_2b
    with dissolve

    polly "Mind taking a picture of me and the star?"

    scene v13s13a_2c
    with dissolve

    u "Haha, sure."

    scene v13s13a_4 # TPP Show MC taking Polly's phone from her while Aubrey moves to sit by Polly
    with dissolve

    pause 0.75

    scene v13s13a_5 # FPP Show MC's view of Camera app on Polly's phone, framing Polly and Aubrey in shot
    with dissolve

    u "Say cheese!"

    scene v13s13a_5a # FPP Same as 5, Aubrey and Polly smiling very broadly, saying "cheese"
    with dissolve

    au "CHEESE!"
    polly "CHEESE!"

    play sound "sounds/capture.mp3"
    scene v13s13a_5b
    with flash

    pause 2.5

    scene v13s13a_6 # TPP Show MC giving Polly her phone back while Aubrey moves back to sit by MC
    with dissolve

    pause 1.25

    scene v13s13a_2i # FPP Same angle as 2, Polly looking down at her phone, smiling with mouth open
    with dissolve

    polly "Oh my god, yes! These are absolutely perfect. I'm going to post these, and I'm definitely going to follow you, Aubrey."

    scene v13s13a_3
    with dissolve

    au "Haha, okay! Thanks."

    scene v13s13a_2e
    with dissolve

    polly "Don't forget me when you're famous... *Chuckles*"

    scene v13s13a_3g # FPP Same as 3, Aubrey looking at Polly and laughing
    with dissolve

    au "*Laughs* I won't."

    scene v13s13a_3h # FPP Same as 3, Aubrey looking at Polly and smiling, mouth closed
    with dissolve

    u "Shit, don't forget me either... The fuck?"

    scene v13s13a_3b
    with dissolve

    au "Haha, I'll try not to. *Chuckles*"

    scene v13s13a_2b
    with dissolve

    polly "Haha, so... Are you guys into clubs?"

    scene v13s13a_2c
    with dissolve

    menu:
        "Not really":
            u "I'm not really... Although, I've probably never been to a real, pop star-worthy nightclub. *Laughs*"

            scene v13s13a_2b
            with dissolve

            polly "Ah, okay. *Chuckles*"

        "Hell, yeah!":
            $ add_point(KCT.TROUBLEMAKER)
            $ v13_after_party = True

            u "Oh, hell yeah. Who doesn't love a good club?"

            scene v13s13a_2b
            with dissolve

            polly "Yes! I'm going to an after party right now and... You guys should come."

            scene v13s13a_3
            with dissolve

            au "Oh, we are."

            scene v13s13a_3h
            with dissolve

            u "*Chuckles*"

            scene v13s13a_2b
            with dissolve

            polly "Haha! Good."

    # -Regardless of choice scene continued
    scene v13s13a_7 # FPP Show Polly standing up, looking at Aubrey and MC, smiling with mouth open
    with dissolve

    polly "Well, I gotta get headed over to the club."

    scene v13s13a_8 # TPP Show MC and Aubrey standing up, looking at Polly
    with dissolve

    pause 0.75

    if v13_after_party: # -If have after party tickets or got invited
        scene v13s13a_9 # FPP Show Polly, standing, looking at MC and Aubrey, smiling with mouth closed
        with dissolve

        u "Lead the way!"

        #scene v13s13a_9a # FPP Same as 9, Polly smiling with mouth open
        scene v13s13a_9
        with dissolve

        polly "Haha, let's hop in my little escape car."

        scene v13s13a_10 # FPP Show Aubrey, now standing, looking at Polly and laughing
        with dissolve

        au "*Laughs*"

        scene v13s13a_11 # TPP Show MC and Aubrey following Polly to a small car 
        with dissolve

        pause 0.5

        scene v13s13a_12 # TPP Show car, with Polly, MC, and Aubrey, pulling up in front of club
        with dissolve

        pause 0.5

        scene v13s13a_13 # TPP Show Polly walking into club, MC and Aubrey close behind
        with dissolve

        pause 0.5

        stop music fadeout 3

        jump v13s14a

    else: # -If don't have after party access or not invited
        scene v13s13a_9
        with dissolve

        u "Guess that's our cue to get outta here, haha."

        scene v13s13a_10a # FPP Same as 10, Aubrey smiling at Polly with mouth open
        with dissolve

        au "It was such a pleasure to meet you. I look forward to working together someday..."

        scene v13s13a_9a
        with dissolve

        polly "You beat me to it. I'll be in touch with you on Kiwii, girl."

        scene v13s13a_14 # FPP Show Polly giving Aubrey a friendly hug
        with dissolve

        pause 0.75

        scene v13s13a_9
        with dissolve

        u "See you around."

        scene v13s13a_9a
        with dissolve

        polly "See ya guys! Thanks again for coming."

        scene v13s13a_15 # TPP Show MC and Aubrey leaving the backstage area
        with dissolve

        pause 0.5

        stop music fadeout 3
        play music "music/v13/Track Scene 12a_2.mp3" fadein 2

        scene v13s13a_16 # TPP Show MC and Aubrey getting into a cab
        with dissolve

        pause 0.5

        scene v13s13a_17 # TPP Show MC and Aubrey entering hotel lobby through the front door
        with dissolve

        pause 0.5

        scene v13s13a_18 # TPP Show Aubrey giving MC a hug in hotel lobby. Aubrey is smiling with her mouth open
        with dissolve

        stop music fadeout 3
        play music "music/v13/Track Scene 12a_1.mp3" fadein 2
        
        au "That was... a once in a lifetime opportunity. Thank you so much."

        scene v13s13a_19 # FPP Show Aubrey, in hotel lobby, smiling with mouth closed
        with dissolve

        u "*Chuckles* Are you kidding? I had a blast. You're more than welcome."

        scene v13s13a_19a # FPP Same as 19, Aubrey's mouth open
        with dissolve

        au "I need to go call my sister... Goodnight, [name]."

        scene v13s13a_19
        with dissolve

        u "Goodnight, Aubs."

        scene v13s13a_20 # TPP Show MC about to enter his room
        with fade

        pause 0.75

        stop music fadeout 3

        if v11_riley_roomate:
            jump v13s15a

        else:
            jump v13s15
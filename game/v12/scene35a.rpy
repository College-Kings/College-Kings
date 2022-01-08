# SCENE 35a: Nora the big talk
# Locations: Hotel room, hotel corridor
# Characters: MC (Outfit: 2), NORA (Outfit: 1)
# Time: Night
# Phone Images: None

label v12_nora_room:
    scene v12nos1 # FPP. MC and Nora sitting next to each other on bed, Nora looking at MC, she is crying, mouth closed
    with dissolve

    u "I heard what happened."

    play music "music/v12/Track Scene 35.mp3" fadein 2

    scene v12nos1a # FPP. Same as v12nos1, Nora crying, mouth open
    with dissolve

    no "I couldn't deal with him, there's nothing I can do to get him to understand so... It's just pointless."

    scene v12nos1
    with dissolve

    menu:
        "Chris is...": 
            #scene v12nos1b # FPP. Same as v12nos1, Nora looking down, crying, mouth closed
            scene v12nos1
            with dissolve

            u "Chris isn't focused on what he should be focused on, no matter what he may think. He says he's trying to get things setup for the two of you, but he can't have a future with you if he doesn't have a present."

            scene v12nos1c # FPP. Same as v12nos1b, Nora crying, mouth open
            with dissolve

            no "How can you understand that and know how to put it into words? I don't know why it's so hard for other men to get this."

            scene v12nos1a
            with dissolve

            no "Like, what's the point in worrying about the future if there are obvious issues right now?"

            scene v12nos1
            with dissolve

            u "Exactly. I guess some men just don't know how to provide. I see being a provider differently than others."
            u "It isn't just about putting food on the table or a roof over your head. You have to be present while you achieve all of those things."

        "You are...":
            $ v12_nora_points += 1

            #scene v12nos1b
            scene v12nos1
            with dissolve

            u "You are the only person I'm concerned about right now. We don't even need to bring him up."

            scene v12nos1c
            with dissolve

            no "*Sighs* I can't even remember what it's like to be the center of someone's world..."

            scene v12nos1
            with dissolve

            u "Well, right now you're the center of mine. No distractions, no other commitments, no broken promises. All yours."

            scene v12nos2 # FPP. MC looking down at his lap as he holds her hand in his lap
            with dissolve

            pause

            scene v12nos1d # FPP. Same as v12nos1, Nora slight smile, still tearing up, mouth open
            with dissolve

            no "Why, though?"

            #scene v12nos1e # FPP. Same as v12nos1d, different pose
            scene v12nos1d
            with dissolve

            no "Why is it so easy for you to understand that a woman needs to be your sole focus from time to time, but other men can't?"

            scene v12nos1f # FPP. Same as v12nos1e, Nora slight smile, still tearing up, mouth closed
            with dissolve

            u "I guess I just see being a provider a little differently than others. It isn't just about putting food on the table or a roof over your head. You have to be present while you achieve all of those things."

    scene v12nos1g # FPP. Same as v12nos1c, Nora slight smile, mouth open, no longer tearing up
    with dissolve

    no "So, if you were in a relationship with me, knowing the type of woman I am, how would you... Provide?"

    scene v12nos1h # FPP. Same as v12nos1g, Nora slight smile, mouth closed
    with dissolve

    u "Well... Over the course of these months that I've gotten to know you and with the insight I have into your relationship, specifically for you and I..."

    menu:
        "Communication is key":
            scene v12nos1i # FPP. Same as v12nos1h, Nora slightly sad, mouth closed
            with dissolve

            u "Communication is key. Times won't always be the way we'd both want, but as long as we can communicate to each other and understand each other, all will work."
            u "Being in a relationship means providing for your partner in every aspect, not just financially."

        "Time is key":
            $ v12_nora_points += 1
            scene v12nos1h
            with dissolve

            u "Time is key. There may be other things that have my attention, but my primary focus should and always would be, you."

            scene v12nos1j # FPP. Same as v12nos1h, Nora looking at MC, Nora slight smile, mouth closed
            with dissolve

            u "You'd be my sunrise and sunset, haha... Being in a relationship means providing for your partner in every aspect, not just financially. You'd be everything to me."

    scene v12nos1h
    with dissolve

    no "*Whispers* Ha..."

    scene v12nos1i
    with dissolve

    no "*Sighs* Wow..."

    scene v12nos1j
    with dissolve

    u "What?"

    scene v12nos1k # FPP. Same as v12nos1j, Nora slight smile, one tear on her face, mouth open, MC wiping the tear off
    with dissolve

    no "You're either one in a million or... I just spent most of my life with a man that doesn't understand even the simplest things about me."

    scene v12nos1j
    with dissolve

    u "I know you well enough to understand how you deserve to be treated."

    scene v12nos1h
    with dissolve

    no "Do... Do you find me attractive?"

    scene v12nos1l # FPP. Same as v12nos1j, Nora slight smile, mouth open
    with dissolve

    no "I mean... Not just looks but, as a person?"

    scene v12nos1j
    with dissolve

    u "Of course I do, Nora. I think you're one of the most interesting people I've ever met."

    scene v12nos1h
    with dissolve

    u "Since the moment I laid eyes on you, it was obvious to me that you're the entire fucking package. Anyone would be lucky to have you in their life."

    scene v12nos1j
    with dissolve

    u "The closer the better... *Chuckles*"

    scene v12nos1l
    with dissolve

    no "Haha, you say things that remind me of Aubrey..."

    scene v12nos1j
    with dissolve

    u "Haven't heard that one before... *Chuckles*"

    scene v12nos1i
    with dissolve

    no "*Sighs* God..."

    scene v12nos1l
    with dissolve

    no "I always get so wrapped up in the Chris mess, I forget how many people actually care about me and that I have things in common with."

    scene v12nos1i
    with dissolve

    no "I've only known you for a fraction of the time that I've known Chris and yet you and I are already so... close."

    scene v12nos1j
    with dissolve

    u "You think so?"

    scene v12nos1l
    with dissolve

    no "Look at where you are right now... You could've easily just not come over here and honestly, most people I would've just told to go away."

    scene v12nos1h
    with dissolve

    u "Well, at first you did. *Chuckles*"

    scene v12nos1l
    with dissolve

    no "Haha, that's true... But, you cared enough to keep trying and that means a lot to me."

    scene v12nos1i
    with dissolve

    no "You don't just tell me you'll be there for me, you actually are."

    scene v12nos1j
    with dissolve

    u "That's how it's supposed to be. *Chuckles*"

    scene v12nos3 # TPP. Show Nora hugging MC, Nora mouth open, slight smile, MC mouth closed, slight smile
    with dissolve

    no "Thank you... Thank you for giving me your time, your honesty..."

    scene v12nos4 # TPP. Same as v12nos3, different angle
    with dissolve

    no "Thank you for being you. Thank you for..."

    scene v12nos5 # TPP. Same as v12nos3, camera focusing on Nora's face, Nora slight smile, mouth open, eyes closed
    with dissolve

    no "For not being like Chris."

    if v12_nora_points == 2 or kct == "loyal":
        if v12_nora_points < 2:
            call screen kct_popup
        
        scene v12nos6 # TPP. Same as v12nos3, different angle, Nora mouth closed, slight smile
        with dissolve

        u "(She's warmed up to me a lot, I could probably take this further... Could I do that though, could I do that to Chris?)"

        scene v12nos3a # TPP. Same as v12nos3, Nora slight smile, mouth closed, MC slight smile, mouth open
        with dissolve

        u "Always..."

        scene v12nos1m # FPP. Same as v12nos1, Nora looking at MC, Nora's arms around MC's neck, Nora looking at MC, her face is close to his, Nora slight smile, mouth open
        with dissolve

        no "[name], I..."

        menu:
            "Be a friend":
                scene v12nos1h
                with dissolve

                u "*Sighs* I wouldn't put you in a situation like this, I don't do things with a motive. I'm just here to be your friend..."

                jump v12_nora_no_sex

            "Kiss her":
                $ sceneList.add("v12_nora")
                $ nora.relationship = Relationship.FWB

                stop music fadeout 3
                play music "music/v12/Track Scene 35a_1.mp3" fadein 2

                jump v12_nora_sex
    else:
        call screen kct_popup(required_kct="loyal")
    
        jump v12_nora_no_sex

label v12_nora_no_sex:
        #scene v12nos1e
        scene v12nos1d
        with dissolve

        no "You really are the perfect guy..."

        scene v12nos1d
        with dissolve

        no "Well, again... Thank you so much [name], I'm really happy you came and talked to me."

        scene v12nos1f
        with dissolve

        u "I'm always gonna be there for you."

        scene v12nos1l
        with dissolve

        no "I... I wanna take a shower and try to clear my head."

        scene v12nos1h
        with dissolve

        u "Say no more, I'll get out of your hair."

        scene v12nos7 # TPP. Show MC and Nora standing up, hugging each other, both smiling, mouths closed
        with dissolve

        pause 0.75

        scene v12nos8 # FPP. MC and Nora standing, looking at each other, Nora slight smile, mouth closed
        with dissolve

        u "Call me if you need anything."

        scene v12nos8a # FPP. Same as v12nos8, Nora slight smile, mouth closed
        with dissolve

        no "Yeah, I will."

        scene v12nos9 # TPP. Show MC walking out of Nora's room, MC slightly worried, mouth closed
        with dissolve

        pause 0.75

        scene v12nos10 # TPP. Show MC walking in hotel hallway, MC slightly worried, mouth closed
        with dissolve

        pause 0.75

        scene v12nos11 # TPP. Show MC walking into his room, his room is dark, mouth closed, slightly worried
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music "music/v12/Track Scene 35a_2.mp3" fadein 2

        scene v12nos12 # TPP. Show MC removing his shirt, slightly worried, mouth closed
        with dissolve

        pause 0.75

        scene v12nos13 # TPP. Show MC lying down in his bed in his boxers, slightly worried, looking up at the ceiling, mouth closed
        with dissolve

        u "(She was actually getting ready to cheat on Chris, with me! I know things are pretty bad between them, but with as loyal as she is... She must be at a serious breaking point.)"

        u "(Maybe it's best for me to rest too. Might be good to just sleep on all this.)"

        scene v12nos14 # TPP. Show MC sleeping on his bed
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v12_lindsey_lobby

label v12_nora_sex:
        play sound "sounds/kiss.mp3"
        scene v12nos15 # TPP. Nora and MC on her bed, kissing
        with dissolve

        pause

        scene v12nos1m
        with dissolve

        no "Is this-"

        play sound "sounds/kiss.mp3"

        scene v12nos15a # TPP. Same as v12nos15, MC and Nora making out even more intensely
        with dissolve

        pause

        scene v12nos16 # TPP. Show Nora pushing MC onto his back, both slightly smiling, mouths closed
        with dissolve

        pause

        scene v12nos17 # TPP. Show Nora climbing on top of MC as they continue to makeout
        with dissolve

        pause

        scene v12nos18 # FPP. Nora on top of MC, looking at each other, Nora slight smile, mouth closed
        with dissolve

        u "You deserve to be treated like a queen, Nora..."

        scene v12nos18a # FPP. Same as v12nos18, Nora slight smile, mouth open
        with dissolve

        no "[name]..."
        
        if config_censored:
            call screen censoredPopup("v12s35a_nsfwSkipLabel1")

        scene v12nos19 # TPP. Show MC and Nora taking off their shirts
        with dissolve

        pause

        scene v12nos20 # TPP. Show Nora moving to lay down on her stomach on the bed, MC moving to sit on top of her to massage her back
        with dissolve

        pause

        scene v12nos21 # TPP. Show Nora laying down on her stomach, MC on top of her, massaging her back, Nora mouth open, MC mouth closed, both slightly smiling
        with dissolve

        no "Mmm... This feels so relaxing... Do you want me to-"

        scene v12nos21a # TPP. Same as v12nos21, MC massaging Nora in a different place, Nora mouth closed, MC mouth open, both slightly smiling
        with dissolve

        u "Shhh, just enjoy tonight."

        scene v12nos22 # TPP. Show MC removing Nora's pants
        with dissolve

        pause 

        scene v12nos23 # TPP. Show MC removing Nora's panties
        with dissolve

        pause

        scene v12nos24 # TPP. Show MC massaging Nora
        with dissolve

        pause

        scene v12nos24a # TPP. Same as v12nos24, Show MC massaging Nora but make his hands move so it looks like he is actually massaging her
        with dissolve

        pause

        scene v12nos24 
        with dissolve

        pause

        scene v12nos24a
        with dissolve

        pause

        scene v12nos25 # TPP. Show MC removing his pants
        with dissolve

        pause

        scene v12nos26 # TPP. Show MC removing his boxers
        with dissolve

        pause

        scene v12nos27 # TPP. Show MC laying down behind Nora, her back towards him, getting ready to fuck her in the spooning position
        with dissolve

        pause

        image v12norsb = Movie(play="images/v12/Scene 35a/v12norsb.webm", loop=True, image="images/v12/Scene 35a/v12norsbStart.webp", start_image="images/v12/Scene 35a/v12norsbStart.webp") # Nora spooning
        image v12norsbf = Movie(play="images/v12/Scene 35a/v12norsbf.webm", loop=True, image="images/v12/Scene 35a/v12norsbStart.webp", start_image="images/v12/Scene 35a/v12norsbStart.webp") # Nora spooning spedup
        image v12norsb2 = Movie(play="images/v12/Scene 35a/v12norsb2.webm", loop=True, image="images/v12/Scene 35a/v12norsb2Start.webp", start_image="images/v12/Scene 35a/v12norsb2Start.webp") # Nora spooning TPP 2
        image v12norsb2f = Movie(play="images/v12/Scene 35a/v12norsb2f.webm", loop=True, image="images/v12/Scene 35a/v12norsb2Start.webp", start_image="images/v12/Scene 35a/v12norsb2Start.webp") # Nora spooning TPP 2 spedup

        scene v12norsb # Ignore as animation
        with dissolve
        pause

        no "Haaa... Mmm... I need you, [name]."

        u "This... is the attention you deserve."

        scene v12norsbf # Ignore as animation
        with dissolve
        pause

        u "This is what being loved..."
        
        no "*Moans* Oh, fuck..."

        u "And cared for..."

        scene v12norsb2 # Ignore as animation
        with dissolve
        pause

        no "Sh-shit... *Moans*"

        u "Feels like."

        no "Y-yes..."

        scene v12norsb2f # Ignore as animation
        with dissolve
        pause

        no "I love... how much you... want me."

        u "I always fucking have."

        scene v12nos28 # TPP. Show MC moving to sit on the edge of the bed, Nora moving to sit on his lap
        with dissolve

        pause

        scene v12nos29 # TPP. Show MC sitting off the edge, holding both of Nora's wrists, Nora sitting on his lap
        with dissolve

        pause

        image v12norst = Movie(play="images/v12/Scene 35a/v12norst.webm", loop=True, image="images/v12/Scene 35a/v12norstStart.webp", start_image="images/v12/Scene 35a/v12norstStart.webp") # Nora sit on throne
        image v12norstf = Movie(play="images/v12/Scene 35a/v12norstf.webm", loop=True, image="images/v12/Scene 35a/v12norstStart.webp", start_image="images/v12/Scene 35a/v12norstStart.webp") # Nora sit on throne spedup
        image v12norst2 = Movie(play="images/v12/Scene 35a/v12norst2.webm", loop=True, image="images/v12/Scene 35a/v12norst2Start.webp", start_image="images/v12/Scene 35a/v12norst2Start.webp") # Nora sit on throne TPP 2
        image v12norst2f = Movie(play="images/v12/Scene 35a/v12norst2f.webm", loop=True, image="images/v12/Scene 35a/v12norst2Start.webp", start_image="images/v12/Scene 35a/v12norst2Start.webp") # Nora sit on throne TPP 2 spedup

        scene v12norst # Ignore as animation
        with dissolve
        pause

        no "*Moans* It's been such a long time since I've felt this... Good... *Moans* Fuck!"

        scene v12norstf # Ignore as animation
        with dissolve
        pause

        u "From now on..."

        no "Mmm, yes [name]!"

        scene v12norst2 # Ignore as animation
        with dissolve
        pause

        u "You're gonna get what you want... when you want it."

        scene v12norst2f # Ignore as animation
        with dissolve
        pause

        no "*Gasps* [name]! I'm- I'm going t-"

        u "Ohhhh no... Not yet, baby. I'm not ready for this to end..."

        scene v12nos30 # TPP. Show MC still holding Nora's wrist, moving her towards the wall in between the beds, her back turned to him
        with dissolve

        pause

        scene v12nos31 # TPP. Show MC ready to fuck her in v12norcw (Check animation)
        with dissolve

        pause

        image v12norcw = Movie(play="images/v12/Scene 35a/v12norcw.webm", loop=True, image="images/v12/Scene 35a/v12norcwStart.webp", start_image="images/v12/Scene 35a/v12norcwStart.webp") # Nora Candle on Wall
        image v12norcwf = Movie(play="images/v12/Scene 35a/v12norcwf.webm", loop=True, image="images/v12/Scene 35a/v12norcwStart.webp", start_image="images/v12/Scene 35a/v12norcwStart.webp") # Nora Candle on Wall spedup
        image v12norcw2 = Movie(play="images/v12/Scene 35a/v12norcw2.webm", loop=True, image="images/v12/Scene 35a/v12norcw2Start.webp", start_image="images/v12/Scene 35a/v12norcw2Start.webp") # Nora Candle on Wall TPP 2
        image v12norcw2f = Movie(play="images/v12/Scene 35a/v12norcw2f.webm", loop=True, image="images/v12/Scene 35a/v12norcw2Start.webp", start_image="images/v12/Scene 35a/v12norcw2Start.webp") # Nora Candle on Wall TPP 2 spedup

        scene v12norcw # Ignore as animation
        with dissolve
        pause

        no "Oh my fucking... God... *Moans*"

        no "This feels so... wrong... *Moans*"

        scene v12norcwf # Ignore as animation
        with dissolve
        pause

        no "But you feel so... fucking... GOOD!"

        u "You don't need to worry about anything except for this. Here, right now."

        scene v12norcw2 # Ignore as animation
        with dissolve
        pause

        no "*Moans* Okay, yeah... You're s- so fucking right... *Moans*"

        scene v12norcw2f # Ignore as animation
        with dissolve
        pause

        no "Yes, [name]! FUCK!"

        no "*Moans* Don't... stop... I'm- *Gasps*"

        scene v12nos32 # TPP. Show MC and Nora switching places, MC's back towards the wall, MC and Nora kissing, Nora giving MC a handjob
        with dissolve

        pause

        image v12norkhj = Movie(play="images/v12/Scene 35a/v12norkhj.webm", loop=True, image="images/v12/Scene 35a/v12norkhjStart.webp", start_image="images/v12/Scene 35a/v12norkhjStart.webp") # Nora kissing handjob
        image v12norkhjf = Movie(play="images/v12/Scene 35a/v12norkhjf.webm", loop=True, image="images/v12/Scene 35a/v12norkhjStart.webp", start_image="images/v12/Scene 35a/v12norkhjStart.webp") # Nora kissing handjob spedup
        image v12norkhj2 = Movie(play="images/v12/Scene 35a/v12norkhj2.webm", loop=True, image="images/v12/Scene 35a/v12norkhj2Start.webp", start_image="images/v12/Scene 35a/v12norkhj2Start.webp") # Nora kissing handjob TPP 2
        image v12norkhj2f = Movie(play="images/v12/Scene 35a/v12norkhj2f.webm", loop=True, image="images/v12/Scene 35a/v12norkhj2Start.webp", start_image="images/v12/Scene 35a/v12norkhj2Start.webp") # Nora kissing handjob TPP 2 spedup

        scene v12norkhj # Ignore as animation
        with dissolve
        pause

        u "Oh my fucking god, Nora..."

        u "I'd never... do you wrong. *Moans* You're too... fucking... amazing."

        scene v12norkhjf # Ignore as animation
        with dissolve
        pause

        no "*Chuckles* I'm glad you know it, babe."

        scene v12norkhj2 # Ignore as animation
        with dissolve
        pause

        u "Ahh, fuck, Nora! I'm gonna cum..."

        scene v12norkhj2f # Ignore as animation
        with dissolve
        pause

        u "*Moans* FUCK-"

        scene v12nos33 # TPP. Show Nora putting one of her hands over MC's shoulder, other hand still on his dick, MC cum shot
        with vpunch

        pause

        scene v12nos34 # TPP. Show Nora putting both ehr hands on MC's shoulders, kissing him
        with dissolve

        pause

        scene v12nos35 # FPP. Same positioning as v12nos35, MC and Nora looking at each other, Nora smiling, mouth closed
        with dissolve

        u "Nora... That was... Thank you."

        scene v12nos35a # FPP. Same as v12nos36, Nora smiling, mouth open
        with dissolve

        no "Thank you for making me feel special. Even if it's just for a moment."

        scene v12nos35
        with dissolve

        u "I'll always make you feel special."

        scene v12nos35a
        with dissolve

        no "We don't have to talk about what happened, just... know that I'm happy you came and checked up on me."

        scene v12nos35
        with dissolve

        u "I am too. *Chuckles*"

        scene v12nos35a
        with dissolve

        no "*Chuckles* I'm sure you are. I'm gonna take a shower, okay?"

        scene v12nos35
        with dissolve

        u "Okay, I'll see you tomorrow?"

        scene v12nos35a
        with dissolve

        no "Yes, of course... You will."

        scene v12nos35
        with dissolve

        u "Good."

        scene v12nos36 # TPP. Show MC getting dressed, Nora walking towards bathroom
        with dissolve

        pause

        scene v12nos37 # FPP. MC looking an Nora, Nora in front of bathroom door, looking at MC, Nora smiling, mouth open
        with dissolve

        no "Have a good night."

        scene v12nos37a # FPP. Same as v12nos38, Nora smiling, mouth closed
        with dissolve

        if "v12_lindsey" in sceneList and "v12_nora" in sceneList and "v12_lauren" in sceneList and "v12_rose" in sceneList:
            $ grant_achievement("city_of_love")

        u "You too..."

        label v12s35a_nsfwSkipLabel1:

        scene v12nos9a # TPP. Same as v12nos9, MC smiling, mouth closed
        with dissolve

        pause 0.75

        scene v12nos10a # TPP. Same as v12nos10, MC smiling, mouth closed
        with dissolve

        pause 0.75

        scene v12nos11a # TPP. Same as v12nos11, MC smiling, mouth closed
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music "music/v12/Track Scene 35a_2.mp3" fadein 2

        scene v12nos12a # TPP. Same as v12nos12, MC smiling, mouth closed
        with dissolve

        pause 0.75

        scene v12nos13a # TPP. Same as v12nos13, MC smiling, mouth closed
        with dissolve

        if joinwolves:
            $ grant_achievement("inside_job")
        else:
            $ grant_achievement("all_is_fair_in_love_and_war")

        u "(I just had sex with Nora. NORA!!! I fucked Chris' girl! Wow... Gonna have to sleep on this one.)"

        scene v12nos14
        with dissolve

        $ renpy.end_replay()

        stop music fadeout 3
        jump v12_lindsey_lobby #scene 36